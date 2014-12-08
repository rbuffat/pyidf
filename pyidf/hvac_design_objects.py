""" Data objects in group "HVAC Design Objects"
"""

from collections import OrderedDict
import logging
from pyidf.helper import DataObject

logger = logging.getLogger("pyidf")
logger.addHandler(logging.NullHandler())



class DesignSpecificationOutdoorAir(DataObject):

    """ Corresponds to IDD object `DesignSpecification:OutdoorAir`
        This object is used to describe general outdoor air requirements which
        are referenced by other objects.
    """
    _schema = {'extensible-fields': OrderedDict(),
               'fields': OrderedDict([(u'name',
                                       {'name': u'Name',
                                        'pyname': u'name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'alpha'}),
                                      (u'outdoor air method',
                                       {'name': u'Outdoor Air Method',
                                        'pyname': u'outdoor_air_method',
                                        'default': u'Flow/Person',
                                        'required-field': False,
                                        'autosizable': False,
                                        'accepted-values': [u'Flow/Person',
                                                            u'Flow/Area',
                                                            u'Flow/Zone',
                                                            u'AirChanges/Hour',
                                                            u'Sum',
                                                            u'Maximum'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'outdoor air flow per person',
                                       {'name': u'Outdoor Air Flow per Person',
                                        'pyname': u'outdoor_air_flow_per_person',
                                        'default': 0.00944,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'm3/s-person'}),
                                      (u'outdoor air flow per zone floor area',
                                       {'name': u'Outdoor Air Flow per Zone Floor Area',
                                        'pyname': u'outdoor_air_flow_per_zone_floor_area',
                                        'default': 0.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': 'real',
                                        'unit': u'm3/s-m2'}),
                                      (u'outdoor air flow per zone',
                                       {'name': u'Outdoor Air Flow per Zone',
                                        'pyname': u'outdoor_air_flow_per_zone',
                                        'default': 0.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'm3/s'}),
                                      (u'outdoor air flow air changes per hour',
                                       {'name': u'Outdoor Air Flow Air Changes per Hour',
                                        'pyname': u'outdoor_air_flow_air_changes_per_hour',
                                        'default': 0.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'1/hr'}),
                                      (u'outdoor air flow rate fraction schedule name',
                                       {'name': u'Outdoor Air Flow Rate Fraction Schedule Name',
                                        'pyname': u'outdoor_air_flow_rate_fraction_schedule_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'})]),
               'format': None,
               'group': u'HVAC Design Objects',
               'min-fields': 1,
               'name': u'DesignSpecification:OutdoorAir',
               'pyname': u'DesignSpecificationOutdoorAir',
               'required-object': False,
               'unique-object': False}

    @property
    def name(self):
        """field `Name`

        Args:
            value (str): value for IDD Field `Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `name` or None if not set

        """
        return self["Name"]

    @name.setter
    def name(self, value=None):
        """Corresponds to IDD field `Name`"""
        self["Name"] = value

    @property
    def outdoor_air_method(self):
        """field `Outdoor Air Method`

        Flow/Person => Outdoor Air Flow per Person * Occupancy = Design Flow Rate,
        Flow/Area => Outdoor Air Flow per Zone Floor Area * Zone Floor Area = Design Flow Rate,
        Flow/Zone => Outdoor Air Flow per Zone = Design Flow Rate,
        AirChanges/Hour => Outdoor Air Flow Air Changes per Hour * Zone Volume adjusted for m3/s = Design Flow Rate

        Args:
            value (str): value for IDD Field `Outdoor Air Method`
                Default value: Flow/Person

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `outdoor_air_method` or None if not set

        """
        return self["Outdoor Air Method"]

    @outdoor_air_method.setter
    def outdoor_air_method(self, value="Flow/Person"):
        """Corresponds to IDD field `Outdoor Air Method`"""
        self["Outdoor Air Method"] = value

    @property
    def outdoor_air_flow_per_person(self):
        """field `Outdoor Air Flow per Person`
        0.00944 m3/s is equivalent to 20 cfm per person
        This input should be used if the field Outdoor Air Method is Flow/Person.
        This input is used if the field Outdoor Air Method is Flow/Person, Sum, or Maximum

        Args:
            value (float): value for IDD Field `Outdoor Air Flow per Person`
                Units: m3/s-person
                Default value: 0.00944

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `outdoor_air_flow_per_person` or None if not set
        """
        return self["Outdoor Air Flow per Person"]

    @outdoor_air_flow_per_person.setter
    def outdoor_air_flow_per_person(self, value=0.00944):
        """Corresponds to IDD field `Outdoor Air Flow per Person`"""
        self["Outdoor Air Flow per Person"] = value

    @property
    def outdoor_air_flow_per_zone_floor_area(self):
        """field `Outdoor Air Flow per Zone Floor Area` This input should be
        used if the field Outdoor Air Method is Flow/Area. This input is used
        if the field Outdoor Air Method is Flow/Area, Sum, or Maximum.

        Args:
            value (float): value for IDD Field `Outdoor Air Flow per Zone Floor Area`
                Units: m3/s-m2

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `outdoor_air_flow_per_zone_floor_area` or None if not set

        """
        return self["Outdoor Air Flow per Zone Floor Area"]

    @outdoor_air_flow_per_zone_floor_area.setter
    def outdoor_air_flow_per_zone_floor_area(self, value=None):
        """Corresponds to IDD field `Outdoor Air Flow per Zone Floor Area`"""
        self["Outdoor Air Flow per Zone Floor Area"] = value

    @property
    def outdoor_air_flow_per_zone(self):
        """field `Outdoor Air Flow per Zone` This input should be used if the
        field Outdoor Air Method is Flow/Zone. This input is used if the field
        Outdoor Air Method is Flow/Zone, Sum, or Maximum.

        Args:
            value (float): value for IDD Field `Outdoor Air Flow per Zone`
                Units: m3/s

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `outdoor_air_flow_per_zone` or None if not set

        """
        return self["Outdoor Air Flow per Zone"]

    @outdoor_air_flow_per_zone.setter
    def outdoor_air_flow_per_zone(self, value=None):
        """Corresponds to IDD field `Outdoor Air Flow per Zone`"""
        self["Outdoor Air Flow per Zone"] = value

    @property
    def outdoor_air_flow_air_changes_per_hour(self):
        """field `Outdoor Air Flow Air Changes per Hour` This input should be
        used if the field Outdoor Air Method is AirChanges/Hour. This input is
        used if the field Outdoor Air Method is AirChanges/Hour, Sum, or
        Maximum.

        Args:
            value (float): value for IDD Field `Outdoor Air Flow Air Changes per Hour`
                Units: 1/hr

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `outdoor_air_flow_air_changes_per_hour` or None if not set

        """
        return self["Outdoor Air Flow Air Changes per Hour"]

    @outdoor_air_flow_air_changes_per_hour.setter
    def outdoor_air_flow_air_changes_per_hour(self, value=None):
        """Corresponds to IDD field `Outdoor Air Flow Air Changes per Hour`"""
        self["Outdoor Air Flow Air Changes per Hour"] = value

    @property
    def outdoor_air_flow_rate_fraction_schedule_name(self):
        """field `Outdoor Air Flow Rate Fraction Schedule Name`
        Schedule values are multiplied by the Outdoor Air Flow rate calculated using
        the previous four inputs. Schedule values are limited to 0 to 1.

        Args:
            value (str): value for IDD Field `Outdoor Air Flow Rate Fraction Schedule Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `outdoor_air_flow_rate_fraction_schedule_name` or None if not set
        """
        return self["Outdoor Air Flow Rate Fraction Schedule Name"]

    @outdoor_air_flow_rate_fraction_schedule_name.setter
    def outdoor_air_flow_rate_fraction_schedule_name(self, value=None):
        """Corresponds to IDD field `Outdoor Air Flow Rate Fraction Schedule
        Name`"""
        self["Outdoor Air Flow Rate Fraction Schedule Name"] = value




class DesignSpecificationZoneAirDistribution(DataObject):

    """ Corresponds to IDD object `DesignSpecification:ZoneAirDistribution`
        This object is used to describe zone air distribution in terms of air distribution
        effectiveness and secondary recirculation fraction. It is referenced by Sizing:Zone
        and Controller:MechanicalVentilation objects
    """
    _schema = {'extensible-fields': OrderedDict(),
               'fields': OrderedDict([(u'name',
                                       {'name': u'Name',
                                        'pyname': u'name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'alpha'}),
                                      (u'zone air distribution effectiveness in cooling mode',
                                       {'name': u'Zone Air Distribution Effectiveness in Cooling Mode',
                                        'pyname': u'zone_air_distribution_effectiveness_in_cooling_mode',
                                        'default': 1.0,
                                        'minimum>': 0.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'dimensionless'}),
                                      (u'zone air distribution effectiveness in heating mode',
                                       {'name': u'Zone Air Distribution Effectiveness in Heating Mode',
                                        'pyname': u'zone_air_distribution_effectiveness_in_heating_mode',
                                        'default': 1.0,
                                        'minimum>': 0.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'dimensionless'}),
                                      (u'zone air distribution effectiveness schedule name',
                                       {'name': u'Zone Air Distribution Effectiveness Schedule Name',
                                        'pyname': u'zone_air_distribution_effectiveness_schedule_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'zone secondary recirculation fraction',
                                       {'name': u'Zone Secondary Recirculation Fraction',
                                        'pyname': u'zone_secondary_recirculation_fraction',
                                        'default': 0.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'dimensionless'})]),
               'format': None,
               'group': u'HVAC Design Objects',
               'min-fields': 1,
               'name': u'DesignSpecification:ZoneAirDistribution',
               'pyname': u'DesignSpecificationZoneAirDistribution',
               'required-object': False,
               'unique-object': False}

    @property
    def name(self):
        """field `Name`

        Args:
            value (str): value for IDD Field `Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `name` or None if not set

        """
        return self["Name"]

    @name.setter
    def name(self, value=None):
        """Corresponds to IDD field `Name`"""
        self["Name"] = value

    @property
    def zone_air_distribution_effectiveness_in_cooling_mode(self):
        """field `Zone Air Distribution Effectiveness in Cooling Mode`

        Args:
            value (float): value for IDD Field `Zone Air Distribution Effectiveness in Cooling Mode`
                Units: dimensionless
                Default value: 1.0

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `zone_air_distribution_effectiveness_in_cooling_mode` or None if not set

        """
        return self["Zone Air Distribution Effectiveness in Cooling Mode"]

    @zone_air_distribution_effectiveness_in_cooling_mode.setter
    def zone_air_distribution_effectiveness_in_cooling_mode(self, value=1.0):
        """Corresponds to IDD field `Zone Air Distribution Effectiveness in
        Cooling Mode`"""
        self["Zone Air Distribution Effectiveness in Cooling Mode"] = value

    @property
    def zone_air_distribution_effectiveness_in_heating_mode(self):
        """field `Zone Air Distribution Effectiveness in Heating Mode`

        Args:
            value (float): value for IDD Field `Zone Air Distribution Effectiveness in Heating Mode`
                Units: dimensionless
                Default value: 1.0

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `zone_air_distribution_effectiveness_in_heating_mode` or None if not set

        """
        return self["Zone Air Distribution Effectiveness in Heating Mode"]

    @zone_air_distribution_effectiveness_in_heating_mode.setter
    def zone_air_distribution_effectiveness_in_heating_mode(self, value=1.0):
        """Corresponds to IDD field `Zone Air Distribution Effectiveness in
        Heating Mode`"""
        self["Zone Air Distribution Effectiveness in Heating Mode"] = value

    @property
    def zone_air_distribution_effectiveness_schedule_name(self):
        """field `Zone Air Distribution Effectiveness Schedule Name` optionally
        used to replace Zone Air Distribution Effectiveness in Cooling and
        Heating Mode.

        Args:
            value (str): value for IDD Field `Zone Air Distribution Effectiveness Schedule Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `zone_air_distribution_effectiveness_schedule_name` or None if not set

        """
        return self["Zone Air Distribution Effectiveness Schedule Name"]

    @zone_air_distribution_effectiveness_schedule_name.setter
    def zone_air_distribution_effectiveness_schedule_name(self, value=None):
        """Corresponds to IDD field `Zone Air Distribution Effectiveness
        Schedule Name`"""
        self["Zone Air Distribution Effectiveness Schedule Name"] = value

    @property
    def zone_secondary_recirculation_fraction(self):
        """field `Zone Secondary Recirculation Fraction`

        Args:
            value (float): value for IDD Field `Zone Secondary Recirculation Fraction`
                Units: dimensionless

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `zone_secondary_recirculation_fraction` or None if not set

        """
        return self["Zone Secondary Recirculation Fraction"]

    @zone_secondary_recirculation_fraction.setter
    def zone_secondary_recirculation_fraction(self, value=None):
        """Corresponds to IDD field `Zone Secondary Recirculation Fraction`"""
        self["Zone Secondary Recirculation Fraction"] = value




class SizingParameters(DataObject):

    """ Corresponds to IDD object `Sizing:Parameters`
        Specifies global heating and cooling sizing factors/ratios.
        These ratios are applied at the zone level to all of the zone heating and cooling loads
        and air flow rates. Then these new loads and air flow rates are used to calculate the
        system level flow rates and capacities and are used in all component sizing calculations.
        Specifies the width (in load timesteps) of a moving average window
        which is used to smooth the peak load across more than one timestep.
    """
    _schema = {'extensible-fields': OrderedDict(),
               'fields': OrderedDict([(u'heating sizing factor',
                                       {'name': u'Heating Sizing Factor',
                                        'pyname': u'heating_sizing_factor',
                                        'default': 1.0,
                                        'minimum>': 0.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'cooling sizing factor',
                                       {'name': u'Cooling Sizing Factor',
                                        'pyname': u'cooling_sizing_factor',
                                        'default': 1.0,
                                        'minimum>': 0.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'timesteps in averaging window',
                                       {'name': u'Timesteps in Averaging Window',
                                        'pyname': u'timesteps_in_averaging_window',
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 1,
                                        'autocalculatable': False,
                                        'type': u'integer'})]),
               'format': None,
               'group': u'HVAC Design Objects',
               'min-fields': 1,
               'name': u'Sizing:Parameters',
               'pyname': u'SizingParameters',
               'required-object': False,
               'unique-object': True}

    @property
    def heating_sizing_factor(self):
        """field `Heating Sizing Factor`

        Args:
            value (float): value for IDD Field `Heating Sizing Factor`
                Default value: 1.0

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `heating_sizing_factor` or None if not set

        """
        return self["Heating Sizing Factor"]

    @heating_sizing_factor.setter
    def heating_sizing_factor(self, value=1.0):
        """Corresponds to IDD field `Heating Sizing Factor`"""
        self["Heating Sizing Factor"] = value

    @property
    def cooling_sizing_factor(self):
        """field `Cooling Sizing Factor`

        Args:
            value (float): value for IDD Field `Cooling Sizing Factor`
                Default value: 1.0

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `cooling_sizing_factor` or None if not set

        """
        return self["Cooling Sizing Factor"]

    @cooling_sizing_factor.setter
    def cooling_sizing_factor(self, value=1.0):
        """Corresponds to IDD field `Cooling Sizing Factor`"""
        self["Cooling Sizing Factor"] = value

    @property
    def timesteps_in_averaging_window(self):
        """field `Timesteps in Averaging Window`
        blank => set the timesteps in averaging window to
        Number of Timesteps per Hour resulting in a 1 hour averaging window
        default is number of timesteps for 1 hour averaging window

        Args:
            value (int): value for IDD Field `Timesteps in Averaging Window`
                value >= 1

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            int: the value of `timesteps_in_averaging_window` or None if not set
        """
        return self["Timesteps in Averaging Window"]

    @timesteps_in_averaging_window.setter
    def timesteps_in_averaging_window(self, value=None):
        """Corresponds to IDD field `Timesteps in Averaging Window`"""
        self["Timesteps in Averaging Window"] = value




class SizingZone(DataObject):

    """ Corresponds to IDD object `Sizing:Zone`
        Specifies the data needed to perform a zone design air flow calculation.
        The calculation is done for every sizing period included in the input. The maximum
        cooling and heating load and cooling, heating, and ventilation air flows are then saved
        for system level and zone component design calculations.
    """
    _schema = {'extensible-fields': OrderedDict(),
               'fields': OrderedDict([(u'zone or zonelist name',
                                       {'name': u'Zone or ZoneList Name',
                                        'pyname': u'zone_or_zonelist_name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'zone cooling design supply air temperature input method',
                                       {'name': u'Zone Cooling Design Supply Air Temperature Input Method',
                                        'pyname': u'zone_cooling_design_supply_air_temperature_input_method',
                                        'default': u'SupplyAirTemperature',
                                        'required-field': True,
                                        'autosizable': False,
                                        'accepted-values': [u'SupplyAirTemperature',
                                                            u'TemperatureDifference'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'zone cooling design supply air temperature',
                                       {'name': u'Zone Cooling Design Supply Air Temperature',
                                        'pyname': u'zone_cooling_design_supply_air_temperature',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'C'}),
                                      (u'zone cooling design supply air temperature difference',
                                       {'name': u'Zone Cooling Design Supply Air Temperature Difference',
                                        'pyname': u'zone_cooling_design_supply_air_temperature_difference',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'deltaC'}),
                                      (u'zone heating design supply air temperature input method',
                                       {'name': u'Zone Heating Design Supply Air Temperature Input Method',
                                        'pyname': u'zone_heating_design_supply_air_temperature_input_method',
                                        'default': u'SupplyAirTemperature',
                                        'required-field': True,
                                        'autosizable': False,
                                        'accepted-values': [u'SupplyAirTemperature',
                                                            u'TemperatureDifference'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'zone heating design supply air temperature',
                                       {'name': u'Zone Heating Design Supply Air Temperature',
                                        'pyname': u'zone_heating_design_supply_air_temperature',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'C'}),
                                      (u'zone heating design supply air temperature difference',
                                       {'name': u'Zone Heating Design Supply Air Temperature Difference',
                                        'pyname': u'zone_heating_design_supply_air_temperature_difference',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'deltaC'}),
                                      (u'zone cooling design supply air humidity ratio',
                                       {'name': u'Zone Cooling Design Supply Air Humidity Ratio',
                                        'pyname': u'zone_cooling_design_supply_air_humidity_ratio',
                                        'required-field': True,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'kgWater/kgDryAir'}),
                                      (u'zone heating design supply air humidity ratio',
                                       {'name': u'Zone Heating Design Supply Air Humidity Ratio',
                                        'pyname': u'zone_heating_design_supply_air_humidity_ratio',
                                        'required-field': True,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'kgWater/kgDryAir'}),
                                      (u'design specification outdoor air object name',
                                       {'name': u'Design Specification Outdoor Air Object Name',
                                        'pyname': u'design_specification_outdoor_air_object_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'zone heating sizing factor',
                                       {'name': u'Zone Heating Sizing Factor',
                                        'pyname': u'zone_heating_sizing_factor',
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': 'real'}),
                                      (u'zone cooling sizing factor',
                                       {'name': u'Zone Cooling Sizing Factor',
                                        'pyname': u'zone_cooling_sizing_factor',
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': 'real'}),
                                      (u'cooling design air flow method',
                                       {'name': u'Cooling Design Air Flow Method',
                                        'pyname': u'cooling_design_air_flow_method',
                                        'default': u'DesignDay',
                                        'required-field': False,
                                        'autosizable': False,
                                        'accepted-values': [u'Flow/Zone',
                                                            u'DesignDay',
                                                            u'DesignDayWithLimit'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'cooling design air flow rate',
                                       {'name': u'Cooling Design Air Flow Rate',
                                        'pyname': u'cooling_design_air_flow_rate',
                                        'default': 0.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'm3/s'}),
                                      (u'cooling minimum air flow per zone floor area',
                                       {'name': u'Cooling Minimum Air Flow per Zone Floor Area',
                                        'pyname': u'cooling_minimum_air_flow_per_zone_floor_area',
                                        'default': 0.000762,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'm3/s-m2'}),
                                      (u'cooling minimum air flow',
                                       {'name': u'Cooling Minimum Air Flow',
                                        'pyname': u'cooling_minimum_air_flow',
                                        'default': 0.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'm3/s'}),
                                      (u'cooling minimum air flow fraction',
                                       {'name': u'Cooling Minimum Air Flow Fraction',
                                        'pyname': u'cooling_minimum_air_flow_fraction',
                                        'default': 0.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'heating design air flow method',
                                       {'name': u'Heating Design Air Flow Method',
                                        'pyname': u'heating_design_air_flow_method',
                                        'default': u'DesignDay',
                                        'required-field': False,
                                        'autosizable': False,
                                        'accepted-values': [u'Flow/Zone',
                                                            u'DesignDay',
                                                            u'DesignDayWithLimit'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'heating design air flow rate',
                                       {'name': u'Heating Design Air Flow Rate',
                                        'pyname': u'heating_design_air_flow_rate',
                                        'default': 0.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'm3/s'}),
                                      (u'heating maximum air flow per zone floor area',
                                       {'name': u'Heating Maximum Air Flow per Zone Floor Area',
                                        'pyname': u'heating_maximum_air_flow_per_zone_floor_area',
                                        'default': 0.002032,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'm3/s-m2'}),
                                      (u'heating maximum air flow',
                                       {'name': u'Heating Maximum Air Flow',
                                        'pyname': u'heating_maximum_air_flow',
                                        'default': 0.1415762,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'm3/s'}),
                                      (u'heating maximum air flow fraction',
                                       {'name': u'Heating Maximum Air Flow Fraction',
                                        'pyname': u'heating_maximum_air_flow_fraction',
                                        'default': 0.3,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'design specification zone air distribution object name',
                                       {'name': u'Design Specification Zone Air Distribution Object Name',
                                        'pyname': u'design_specification_zone_air_distribution_object_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'})]),
               'format': None,
               'group': u'HVAC Design Objects',
               'min-fields': 18,
               'name': u'Sizing:Zone',
               'pyname': u'SizingZone',
               'required-object': False,
               'unique-object': False}

    @property
    def zone_or_zonelist_name(self):
        """field `Zone or ZoneList Name`

        Args:
            value (str): value for IDD Field `Zone or ZoneList Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `zone_or_zonelist_name` or None if not set

        """
        return self["Zone or ZoneList Name"]

    @zone_or_zonelist_name.setter
    def zone_or_zonelist_name(self, value=None):
        """Corresponds to IDD field `Zone or ZoneList Name`"""
        self["Zone or ZoneList Name"] = value

    @property
    def zone_cooling_design_supply_air_temperature_input_method(self):
        """field `Zone Cooling Design Supply Air Temperature Input Method`

        Args:
            value (str): value for IDD Field `Zone Cooling Design Supply Air Temperature Input Method`
                Default value: SupplyAirTemperature

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `zone_cooling_design_supply_air_temperature_input_method` or None if not set

        """
        return self["Zone Cooling Design Supply Air Temperature Input Method"]

    @zone_cooling_design_supply_air_temperature_input_method.setter
    def zone_cooling_design_supply_air_temperature_input_method(
            self,
            value="SupplyAirTemperature"):
        """Corresponds to IDD field `Zone Cooling Design Supply Air Temperature
        Input Method`"""
        self["Zone Cooling Design Supply Air Temperature Input Method"] = value

    @property
    def zone_cooling_design_supply_air_temperature(self):
        """field `Zone Cooling Design Supply Air Temperature`
        Zone Cooling Design Supply Air Temperature is only used when Zone Cooling Design
        Supply Air Temperature Input Method = SupplyAirTemperature

        Args:
            value (float): value for IDD Field `Zone Cooling Design Supply Air Temperature`
                Units: C

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `zone_cooling_design_supply_air_temperature` or None if not set
        """
        return self["Zone Cooling Design Supply Air Temperature"]

    @zone_cooling_design_supply_air_temperature.setter
    def zone_cooling_design_supply_air_temperature(self, value=None):
        """Corresponds to IDD field `Zone Cooling Design Supply Air
        Temperature`"""
        self["Zone Cooling Design Supply Air Temperature"] = value

    @property
    def zone_cooling_design_supply_air_temperature_difference(self):
        """field `Zone Cooling Design Supply Air Temperature Difference`
        Zone Cooling Design Supply Air Temperature is only used when Zone Cooling Design
        Supply Air Temperature Input Method = TemperatureDifference
        The absolute value of this field will be subtracted from the zone temperature
        at peak load to calculate the Zone Cooling Design Supply Air Temperature.

        Args:
            value (float): value for IDD Field `Zone Cooling Design Supply Air Temperature Difference`
                Units: deltaC

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `zone_cooling_design_supply_air_temperature_difference` or None if not set
        """
        return self["Zone Cooling Design Supply Air Temperature Difference"]

    @zone_cooling_design_supply_air_temperature_difference.setter
    def zone_cooling_design_supply_air_temperature_difference(
            self,
            value=None):
        """Corresponds to IDD field `Zone Cooling Design Supply Air Temperature
        Difference`"""
        self["Zone Cooling Design Supply Air Temperature Difference"] = value

    @property
    def zone_heating_design_supply_air_temperature_input_method(self):
        """field `Zone Heating Design Supply Air Temperature Input Method`

        Args:
            value (str): value for IDD Field `Zone Heating Design Supply Air Temperature Input Method`
                Default value: SupplyAirTemperature

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `zone_heating_design_supply_air_temperature_input_method` or None if not set

        """
        return self["Zone Heating Design Supply Air Temperature Input Method"]

    @zone_heating_design_supply_air_temperature_input_method.setter
    def zone_heating_design_supply_air_temperature_input_method(
            self,
            value="SupplyAirTemperature"):
        """Corresponds to IDD field `Zone Heating Design Supply Air Temperature
        Input Method`"""
        self["Zone Heating Design Supply Air Temperature Input Method"] = value

    @property
    def zone_heating_design_supply_air_temperature(self):
        """field `Zone Heating Design Supply Air Temperature`
        Zone Heating Design Supply Air Temperature is only used when Zone Heating Design
        Supply Air Temperature Input Method = SupplyAirTemperature

        Args:
            value (float): value for IDD Field `Zone Heating Design Supply Air Temperature`
                Units: C

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `zone_heating_design_supply_air_temperature` or None if not set
        """
        return self["Zone Heating Design Supply Air Temperature"]

    @zone_heating_design_supply_air_temperature.setter
    def zone_heating_design_supply_air_temperature(self, value=None):
        """Corresponds to IDD field `Zone Heating Design Supply Air
        Temperature`"""
        self["Zone Heating Design Supply Air Temperature"] = value

    @property
    def zone_heating_design_supply_air_temperature_difference(self):
        """field `Zone Heating Design Supply Air Temperature Difference`
        Zone Heating Design Supply Air Temperature is only used when Zone Heating Design
        Supply Air Temperature Input Method = TemperatureDifference
        The absolute value of this field will be added to the zone temperature
        at peak load to calculate the Zone Heating Design Supply Air Temperature.

        Args:
            value (float): value for IDD Field `Zone Heating Design Supply Air Temperature Difference`
                Units: deltaC

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `zone_heating_design_supply_air_temperature_difference` or None if not set
        """
        return self["Zone Heating Design Supply Air Temperature Difference"]

    @zone_heating_design_supply_air_temperature_difference.setter
    def zone_heating_design_supply_air_temperature_difference(
            self,
            value=None):
        """Corresponds to IDD field `Zone Heating Design Supply Air Temperature
        Difference`"""
        self["Zone Heating Design Supply Air Temperature Difference"] = value

    @property
    def zone_cooling_design_supply_air_humidity_ratio(self):
        """field `Zone Cooling Design Supply Air Humidity Ratio`

        Args:
            value (float): value for IDD Field `Zone Cooling Design Supply Air Humidity Ratio`
                Units: kgWater/kgDryAir

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `zone_cooling_design_supply_air_humidity_ratio` or None if not set

        """
        return self["Zone Cooling Design Supply Air Humidity Ratio"]

    @zone_cooling_design_supply_air_humidity_ratio.setter
    def zone_cooling_design_supply_air_humidity_ratio(self, value=None):
        """Corresponds to IDD field `Zone Cooling Design Supply Air Humidity
        Ratio`"""
        self["Zone Cooling Design Supply Air Humidity Ratio"] = value

    @property
    def zone_heating_design_supply_air_humidity_ratio(self):
        """field `Zone Heating Design Supply Air Humidity Ratio`

        Args:
            value (float): value for IDD Field `Zone Heating Design Supply Air Humidity Ratio`
                Units: kgWater/kgDryAir

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `zone_heating_design_supply_air_humidity_ratio` or None if not set

        """
        return self["Zone Heating Design Supply Air Humidity Ratio"]

    @zone_heating_design_supply_air_humidity_ratio.setter
    def zone_heating_design_supply_air_humidity_ratio(self, value=None):
        """Corresponds to IDD field `Zone Heating Design Supply Air Humidity
        Ratio`"""
        self["Zone Heating Design Supply Air Humidity Ratio"] = value

    @property
    def design_specification_outdoor_air_object_name(self):
        """field `Design Specification Outdoor Air Object Name`

        Args:
            value (str): value for IDD Field `Design Specification Outdoor Air Object Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `design_specification_outdoor_air_object_name` or None if not set

        """
        return self["Design Specification Outdoor Air Object Name"]

    @design_specification_outdoor_air_object_name.setter
    def design_specification_outdoor_air_object_name(self, value=None):
        """Corresponds to IDD field `Design Specification Outdoor Air Object
        Name`"""
        self["Design Specification Outdoor Air Object Name"] = value

    @property
    def zone_heating_sizing_factor(self):
        """field `Zone Heating Sizing Factor`
        if blank or zero, global heating sizing factor from Sizing:Parameters is used.

        Args:
            value (float): value for IDD Field `Zone Heating Sizing Factor`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `zone_heating_sizing_factor` or None if not set
        """
        return self["Zone Heating Sizing Factor"]

    @zone_heating_sizing_factor.setter
    def zone_heating_sizing_factor(self, value=None):
        """Corresponds to IDD field `Zone Heating Sizing Factor`"""
        self["Zone Heating Sizing Factor"] = value

    @property
    def zone_cooling_sizing_factor(self):
        """field `Zone Cooling Sizing Factor`
        if blank or zero, global cooling sizing factor from Sizing:Parameters is used.

        Args:
            value (float): value for IDD Field `Zone Cooling Sizing Factor`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `zone_cooling_sizing_factor` or None if not set
        """
        return self["Zone Cooling Sizing Factor"]

    @zone_cooling_sizing_factor.setter
    def zone_cooling_sizing_factor(self, value=None):
        """Corresponds to IDD field `Zone Cooling Sizing Factor`"""
        self["Zone Cooling Sizing Factor"] = value

    @property
    def cooling_design_air_flow_method(self):
        """field `Cooling Design Air Flow Method`

        Args:
            value (str): value for IDD Field `Cooling Design Air Flow Method`
                Default value: DesignDay

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `cooling_design_air_flow_method` or None if not set

        """
        return self["Cooling Design Air Flow Method"]

    @cooling_design_air_flow_method.setter
    def cooling_design_air_flow_method(self, value="DesignDay"):
        """Corresponds to IDD field `Cooling Design Air Flow Method`"""
        self["Cooling Design Air Flow Method"] = value

    @property
    def cooling_design_air_flow_rate(self):
        """field `Cooling Design Air Flow Rate` This input is used if Cooling
        Design Air Flow Method is Flow/Zone This value will be multiplied by
        the global or zone sizing factor and by zone multipliers.

        Args:
            value (float): value for IDD Field `Cooling Design Air Flow Rate`
                Units: m3/s

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `cooling_design_air_flow_rate` or None if not set

        """
        return self["Cooling Design Air Flow Rate"]

    @cooling_design_air_flow_rate.setter
    def cooling_design_air_flow_rate(self, value=None):
        """Corresponds to IDD field `Cooling Design Air Flow Rate`"""
        self["Cooling Design Air Flow Rate"] = value

    @property
    def cooling_minimum_air_flow_per_zone_floor_area(self):
        """field `Cooling Minimum Air Flow per Zone Floor Area` default is .15
        cfm/ft2 This input is used if Cooling Design Air Flow Method is
        DesignDayWithLimit.

        Args:
            value (float): value for IDD Field `Cooling Minimum Air Flow per Zone Floor Area`
                Units: m3/s-m2
                Default value: 0.000762

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `cooling_minimum_air_flow_per_zone_floor_area` or None if not set

        """
        return self["Cooling Minimum Air Flow per Zone Floor Area"]

    @cooling_minimum_air_flow_per_zone_floor_area.setter
    def cooling_minimum_air_flow_per_zone_floor_area(self, value=0.000762):
        """Corresponds to IDD field `Cooling Minimum Air Flow per Zone Floor
        Area`"""
        self["Cooling Minimum Air Flow per Zone Floor Area"] = value

    @property
    def cooling_minimum_air_flow(self):
        """field `Cooling Minimum Air Flow` This input is used if Cooling
        Design Air Flow Method is DesignDayWithLimit.

        Args:
            value (float): value for IDD Field `Cooling Minimum Air Flow`
                Units: m3/s

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `cooling_minimum_air_flow` or None if not set

        """
        return self["Cooling Minimum Air Flow"]

    @cooling_minimum_air_flow.setter
    def cooling_minimum_air_flow(self, value=None):
        """Corresponds to IDD field `Cooling Minimum Air Flow`"""
        self["Cooling Minimum Air Flow"] = value

    @property
    def cooling_minimum_air_flow_fraction(self):
        """field `Cooling Minimum Air Flow Fraction` fraction of the Cooling
        design Air Flow Rate This input is currently used in sizing the Fan
        minimum Flow Rate. It does not currently affect other component
        autosizing.

        Args:
            value (float): value for IDD Field `Cooling Minimum Air Flow Fraction`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `cooling_minimum_air_flow_fraction` or None if not set

        """
        return self["Cooling Minimum Air Flow Fraction"]

    @cooling_minimum_air_flow_fraction.setter
    def cooling_minimum_air_flow_fraction(self, value=None):
        """Corresponds to IDD field `Cooling Minimum Air Flow Fraction`"""
        self["Cooling Minimum Air Flow Fraction"] = value

    @property
    def heating_design_air_flow_method(self):
        """field `Heating Design Air Flow Method`

        Args:
            value (str): value for IDD Field `Heating Design Air Flow Method`
                Default value: DesignDay

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `heating_design_air_flow_method` or None if not set

        """
        return self["Heating Design Air Flow Method"]

    @heating_design_air_flow_method.setter
    def heating_design_air_flow_method(self, value="DesignDay"):
        """Corresponds to IDD field `Heating Design Air Flow Method`"""
        self["Heating Design Air Flow Method"] = value

    @property
    def heating_design_air_flow_rate(self):
        """field `Heating Design Air Flow Rate` This input is used if Heating
        Design Air Flow Method is Flow/Zone. This value will be multiplied by
        the global or zone sizing factor and by zone multipliers.

        Args:
            value (float): value for IDD Field `Heating Design Air Flow Rate`
                Units: m3/s

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `heating_design_air_flow_rate` or None if not set

        """
        return self["Heating Design Air Flow Rate"]

    @heating_design_air_flow_rate.setter
    def heating_design_air_flow_rate(self, value=None):
        """Corresponds to IDD field `Heating Design Air Flow Rate`"""
        self["Heating Design Air Flow Rate"] = value

    @property
    def heating_maximum_air_flow_per_zone_floor_area(self):
        """field `Heating Maximum Air Flow per Zone Floor Area`
        default is .40 cfm/ft2
        This field is used to size the heating design flow rate when Heating Design Air Flow Method = Flow/Zone.
        This input is used for autosizing components when Heating Design Air Flow Method = DesignDayWithLimit.

        Args:
            value (float): value for IDD Field `Heating Maximum Air Flow per Zone Floor Area`
                Units: m3/s-m2
                Default value: 0.002032

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `heating_maximum_air_flow_per_zone_floor_area` or None if not set
        """
        return self["Heating Maximum Air Flow per Zone Floor Area"]

    @heating_maximum_air_flow_per_zone_floor_area.setter
    def heating_maximum_air_flow_per_zone_floor_area(self, value=0.002032):
        """Corresponds to IDD field `Heating Maximum Air Flow per Zone Floor
        Area`"""
        self["Heating Maximum Air Flow per Zone Floor Area"] = value

    @property
    def heating_maximum_air_flow(self):
        """field `Heating Maximum Air Flow`
        default is 300 cfm
        This input is used for autosizing components when Heating Design Air Flow Method = DesignDayWithLimit.

        Args:
            value (float): value for IDD Field `Heating Maximum Air Flow`
                Units: m3/s
                Default value: 0.1415762

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `heating_maximum_air_flow` or None if not set
        """
        return self["Heating Maximum Air Flow"]

    @heating_maximum_air_flow.setter
    def heating_maximum_air_flow(self, value=0.1415762):
        """Corresponds to IDD field `Heating Maximum Air Flow`"""
        self["Heating Maximum Air Flow"] = value

    @property
    def heating_maximum_air_flow_fraction(self):
        """field `Heating Maximum Air Flow Fraction`
        fraction of the Heating Design Air Flow Rate
        This input is used for autosizing components when Heating Design Air Flow Method = DesignDayWithLimit.

        Args:
            value (float): value for IDD Field `Heating Maximum Air Flow Fraction`
                Default value: 0.3

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `heating_maximum_air_flow_fraction` or None if not set
        """
        return self["Heating Maximum Air Flow Fraction"]

    @heating_maximum_air_flow_fraction.setter
    def heating_maximum_air_flow_fraction(self, value=0.3):
        """Corresponds to IDD field `Heating Maximum Air Flow Fraction`"""
        self["Heating Maximum Air Flow Fraction"] = value

    @property
    def design_specification_zone_air_distribution_object_name(self):
        """field `Design Specification Zone Air Distribution Object Name`

        Args:
            value (str): value for IDD Field `Design Specification Zone Air Distribution Object Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `design_specification_zone_air_distribution_object_name` or None if not set

        """
        return self["Design Specification Zone Air Distribution Object Name"]

    @design_specification_zone_air_distribution_object_name.setter
    def design_specification_zone_air_distribution_object_name(
            self,
            value=None):
        """Corresponds to IDD field `Design Specification Zone Air Distribution
        Object Name`"""
        self["Design Specification Zone Air Distribution Object Name"] = value




class DesignSpecificationZoneHvacSizing(DataObject):

    """ Corresponds to IDD object `DesignSpecification:ZoneHVAC:Sizing`
        This object is used to describe general scalable zone HVAC equipment sizing which
        are referenced by other objects.
    """
    _schema = {'extensible-fields': OrderedDict(),
               'fields': OrderedDict([(u'name',
                                       {'name': u'Name',
                                        'pyname': u'name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'alpha'}),
                                      (u'cooling design air flow method',
                                       {'name': u'Cooling Design Air Flow Method',
                                        'pyname': u'cooling_design_air_flow_method',
                                        'default': u'SupplyAirFlowRate',
                                        'required-field': False,
                                        'autosizable': False,
                                        'accepted-values': [u'None',
                                                            u'SupplyAirFlowRate',
                                                            u'FlowPerFloorArea',
                                                            u'FractionOfAutosizedCoolingAirflow',
                                                            u'FlowPerCoolingCapacity'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'cooling design supply air flow rate',
                                       {'name': u'Cooling Design Supply Air Flow Rate',
                                        'pyname': u'cooling_design_supply_air_flow_rate',
                                        'required-field': False,
                                        'autosizable': True,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'm3/s'}),
                                      (u'cooling design supply air flow rate per floor area',
                                       {'name': u'Cooling Design Supply Air Flow Rate Per Floor Area',
                                        'pyname': u'cooling_design_supply_air_flow_rate_per_floor_area',
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'm3/s-m2'}),
                                      (u'fraction of autosized cooling design supply air flow rate',
                                       {'name': u'Fraction of Autosized Cooling Design Supply Air Flow Rate',
                                        'pyname': u'fraction_of_autosized_cooling_design_supply_air_flow_rate',
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'cooling design supply air flow rate per unit cooling capacity',
                                       {'name': u'Cooling Design Supply Air Flow Rate Per Unit Cooling Capacity',
                                        'pyname': u'cooling_design_supply_air_flow_rate_per_unit_cooling_capacity',
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'm3/s-W'}),
                                      (u'supply air flow rate method when no cooling or heating is required',
                                       {'name': u'Supply Air Flow Rate Method When No Cooling or Heating is Required',
                                        'pyname': u'supply_air_flow_rate_method_when_no_cooling_or_heating_is_required',
                                        'default': u'SupplyAirFlowRate',
                                        'required-field': False,
                                        'autosizable': False,
                                        'accepted-values': [u'None',
                                                            u'SupplyAirFlowRate',
                                                            u'FlowPerFloorArea',
                                                            u'FractionOfAutosizedCoolingAirflow',
                                                            u'FractionOfAutosizedHeatingAirflow'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'supply air flow rate when no cooling or heating is required',
                                       {'name': u'Supply Air Flow Rate When No Cooling or Heating is Required',
                                        'pyname': u'supply_air_flow_rate_when_no_cooling_or_heating_is_required',
                                        'required-field': False,
                                        'autosizable': True,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'm3/s'}),
                                      (u'supply air flow rate per floor area when no clg or htg is required',
                                       {'name': u'Supply Air Flow Rate Per Floor Area When No Clg or Htg is Required',
                                        'pyname': u'supply_air_flow_rate_per_floor_area_when_no_clg_or_htg_is_required',
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'm3/s-m2'}),
                                      (u'fraction of design cooling supply air flow rate when no clg or htg required',
                                       {'name': u'Fraction of Design Cooling Supply Air Flow Rate When No Clg or Htg Required',
                                        'pyname': u'fraction_of_design_cooling_supply_air_flow_rate_when_no_clg_or_htg_required',
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'fraction of design heating supply air flow rate when no clg or htg required',
                                       {'name': u'Fraction of Design Heating Supply Air Flow Rate When No Clg or Htg Required',
                                        'pyname': u'fraction_of_design_heating_supply_air_flow_rate_when_no_clg_or_htg_required',
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'heating design air flow method',
                                       {'name': u'Heating Design Air Flow Method',
                                        'pyname': u'heating_design_air_flow_method',
                                        'default': u'SupplyAirFlowRate',
                                        'required-field': False,
                                        'autosizable': False,
                                        'accepted-values': [u'None',
                                                            u'SupplyAirFlowRate',
                                                            u'FlowPerFloorArea',
                                                            u'FractionOfAutosizedHeatingAirflow',
                                                            u'FlowPerHeatingCapacity'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'heating design supply air flow rate',
                                       {'name': u'Heating Design Supply Air Flow Rate',
                                        'pyname': u'heating_design_supply_air_flow_rate',
                                        'required-field': False,
                                        'autosizable': True,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'm3/s'}),
                                      (u'heating design supply air flow rate per floor area',
                                       {'name': u'Heating Design Supply Air Flow Rate Per Floor Area',
                                        'pyname': u'heating_design_supply_air_flow_rate_per_floor_area',
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'm3/s-m2'}),
                                      (u'fraction of heating design supply air flow rate',
                                       {'name': u'Fraction of Heating Design Supply Air Flow Rate',
                                        'pyname': u'fraction_of_heating_design_supply_air_flow_rate',
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'heating design supply air flow rate per unit heating capacity',
                                       {'name': u'Heating Design Supply Air Flow Rate Per Unit Heating Capacity',
                                        'pyname': u'heating_design_supply_air_flow_rate_per_unit_heating_capacity',
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'm3/s-W'}),
                                      (u'cooling design capacity method',
                                       {'name': u'Cooling Design Capacity Method',
                                        'pyname': u'cooling_design_capacity_method',
                                        'default': u'None',
                                        'required-field': False,
                                        'autosizable': False,
                                        'accepted-values': [u'None',
                                                            u'CoolingDesignCapacity',
                                                            u'CapacityPerFloorArea',
                                                            u'FractionOfAutosizedCoolingCapacity'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'cooling design capacity',
                                       {'name': u'Cooling Design Capacity',
                                        'pyname': u'cooling_design_capacity',
                                        'required-field': False,
                                        'autosizable': True,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'W'}),
                                      (u'cooling design capacity per floor area',
                                       {'name': u'Cooling Design Capacity Per Floor Area',
                                        'pyname': u'cooling_design_capacity_per_floor_area',
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'W/m2'}),
                                      (u'fraction of autosized cooling design capacity',
                                       {'name': u'Fraction of Autosized Cooling Design Capacity',
                                        'pyname': u'fraction_of_autosized_cooling_design_capacity',
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'heating design capacity method',
                                       {'name': u'Heating Design Capacity Method',
                                        'pyname': u'heating_design_capacity_method',
                                        'default': u'None',
                                        'required-field': False,
                                        'autosizable': False,
                                        'accepted-values': [u'None',
                                                            u'HeatingDesignCapacity',
                                                            u'CapacityPerFloorArea',
                                                            u'FractionOfAutosizedHeatingCapacity'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'heating design capacity',
                                       {'name': u'Heating Design Capacity',
                                        'pyname': u'heating_design_capacity',
                                        'required-field': False,
                                        'autosizable': True,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'W'}),
                                      (u'heating design capacity per floor area',
                                       {'name': u'Heating Design Capacity Per Floor Area',
                                        'pyname': u'heating_design_capacity_per_floor_area',
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'W/m2'}),
                                      (u'fraction of autosized heating design capacity',
                                       {'name': u'Fraction of Autosized Heating Design Capacity',
                                        'pyname': u'fraction_of_autosized_heating_design_capacity',
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real'})]),
               'format': None,
               'group': u'HVAC Design Objects',
               'min-fields': 1,
               'name': u'DesignSpecification:ZoneHVAC:Sizing',
               'pyname': u'DesignSpecificationZoneHvacSizing',
               'required-object': False,
               'unique-object': False}

    @property
    def name(self):
        """field `Name`

        Args:
            value (str): value for IDD Field `Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `name` or None if not set

        """
        return self["Name"]

    @name.setter
    def name(self, value=None):
        """Corresponds to IDD field `Name`"""
        self["Name"] = value

    @property
    def cooling_design_air_flow_method(self):
        """field `Cooling Design Air Flow Method`
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
                Default value: SupplyAirFlowRate

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `cooling_design_air_flow_method` or None if not set
        """
        return self["Cooling Design Air Flow Method"]

    @cooling_design_air_flow_method.setter
    def cooling_design_air_flow_method(self, value="SupplyAirFlowRate"):
        """Corresponds to IDD field `Cooling Design Air Flow Method`"""
        self["Cooling Design Air Flow Method"] = value

    @property
    def cooling_design_supply_air_flow_rate(self):
        """field `Cooling Design Supply Air Flow Rate` Enter the magnitude of
        supply air volume flow rate during cooling operation. Required field
        when Supply air Flow Rate Method During Cooling Operation is
        SupplyAirFlowRate. This field may be blank if a cooling coil is not
        included in the Zone HVAC equipment.

        Args:
            value (float or "Autosize"): value for IDD Field `Cooling Design Supply Air Flow Rate`
                Units: m3/s

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `cooling_design_supply_air_flow_rate` or None if not set

        """
        return self["Cooling Design Supply Air Flow Rate"]

    @cooling_design_supply_air_flow_rate.setter
    def cooling_design_supply_air_flow_rate(self, value=None):
        """Corresponds to IDD field `Cooling Design Supply Air Flow Rate`"""
        self["Cooling Design Supply Air Flow Rate"] = value

    @property
    def cooling_design_supply_air_flow_rate_per_floor_area(self):
        """field `Cooling Design Supply Air Flow Rate Per Floor Area` Enter the
        cooling supply air volume flow rate per total conditioned floor area.
        Required field when Supply air Flow Rate Method During Cooling
        Operation is FlowPerFloorArea. This field may be blank if a cooling
        coil is not included in the Zone HVAC equipment.

        Args:
            value (float): value for IDD Field `Cooling Design Supply Air Flow Rate Per Floor Area`
                Units: m3/s-m2

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `cooling_design_supply_air_flow_rate_per_floor_area` or None if not set

        """
        return self["Cooling Design Supply Air Flow Rate Per Floor Area"]

    @cooling_design_supply_air_flow_rate_per_floor_area.setter
    def cooling_design_supply_air_flow_rate_per_floor_area(self, value=None):
        """Corresponds to IDD field `Cooling Design Supply Air Flow Rate Per
        Floor Area`"""
        self["Cooling Design Supply Air Flow Rate Per Floor Area"] = value

    @property
    def fraction_of_autosized_cooling_design_supply_air_flow_rate(self):
        """field `Fraction of Autosized Cooling Design Supply Air Flow Rate`
        Enter the supply air volume flow rate as a fraction of the cooling
        supply air flow rate. Required field when Supply air Flow Rate Method
        During Cooling Operation is FractionOfAutosizedCoolingAirflow. This
        field may be blank if a cooling coil is not included in the Zone HVAC
        equipment.

        Args:
            value (float): value for IDD Field `Fraction of Autosized Cooling Design Supply Air Flow Rate`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `fraction_of_autosized_cooling_design_supply_air_flow_rate` or None if not set

        """
        return self[
            "Fraction of Autosized Cooling Design Supply Air Flow Rate"]

    @fraction_of_autosized_cooling_design_supply_air_flow_rate.setter
    def fraction_of_autosized_cooling_design_supply_air_flow_rate(
            self,
            value=None):
        """Corresponds to IDD field `Fraction of Autosized Cooling Design
        Supply Air Flow Rate`"""
        self[
            "Fraction of Autosized Cooling Design Supply Air Flow Rate"] = value

    @property
    def cooling_design_supply_air_flow_rate_per_unit_cooling_capacity(self):
        """field `Cooling Design Supply Air Flow Rate Per Unit Cooling
        Capacity` Enter the cooling supply air volume flow rate unit cooling
        capacity. Required field when Supply air Flow Rate Method During
        Cooling Operation is FlowPerCoolingCapacity. This field may be blank if
        a cooling coil is not included in the Zone HVAC equipment.

        Args:
            value (float): value for IDD Field `Cooling Design Supply Air Flow Rate Per Unit Cooling Capacity`
                Units: m3/s-W

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `cooling_design_supply_air_flow_rate_per_unit_cooling_capacity` or None if not set

        """
        return self[
            "Cooling Design Supply Air Flow Rate Per Unit Cooling Capacity"]

    @cooling_design_supply_air_flow_rate_per_unit_cooling_capacity.setter
    def cooling_design_supply_air_flow_rate_per_unit_cooling_capacity(
            self,
            value=None):
        """Corresponds to IDD field `Cooling Design Supply Air Flow Rate Per
        Unit Cooling Capacity`"""
        self[
            "Cooling Design Supply Air Flow Rate Per Unit Cooling Capacity"] = value

    @property
    def supply_air_flow_rate_method_when_no_cooling_or_heating_is_required(
            self):
        """field `Supply Air Flow Rate Method When No Cooling or Heating is Required`
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
                Default value: SupplyAirFlowRate

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `supply_air_flow_rate_method_when_no_cooling_or_heating_is_required` or None if not set
        """
        return self[
            "Supply Air Flow Rate Method When No Cooling or Heating is Required"]

    @supply_air_flow_rate_method_when_no_cooling_or_heating_is_required.setter
    def supply_air_flow_rate_method_when_no_cooling_or_heating_is_required(
            self,
            value="SupplyAirFlowRate"):
        """Corresponds to IDD field `Supply Air Flow Rate Method When No
        Cooling or Heating is Required`"""
        self[
            "Supply Air Flow Rate Method When No Cooling or Heating is Required"] = value

    @property
    def supply_air_flow_rate_when_no_cooling_or_heating_is_required(self):
        """field `Supply Air Flow Rate When No Cooling or Heating is Required`
        Enter the magnitude of the supply air volume flow rate during when no
        cooling or heating is required. Required field when Supply air Flow
        Rate Method When No Cooling or Heating is Required is
        SupplyAirFlowRate.

        Args:
            value (float or "Autosize"): value for IDD Field `Supply Air Flow Rate When No Cooling or Heating is Required`
                Units: m3/s

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `supply_air_flow_rate_when_no_cooling_or_heating_is_required` or None if not set

        """
        return self[
            "Supply Air Flow Rate When No Cooling or Heating is Required"]

    @supply_air_flow_rate_when_no_cooling_or_heating_is_required.setter
    def supply_air_flow_rate_when_no_cooling_or_heating_is_required(
            self,
            value=None):
        """Corresponds to IDD field `Supply Air Flow Rate When No Cooling or
        Heating is Required`"""
        self[
            "Supply Air Flow Rate When No Cooling or Heating is Required"] = value

    @property
    def supply_air_flow_rate_per_floor_area_when_no_clg_or_htg_is_required(
            self):
        """field `Supply Air Flow Rate Per Floor Area When No Clg or Htg is
        Required` Enter the supply air volume flow rate per total floor area.
        Required field when Supply air Flow Rate Method When No Cooling or
        Heating is Required is FlowPerFloorArea.

        Args:
            value (float): value for IDD Field `Supply Air Flow Rate Per Floor Area When No Clg or Htg is Required`
                Units: m3/s-m2

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `supply_air_flow_rate_per_floor_area_when_no_clg_or_htg_is_required` or None if not set

        """
        return self[
            "Supply Air Flow Rate Per Floor Area When No Clg or Htg is Required"]

    @supply_air_flow_rate_per_floor_area_when_no_clg_or_htg_is_required.setter
    def supply_air_flow_rate_per_floor_area_when_no_clg_or_htg_is_required(
            self,
            value=None):
        """Corresponds to IDD field `Supply Air Flow Rate Per Floor Area When
        No Clg or Htg is Required`"""
        self[
            "Supply Air Flow Rate Per Floor Area When No Clg or Htg is Required"] = value

    @property
    def fraction_of_design_cooling_supply_air_flow_rate_when_no_clg_or_htg_required(
            self):
        """field `Fraction of Design Cooling Supply Air Flow Rate When No Clg
        or Htg Required` Enter the supply air volume flow rate as a fraction of
        the cooling supply air flow rate. Required field when Supply air Flow
        Rate Method When No Cooling or Heating is Required is
        FractionOfAutosizedCoolingAirflow.

        Args:
            value (float): value for IDD Field `Fraction of Design Cooling Supply Air Flow Rate When No Clg or Htg Required`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `fraction_of_design_cooling_supply_air_flow_rate_when_no_clg_or_htg_required` or None if not set

        """
        return self[
            "Fraction of Design Cooling Supply Air Flow Rate When No Clg or Htg Required"]

    @fraction_of_design_cooling_supply_air_flow_rate_when_no_clg_or_htg_required.setter
    def fraction_of_design_cooling_supply_air_flow_rate_when_no_clg_or_htg_required(
            self,
            value=None):
        """Corresponds to IDD field `Fraction of Design Cooling Supply Air Flow
        Rate When No Clg or Htg Required`"""
        self[
            "Fraction of Design Cooling Supply Air Flow Rate When No Clg or Htg Required"] = value

    @property
    def fraction_of_design_heating_supply_air_flow_rate_when_no_clg_or_htg_required(
            self):
        """field `Fraction of Design Heating Supply Air Flow Rate When No Clg
        or Htg Required` Enter the supply air volume flow rate as a fraction of
        the heating supply air flow rate. Required field when Supply air Flow
        Rate Method When No Cooling or Heating is Required is
        FractionOfAutosizedHeatingAirflow.

        Args:
            value (float): value for IDD Field `Fraction of Design Heating Supply Air Flow Rate When No Clg or Htg Required`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `fraction_of_design_heating_supply_air_flow_rate_when_no_clg_or_htg_required` or None if not set

        """
        return self[
            "Fraction of Design Heating Supply Air Flow Rate When No Clg or Htg Required"]

    @fraction_of_design_heating_supply_air_flow_rate_when_no_clg_or_htg_required.setter
    def fraction_of_design_heating_supply_air_flow_rate_when_no_clg_or_htg_required(
            self,
            value=None):
        """Corresponds to IDD field `Fraction of Design Heating Supply Air Flow
        Rate When No Clg or Htg Required`"""
        self[
            "Fraction of Design Heating Supply Air Flow Rate When No Clg or Htg Required"] = value

    @property
    def heating_design_air_flow_method(self):
        """field `Heating Design Air Flow Method`
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
                Default value: SupplyAirFlowRate

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `heating_design_air_flow_method` or None if not set
        """
        return self["Heating Design Air Flow Method"]

    @heating_design_air_flow_method.setter
    def heating_design_air_flow_method(self, value="SupplyAirFlowRate"):
        """Corresponds to IDD field `Heating Design Air Flow Method`"""
        self["Heating Design Air Flow Method"] = value

    @property
    def heating_design_supply_air_flow_rate(self):
        """field `Heating Design Supply Air Flow Rate` Enter the magnitude of
        the supply air volume flow rate during heating operation. Required
        field when Supply air Flow Rate Method During Heating Operation is
        SupplyAirFlowRate. This field may be blank if a heating coil is not
        included in the Zone HVAC equipment.

        Args:
            value (float or "Autosize"): value for IDD Field `Heating Design Supply Air Flow Rate`
                Units: m3/s

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `heating_design_supply_air_flow_rate` or None if not set

        """
        return self["Heating Design Supply Air Flow Rate"]

    @heating_design_supply_air_flow_rate.setter
    def heating_design_supply_air_flow_rate(self, value=None):
        """Corresponds to IDD field `Heating Design Supply Air Flow Rate`"""
        self["Heating Design Supply Air Flow Rate"] = value

    @property
    def heating_design_supply_air_flow_rate_per_floor_area(self):
        """field `Heating Design Supply Air Flow Rate Per Floor Area` Enter the
        heating supply air volume flow rate per total conditioned floor area.
        Required field when Supply air Flow Rate Method During Heating
        Operation is FlowPerFloorArea. This field may be blank if a heating
        coil is not included in the Zone HVAC equipment.

        Args:
            value (float): value for IDD Field `Heating Design Supply Air Flow Rate Per Floor Area`
                Units: m3/s-m2

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `heating_design_supply_air_flow_rate_per_floor_area` or None if not set

        """
        return self["Heating Design Supply Air Flow Rate Per Floor Area"]

    @heating_design_supply_air_flow_rate_per_floor_area.setter
    def heating_design_supply_air_flow_rate_per_floor_area(self, value=None):
        """Corresponds to IDD field `Heating Design Supply Air Flow Rate Per
        Floor Area`"""
        self["Heating Design Supply Air Flow Rate Per Floor Area"] = value

    @property
    def fraction_of_heating_design_supply_air_flow_rate(self):
        """field `Fraction of Heating Design Supply Air Flow Rate` Enter the
        supply air volume flow rate as a fraction of the heating supply air
        flow rate. Required field when Supply air Flow Rate Method During
        Heating Operation is FractionOfAutosizedHeatingAirflow. This field may
        be blank if a heating coil is not included in the Zone HVAC equipment.

        Args:
            value (float): value for IDD Field `Fraction of Heating Design Supply Air Flow Rate`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `fraction_of_heating_design_supply_air_flow_rate` or None if not set

        """
        return self["Fraction of Heating Design Supply Air Flow Rate"]

    @fraction_of_heating_design_supply_air_flow_rate.setter
    def fraction_of_heating_design_supply_air_flow_rate(self, value=None):
        """Corresponds to IDD field `Fraction of Heating Design Supply Air Flow
        Rate`"""
        self["Fraction of Heating Design Supply Air Flow Rate"] = value

    @property
    def heating_design_supply_air_flow_rate_per_unit_heating_capacity(self):
        """field `Heating Design Supply Air Flow Rate Per Unit Heating
        Capacity` Enter the supply air volume flow rate per unit heating
        capacity. Required field when Supply air Flow Rate Method During
        Heating Operation is FlowPerHeatingCapacity. This field may be blank if
        a heating coil is not included in the Zone HVAC equipment.

        Args:
            value (float): value for IDD Field `Heating Design Supply Air Flow Rate Per Unit Heating Capacity`
                Units: m3/s-W

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `heating_design_supply_air_flow_rate_per_unit_heating_capacity` or None if not set

        """
        return self[
            "Heating Design Supply Air Flow Rate Per Unit Heating Capacity"]

    @heating_design_supply_air_flow_rate_per_unit_heating_capacity.setter
    def heating_design_supply_air_flow_rate_per_unit_heating_capacity(
            self,
            value=None):
        """Corresponds to IDD field `Heating Design Supply Air Flow Rate Per
        Unit Heating Capacity`"""
        self[
            "Heating Design Supply Air Flow Rate Per Unit Heating Capacity"] = value

    @property
    def cooling_design_capacity_method(self):
        """field `Cooling Design Capacity Method`
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
                Default value: None

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `cooling_design_capacity_method` or None if not set
        """
        return self["Cooling Design Capacity Method"]

    @cooling_design_capacity_method.setter
    def cooling_design_capacity_method(self, value="None"):
        """Corresponds to IDD field `Cooling Design Capacity Method`"""
        self["Cooling Design Capacity Method"] = value

    @property
    def cooling_design_capacity(self):
        """field `Cooling Design Capacity` Enter the design cooling capacity.
        Required field when the cooling design capacity method
        CoolingDesignCapacity.

        Args:
            value (float or "Autosize"): value for IDD Field `Cooling Design Capacity`
                Units: W

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `cooling_design_capacity` or None if not set

        """
        return self["Cooling Design Capacity"]

    @cooling_design_capacity.setter
    def cooling_design_capacity(self, value=None):
        """Corresponds to IDD field `Cooling Design Capacity`"""
        self["Cooling Design Capacity"] = value

    @property
    def cooling_design_capacity_per_floor_area(self):
        """field `Cooling Design Capacity Per Floor Area` Enter the cooling
        design capacity per zone floor area. Required field when the cooling
        design capacity method field is CapacityPerFloorArea.

        Args:
            value (float): value for IDD Field `Cooling Design Capacity Per Floor Area`
                Units: W/m2

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `cooling_design_capacity_per_floor_area` or None if not set

        """
        return self["Cooling Design Capacity Per Floor Area"]

    @cooling_design_capacity_per_floor_area.setter
    def cooling_design_capacity_per_floor_area(self, value=None):
        """Corresponds to IDD field `Cooling Design Capacity Per Floor Area`"""
        self["Cooling Design Capacity Per Floor Area"] = value

    @property
    def fraction_of_autosized_cooling_design_capacity(self):
        """field `Fraction of Autosized Cooling Design Capacity`
        Enter the fraction of auto-sized cooling design capacity. Required field when the cooling
        design capacity method field is FractionOfAutosizedCoolingCapacity.

        Args:
            value (float): value for IDD Field `Fraction of Autosized Cooling Design Capacity`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `fraction_of_autosized_cooling_design_capacity` or None if not set
        """
        return self["Fraction of Autosized Cooling Design Capacity"]

    @fraction_of_autosized_cooling_design_capacity.setter
    def fraction_of_autosized_cooling_design_capacity(self, value=None):
        """Corresponds to IDD field `Fraction of Autosized Cooling Design
        Capacity`"""
        self["Fraction of Autosized Cooling Design Capacity"] = value

    @property
    def heating_design_capacity_method(self):
        """field `Heating Design Capacity Method`
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
                Default value: None

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `heating_design_capacity_method` or None if not set
        """
        return self["Heating Design Capacity Method"]

    @heating_design_capacity_method.setter
    def heating_design_capacity_method(self, value="None"):
        """Corresponds to IDD field `Heating Design Capacity Method`"""
        self["Heating Design Capacity Method"] = value

    @property
    def heating_design_capacity(self):
        """field `Heating Design Capacity` Enter the design heating capacity.
        Required field when the heating design capacity method
        HeatingDesignCapacity.

        Args:
            value (float or "Autosize"): value for IDD Field `Heating Design Capacity`
                Units: W

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `heating_design_capacity` or None if not set

        """
        return self["Heating Design Capacity"]

    @heating_design_capacity.setter
    def heating_design_capacity(self, value=None):
        """Corresponds to IDD field `Heating Design Capacity`"""
        self["Heating Design Capacity"] = value

    @property
    def heating_design_capacity_per_floor_area(self):
        """field `Heating Design Capacity Per Floor Area` Enter the heating
        design capacity per zone floor area. Required field when the heating
        design capacity method field is CapacityPerFloorArea.

        Args:
            value (float): value for IDD Field `Heating Design Capacity Per Floor Area`
                Units: W/m2

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `heating_design_capacity_per_floor_area` or None if not set

        """
        return self["Heating Design Capacity Per Floor Area"]

    @heating_design_capacity_per_floor_area.setter
    def heating_design_capacity_per_floor_area(self, value=None):
        """Corresponds to IDD field `Heating Design Capacity Per Floor Area`"""
        self["Heating Design Capacity Per Floor Area"] = value

    @property
    def fraction_of_autosized_heating_design_capacity(self):
        """field `Fraction of Autosized Heating Design Capacity`
        Enter the fraction of auto-sized heating design capacity. Required field when capacity the
        heating design capacity method field is FractionOfAutosizedHeatingCapacity.

        Args:
            value (float): value for IDD Field `Fraction of Autosized Heating Design Capacity`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `fraction_of_autosized_heating_design_capacity` or None if not set
        """
        return self["Fraction of Autosized Heating Design Capacity"]

    @fraction_of_autosized_heating_design_capacity.setter
    def fraction_of_autosized_heating_design_capacity(self, value=None):
        """Corresponds to IDD field `Fraction of Autosized Heating Design
        Capacity`"""
        self["Fraction of Autosized Heating Design Capacity"] = value




class SizingSystem(DataObject):

    """ Corresponds to IDD object `Sizing:System`
        Specifies the input needed to perform sizing calculations for a central forced air
        system design air flow, heating capacity, and cooling capacity.
    """
    _schema = {'extensible-fields': OrderedDict(),
               'fields': OrderedDict([(u'airloop name',
                                       {'name': u'AirLoop Name',
                                        'pyname': u'airloop_name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'type of load to size on',
                                       {'name': u'Type of Load to Size On',
                                        'pyname': u'type_of_load_to_size_on',
                                        'default': u'Sensible',
                                        'required-field': True,
                                        'autosizable': False,
                                        'accepted-values': [u'Sensible',
                                                            u'VentilationRequirement'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'design outdoor air flow rate',
                                       {'name': u'Design Outdoor Air Flow Rate',
                                        'pyname': u'design_outdoor_air_flow_rate',
                                        'default': 'autosize',
                                        'required-field': False,
                                        'autosizable': True,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'm3/s'}),
                                      (u'minimum system air flow ratio',
                                       {'name': u'Minimum System Air Flow Ratio',
                                        'pyname': u'minimum_system_air_flow_ratio',
                                        'maximum': 1.0,
                                        'required-field': True,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'preheat design temperature',
                                       {'name': u'Preheat Design Temperature',
                                        'pyname': u'preheat_design_temperature',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'C'}),
                                      (u'preheat design humidity ratio',
                                       {'name': u'Preheat Design Humidity Ratio',
                                        'pyname': u'preheat_design_humidity_ratio',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'kgWater/kgDryAir'}),
                                      (u'precool design temperature',
                                       {'name': u'Precool Design Temperature',
                                        'pyname': u'precool_design_temperature',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'C'}),
                                      (u'precool design humidity ratio',
                                       {'name': u'Precool Design Humidity Ratio',
                                        'pyname': u'precool_design_humidity_ratio',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'kgWater/kgDryAir'}),
                                      (u'central cooling design supply air temperature',
                                       {'name': u'Central Cooling Design Supply Air Temperature',
                                        'pyname': u'central_cooling_design_supply_air_temperature',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'C'}),
                                      (u'central heating design supply air temperature',
                                       {'name': u'Central Heating Design Supply Air Temperature',
                                        'pyname': u'central_heating_design_supply_air_temperature',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'C'}),
                                      (u'sizing option',
                                       {'name': u'Sizing Option',
                                        'pyname': u'sizing_option',
                                        'default': u'NonCoincident',
                                        'required-field': False,
                                        'autosizable': False,
                                        'accepted-values': [u'Coincident',
                                                            u'NonCoincident'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'100% outdoor air in cooling',
                                       {'name': u'100% Outdoor Air in Cooling',
                                        'pyname': u'a_100_outdoor_air_in_cooling',
                                        'default': u'No',
                                        'required-field': False,
                                        'autosizable': False,
                                        'accepted-values': [u'Yes',
                                                            u'No'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'100% outdoor air in heating',
                                       {'name': u'100% Outdoor Air in Heating',
                                        'pyname': u'a_100_outdoor_air_in_heating',
                                        'default': u'No',
                                        'required-field': False,
                                        'autosizable': False,
                                        'accepted-values': [u'Yes',
                                                            u'No'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'central cooling design supply air humidity ratio',
                                       {'name': u'Central Cooling Design Supply Air Humidity Ratio',
                                        'pyname': u'central_cooling_design_supply_air_humidity_ratio',
                                        'default': 0.008,
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'kgWater/kgDryAir'}),
                                      (u'central heating design supply air humidity ratio',
                                       {'name': u'Central Heating Design Supply Air Humidity Ratio',
                                        'pyname': u'central_heating_design_supply_air_humidity_ratio',
                                        'default': 0.008,
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'kgWater/kgDryAir'}),
                                      (u'cooling design air flow method',
                                       {'name': u'Cooling Design Air Flow Method',
                                        'pyname': u'cooling_design_air_flow_method',
                                        'default': u'DesignDay',
                                        'required-field': False,
                                        'autosizable': False,
                                        'accepted-values': [u'Flow/System',
                                                            u'DesignDay',
                                                            u'FlowPerFloorArea',
                                                            u'FractionOfAutosizedCoolingAirflow',
                                                            u'FlowPerCoolingCapacity'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'cooling design air flow rate',
                                       {'name': u'Cooling Design Air Flow Rate',
                                        'pyname': u'cooling_design_air_flow_rate',
                                        'default': 0.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'm3/s'}),
                                      (u'supply air flow rate per floor area during cooling operation',
                                       {'name': u'Supply Air Flow Rate Per Floor Area During Cooling Operation',
                                        'pyname': u'supply_air_flow_rate_per_floor_area_during_cooling_operation',
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'm3/s-m2'}),
                                      (u'fraction of autosized design cooling supply air flow rate',
                                       {'name': u'Fraction of Autosized Design Cooling Supply Air Flow Rate',
                                        'pyname': u'fraction_of_autosized_design_cooling_supply_air_flow_rate',
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'design supply air flow rate per unit cooling capacity',
                                       {'name': u'Design Supply Air Flow Rate Per Unit Cooling Capacity',
                                        'pyname': u'design_supply_air_flow_rate_per_unit_cooling_capacity',
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'm3/s-W'}),
                                      (u'heating design air flow method',
                                       {'name': u'Heating Design Air Flow Method',
                                        'pyname': u'heating_design_air_flow_method',
                                        'default': u'DesignDay',
                                        'required-field': False,
                                        'autosizable': False,
                                        'accepted-values': [u'Flow/System',
                                                            u'DesignDay',
                                                            u'FlowPerFloorArea',
                                                            u'FractionOfAutosizedHeatingAirflow',
                                                            u'FractionOfAutosizedCoolingAirflow',
                                                            u'FlowPerCoolingCapacity'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'heating design air flow rate',
                                       {'name': u'Heating Design Air Flow Rate',
                                        'pyname': u'heating_design_air_flow_rate',
                                        'default': 0.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'm3/s'}),
                                      (u'supply air flow rate per floor area during heating operation',
                                       {'name': u'Supply Air Flow Rate Per Floor Area During Heating Operation',
                                        'pyname': u'supply_air_flow_rate_per_floor_area_during_heating_operation',
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'm3/s-m2'}),
                                      (u'fraction of autosized design heating supply air flow rate',
                                       {'name': u'Fraction of Autosized Design Heating Supply Air Flow Rate',
                                        'pyname': u'fraction_of_autosized_design_heating_supply_air_flow_rate',
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      ('fraction of autosized design cooling supply air flow rate v3',
                                       {'name': 'Fraction of Autosized Design Cooling Supply Air Flow Rate v3',
                                        'pyname': 'fraction_of_autosized_design_cooling_supply_air_flow_rate_v3',
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'design supply air flow rate per unit heating capacity',
                                       {'name': u'Design Supply Air Flow Rate Per Unit Heating Capacity',
                                        'pyname': u'design_supply_air_flow_rate_per_unit_heating_capacity',
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'm3/s-W'}),
                                      (u'system outdoor air method',
                                       {'name': u'System Outdoor Air Method',
                                        'pyname': u'system_outdoor_air_method',
                                        'default': u'ZoneSum',
                                        'required-field': False,
                                        'autosizable': False,
                                        'accepted-values': [u'ZoneSum',
                                                            u'VentilationRateProcedure'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'zone maximum outdoor air fraction',
                                       {'name': u'Zone Maximum Outdoor Air Fraction',
                                        'pyname': u'zone_maximum_outdoor_air_fraction',
                                        'default': 1.0,
                                        'minimum>': 0.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'dimensionless'}),
                                      (u'cooling design capacity method',
                                       {'name': u'Cooling Design Capacity Method',
                                        'pyname': u'cooling_design_capacity_method',
                                        'default': u'CoolingDesignCapacity',
                                        'required-field': False,
                                        'autosizable': False,
                                        'accepted-values': [u'None',
                                                            u'CoolingDesignCapacity',
                                                            u'CapacityPerFloorArea',
                                                            u'FractionOfAutosizedCoolingCapacity'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'cooling design capacity',
                                       {'name': u'Cooling Design Capacity',
                                        'pyname': u'cooling_design_capacity',
                                        'default': 'autosize',
                                        'required-field': False,
                                        'autosizable': True,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'W'}),
                                      (u'cooling design capacity per floor area',
                                       {'name': u'Cooling Design Capacity Per Floor Area',
                                        'pyname': u'cooling_design_capacity_per_floor_area',
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'W/m2'}),
                                      (u'fraction of autosized cooling design capacity',
                                       {'name': u'Fraction of Autosized Cooling Design Capacity',
                                        'pyname': u'fraction_of_autosized_cooling_design_capacity',
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'heating design capacity method',
                                       {'name': u'Heating Design Capacity Method',
                                        'pyname': u'heating_design_capacity_method',
                                        'default': u'HeatingDesignCapacity',
                                        'required-field': False,
                                        'autosizable': False,
                                        'accepted-values': [u'None',
                                                            u'HeatingDesignCapacity',
                                                            u'CapacityPerFloorArea',
                                                            u'FractionOfAutosizedHeatingCapacity'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'heating design capacity',
                                       {'name': u'Heating Design Capacity',
                                        'pyname': u'heating_design_capacity',
                                        'default': 'autosize',
                                        'required-field': False,
                                        'autosizable': True,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'W'}),
                                      (u'heating design capacity per floor area',
                                       {'name': u'Heating Design Capacity Per Floor Area',
                                        'pyname': u'heating_design_capacity_per_floor_area',
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'W/m2'}),
                                      (u'fraction of autosized heating design capacity',
                                       {'name': u'Fraction of Autosized Heating Design Capacity',
                                        'pyname': u'fraction_of_autosized_heating_design_capacity',
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real'})]),
               'format': None,
               'group': u'HVAC Design Objects',
               'min-fields': 27,
               'name': u'Sizing:System',
               'pyname': u'SizingSystem',
               'required-object': False,
               'unique-object': False}

    @property
    def airloop_name(self):
        """field `AirLoop Name`

        Args:
            value (str): value for IDD Field `AirLoop Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `airloop_name` or None if not set

        """
        return self["AirLoop Name"]

    @airloop_name.setter
    def airloop_name(self, value=None):
        """Corresponds to IDD field `AirLoop Name`"""
        self["AirLoop Name"] = value

    @property
    def type_of_load_to_size_on(self):
        """field `Type of Load to Size On` Specifies the basis for sizing the
        system supply air flow rate Sensible and VentilationRequirement are the
        only available options Sensible uses the zone design air flow rates
        VentilationRequirement uses the system ventilation requirement.

        Args:
            value (str): value for IDD Field `Type of Load to Size On`
                Default value: Sensible

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `type_of_load_to_size_on` or None if not set

        """
        return self["Type of Load to Size On"]

    @type_of_load_to_size_on.setter
    def type_of_load_to_size_on(self, value="Sensible"):
        """Corresponds to IDD field `Type of Load to Size On`"""
        self["Type of Load to Size On"] = value

    @property
    def design_outdoor_air_flow_rate(self):
        """field `Design Outdoor Air Flow Rate`

        Args:
            value (float or "Autosize"): value for IDD Field `Design Outdoor Air Flow Rate`
                Units: m3/s
                Default value: "autosize"

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `design_outdoor_air_flow_rate` or None if not set

        """
        return self["Design Outdoor Air Flow Rate"]

    @design_outdoor_air_flow_rate.setter
    def design_outdoor_air_flow_rate(self, value="autosize"):
        """Corresponds to IDD field `Design Outdoor Air Flow Rate`"""
        self["Design Outdoor Air Flow Rate"] = value

    @property
    def minimum_system_air_flow_ratio(self):
        """field `Minimum System Air Flow Ratio`

        Args:
            value (float): value for IDD Field `Minimum System Air Flow Ratio`
                value <= 1.0

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `minimum_system_air_flow_ratio` or None if not set

        """
        return self["Minimum System Air Flow Ratio"]

    @minimum_system_air_flow_ratio.setter
    def minimum_system_air_flow_ratio(self, value=None):
        """Corresponds to IDD field `Minimum System Air Flow Ratio`"""
        self["Minimum System Air Flow Ratio"] = value

    @property
    def preheat_design_temperature(self):
        """field `Preheat Design Temperature`

        Args:
            value (float): value for IDD Field `Preheat Design Temperature`
                Units: C

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `preheat_design_temperature` or None if not set

        """
        return self["Preheat Design Temperature"]

    @preheat_design_temperature.setter
    def preheat_design_temperature(self, value=None):
        """Corresponds to IDD field `Preheat Design Temperature`"""
        self["Preheat Design Temperature"] = value

    @property
    def preheat_design_humidity_ratio(self):
        """field `Preheat Design Humidity Ratio`

        Args:
            value (float): value for IDD Field `Preheat Design Humidity Ratio`
                Units: kgWater/kgDryAir

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `preheat_design_humidity_ratio` or None if not set

        """
        return self["Preheat Design Humidity Ratio"]

    @preheat_design_humidity_ratio.setter
    def preheat_design_humidity_ratio(self, value=None):
        """Corresponds to IDD field `Preheat Design Humidity Ratio`"""
        self["Preheat Design Humidity Ratio"] = value

    @property
    def precool_design_temperature(self):
        """field `Precool Design Temperature`

        Args:
            value (float): value for IDD Field `Precool Design Temperature`
                Units: C

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `precool_design_temperature` or None if not set

        """
        return self["Precool Design Temperature"]

    @precool_design_temperature.setter
    def precool_design_temperature(self, value=None):
        """Corresponds to IDD field `Precool Design Temperature`"""
        self["Precool Design Temperature"] = value

    @property
    def precool_design_humidity_ratio(self):
        """field `Precool Design Humidity Ratio`

        Args:
            value (float): value for IDD Field `Precool Design Humidity Ratio`
                Units: kgWater/kgDryAir

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `precool_design_humidity_ratio` or None if not set

        """
        return self["Precool Design Humidity Ratio"]

    @precool_design_humidity_ratio.setter
    def precool_design_humidity_ratio(self, value=None):
        """Corresponds to IDD field `Precool Design Humidity Ratio`"""
        self["Precool Design Humidity Ratio"] = value

    @property
    def central_cooling_design_supply_air_temperature(self):
        """field `Central Cooling Design Supply Air Temperature`

        Args:
            value (float): value for IDD Field `Central Cooling Design Supply Air Temperature`
                Units: C

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `central_cooling_design_supply_air_temperature` or None if not set

        """
        return self["Central Cooling Design Supply Air Temperature"]

    @central_cooling_design_supply_air_temperature.setter
    def central_cooling_design_supply_air_temperature(self, value=None):
        """Corresponds to IDD field `Central Cooling Design Supply Air
        Temperature`"""
        self["Central Cooling Design Supply Air Temperature"] = value

    @property
    def central_heating_design_supply_air_temperature(self):
        """field `Central Heating Design Supply Air Temperature`

        Args:
            value (float): value for IDD Field `Central Heating Design Supply Air Temperature`
                Units: C

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `central_heating_design_supply_air_temperature` or None if not set

        """
        return self["Central Heating Design Supply Air Temperature"]

    @central_heating_design_supply_air_temperature.setter
    def central_heating_design_supply_air_temperature(self, value=None):
        """Corresponds to IDD field `Central Heating Design Supply Air
        Temperature`"""
        self["Central Heating Design Supply Air Temperature"] = value

    @property
    def sizing_option(self):
        """field `Sizing Option`

        Args:
            value (str): value for IDD Field `Sizing Option`
                Default value: NonCoincident

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `sizing_option` or None if not set

        """
        return self["Sizing Option"]

    @sizing_option.setter
    def sizing_option(self, value="NonCoincident"):
        """Corresponds to IDD field `Sizing Option`"""
        self["Sizing Option"] = value

    @property
    def a_100_outdoor_air_in_cooling(self):
        """field `100% Outdoor Air in Cooling`

        Args:
            value (str): value for IDD Field `100% Outdoor Air in Cooling`
                Default value: No

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `a_100_outdoor_air_in_cooling` or None if not set

        """
        return self["100% Outdoor Air in Cooling"]

    @a_100_outdoor_air_in_cooling.setter
    def a_100_outdoor_air_in_cooling(self, value="No"):
        """Corresponds to IDD field `100% Outdoor Air in Cooling`"""
        self["100% Outdoor Air in Cooling"] = value

    @property
    def a_100_outdoor_air_in_heating(self):
        """field `100% Outdoor Air in Heating`

        Args:
            value (str): value for IDD Field `100% Outdoor Air in Heating`
                Default value: No

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `a_100_outdoor_air_in_heating` or None if not set

        """
        return self["100% Outdoor Air in Heating"]

    @a_100_outdoor_air_in_heating.setter
    def a_100_outdoor_air_in_heating(self, value="No"):
        """Corresponds to IDD field `100% Outdoor Air in Heating`"""
        self["100% Outdoor Air in Heating"] = value

    @property
    def central_cooling_design_supply_air_humidity_ratio(self):
        """field `Central Cooling Design Supply Air Humidity Ratio`

        Args:
            value (float): value for IDD Field `Central Cooling Design Supply Air Humidity Ratio`
                Units: kgWater/kgDryAir
                Default value: 0.008

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `central_cooling_design_supply_air_humidity_ratio` or None if not set

        """
        return self["Central Cooling Design Supply Air Humidity Ratio"]

    @central_cooling_design_supply_air_humidity_ratio.setter
    def central_cooling_design_supply_air_humidity_ratio(self, value=0.008):
        """Corresponds to IDD field `Central Cooling Design Supply Air Humidity
        Ratio`"""
        self["Central Cooling Design Supply Air Humidity Ratio"] = value

    @property
    def central_heating_design_supply_air_humidity_ratio(self):
        """field `Central Heating Design Supply Air Humidity Ratio`

        Args:
            value (float): value for IDD Field `Central Heating Design Supply Air Humidity Ratio`
                Units: kgWater/kgDryAir
                Default value: 0.008

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `central_heating_design_supply_air_humidity_ratio` or None if not set

        """
        return self["Central Heating Design Supply Air Humidity Ratio"]

    @central_heating_design_supply_air_humidity_ratio.setter
    def central_heating_design_supply_air_humidity_ratio(self, value=0.008):
        """Corresponds to IDD field `Central Heating Design Supply Air Humidity
        Ratio`"""
        self["Central Heating Design Supply Air Humidity Ratio"] = value

    @property
    def cooling_design_air_flow_method(self):
        """field `Cooling Design Air Flow Method`

        Args:
            value (str): value for IDD Field `Cooling Design Air Flow Method`
                Default value: DesignDay

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `cooling_design_air_flow_method` or None if not set

        """
        return self["Cooling Design Air Flow Method"]

    @cooling_design_air_flow_method.setter
    def cooling_design_air_flow_method(self, value="DesignDay"):
        """Corresponds to IDD field `Cooling Design Air Flow Method`"""
        self["Cooling Design Air Flow Method"] = value

    @property
    def cooling_design_air_flow_rate(self):
        """field `Cooling Design Air Flow Rate`
        This input is used if Cooling Design Air Flow Method is Flow/System
        This value will *not* be multiplied by any sizing factor or by zone multipliers.
        If using zone multipliers, this value must be large enough to serve the multiplied zones.

        Args:
            value (float): value for IDD Field `Cooling Design Air Flow Rate`
                Units: m3/s

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `cooling_design_air_flow_rate` or None if not set
        """
        return self["Cooling Design Air Flow Rate"]

    @cooling_design_air_flow_rate.setter
    def cooling_design_air_flow_rate(self, value=None):
        """Corresponds to IDD field `Cooling Design Air Flow Rate`"""
        self["Cooling Design Air Flow Rate"] = value

    @property
    def supply_air_flow_rate_per_floor_area_during_cooling_operation(self):
        """field `Supply Air Flow Rate Per Floor Area During Cooling Operation`
        Enter the cooling supply air volume flow rate per total conditioned
        floor area. Required field when Supply air Flow Rate Method during
        cooling operation is FlowPerFloorArea.

        Args:
            value (float): value for IDD Field `Supply Air Flow Rate Per Floor Area During Cooling Operation`
                Units: m3/s-m2

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `supply_air_flow_rate_per_floor_area_during_cooling_operation` or None if not set

        """
        return self[
            "Supply Air Flow Rate Per Floor Area During Cooling Operation"]

    @supply_air_flow_rate_per_floor_area_during_cooling_operation.setter
    def supply_air_flow_rate_per_floor_area_during_cooling_operation(
            self,
            value=None):
        """Corresponds to IDD field `Supply Air Flow Rate Per Floor Area During
        Cooling Operation`"""
        self[
            "Supply Air Flow Rate Per Floor Area During Cooling Operation"] = value

    @property
    def fraction_of_autosized_design_cooling_supply_air_flow_rate(self):
        """field `Fraction of Autosized Design Cooling Supply Air Flow Rate`
        Enter the supply air volume flow rate as a fraction of the cooling
        supply air flow rate. Required field when Supply air Flow Rate Method
        during cooling operation is FractionOfAutosizedCoolingAirflow.

        Args:
            value (float): value for IDD Field `Fraction of Autosized Design Cooling Supply Air Flow Rate`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `fraction_of_autosized_design_cooling_supply_air_flow_rate` or None if not set

        """
        return self[
            "Fraction of Autosized Design Cooling Supply Air Flow Rate"]

    @fraction_of_autosized_design_cooling_supply_air_flow_rate.setter
    def fraction_of_autosized_design_cooling_supply_air_flow_rate(
            self,
            value=None):
        """Corresponds to IDD field `Fraction of Autosized Design Cooling
        Supply Air Flow Rate`"""
        self[
            "Fraction of Autosized Design Cooling Supply Air Flow Rate"] = value

    @property
    def design_supply_air_flow_rate_per_unit_cooling_capacity(self):
        """field `Design Supply Air Flow Rate Per Unit Cooling Capacity` Enter
        the supply air volume flow rate per unit cooling capacity. Required
        field when Supply air Flow Rate Method During Cooling Operation is
        FlowPerCoolingCapacity.

        Args:
            value (float): value for IDD Field `Design Supply Air Flow Rate Per Unit Cooling Capacity`
                Units: m3/s-W

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `design_supply_air_flow_rate_per_unit_cooling_capacity` or None if not set

        """
        return self["Design Supply Air Flow Rate Per Unit Cooling Capacity"]

    @design_supply_air_flow_rate_per_unit_cooling_capacity.setter
    def design_supply_air_flow_rate_per_unit_cooling_capacity(
            self,
            value=None):
        """Corresponds to IDD field `Design Supply Air Flow Rate Per Unit
        Cooling Capacity`"""
        self["Design Supply Air Flow Rate Per Unit Cooling Capacity"] = value

    @property
    def heating_design_air_flow_method(self):
        """field `Heating Design Air Flow Method`

        Args:
            value (str): value for IDD Field `Heating Design Air Flow Method`
                Default value: DesignDay

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `heating_design_air_flow_method` or None if not set

        """
        return self["Heating Design Air Flow Method"]

    @heating_design_air_flow_method.setter
    def heating_design_air_flow_method(self, value="DesignDay"):
        """Corresponds to IDD field `Heating Design Air Flow Method`"""
        self["Heating Design Air Flow Method"] = value

    @property
    def heating_design_air_flow_rate(self):
        """field `Heating Design Air Flow Rate`
        This input is used if Heating Design Air Flow Method is Flow/System
        This value will *not* be multiplied by any sizing factor or by zone multipliers.
        If using zone multipliers, this value must be large enough to serve the multiplied zones.

        Args:
            value (float): value for IDD Field `Heating Design Air Flow Rate`
                Units: m3/s

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `heating_design_air_flow_rate` or None if not set
        """
        return self["Heating Design Air Flow Rate"]

    @heating_design_air_flow_rate.setter
    def heating_design_air_flow_rate(self, value=None):
        """Corresponds to IDD field `Heating Design Air Flow Rate`"""
        self["Heating Design Air Flow Rate"] = value

    @property
    def supply_air_flow_rate_per_floor_area_during_heating_operation(self):
        """field `Supply Air Flow Rate Per Floor Area During Heating Operation`
        Enter the heating supply air volume flow rate per total conditioned
        floor area. Required field when Supply air Flow Rate Method during
        heating operation is FlowPerFloorArea.

        Args:
            value (float): value for IDD Field `Supply Air Flow Rate Per Floor Area During Heating Operation`
                Units: m3/s-m2

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `supply_air_flow_rate_per_floor_area_during_heating_operation` or None if not set

        """
        return self[
            "Supply Air Flow Rate Per Floor Area During Heating Operation"]

    @supply_air_flow_rate_per_floor_area_during_heating_operation.setter
    def supply_air_flow_rate_per_floor_area_during_heating_operation(
            self,
            value=None):
        """Corresponds to IDD field `Supply Air Flow Rate Per Floor Area During
        Heating Operation`"""
        self[
            "Supply Air Flow Rate Per Floor Area During Heating Operation"] = value

    @property
    def fraction_of_autosized_design_heating_supply_air_flow_rate(self):
        """field `Fraction of Autosized Design Heating Supply Air Flow Rate`
        Enter the supply air volume flow rate as a fraction of the heating
        supply air flow rate. Required field when Supply air Flow Rate Method
        during heating operation is FractionOfAutosizedHeatingAirflow.

        Args:
            value (float): value for IDD Field `Fraction of Autosized Design Heating Supply Air Flow Rate`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `fraction_of_autosized_design_heating_supply_air_flow_rate` or None if not set

        """
        return self[
            "Fraction of Autosized Design Heating Supply Air Flow Rate"]

    @fraction_of_autosized_design_heating_supply_air_flow_rate.setter
    def fraction_of_autosized_design_heating_supply_air_flow_rate(
            self,
            value=None):
        """Corresponds to IDD field `Fraction of Autosized Design Heating
        Supply Air Flow Rate`"""
        self[
            "Fraction of Autosized Design Heating Supply Air Flow Rate"] = value

    @property
    def fraction_of_autosized_design_cooling_supply_air_flow_rate_v3(self):
        """field `Fraction of Autosized Design Cooling Supply Air Flow Rate v3`
        Enter the supply air volume flow rate as a fraction of the cooling
        supply air flow rate. Required field when Supply air Flow Rate Method
        during heating operation is FractionOfAutosizedCoolingAirflow.

        Args:
            value (float): value for IDD Field `Fraction of Autosized Design Cooling Supply Air Flow Rate v3`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `fraction_of_autosized_design_cooling_supply_air_flow_rate_v3` or None if not set

        """
        return self[
            "Fraction of Autosized Design Cooling Supply Air Flow Rate v3"]

    @fraction_of_autosized_design_cooling_supply_air_flow_rate_v3.setter
    def fraction_of_autosized_design_cooling_supply_air_flow_rate_v3(
            self,
            value=None):
        """Corresponds to IDD field `Fraction of Autosized Design Cooling
        Supply Air Flow Rate v3`"""
        self[
            "Fraction of Autosized Design Cooling Supply Air Flow Rate v3"] = value

    @property
    def design_supply_air_flow_rate_per_unit_heating_capacity(self):
        """field `Design Supply Air Flow Rate Per Unit Heating Capacity` Enter
        the heating supply air volume flow rate per unit heating capacity.
        Required field when Supply air Flow Rate Method during heating
        operation is FlowPerHeatingCapacity.

        Args:
            value (float): value for IDD Field `Design Supply Air Flow Rate Per Unit Heating Capacity`
                Units: m3/s-W

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `design_supply_air_flow_rate_per_unit_heating_capacity` or None if not set

        """
        return self["Design Supply Air Flow Rate Per Unit Heating Capacity"]

    @design_supply_air_flow_rate_per_unit_heating_capacity.setter
    def design_supply_air_flow_rate_per_unit_heating_capacity(
            self,
            value=None):
        """Corresponds to IDD field `Design Supply Air Flow Rate Per Unit
        Heating Capacity`"""
        self["Design Supply Air Flow Rate Per Unit Heating Capacity"] = value

    @property
    def system_outdoor_air_method(self):
        """field `System Outdoor Air Method`

        Args:
            value (str): value for IDD Field `System Outdoor Air Method`
                Default value: ZoneSum

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `system_outdoor_air_method` or None if not set

        """
        return self["System Outdoor Air Method"]

    @system_outdoor_air_method.setter
    def system_outdoor_air_method(self, value="ZoneSum"):
        """Corresponds to IDD field `System Outdoor Air Method`"""
        self["System Outdoor Air Method"] = value

    @property
    def zone_maximum_outdoor_air_fraction(self):
        """field `Zone Maximum Outdoor Air Fraction`

        Args:
            value (float): value for IDD Field `Zone Maximum Outdoor Air Fraction`
                Units: dimensionless
                Default value: 1.0

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `zone_maximum_outdoor_air_fraction` or None if not set

        """
        return self["Zone Maximum Outdoor Air Fraction"]

    @zone_maximum_outdoor_air_fraction.setter
    def zone_maximum_outdoor_air_fraction(self, value=1.0):
        """Corresponds to IDD field `Zone Maximum Outdoor Air Fraction`"""
        self["Zone Maximum Outdoor Air Fraction"] = value

    @property
    def cooling_design_capacity_method(self):
        """field `Cooling Design Capacity Method`
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
                Default value: CoolingDesignCapacity

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `cooling_design_capacity_method` or None if not set
        """
        return self["Cooling Design Capacity Method"]

    @cooling_design_capacity_method.setter
    def cooling_design_capacity_method(self, value="CoolingDesignCapacity"):
        """Corresponds to IDD field `Cooling Design Capacity Method`"""
        self["Cooling Design Capacity Method"] = value

    @property
    def cooling_design_capacity(self):
        """field `Cooling Design Capacity` Enter the design cooling capacity.
        Required field when the cooling design capacity method
        CoolingDesignCapacity.

        Args:
            value (float or "Autosize"): value for IDD Field `Cooling Design Capacity`
                Units: W
                Default value: "autosize"

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `cooling_design_capacity` or None if not set

        """
        return self["Cooling Design Capacity"]

    @cooling_design_capacity.setter
    def cooling_design_capacity(self, value="autosize"):
        """Corresponds to IDD field `Cooling Design Capacity`"""
        self["Cooling Design Capacity"] = value

    @property
    def cooling_design_capacity_per_floor_area(self):
        """field `Cooling Design Capacity Per Floor Area` Enter the cooling
        design capacity per total floor area of cooled zones served by an
        airloop. Required field when the cooling design capacity method field
        is CapacityPerFloorArea.

        Args:
            value (float): value for IDD Field `Cooling Design Capacity Per Floor Area`
                Units: W/m2

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `cooling_design_capacity_per_floor_area` or None if not set

        """
        return self["Cooling Design Capacity Per Floor Area"]

    @cooling_design_capacity_per_floor_area.setter
    def cooling_design_capacity_per_floor_area(self, value=None):
        """Corresponds to IDD field `Cooling Design Capacity Per Floor Area`"""
        self["Cooling Design Capacity Per Floor Area"] = value

    @property
    def fraction_of_autosized_cooling_design_capacity(self):
        """field `Fraction of Autosized Cooling Design Capacity`
        Enter the fraction of auto-sized cooling design capacity. Required field when the cooling
        design capacity method field is FractionOfAutosizedCoolingCapacity.

        Args:
            value (float): value for IDD Field `Fraction of Autosized Cooling Design Capacity`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `fraction_of_autosized_cooling_design_capacity` or None if not set
        """
        return self["Fraction of Autosized Cooling Design Capacity"]

    @fraction_of_autosized_cooling_design_capacity.setter
    def fraction_of_autosized_cooling_design_capacity(self, value=None):
        """Corresponds to IDD field `Fraction of Autosized Cooling Design
        Capacity`"""
        self["Fraction of Autosized Cooling Design Capacity"] = value

    @property
    def heating_design_capacity_method(self):
        """field `Heating Design Capacity Method`
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
                Default value: HeatingDesignCapacity

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `heating_design_capacity_method` or None if not set
        """
        return self["Heating Design Capacity Method"]

    @heating_design_capacity_method.setter
    def heating_design_capacity_method(self, value="HeatingDesignCapacity"):
        """Corresponds to IDD field `Heating Design Capacity Method`"""
        self["Heating Design Capacity Method"] = value

    @property
    def heating_design_capacity(self):
        """field `Heating Design Capacity` Enter the design heating capacity.
        Required field when the heating design capacity method
        HeatingDesignCapacity.

        Args:
            value (float or "Autosize"): value for IDD Field `Heating Design Capacity`
                Units: W
                Default value: "autosize"

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `heating_design_capacity` or None if not set

        """
        return self["Heating Design Capacity"]

    @heating_design_capacity.setter
    def heating_design_capacity(self, value="autosize"):
        """Corresponds to IDD field `Heating Design Capacity`"""
        self["Heating Design Capacity"] = value

    @property
    def heating_design_capacity_per_floor_area(self):
        """field `Heating Design Capacity Per Floor Area` Enter the heating
        design capacity per zone floor area. Required field when the heating
        design capacity method field is CapacityPerFloorArea.

        Args:
            value (float): value for IDD Field `Heating Design Capacity Per Floor Area`
                Units: W/m2

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `heating_design_capacity_per_floor_area` or None if not set

        """
        return self["Heating Design Capacity Per Floor Area"]

    @heating_design_capacity_per_floor_area.setter
    def heating_design_capacity_per_floor_area(self, value=None):
        """Corresponds to IDD field `Heating Design Capacity Per Floor Area`"""
        self["Heating Design Capacity Per Floor Area"] = value

    @property
    def fraction_of_autosized_heating_design_capacity(self):
        """field `Fraction of Autosized Heating Design Capacity`
        Enter the fraction of auto-sized heating design capacity. Required field when capacity the
        heating design capacity method field is FractionOfAutosizedHeatingCapacity.

        Args:
            value (float): value for IDD Field `Fraction of Autosized Heating Design Capacity`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `fraction_of_autosized_heating_design_capacity` or None if not set
        """
        return self["Fraction of Autosized Heating Design Capacity"]

    @fraction_of_autosized_heating_design_capacity.setter
    def fraction_of_autosized_heating_design_capacity(self, value=None):
        """Corresponds to IDD field `Fraction of Autosized Heating Design
        Capacity`"""
        self["Fraction of Autosized Heating Design Capacity"] = value




class SizingPlant(DataObject):

    """ Corresponds to IDD object `Sizing:Plant`
        Specifies the input needed to autosize plant loop flow rates and equipment capacities.
        This information is initially used by components that use water for heating or cooling
        such as hot or chilled water coils to calculate their maximum water flow rates. These
        flow rates are then summed for use in calculating the Plant Loop flow rates.
    """
    _schema = {'extensible-fields': OrderedDict(),
               'fields': OrderedDict([(u'plant or condenser loop name',
                                       {'name': u'Plant or Condenser Loop Name',
                                        'pyname': u'plant_or_condenser_loop_name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'loop type',
                                       {'name': u'Loop Type',
                                        'pyname': u'loop_type',
                                        'required-field': True,
                                        'autosizable': False,
                                        'accepted-values': [u'Heating',
                                                            u'Cooling',
                                                            u'Condenser',
                                                            u'Steam'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'design loop exit temperature',
                                       {'name': u'Design Loop Exit Temperature',
                                        'pyname': u'design_loop_exit_temperature',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'C'}),
                                      (u'loop design temperature difference',
                                       {'name': u'Loop Design Temperature Difference',
                                        'pyname': u'loop_design_temperature_difference',
                                        'minimum>': 0.0,
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'deltaC'})]),
               'format': None,
               'group': u'HVAC Design Objects',
               'min-fields': 4,
               'name': u'Sizing:Plant',
               'pyname': u'SizingPlant',
               'required-object': False,
               'unique-object': False}

    @property
    def plant_or_condenser_loop_name(self):
        """field `Plant or Condenser Loop Name` Enter the name of a PlantLoop
        or a CondenserLoop object.

        Args:
            value (str): value for IDD Field `Plant or Condenser Loop Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `plant_or_condenser_loop_name` or None if not set

        """
        return self["Plant or Condenser Loop Name"]

    @plant_or_condenser_loop_name.setter
    def plant_or_condenser_loop_name(self, value=None):
        """Corresponds to IDD field `Plant or Condenser Loop Name`"""
        self["Plant or Condenser Loop Name"] = value

    @property
    def loop_type(self):
        """field `Loop Type`

        Args:
            value (str): value for IDD Field `Loop Type`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `loop_type` or None if not set

        """
        return self["Loop Type"]

    @loop_type.setter
    def loop_type(self, value=None):
        """Corresponds to IDD field `Loop Type`"""
        self["Loop Type"] = value

    @property
    def design_loop_exit_temperature(self):
        """field `Design Loop Exit Temperature`

        Args:
            value (float): value for IDD Field `Design Loop Exit Temperature`
                Units: C

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `design_loop_exit_temperature` or None if not set

        """
        return self["Design Loop Exit Temperature"]

    @design_loop_exit_temperature.setter
    def design_loop_exit_temperature(self, value=None):
        """Corresponds to IDD field `Design Loop Exit Temperature`"""
        self["Design Loop Exit Temperature"] = value

    @property
    def loop_design_temperature_difference(self):
        """field `Loop Design Temperature Difference`

        Args:
            value (float): value for IDD Field `Loop Design Temperature Difference`
                Units: deltaC

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `loop_design_temperature_difference` or None if not set

        """
        return self["Loop Design Temperature Difference"]

    @loop_design_temperature_difference.setter
    def loop_design_temperature_difference(self, value=None):
        """Corresponds to IDD field `Loop Design Temperature Difference`"""
        self["Loop Design Temperature Difference"] = value




class OutputControlSizingStyle(DataObject):

    """ Corresponds to IDD object `OutputControl:Sizing:Style`
        default style for the Sizing output files is comma -- this works well for
        importing into spreadsheet programs such as Excel(tm) but not so well for word
        processing progams -- there tab may be a better choice.  fixed puts spaces between
        the "columns"
    """
    _schema = {'extensible-fields': OrderedDict(),
               'fields': OrderedDict([(u'column separator',
                                       {'name': u'Column Separator',
                                        'pyname': u'column_separator',
                                        'required-field': True,
                                        'autosizable': False,
                                        'accepted-values': [u'Comma',
                                                            u'Tab',
                                                            u'Fixed'],
                                        'autocalculatable': False,
                                        'type': 'alpha'})]),
               'format': None,
               'group': u'HVAC Design Objects',
               'min-fields': 0,
               'name': u'OutputControl:Sizing:Style',
               'pyname': u'OutputControlSizingStyle',
               'required-object': False,
               'unique-object': True}

    @property
    def column_separator(self):
        """field `Column Separator`

        Args:
            value (str): value for IDD Field `Column Separator`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `column_separator` or None if not set

        """
        return self["Column Separator"]

    @column_separator.setter
    def column_separator(self, value=None):
        """Corresponds to IDD field `Column Separator`"""
        self["Column Separator"] = value


