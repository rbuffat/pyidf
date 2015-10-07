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

        |  Flow/Person => Outdoor Air Flow per Person * Occupancy = Design Flow Rate,
        |  Flow/Area => Outdoor Air Flow per Zone Floor Area * Zone Floor Area = Design Flow Rate,
        |  Flow/Zone => Outdoor Air Flow per Zone = Design Flow Rate,
        |  AirChanges/Hour => Outdoor Air Flow Air Changes per Hour * Zone Volume adjusted for m3/s = Design Flow Rate
        |  Default value: Flow/Person

        Args:
            value (str): value for IDD Field `Outdoor Air Method`

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

        |  0.00944 m3/s is equivalent to 20 cfm per person
        |  This input should be used if the field Outdoor Air Method is Flow/Person.
        |  This input is used if the field Outdoor Air Method is Flow/Person, Sum, or Maximum
        |  Units: m3/s-person
        |  Default value: 0.00944

        Args:
            value (float): value for IDD Field `Outdoor Air Flow per Person`

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
        """field `Outdoor Air Flow per Zone Floor Area`

        |  This input should be used if the field Outdoor Air Method is Flow/Area.
        |  This input is used if the field Outdoor Air Method is Flow/Area, Sum, or Maximum
        |  Units: m3/s-m2

        Args:
            value (float): value for IDD Field `Outdoor Air Flow per Zone Floor Area`

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
        """field `Outdoor Air Flow per Zone`

        |  This input should be used if the field Outdoor Air Method is Flow/Zone.
        |  This input is used if the field Outdoor Air Method is Flow/Zone, Sum, or Maximum
        |  Units: m3/s

        Args:
            value (float): value for IDD Field `Outdoor Air Flow per Zone`

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
        """field `Outdoor Air Flow Air Changes per Hour`

        |  This input should be used if the field Outdoor Air Method is AirChanges/Hour.
        |  This input is used if the field Outdoor Air Method is AirChanges/Hour, Sum, or Maximum
        |  Units: 1/hr

        Args:
            value (float): value for IDD Field `Outdoor Air Flow Air Changes per Hour`

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

        |  Schedule values are multiplied by the Outdoor Air Flow rate calculated using
        |  the previous four inputs. Schedule values are limited to 0 to 1.

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

        |  Units: dimensionless
        |  Default value: 1.0

        Args:
            value (float): value for IDD Field `Zone Air Distribution Effectiveness in Cooling Mode`

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

        |  Units: dimensionless
        |  Default value: 1.0

        Args:
            value (float): value for IDD Field `Zone Air Distribution Effectiveness in Heating Mode`

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
        """field `Zone Air Distribution Effectiveness Schedule Name`

        |  optionally used to replace Zone Air Distribution Effectiveness in Cooling and
        |  Heating Mode

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

        |  Units: dimensionless

        Args:
            value (float): value for IDD Field `Zone Secondary Recirculation Fraction`

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

        |  Default value: 1.0

        Args:
            value (float): value for IDD Field `Heating Sizing Factor`

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

        |  Default value: 1.0

        Args:
            value (float): value for IDD Field `Cooling Sizing Factor`

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

        |  blank => set the timesteps in averaging window to
        |  Number of Timesteps per Hour resulting in a 1 hour averaging window
        |  default is number of timesteps for 1 hour averaging window
        |  value >= 1

        Args:
            value (int): value for IDD Field `Timesteps in Averaging Window`

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
                                        'type': u'object-list'}),
                                      (u'account for dedicated outdoor air system',
                                       {'name': u'Account for Dedicated Outdoor Air System',
                                        'pyname': u'account_for_dedicated_outdoor_air_system',
                                        'default': u'No',
                                        'required-field': False,
                                        'autosizable': False,
                                        'accepted-values': [u'Yes',
                                                            u'No'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'dedicated outdoor air system control strategy',
                                       {'name': u'Dedicated Outdoor Air System Control Strategy',
                                        'pyname': u'dedicated_outdoor_air_system_control_strategy',
                                        'default': u'NeutralSupplyAir',
                                        'required-field': False,
                                        'autosizable': False,
                                        'accepted-values': [u'NeutralSupplyAir',
                                                            u'NeutralDehumidifiedSupplyAir',
                                                            u'ColdSupplyAir'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'dedicated outdoor air low setpoint temperature for design',
                                       {'name': u'Dedicated Outdoor Air Low Setpoint Temperature for Design',
                                        'pyname': u'dedicated_outdoor_air_low_setpoint_temperature_for_design',
                                        'default': 'autosize',
                                        'required-field': False,
                                        'autosizable': True,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'C'}),
                                      (u'dedicated outdoor air high setpoint temperature for design',
                                       {'name': u'Dedicated Outdoor Air High Setpoint Temperature for Design',
                                        'pyname': u'dedicated_outdoor_air_high_setpoint_temperature_for_design',
                                        'default': 'autosize',
                                        'required-field': False,
                                        'autosizable': True,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'C'})]),
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

        |  Default value: SupplyAirTemperature

        Args:
            value (str): value for IDD Field `Zone Cooling Design Supply Air Temperature Input Method`

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

        |  Zone Cooling Design Supply Air Temperature is only used when Zone Cooling Design
        |  Supply Air Temperature Input Method = SupplyAirTemperature
        |  Units: C

        Args:
            value (float): value for IDD Field `Zone Cooling Design Supply Air Temperature`

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

        |  Zone Cooling Design Supply Air Temperature is only used when Zone Cooling Design
        |  Supply Air Temperature Input Method = TemperatureDifference
        |  The absolute value of this field will be subtracted from the zone temperature
        |  at peak load to calculate the Zone Cooling Design Supply Air Temperature.
        |  Units: deltaC

        Args:
            value (float): value for IDD Field `Zone Cooling Design Supply Air Temperature Difference`

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

        |  Default value: SupplyAirTemperature

        Args:
            value (str): value for IDD Field `Zone Heating Design Supply Air Temperature Input Method`

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

        |  Zone Heating Design Supply Air Temperature is only used when Zone Heating Design
        |  Supply Air Temperature Input Method = SupplyAirTemperature
        |  Units: C

        Args:
            value (float): value for IDD Field `Zone Heating Design Supply Air Temperature`

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

        |  Zone Heating Design Supply Air Temperature is only used when Zone Heating Design
        |  Supply Air Temperature Input Method = TemperatureDifference
        |  The absolute value of this field will be added to the zone temperature
        |  at peak load to calculate the Zone Heating Design Supply Air Temperature.
        |  Units: deltaC

        Args:
            value (float): value for IDD Field `Zone Heating Design Supply Air Temperature Difference`

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

        |  Units: kgWater/kgDryAir

        Args:
            value (float): value for IDD Field `Zone Cooling Design Supply Air Humidity Ratio`

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

        |  Units: kgWater/kgDryAir

        Args:
            value (float): value for IDD Field `Zone Heating Design Supply Air Humidity Ratio`

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

        |  if blank or zero, global heating sizing factor from Sizing:Parameters is used.

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

        |  if blank or zero, global cooling sizing factor from Sizing:Parameters is used.

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

        |  Default value: DesignDay

        Args:
            value (str): value for IDD Field `Cooling Design Air Flow Method`

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

        |  This input is used if Cooling Design Air Flow Method is Flow/Zone
        |  This value will be multiplied by the global or zone sizing factor and
        |  by zone multipliers.
        |  Units: m3/s

        Args:
            value (float): value for IDD Field `Cooling Design Air Flow Rate`

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
        """field `Cooling Minimum Air Flow per Zone Floor Area`

        |  default is .15 cfm/ft2
        |  This input is used if Cooling Design Air Flow Method is DesignDayWithLimit
        |  Units: m3/s-m2
        |  Default value: 0.000762

        Args:
            value (float): value for IDD Field `Cooling Minimum Air Flow per Zone Floor Area`

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
        """field `Cooling Minimum Air Flow`

        |  This input is used if Cooling Design Air Flow Method is DesignDayWithLimit
        |  Units: m3/s

        Args:
            value (float): value for IDD Field `Cooling Minimum Air Flow`

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
        """field `Cooling Minimum Air Flow Fraction`

        |  fraction of the Cooling design Air Flow Rate
        |  This input is currently used in sizing the Fan minimum Flow Rate.
        |  It does not currently affect other component autosizing.

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

        |  Default value: DesignDay

        Args:
            value (str): value for IDD Field `Heating Design Air Flow Method`

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

        |  This input is used if Heating Design Air Flow Method is Flow/Zone.
        |  This value will be multiplied by the global or zone sizing factor and
        |  by zone multipliers.
        |  Units: m3/s

        Args:
            value (float): value for IDD Field `Heating Design Air Flow Rate`

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

        |  default is .40 cfm/ft2
        |  This field is used to size the heating design flow rate when Heating Design Air Flow Method = Flow/Zone.
        |  This input is used for autosizing components when Heating Design Air Flow Method = DesignDayWithLimit.
        |  Units: m3/s-m2
        |  Default value: 0.002032

        Args:
            value (float): value for IDD Field `Heating Maximum Air Flow per Zone Floor Area`

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

        |  default is 300 cfm
        |  This input is used for autosizing components when Heating Design Air Flow Method = DesignDayWithLimit.
        |  Units: m3/s
        |  Default value: 0.1415762

        Args:
            value (float): value for IDD Field `Heating Maximum Air Flow`

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

        |  fraction of the Heating Design Air Flow Rate
        |  This input is used for autosizing components when Heating Design Air Flow Method = DesignDayWithLimit.
        |  Default value: 0.3

        Args:
            value (float): value for IDD Field `Heating Maximum Air Flow Fraction`

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

    @property
    def account_for_dedicated_outdoor_air_system(self):
        """field `Account for Dedicated Outdoor Air System`

        |  account for effect of dedicated outdoor air system supplying air directly to the zone
        |  Default value: No

        Args:
            value (str): value for IDD Field `Account for Dedicated Outdoor Air System`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `account_for_dedicated_outdoor_air_system` or None if not set

        """
        return self["Account for Dedicated Outdoor Air System"]

    @account_for_dedicated_outdoor_air_system.setter
    def account_for_dedicated_outdoor_air_system(self, value="No"):
        """Corresponds to IDD field `Account for Dedicated Outdoor Air
        System`"""
        self["Account for Dedicated Outdoor Air System"] = value

    @property
    def dedicated_outdoor_air_system_control_strategy(self):
        """field `Dedicated Outdoor Air System Control Strategy`

        |  1)supply neutral ventilation air; 2)supply neutral dehumidified and reheated
        |  ventilation air; 3)supply cold ventilation air
        |  Default value: NeutralSupplyAir

        Args:
            value (str): value for IDD Field `Dedicated Outdoor Air System Control Strategy`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `dedicated_outdoor_air_system_control_strategy` or None if not set

        """
        return self["Dedicated Outdoor Air System Control Strategy"]

    @dedicated_outdoor_air_system_control_strategy.setter
    def dedicated_outdoor_air_system_control_strategy(
            self,
            value="NeutralSupplyAir"):
        """Corresponds to IDD field `Dedicated Outdoor Air System Control
        Strategy`"""
        self["Dedicated Outdoor Air System Control Strategy"] = value

    @property
    def dedicated_outdoor_air_low_setpoint_temperature_for_design(self):
        """field `Dedicated Outdoor Air Low Setpoint Temperature for Design`

        |  Units: C
        |  Default value: "autosize"

        Args:
            value (float or "Autosize"): value for IDD Field `Dedicated Outdoor Air Low Setpoint Temperature for Design`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float or "Autosize": the value of `dedicated_outdoor_air_low_setpoint_temperature_for_design` or None if not set

        """
        return self[
            "Dedicated Outdoor Air Low Setpoint Temperature for Design"]

    @dedicated_outdoor_air_low_setpoint_temperature_for_design.setter
    def dedicated_outdoor_air_low_setpoint_temperature_for_design(
            self,
            value="autosize"):
        """Corresponds to IDD field `Dedicated Outdoor Air Low Setpoint
        Temperature for Design`"""
        self[
            "Dedicated Outdoor Air Low Setpoint Temperature for Design"] = value

    @property
    def dedicated_outdoor_air_high_setpoint_temperature_for_design(self):
        """field `Dedicated Outdoor Air High Setpoint Temperature for Design`

        |  Units: C
        |  Default value: "autosize"

        Args:
            value (float or "Autosize"): value for IDD Field `Dedicated Outdoor Air High Setpoint Temperature for Design`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float or "Autosize": the value of `dedicated_outdoor_air_high_setpoint_temperature_for_design` or None if not set

        """
        return self[
            "Dedicated Outdoor Air High Setpoint Temperature for Design"]

    @dedicated_outdoor_air_high_setpoint_temperature_for_design.setter
    def dedicated_outdoor_air_high_setpoint_temperature_for_design(
            self,
            value="autosize"):
        """Corresponds to IDD field `Dedicated Outdoor Air High Setpoint
        Temperature for Design`"""
        self[
            "Dedicated Outdoor Air High Setpoint Temperature for Design"] = value




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
                                      (u'cooling supply air flow rate method',
                                       {'name': u'Cooling Supply Air Flow Rate Method',
                                        'pyname': u'cooling_supply_air_flow_rate_method',
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
                                      (u'cooling supply air flow rate',
                                       {'name': u'Cooling Supply Air Flow Rate',
                                        'pyname': u'cooling_supply_air_flow_rate',
                                        'required-field': False,
                                        'autosizable': True,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'm3/s'}),
                                      (u'cooling supply air flow rate per floor area',
                                       {'name': u'Cooling Supply Air Flow Rate Per Floor Area',
                                        'pyname': u'cooling_supply_air_flow_rate_per_floor_area',
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'm3/s-m2'}),
                                      (u'cooling fraction of autosized cooling supply air flow rate',
                                       {'name': u'Cooling Fraction of Autosized Cooling Supply Air Flow Rate',
                                        'pyname': u'cooling_fraction_of_autosized_cooling_supply_air_flow_rate',
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'cooling supply air flow rate per unit cooling capacity',
                                       {'name': u'Cooling Supply Air Flow Rate Per Unit Cooling Capacity',
                                        'pyname': u'cooling_supply_air_flow_rate_per_unit_cooling_capacity',
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'm3/s-W'}),
                                      (u'no load supply air flow rate method',
                                       {'name': u'No Load Supply Air Flow Rate Method',
                                        'pyname': u'no_load_supply_air_flow_rate_method',
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
                                      (u'no load supply air flow rate',
                                       {'name': u'No Load Supply Air Flow Rate',
                                        'pyname': u'no_load_supply_air_flow_rate',
                                        'required-field': False,
                                        'autosizable': True,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'm3/s'}),
                                      (u'no load supply air flow rate per floor area',
                                       {'name': u'No Load Supply Air Flow Rate Per Floor Area',
                                        'pyname': u'no_load_supply_air_flow_rate_per_floor_area',
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'm3/s-m2'}),
                                      (u'no load fraction of cooling supply air flow rate',
                                       {'name': u'No Load Fraction of Cooling Supply Air Flow Rate',
                                        'pyname': u'no_load_fraction_of_cooling_supply_air_flow_rate',
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'no load fraction of heating supply air flow rate',
                                       {'name': u'No Load Fraction of Heating Supply Air Flow Rate',
                                        'pyname': u'no_load_fraction_of_heating_supply_air_flow_rate',
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'heating supply air flow rate method',
                                       {'name': u'Heating Supply Air Flow Rate Method',
                                        'pyname': u'heating_supply_air_flow_rate_method',
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
                                      (u'heating supply air flow rate',
                                       {'name': u'Heating Supply Air Flow Rate',
                                        'pyname': u'heating_supply_air_flow_rate',
                                        'required-field': False,
                                        'autosizable': True,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'm3/s'}),
                                      (u'heating supply air flow rate per floor area',
                                       {'name': u'Heating Supply Air Flow Rate Per Floor Area',
                                        'pyname': u'heating_supply_air_flow_rate_per_floor_area',
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'm3/s-m2'}),
                                      (u'heating fraction of heating supply air flow rate',
                                       {'name': u'Heating Fraction of Heating Supply Air Flow Rate',
                                        'pyname': u'heating_fraction_of_heating_supply_air_flow_rate',
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'heating supply air flow rate per unit heating capacity',
                                       {'name': u'Heating Supply Air Flow Rate Per Unit Heating Capacity',
                                        'pyname': u'heating_supply_air_flow_rate_per_unit_heating_capacity',
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
    def cooling_supply_air_flow_rate_method(self):
        """field `Cooling Supply Air Flow Rate Method`

        |  Enter the method used to determine the cooling supply air volume flow rate.
        |  None is used when a cooling coil is not included in the Zone HVAC Equip or this field
        |  may be blank. SupplyAirFlowRate => selected when the magnitude of the supply air volume
        |  flow rate is specified. FlowPerFloorArea => selected when the supply air volume flow rate
        |  is determined from total floor area served by the Zone HVAC unit and Flow Per Floor Area
        |  value specified. FractionOfAutosizedCoolingAirflow => is selected when the supply air volume
        |  is determined from a user specified fraction and the autosized cooling supply air flow rate
        |  value determined by the simulation. FlowPerCoolingCapacity => is selected when the supply
        |  air volume is determined from user specified flow per Cooling Capacity and Cooling Capacity
        |  determined by the simulation.
        |  Default value: SupplyAirFlowRate

        Args:
            value (str): value for IDD Field `Cooling Supply Air Flow Rate Method`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `cooling_supply_air_flow_rate_method` or None if not set

        """
        return self["Cooling Supply Air Flow Rate Method"]

    @cooling_supply_air_flow_rate_method.setter
    def cooling_supply_air_flow_rate_method(self, value="SupplyAirFlowRate"):
        """Corresponds to IDD field `Cooling Supply Air Flow Rate Method`"""
        self["Cooling Supply Air Flow Rate Method"] = value

    @property
    def cooling_supply_air_flow_rate(self):
        """field `Cooling Supply Air Flow Rate`

        |  Enter the magnitude of supply air volume flow rate during cooling operation.
        |  Required field when Cooling Supply Air Flow Rate Method is SupplyAirFlowRate.
        |  This field may be blank if a cooling coil is not included in the Zone HVAC equipment.
        |  Units: m3/s

        Args:
            value (float or "Autosize"): value for IDD Field `Cooling Supply Air Flow Rate`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float or "Autosize": the value of `cooling_supply_air_flow_rate` or None if not set

        """
        return self["Cooling Supply Air Flow Rate"]

    @cooling_supply_air_flow_rate.setter
    def cooling_supply_air_flow_rate(self, value=None):
        """Corresponds to IDD field `Cooling Supply Air Flow Rate`"""
        self["Cooling Supply Air Flow Rate"] = value

    @property
    def cooling_supply_air_flow_rate_per_floor_area(self):
        """field `Cooling Supply Air Flow Rate Per Floor Area`

        |  Enter the cooling supply air volume flow rate per total conditioned floor area.
        |  Required field when Cooling Supply Air Flow Rate Method is FlowPerFloorArea.
        |  This field may be blank if a cooling coil is not included in the Zone HVAC equipment.
        |  Units: m3/s-m2

        Args:
            value (float): value for IDD Field `Cooling Supply Air Flow Rate Per Floor Area`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `cooling_supply_air_flow_rate_per_floor_area` or None if not set

        """
        return self["Cooling Supply Air Flow Rate Per Floor Area"]

    @cooling_supply_air_flow_rate_per_floor_area.setter
    def cooling_supply_air_flow_rate_per_floor_area(self, value=None):
        """Corresponds to IDD field `Cooling Supply Air Flow Rate Per Floor
        Area`"""
        self["Cooling Supply Air Flow Rate Per Floor Area"] = value

    @property
    def cooling_fraction_of_autosized_cooling_supply_air_flow_rate(self):
        """field `Cooling Fraction of Autosized Cooling Supply Air Flow Rate`

        |  Enter the supply air volume flow rate as a fraction of the cooling supply air flow rate.
        |  Required field when Cooling Supply Air Flow Rate Method is
        |  FractionOfAutosizedCoolingAirflow.
        |  This field may be blank if a cooling coil is not included in the Zone HVAC equipment.

        Args:
            value (float): value for IDD Field `Cooling Fraction of Autosized Cooling Supply Air Flow Rate`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `cooling_fraction_of_autosized_cooling_supply_air_flow_rate` or None if not set

        """
        return self[
            "Cooling Fraction of Autosized Cooling Supply Air Flow Rate"]

    @cooling_fraction_of_autosized_cooling_supply_air_flow_rate.setter
    def cooling_fraction_of_autosized_cooling_supply_air_flow_rate(
            self,
            value=None):
        """Corresponds to IDD field `Cooling Fraction of Autosized Cooling
        Supply Air Flow Rate`"""
        self[
            "Cooling Fraction of Autosized Cooling Supply Air Flow Rate"] = value

    @property
    def cooling_supply_air_flow_rate_per_unit_cooling_capacity(self):
        """field `Cooling Supply Air Flow Rate Per Unit Cooling Capacity`

        |  Enter the cooling supply air volume flow rate unit cooling capacity.
        |  Required field when Cooling Supply Air Flow Rate Method is
        |  FlowPerCoolingCapacity. This field may be blank if a cooling coil is not
        |  included in the Zone HVAC equipment.
        |  Units: m3/s-W

        Args:
            value (float): value for IDD Field `Cooling Supply Air Flow Rate Per Unit Cooling Capacity`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `cooling_supply_air_flow_rate_per_unit_cooling_capacity` or None if not set

        """
        return self["Cooling Supply Air Flow Rate Per Unit Cooling Capacity"]

    @cooling_supply_air_flow_rate_per_unit_cooling_capacity.setter
    def cooling_supply_air_flow_rate_per_unit_cooling_capacity(
            self,
            value=None):
        """Corresponds to IDD field `Cooling Supply Air Flow Rate Per Unit
        Cooling Capacity`"""
        self["Cooling Supply Air Flow Rate Per Unit Cooling Capacity"] = value

    @property
    def no_load_supply_air_flow_rate_method(self):
        """field `No Load Supply Air Flow Rate Method`

        |  Enter the method used to determine the supply air volume flow rate When No Cooling or Heating
        |  is Required. None is used when a cooling or heating coil is not included in the Zone HVAC
        |  Equipment or this field may be blank. SupplyAirFlowRate => selected when the magnitude of the
        |  supply air volume flow rate is specified. FlowPerFloorArea => selected when the supply air
        |  volume flow rate is determined from total floor area served by the Zone HVAC unit and Flow Per
        |  Floor Area is specified. FractionOfAutosizedCoolingAirflow => is selected when the supply
        |  air volume is determined from a user specified fraction and the Autosized cooling supply
        |  air flow rate value determined by the simulation. FractionOfAutosizedHeatingAirflow => is
        |  selected when the supply air volume is determined from a user specified fraction and the
        |  Autosized heating supply air flow rate value determined by the simulation.
        |  Default value: SupplyAirFlowRate

        Args:
            value (str): value for IDD Field `No Load Supply Air Flow Rate Method`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `no_load_supply_air_flow_rate_method` or None if not set

        """
        return self["No Load Supply Air Flow Rate Method"]

    @no_load_supply_air_flow_rate_method.setter
    def no_load_supply_air_flow_rate_method(self, value="SupplyAirFlowRate"):
        """Corresponds to IDD field `No Load Supply Air Flow Rate Method`"""
        self["No Load Supply Air Flow Rate Method"] = value

    @property
    def no_load_supply_air_flow_rate(self):
        """field `No Load Supply Air Flow Rate`

        |  Enter the magnitude of the supply air volume flow rate during when no cooling or heating
        |  is required. Required field when No Load Supply Air Flow Rate Method
        |  is SupplyAirFlowRate.
        |  Units: m3/s

        Args:
            value (float or "Autosize"): value for IDD Field `No Load Supply Air Flow Rate`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float or "Autosize": the value of `no_load_supply_air_flow_rate` or None if not set

        """
        return self["No Load Supply Air Flow Rate"]

    @no_load_supply_air_flow_rate.setter
    def no_load_supply_air_flow_rate(self, value=None):
        """Corresponds to IDD field `No Load Supply Air Flow Rate`"""
        self["No Load Supply Air Flow Rate"] = value

    @property
    def no_load_supply_air_flow_rate_per_floor_area(self):
        """field `No Load Supply Air Flow Rate Per Floor Area`

        |  Enter the supply air volume flow rate per total floor area.
        |  Required field when No Load Supply Air Flow Rate Method
        |  is FlowPerFloorArea.
        |  Units: m3/s-m2

        Args:
            value (float): value for IDD Field `No Load Supply Air Flow Rate Per Floor Area`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `no_load_supply_air_flow_rate_per_floor_area` or None if not set

        """
        return self["No Load Supply Air Flow Rate Per Floor Area"]

    @no_load_supply_air_flow_rate_per_floor_area.setter
    def no_load_supply_air_flow_rate_per_floor_area(self, value=None):
        """Corresponds to IDD field `No Load Supply Air Flow Rate Per Floor
        Area`"""
        self["No Load Supply Air Flow Rate Per Floor Area"] = value

    @property
    def no_load_fraction_of_cooling_supply_air_flow_rate(self):
        """field `No Load Fraction of Cooling Supply Air Flow Rate`

        |  Enter the supply air volume flow rate as a fraction of the cooling supply air flow rate.
        |  Required field when No Load Supply Air Flow Rate Method
        |  is FractionOfAutosizedCoolingAirflow.

        Args:
            value (float): value for IDD Field `No Load Fraction of Cooling Supply Air Flow Rate`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `no_load_fraction_of_cooling_supply_air_flow_rate` or None if not set

        """
        return self["No Load Fraction of Cooling Supply Air Flow Rate"]

    @no_load_fraction_of_cooling_supply_air_flow_rate.setter
    def no_load_fraction_of_cooling_supply_air_flow_rate(self, value=None):
        """Corresponds to IDD field `No Load Fraction of Cooling Supply Air
        Flow Rate`"""
        self["No Load Fraction of Cooling Supply Air Flow Rate"] = value

    @property
    def no_load_fraction_of_heating_supply_air_flow_rate(self):
        """field `No Load Fraction of Heating Supply Air Flow Rate`

        |  Enter the supply air volume flow rate as a fraction of the heating supply air flow rate.
        |  Required field when No Load Supply Air Flow Rate Method
        |  is FractionOfAutosizedHeatingAirflow.

        Args:
            value (float): value for IDD Field `No Load Fraction of Heating Supply Air Flow Rate`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `no_load_fraction_of_heating_supply_air_flow_rate` or None if not set

        """
        return self["No Load Fraction of Heating Supply Air Flow Rate"]

    @no_load_fraction_of_heating_supply_air_flow_rate.setter
    def no_load_fraction_of_heating_supply_air_flow_rate(self, value=None):
        """Corresponds to IDD field `No Load Fraction of Heating Supply Air
        Flow Rate`"""
        self["No Load Fraction of Heating Supply Air Flow Rate"] = value

    @property
    def heating_supply_air_flow_rate_method(self):
        """field `Heating Supply Air Flow Rate Method`

        |  Enter the method used to determine the heating supply air volume flow rate.
        |  None is used when a heating coil is not included in the Zone HVAC Equipment or this field may
        |  be blank. SupplyAirFlowRate => selected when the magnitude of the heating supply air volume
        |  flow rate is specified.  FlowPerFloorArea => selected when the supply air volume flow rate is
        |  determined from total floor area served by a Zone HVAC unit and user specified value of Flow
        |  Per Floor Area. FractionOfAutosizedHeatingAirflow => is selected when the supply air volume
        |  is determined from a user specified fraction and the Autosized heating supply air flow rate
        |  value determined by the simulation. FlowPerHeatingCapacity => is selected when the supply
        |  air volume is determined from user specified flow per Heating Capacity and Heating Capacity
        |  determined by the simulation.
        |  Default value: SupplyAirFlowRate

        Args:
            value (str): value for IDD Field `Heating Supply Air Flow Rate Method`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `heating_supply_air_flow_rate_method` or None if not set

        """
        return self["Heating Supply Air Flow Rate Method"]

    @heating_supply_air_flow_rate_method.setter
    def heating_supply_air_flow_rate_method(self, value="SupplyAirFlowRate"):
        """Corresponds to IDD field `Heating Supply Air Flow Rate Method`"""
        self["Heating Supply Air Flow Rate Method"] = value

    @property
    def heating_supply_air_flow_rate(self):
        """field `Heating Supply Air Flow Rate`

        |  Enter the magnitude of the supply air volume flow rate during heating operation.
        |  Required field when Heating Supply Air Flow Rate Method is SupplyAirFlowRate.
        |  This field may be blank if a heating coil is not included in the Zone HVAC equipment.
        |  Units: m3/s

        Args:
            value (float or "Autosize"): value for IDD Field `Heating Supply Air Flow Rate`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float or "Autosize": the value of `heating_supply_air_flow_rate` or None if not set

        """
        return self["Heating Supply Air Flow Rate"]

    @heating_supply_air_flow_rate.setter
    def heating_supply_air_flow_rate(self, value=None):
        """Corresponds to IDD field `Heating Supply Air Flow Rate`"""
        self["Heating Supply Air Flow Rate"] = value

    @property
    def heating_supply_air_flow_rate_per_floor_area(self):
        """field `Heating Supply Air Flow Rate Per Floor Area`

        |  Enter the heating supply air volume flow rate per total conditioned floor area.
        |  Required field when Heating Supply Air Flow Rate Method is FlowPerFloorArea.
        |  This field may be blank if a heating coil is not included in the Zone HVAC equipment.
        |  Units: m3/s-m2

        Args:
            value (float): value for IDD Field `Heating Supply Air Flow Rate Per Floor Area`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `heating_supply_air_flow_rate_per_floor_area` or None if not set

        """
        return self["Heating Supply Air Flow Rate Per Floor Area"]

    @heating_supply_air_flow_rate_per_floor_area.setter
    def heating_supply_air_flow_rate_per_floor_area(self, value=None):
        """Corresponds to IDD field `Heating Supply Air Flow Rate Per Floor
        Area`"""
        self["Heating Supply Air Flow Rate Per Floor Area"] = value

    @property
    def heating_fraction_of_heating_supply_air_flow_rate(self):
        """field `Heating Fraction of Heating Supply Air Flow Rate`

        |  Enter the supply air volume flow rate as a fraction of the heating supply air flow rate.
        |  Required field when Heating Supply Air Flow Rate Method is
        |  FractionOfAutosizedHeatingAirflow.
        |  This field may be blank if a heating coil is not included in the Zone HVAC equipment.

        Args:
            value (float): value for IDD Field `Heating Fraction of Heating Supply Air Flow Rate`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `heating_fraction_of_heating_supply_air_flow_rate` or None if not set

        """
        return self["Heating Fraction of Heating Supply Air Flow Rate"]

    @heating_fraction_of_heating_supply_air_flow_rate.setter
    def heating_fraction_of_heating_supply_air_flow_rate(self, value=None):
        """Corresponds to IDD field `Heating Fraction of Heating Supply Air
        Flow Rate`"""
        self["Heating Fraction of Heating Supply Air Flow Rate"] = value

    @property
    def heating_supply_air_flow_rate_per_unit_heating_capacity(self):
        """field `Heating Supply Air Flow Rate Per Unit Heating Capacity`

        |  Enter the supply air volume flow rate per unit heating capacity.
        |  Required field when Heating Supply Air Flow Rate Method is
        |  FlowPerHeatingCapacity.
        |  This field may be blank if a heating coil is not included in the Zone HVAC equipment.
        |  Units: m3/s-W

        Args:
            value (float): value for IDD Field `Heating Supply Air Flow Rate Per Unit Heating Capacity`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `heating_supply_air_flow_rate_per_unit_heating_capacity` or None if not set

        """
        return self["Heating Supply Air Flow Rate Per Unit Heating Capacity"]

    @heating_supply_air_flow_rate_per_unit_heating_capacity.setter
    def heating_supply_air_flow_rate_per_unit_heating_capacity(
            self,
            value=None):
        """Corresponds to IDD field `Heating Supply Air Flow Rate Per Unit
        Heating Capacity`"""
        self["Heating Supply Air Flow Rate Per Unit Heating Capacity"] = value

    @property
    def cooling_design_capacity_method(self):
        """field `Cooling Design Capacity Method`

        |  Enter the method used to determine the cooling design capacity for scalable sizing.
        |  None is used when a cooling coils is not included in the Zone HVAC Equipment or
        |  this field may be blank. If this input field is left blank, then the design cooling
        |  capacity is set to zero. CoolingDesignCapacity => selected when the design cooling capacity
        |  value is specified or auto-sized. CapacityPerFloorArea => selected when the design cooling
        |  capacity is determine from user specified cooling capacity per floor area and zone floor area.
        |  FractionOfAutosizedCoolingCapacity => is selected when the design cooling capacity is
        |  determined from a user specified fraction and the auto-sized design cooling capacity.
        |  Default value: None

        Args:
            value (str): value for IDD Field `Cooling Design Capacity Method`

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
        """field `Cooling Design Capacity`

        |  Enter the design cooling capacity. Required field when the cooling design capacity method
        |  CoolingDesignCapacity.
        |  Units: W

        Args:
            value (float or "Autosize"): value for IDD Field `Cooling Design Capacity`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float or "Autosize": the value of `cooling_design_capacity` or None if not set

        """
        return self["Cooling Design Capacity"]

    @cooling_design_capacity.setter
    def cooling_design_capacity(self, value=None):
        """Corresponds to IDD field `Cooling Design Capacity`"""
        self["Cooling Design Capacity"] = value

    @property
    def cooling_design_capacity_per_floor_area(self):
        """field `Cooling Design Capacity Per Floor Area`

        |  Enter the cooling design capacity per zone floor area. Required field when the cooling design
        |  capacity method field is CapacityPerFloorArea.
        |  Units: W/m2

        Args:
            value (float): value for IDD Field `Cooling Design Capacity Per Floor Area`

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

        |  Enter the fraction of auto-sized cooling design capacity. Required field when the cooling
        |  design capacity method field is FractionOfAutosizedCoolingCapacity.

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

        |  Enter the method used to determine the heating design capacity for scalable sizing.
        |  None is used when a heating coil is not included in the Zone HVAC Equipment or
        |  this field may be blank. If this input field is left blank, then the design heating
        |  capacity is set to zero. HeatingDesignCapacity => selected when the design heating capacity
        |  value is specified or auto-sized. CapacityPerFloorArea => selected when the design cooling
        |  capacity is determine from user specified heating capacity per flow area and zone floor area.
        |  FractionOfAutosizedHeatingCapacity => is selected when the design heating capacity is
        |  determined from a user specified fraction and the auto-sized design heating capacity
        |  Default value: None

        Args:
            value (str): value for IDD Field `Heating Design Capacity Method`

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
        """field `Heating Design Capacity`

        |  Enter the design heating capacity. Required field when the heating design capacity method
        |  HeatingDesignCapacity.
        |  Units: W

        Args:
            value (float or "Autosize"): value for IDD Field `Heating Design Capacity`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float or "Autosize": the value of `heating_design_capacity` or None if not set

        """
        return self["Heating Design Capacity"]

    @heating_design_capacity.setter
    def heating_design_capacity(self, value=None):
        """Corresponds to IDD field `Heating Design Capacity`"""
        self["Heating Design Capacity"] = value

    @property
    def heating_design_capacity_per_floor_area(self):
        """field `Heating Design Capacity Per Floor Area`

        |  Enter the heating design capacity per zone floor area. Required field when the heating design
        |  capacity method field is CapacityPerFloorArea.
        |  Units: W/m2

        Args:
            value (float): value for IDD Field `Heating Design Capacity Per Floor Area`

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

        |  Enter the fraction of auto-sized heating design capacity. Required field when capacity the
        |  heating design capacity method field is FractionOfAutosizedHeatingCapacity.

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
        system. System design air flow, heating capacity, and cooling capacity will be calculated
        using this input data.
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
                                        'required-field': False,
                                        'autosizable': False,
                                        'accepted-values': [u'Sensible',
                                                            u'Total',
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
                                      (u'central heating maximum system air flow ratio',
                                       {'name': u'Central Heating Maximum System Air Flow Ratio',
                                        'pyname': u'central_heating_maximum_system_air_flow_ratio',
                                        'default': 0.5,
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
                                      (u'type of zone sum to use',
                                       {'name': u'Type of Zone Sum to Use',
                                        'pyname': u'type_of_zone_sum_to_use',
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
                                      (u'cooling supply air flow rate method',
                                       {'name': u'Cooling Supply Air Flow Rate Method',
                                        'pyname': u'cooling_supply_air_flow_rate_method',
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
                                      (u'cooling supply air flow rate',
                                       {'name': u'Cooling Supply Air Flow Rate',
                                        'pyname': u'cooling_supply_air_flow_rate',
                                        'default': 0.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'm3/s'}),
                                      (u'cooling supply air flow rate per floor area',
                                       {'name': u'Cooling Supply Air Flow Rate Per Floor Area',
                                        'pyname': u'cooling_supply_air_flow_rate_per_floor_area',
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'm3/s-m2'}),
                                      (u'cooling fraction of autosized cooling supply air flow rate',
                                       {'name': u'Cooling Fraction of Autosized Cooling Supply Air Flow Rate',
                                        'pyname': u'cooling_fraction_of_autosized_cooling_supply_air_flow_rate',
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'cooling supply air flow rate per unit cooling capacity',
                                       {'name': u'Cooling Supply Air Flow Rate Per Unit Cooling Capacity',
                                        'pyname': u'cooling_supply_air_flow_rate_per_unit_cooling_capacity',
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'm3/s-W'}),
                                      (u'heating supply air flow rate method',
                                       {'name': u'Heating Supply Air Flow Rate Method',
                                        'pyname': u'heating_supply_air_flow_rate_method',
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
                                      (u'heating supply air flow rate',
                                       {'name': u'Heating Supply Air Flow Rate',
                                        'pyname': u'heating_supply_air_flow_rate',
                                        'default': 0.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'm3/s'}),
                                      (u'heating supply air flow rate per floor area',
                                       {'name': u'Heating Supply Air Flow Rate Per Floor Area',
                                        'pyname': u'heating_supply_air_flow_rate_per_floor_area',
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'm3/s-m2'}),
                                      (u'heating fraction of autosized heating supply air flow rate',
                                       {'name': u'Heating Fraction of Autosized Heating Supply Air Flow Rate',
                                        'pyname': u'heating_fraction_of_autosized_heating_supply_air_flow_rate',
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'heating fraction of autosized cooling supply air flow rate',
                                       {'name': u'Heating Fraction of Autosized Cooling Supply Air Flow Rate',
                                        'pyname': u'heating_fraction_of_autosized_cooling_supply_air_flow_rate',
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'heating supply air flow rate per unit heating capacity',
                                       {'name': u'Heating Supply Air Flow Rate Per Unit Heating Capacity',
                                        'pyname': u'heating_supply_air_flow_rate_per_unit_heating_capacity',
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
                                        'type': u'real'}),
                                      (u'central cooling capacity control method',
                                       {'name': u'Central Cooling Capacity Control Method',
                                        'pyname': u'central_cooling_capacity_control_method',
                                        'default': u'OnOff',
                                        'required-field': False,
                                        'autosizable': False,
                                        'accepted-values': [u'VAV',
                                                            u'Bypass',
                                                            u'VT',
                                                            u'OnOff'],
                                        'autocalculatable': False,
                                        'type': 'alpha'})]),
               'format': None,
               'group': u'HVAC Design Objects',
               'min-fields': 37,
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
        """field `Type of Load to Size On`

        |  Specifies the basis for sizing the system supply air flow rate
        |  Sensible and VentilationRequirement are the only available options
        |  Sensible uses the zone design air flow rates
        |  VentilationRequirement uses the system ventilation requirement
        |  Default value: Sensible

        Args:
            value (str): value for IDD Field `Type of Load to Size On`

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

        |  Units: m3/s
        |  Default value: "autosize"

        Args:
            value (float or "Autosize"): value for IDD Field `Design Outdoor Air Flow Rate`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float or "Autosize": the value of `design_outdoor_air_flow_rate` or None if not set

        """
        return self["Design Outdoor Air Flow Rate"]

    @design_outdoor_air_flow_rate.setter
    def design_outdoor_air_flow_rate(self, value="autosize"):
        """Corresponds to IDD field `Design Outdoor Air Flow Rate`"""
        self["Design Outdoor Air Flow Rate"] = value

    @property
    def central_heating_maximum_system_air_flow_ratio(self):
        """field `Central Heating Maximum System Air Flow Ratio`

        |  Default value: 0.5
        |  value <= 1.0

        Args:
            value (float): value for IDD Field `Central Heating Maximum System Air Flow Ratio`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `central_heating_maximum_system_air_flow_ratio` or None if not set

        """
        return self["Central Heating Maximum System Air Flow Ratio"]

    @central_heating_maximum_system_air_flow_ratio.setter
    def central_heating_maximum_system_air_flow_ratio(self, value=0.5):
        """Corresponds to IDD field `Central Heating Maximum System Air Flow
        Ratio`"""
        self["Central Heating Maximum System Air Flow Ratio"] = value

    @property
    def preheat_design_temperature(self):
        """field `Preheat Design Temperature`

        |  Units: C

        Args:
            value (float): value for IDD Field `Preheat Design Temperature`

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

        |  Units: kgWater/kgDryAir

        Args:
            value (float): value for IDD Field `Preheat Design Humidity Ratio`

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

        |  Units: C

        Args:
            value (float): value for IDD Field `Precool Design Temperature`

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

        |  Units: kgWater/kgDryAir

        Args:
            value (float): value for IDD Field `Precool Design Humidity Ratio`

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

        |  Units: C

        Args:
            value (float): value for IDD Field `Central Cooling Design Supply Air Temperature`

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

        |  Units: C

        Args:
            value (float): value for IDD Field `Central Heating Design Supply Air Temperature`

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
    def type_of_zone_sum_to_use(self):
        """field `Type of Zone Sum to Use`

        |  Default value: NonCoincident

        Args:
            value (str): value for IDD Field `Type of Zone Sum to Use`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `type_of_zone_sum_to_use` or None if not set

        """
        return self["Type of Zone Sum to Use"]

    @type_of_zone_sum_to_use.setter
    def type_of_zone_sum_to_use(self, value="NonCoincident"):
        """Corresponds to IDD field `Type of Zone Sum to Use`"""
        self["Type of Zone Sum to Use"] = value

    @property
    def a_100_outdoor_air_in_cooling(self):
        """field `100% Outdoor Air in Cooling`

        |  Default value: No

        Args:
            value (str): value for IDD Field `100% Outdoor Air in Cooling`

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

        |  Default value: No

        Args:
            value (str): value for IDD Field `100% Outdoor Air in Heating`

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

        |  Units: kgWater/kgDryAir
        |  Default value: 0.008

        Args:
            value (float): value for IDD Field `Central Cooling Design Supply Air Humidity Ratio`

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

        |  Units: kgWater/kgDryAir
        |  Default value: 0.008

        Args:
            value (float): value for IDD Field `Central Heating Design Supply Air Humidity Ratio`

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
    def cooling_supply_air_flow_rate_method(self):
        """field `Cooling Supply Air Flow Rate Method`

        |  Default value: DesignDay

        Args:
            value (str): value for IDD Field `Cooling Supply Air Flow Rate Method`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `cooling_supply_air_flow_rate_method` or None if not set

        """
        return self["Cooling Supply Air Flow Rate Method"]

    @cooling_supply_air_flow_rate_method.setter
    def cooling_supply_air_flow_rate_method(self, value="DesignDay"):
        """Corresponds to IDD field `Cooling Supply Air Flow Rate Method`"""
        self["Cooling Supply Air Flow Rate Method"] = value

    @property
    def cooling_supply_air_flow_rate(self):
        """field `Cooling Supply Air Flow Rate`

        |  This input is used if Cooling Supply Air Flow Rate Method is Flow/System
        |  This value will *not* be multiplied by any sizing factor or by zone multipliers.
        |  If using zone multipliers, this value must be large enough to serve the multiplied zones.
        |  Units: m3/s

        Args:
            value (float): value for IDD Field `Cooling Supply Air Flow Rate`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `cooling_supply_air_flow_rate` or None if not set

        """
        return self["Cooling Supply Air Flow Rate"]

    @cooling_supply_air_flow_rate.setter
    def cooling_supply_air_flow_rate(self, value=None):
        """Corresponds to IDD field `Cooling Supply Air Flow Rate`"""
        self["Cooling Supply Air Flow Rate"] = value

    @property
    def cooling_supply_air_flow_rate_per_floor_area(self):
        """field `Cooling Supply Air Flow Rate Per Floor Area`

        |  Enter the cooling supply air volume flow rate per total conditioned floor area.
        |  Required field when Cooling Supply Air Flow Rate Method is FlowPerFloorArea.
        |  Units: m3/s-m2

        Args:
            value (float): value for IDD Field `Cooling Supply Air Flow Rate Per Floor Area`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `cooling_supply_air_flow_rate_per_floor_area` or None if not set

        """
        return self["Cooling Supply Air Flow Rate Per Floor Area"]

    @cooling_supply_air_flow_rate_per_floor_area.setter
    def cooling_supply_air_flow_rate_per_floor_area(self, value=None):
        """Corresponds to IDD field `Cooling Supply Air Flow Rate Per Floor
        Area`"""
        self["Cooling Supply Air Flow Rate Per Floor Area"] = value

    @property
    def cooling_fraction_of_autosized_cooling_supply_air_flow_rate(self):
        """field `Cooling Fraction of Autosized Cooling Supply Air Flow Rate`

        |  Enter the supply air volume flow rate as a fraction of the cooling supply air flow rate.
        |  Required field when Cooling Supply Air Flow Rate Method is
        |  FractionOfAutosizedCoolingAirflow.

        Args:
            value (float): value for IDD Field `Cooling Fraction of Autosized Cooling Supply Air Flow Rate`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `cooling_fraction_of_autosized_cooling_supply_air_flow_rate` or None if not set

        """
        return self[
            "Cooling Fraction of Autosized Cooling Supply Air Flow Rate"]

    @cooling_fraction_of_autosized_cooling_supply_air_flow_rate.setter
    def cooling_fraction_of_autosized_cooling_supply_air_flow_rate(
            self,
            value=None):
        """Corresponds to IDD field `Cooling Fraction of Autosized Cooling
        Supply Air Flow Rate`"""
        self[
            "Cooling Fraction of Autosized Cooling Supply Air Flow Rate"] = value

    @property
    def cooling_supply_air_flow_rate_per_unit_cooling_capacity(self):
        """field `Cooling Supply Air Flow Rate Per Unit Cooling Capacity`

        |  Enter the supply air volume flow rate per unit cooling capacity.
        |  Required field when Cooling Supply Air Flow Rate Method is
        |  FlowPerCoolingCapacity.
        |  Units: m3/s-W

        Args:
            value (float): value for IDD Field `Cooling Supply Air Flow Rate Per Unit Cooling Capacity`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `cooling_supply_air_flow_rate_per_unit_cooling_capacity` or None if not set

        """
        return self["Cooling Supply Air Flow Rate Per Unit Cooling Capacity"]

    @cooling_supply_air_flow_rate_per_unit_cooling_capacity.setter
    def cooling_supply_air_flow_rate_per_unit_cooling_capacity(
            self,
            value=None):
        """Corresponds to IDD field `Cooling Supply Air Flow Rate Per Unit
        Cooling Capacity`"""
        self["Cooling Supply Air Flow Rate Per Unit Cooling Capacity"] = value

    @property
    def heating_supply_air_flow_rate_method(self):
        """field `Heating Supply Air Flow Rate Method`

        |  Default value: DesignDay

        Args:
            value (str): value for IDD Field `Heating Supply Air Flow Rate Method`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `heating_supply_air_flow_rate_method` or None if not set

        """
        return self["Heating Supply Air Flow Rate Method"]

    @heating_supply_air_flow_rate_method.setter
    def heating_supply_air_flow_rate_method(self, value="DesignDay"):
        """Corresponds to IDD field `Heating Supply Air Flow Rate Method`"""
        self["Heating Supply Air Flow Rate Method"] = value

    @property
    def heating_supply_air_flow_rate(self):
        """field `Heating Supply Air Flow Rate`

        |  Required field when Heating Supply Air Flow Rate Method is Flow/System
        |  This value will *not* be multiplied by any sizing factor or by zone multipliers.
        |  If using zone multipliers, this value must be large enough to serve the multiplied zones.
        |  Units: m3/s

        Args:
            value (float): value for IDD Field `Heating Supply Air Flow Rate`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `heating_supply_air_flow_rate` or None if not set

        """
        return self["Heating Supply Air Flow Rate"]

    @heating_supply_air_flow_rate.setter
    def heating_supply_air_flow_rate(self, value=None):
        """Corresponds to IDD field `Heating Supply Air Flow Rate`"""
        self["Heating Supply Air Flow Rate"] = value

    @property
    def heating_supply_air_flow_rate_per_floor_area(self):
        """field `Heating Supply Air Flow Rate Per Floor Area`

        |  Enter the heating supply air volume flow rate per total conditioned floor area.
        |  Required field when Heating Supply Air Flow Rate Method is FlowPerFloorArea.
        |  Units: m3/s-m2

        Args:
            value (float): value for IDD Field `Heating Supply Air Flow Rate Per Floor Area`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `heating_supply_air_flow_rate_per_floor_area` or None if not set

        """
        return self["Heating Supply Air Flow Rate Per Floor Area"]

    @heating_supply_air_flow_rate_per_floor_area.setter
    def heating_supply_air_flow_rate_per_floor_area(self, value=None):
        """Corresponds to IDD field `Heating Supply Air Flow Rate Per Floor
        Area`"""
        self["Heating Supply Air Flow Rate Per Floor Area"] = value

    @property
    def heating_fraction_of_autosized_heating_supply_air_flow_rate(self):
        """field `Heating Fraction of Autosized Heating Supply Air Flow Rate`

        |  Enter the supply air volume flow rate as a fraction of the heating supply air flow rate.
        |  Required field when Heating Supply Air Flow Rate Method is
        |  FractionOfAutosizedHeatingAirflow.

        Args:
            value (float): value for IDD Field `Heating Fraction of Autosized Heating Supply Air Flow Rate`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `heating_fraction_of_autosized_heating_supply_air_flow_rate` or None if not set

        """
        return self[
            "Heating Fraction of Autosized Heating Supply Air Flow Rate"]

    @heating_fraction_of_autosized_heating_supply_air_flow_rate.setter
    def heating_fraction_of_autosized_heating_supply_air_flow_rate(
            self,
            value=None):
        """Corresponds to IDD field `Heating Fraction of Autosized Heating
        Supply Air Flow Rate`"""
        self[
            "Heating Fraction of Autosized Heating Supply Air Flow Rate"] = value

    @property
    def heating_fraction_of_autosized_cooling_supply_air_flow_rate(self):
        """field `Heating Fraction of Autosized Cooling Supply Air Flow Rate`

        |  Enter the supply air volume flow rate as a fraction of the cooling supply air flow rate.
        |  Required field when Heating Supply Air Flow Rate Method is
        |  FractionOfAutosizedCoolingAirflow.

        Args:
            value (float): value for IDD Field `Heating Fraction of Autosized Cooling Supply Air Flow Rate`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `heating_fraction_of_autosized_cooling_supply_air_flow_rate` or None if not set

        """
        return self[
            "Heating Fraction of Autosized Cooling Supply Air Flow Rate"]

    @heating_fraction_of_autosized_cooling_supply_air_flow_rate.setter
    def heating_fraction_of_autosized_cooling_supply_air_flow_rate(
            self,
            value=None):
        """Corresponds to IDD field `Heating Fraction of Autosized Cooling
        Supply Air Flow Rate`"""
        self[
            "Heating Fraction of Autosized Cooling Supply Air Flow Rate"] = value

    @property
    def heating_supply_air_flow_rate_per_unit_heating_capacity(self):
        """field `Heating Supply Air Flow Rate Per Unit Heating Capacity`

        |  Enter the heating supply air volume flow rate per unit heating capacity.
        |  Required field when Heating Supply Air Flow Rate Method is
        |  FlowPerHeatingCapacity.
        |  Units: m3/s-W

        Args:
            value (float): value for IDD Field `Heating Supply Air Flow Rate Per Unit Heating Capacity`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `heating_supply_air_flow_rate_per_unit_heating_capacity` or None if not set

        """
        return self["Heating Supply Air Flow Rate Per Unit Heating Capacity"]

    @heating_supply_air_flow_rate_per_unit_heating_capacity.setter
    def heating_supply_air_flow_rate_per_unit_heating_capacity(
            self,
            value=None):
        """Corresponds to IDD field `Heating Supply Air Flow Rate Per Unit
        Heating Capacity`"""
        self["Heating Supply Air Flow Rate Per Unit Heating Capacity"] = value

    @property
    def system_outdoor_air_method(self):
        """field `System Outdoor Air Method`

        |  Default value: ZoneSum

        Args:
            value (str): value for IDD Field `System Outdoor Air Method`

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

        |  Units: dimensionless
        |  Default value: 1.0

        Args:
            value (float): value for IDD Field `Zone Maximum Outdoor Air Fraction`

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

        |  Enter the method used to determine the system cooling design capacity for scalable sizing.
        |  None is used when a cooling coils is not included in an airloop or this field may be blank.
        |  If this input field is left blank, then the design cooling capacity is set to zero.
        |  CoolingDesignCapacity => selected when the design cooling capacity value is specified or
        |  auto-sized. CapacityPerFloorArea => selected when the design cooling capacity is determined
        |  from user specified cooling capacity per floor area and total floor area of cooled zones
        |  served by an airloop. FractionOfAutosizedCoolingCapacity => is selected when the design
        |  cooling capacity is determined from a user specified fraction and the auto-sized design
        |  cooling capacity of the system.
        |  Default value: CoolingDesignCapacity

        Args:
            value (str): value for IDD Field `Cooling Design Capacity Method`

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
        """field `Cooling Design Capacity`

        |  Enter the design cooling capacity.
        |  Units: W
        |  Default value: "autosize"

        Args:
            value (float or "Autosize"): value for IDD Field `Cooling Design Capacity`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float or "Autosize": the value of `cooling_design_capacity` or None if not set

        """
        return self["Cooling Design Capacity"]

    @cooling_design_capacity.setter
    def cooling_design_capacity(self, value="autosize"):
        """Corresponds to IDD field `Cooling Design Capacity`"""
        self["Cooling Design Capacity"] = value

    @property
    def cooling_design_capacity_per_floor_area(self):
        """field `Cooling Design Capacity Per Floor Area`

        |  Enter the cooling design capacity per total floor area of cooled zones served by an airloop.
        |  Required field when the cooling design capacity method field is CapacityPerFloorArea.
        |  Units: W/m2

        Args:
            value (float): value for IDD Field `Cooling Design Capacity Per Floor Area`

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

        |  Enter the fraction of auto-sized cooling design capacity. Required field when the cooling
        |  design capacity method field is FractionOfAutosizedCoolingCapacity.

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

        |  Enter the method used to determine the heating design capacity for scalable sizing.
        |  None is used when a heating coil not included in an airloop or this field may be blank.
        |  If this input field is left blank, then the design heating capacity is set to zero.
        |  HeatingDesignCapacity => selected when the design heating capacity value is specified or
        |  auto-sized. CapacityPerFloorArea => selected when the design heating capacity is determined
        |  from user specified heating capacity per flow area and total floor area of heated zones
        |  served by an airloop. FractionOfAutosizedHeatingCapacity => is selected when the design
        |  heating capacity is determined from a user specified fraction and the auto-sized design
        |  heating capacity of the system.
        |  Default value: HeatingDesignCapacity

        Args:
            value (str): value for IDD Field `Heating Design Capacity Method`

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
        """field `Heating Design Capacity`

        |  Enter the design heating capacity.
        |  Units: W
        |  Default value: "autosize"

        Args:
            value (float or "Autosize"): value for IDD Field `Heating Design Capacity`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float or "Autosize": the value of `heating_design_capacity` or None if not set

        """
        return self["Heating Design Capacity"]

    @heating_design_capacity.setter
    def heating_design_capacity(self, value="autosize"):
        """Corresponds to IDD field `Heating Design Capacity`"""
        self["Heating Design Capacity"] = value

    @property
    def heating_design_capacity_per_floor_area(self):
        """field `Heating Design Capacity Per Floor Area`

        |  Enter the heating design capacity per zone floor area. Required field when the heating design
        |  capacity method field is CapacityPerFloorArea.
        |  Units: W/m2

        Args:
            value (float): value for IDD Field `Heating Design Capacity Per Floor Area`

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

        |  Enter the fraction of auto-sized heating design capacity. Required field when capacity the
        |  heating design capacity method field is FractionOfAutosizedHeatingCapacity.

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

    @property
    def central_cooling_capacity_control_method(self):
        """field `Central Cooling Capacity Control Method`

        |  Method used to control the coil's output
        |  Default value: OnOff

        Args:
            value (str): value for IDD Field `Central Cooling Capacity Control Method`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `central_cooling_capacity_control_method` or None if not set

        """
        return self["Central Cooling Capacity Control Method"]

    @central_cooling_capacity_control_method.setter
    def central_cooling_capacity_control_method(self, value="OnOff"):
        """Corresponds to IDD field `Central Cooling Capacity Control
        Method`"""
        self["Central Cooling Capacity Control Method"] = value




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
                                        'unit': u'deltaC'}),
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
                                      (u'zone timesteps in averaging window',
                                       {'name': u'Zone Timesteps in Averaging Window',
                                        'pyname': u'zone_timesteps_in_averaging_window',
                                        'default': 1,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 1,
                                        'autocalculatable': False,
                                        'type': u'integer'}),
                                      (u'coincident sizing factor mode',
                                       {'name': u'Coincident Sizing Factor Mode',
                                        'pyname': u'coincident_sizing_factor_mode',
                                        'required-field': False,
                                        'autosizable': False,
                                        'accepted-values': [u'None',
                                                            u'GlobalHeatingSizingFactor',
                                                            u'GlobalCoolingSizingFactor',
                                                            u'LoopComponentSizingFactor'],
                                        'autocalculatable': False,
                                        'type': 'alpha'})]),
               'format': None,
               'group': u'HVAC Design Objects',
               'min-fields': 4,
               'name': u'Sizing:Plant',
               'pyname': u'SizingPlant',
               'required-object': False,
               'unique-object': False}

    @property
    def plant_or_condenser_loop_name(self):
        """field `Plant or Condenser Loop Name`

        |  Enter the name of a PlantLoop or a CondenserLoop object

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

        |  Units: C

        Args:
            value (float): value for IDD Field `Design Loop Exit Temperature`

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

        |  Units: deltaC

        Args:
            value (float): value for IDD Field `Loop Design Temperature Difference`

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

    @property
    def sizing_option(self):
        """field `Sizing Option`

        |  if Coincident is chosen, then sizing is based on HVAC Sizing Simulations and
        |  the input field called Do HVAC Sizing Simulation for Sizing Periods in SimulationControl must be set to Yes
        |  Default value: NonCoincident

        Args:
            value (str): value for IDD Field `Sizing Option`

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
    def zone_timesteps_in_averaging_window(self):
        """field `Zone Timesteps in Averaging Window`

        |  this is used in the coincident sizing algorithm to apply a running average to peak flow rates
        |  that occur during HVAC Sizing Simulations
        |  Default value: 1
        |  value >= 1

        Args:
            value (int): value for IDD Field `Zone Timesteps in Averaging Window`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            int: the value of `zone_timesteps_in_averaging_window` or None if not set

        """
        return self["Zone Timesteps in Averaging Window"]

    @zone_timesteps_in_averaging_window.setter
    def zone_timesteps_in_averaging_window(self, value=1):
        """Corresponds to IDD field `Zone Timesteps in Averaging Window`"""
        self["Zone Timesteps in Averaging Window"] = value

    @property
    def coincident_sizing_factor_mode(self):
        """field `Coincident Sizing Factor Mode`

        |  this is used to adjust the result for coincident sizing by applying a sizing factor

        Args:
            value (str): value for IDD Field `Coincident Sizing Factor Mode`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `coincident_sizing_factor_mode` or None if not set

        """
        return self["Coincident Sizing Factor Mode"]

    @coincident_sizing_factor_mode.setter
    def coincident_sizing_factor_mode(self, value=None):
        """Corresponds to IDD field `Coincident Sizing Factor Mode`"""
        self["Coincident Sizing Factor Mode"] = value




class OutputControlSizingStyle(DataObject):

    """ Corresponds to IDD object `OutputControl:Sizing:Style`
        Default style for the Sizing output files is comma -- this works well for
        importing into spreadsheet programs such as Excel(tm) but not so well for word
        processing programs -- there tab may be a better choice.  Fixed puts spaces between
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


