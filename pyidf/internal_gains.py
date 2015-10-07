""" Data objects in group "Internal Gains"
"""

from collections import OrderedDict
import logging
from pyidf.helper import DataObject

logger = logging.getLogger("pyidf")
logger.addHandler(logging.NullHandler())



class People(DataObject):

    """Corresponds to IDD object `People` Sets internal gains and contaminant
    rates for occupants in the zone.

    If you use a ZoneList in the Zone or ZoneList name field then this
    definition applies to all the zones in the ZoneList.

    """
    _schema = {'extensible-fields': OrderedDict(),
               'fields': OrderedDict([(u'name',
                                       {'name': u'Name',
                                        'pyname': u'name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'alpha'}),
                                      (u'zone or zonelist name',
                                       {'name': u'Zone or ZoneList Name',
                                        'pyname': u'zone_or_zonelist_name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'number of people schedule name',
                                       {'name': u'Number of People Schedule Name',
                                        'pyname': u'number_of_people_schedule_name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'number of people calculation method',
                                       {'name': u'Number of People Calculation Method',
                                        'pyname': u'number_of_people_calculation_method',
                                        'default': u'People',
                                        'required-field': True,
                                        'autosizable': False,
                                        'accepted-values': [u'People',
                                                            u'People/Area',
                                                            u'Area/Person'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'number of people',
                                       {'name': u'Number of People',
                                        'pyname': u'number_of_people',
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'people per zone floor area',
                                       {'name': u'People per Zone Floor Area',
                                        'pyname': u'people_per_zone_floor_area',
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'person/m2'}),
                                      (u'zone floor area per person',
                                       {'name': u'Zone Floor Area per Person',
                                        'pyname': u'zone_floor_area_per_person',
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'm2/person'}),
                                      (u'fraction radiant',
                                       {'name': u'Fraction Radiant',
                                        'pyname': u'fraction_radiant',
                                        'maximum': 1.0,
                                        'required-field': True,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'sensible heat fraction',
                                       {'name': u'Sensible Heat Fraction',
                                        'pyname': u'sensible_heat_fraction',
                                        'default': 'autocalculate',
                                        'maximum': 1.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': True,
                                        'type': 'real'}),
                                      (u'activity level schedule name',
                                       {'name': u'Activity Level Schedule Name',
                                        'pyname': u'activity_level_schedule_name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'carbon dioxide generation rate',
                                       {'name': u'Carbon Dioxide Generation Rate',
                                        'pyname': u'carbon_dioxide_generation_rate',
                                        'default': 3.82e-08,
                                        'maximum': 3.82e-07,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'm3/s-W'}),
                                      (u'enable ashrae 55 comfort warnings',
                                       {'name': u'Enable ASHRAE 55 Comfort Warnings',
                                        'pyname': u'enable_ashrae_55_comfort_warnings',
                                        'default': u'No',
                                        'required-field': False,
                                        'autosizable': False,
                                        'accepted-values': [u'Yes',
                                                            u'No'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'mean radiant temperature calculation type',
                                       {'name': u'Mean Radiant Temperature Calculation Type',
                                        'pyname': u'mean_radiant_temperature_calculation_type',
                                        'default': u'ZoneAveraged',
                                        'required-field': False,
                                        'autosizable': False,
                                        'accepted-values': [u'ZoneAveraged',
                                                            u'SurfaceWeighted',
                                                            u'AngleFactor'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'surface name/angle factor list name',
                                       {'name': u'Surface Name/Angle Factor List Name',
                                        'pyname': u'surface_name_or_angle_factor_list_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'work efficiency schedule name',
                                       {'name': u'Work Efficiency Schedule Name',
                                        'pyname': u'work_efficiency_schedule_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'clothing insulation calculation method',
                                       {'name': u'Clothing Insulation Calculation Method',
                                        'pyname': u'clothing_insulation_calculation_method',
                                        'default': u'ClothingInsulationSchedule',
                                        'required-field': False,
                                        'autosizable': False,
                                        'accepted-values': [u'ClothingInsulationSchedule',
                                                            u'DynamicClothingModelASHRAE55',
                                                            u'CalculationMethodSchedule'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'clothing insulation calculation method schedule name',
                                       {'name': u'Clothing Insulation Calculation Method Schedule Name',
                                        'pyname': u'clothing_insulation_calculation_method_schedule_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'clothing insulation schedule name',
                                       {'name': u'Clothing Insulation Schedule Name',
                                        'pyname': u'clothing_insulation_schedule_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'air velocity schedule name',
                                       {'name': u'Air Velocity Schedule Name',
                                        'pyname': u'air_velocity_schedule_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'thermal comfort model 1 type',
                                       {'name': u'Thermal Comfort Model 1 Type',
                                        'pyname': u'thermal_comfort_model_1_type',
                                        'required-field': False,
                                        'autosizable': False,
                                        'accepted-values': [u'Fanger',
                                                            u'Pierce',
                                                            u'KSU',
                                                            u'AdaptiveASH55',
                                                            u'AdaptiveCEN15251'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'thermal comfort model 2 type',
                                       {'name': u'Thermal Comfort Model 2 Type',
                                        'pyname': u'thermal_comfort_model_2_type',
                                        'required-field': False,
                                        'autosizable': False,
                                        'accepted-values': [u'Fanger',
                                                            u'Pierce',
                                                            u'KSU',
                                                            u'AdaptiveASH55',
                                                            u'AdaptiveCEN15251'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'thermal comfort model 3 type',
                                       {'name': u'Thermal Comfort Model 3 Type',
                                        'pyname': u'thermal_comfort_model_3_type',
                                        'required-field': False,
                                        'autosizable': False,
                                        'accepted-values': [u'Fanger',
                                                            u'Pierce',
                                                            u'KSU',
                                                            u'AdaptiveASH55',
                                                            u'AdaptiveCEN15251'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'thermal comfort model 4 type',
                                       {'name': u'Thermal Comfort Model 4 Type',
                                        'pyname': u'thermal_comfort_model_4_type',
                                        'required-field': False,
                                        'autosizable': False,
                                        'accepted-values': [u'Fanger',
                                                            u'Pierce',
                                                            u'KSU',
                                                            u'AdaptiveASH55',
                                                            u'AdaptiveCEN15251'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'thermal comfort model 5 type',
                                       {'name': u'Thermal Comfort Model 5 Type',
                                        'pyname': u'thermal_comfort_model_5_type',
                                        'required-field': False,
                                        'autosizable': False,
                                        'accepted-values': [u'Fanger',
                                                            u'Pierce',
                                                            u'KSU',
                                                            u'AdaptiveASH55',
                                                            u'AdaptiveCEN15251'],
                                        'autocalculatable': False,
                                        'type': 'alpha'})]),
               'format': None,
               'group': u'Internal Gains',
               'min-fields': 0,
               'name': u'People',
               'pyname': u'People',
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
    def number_of_people_schedule_name(self):
        """field `Number of People Schedule Name`

        |  units in schedule should be fraction applied to number of people (0.0 - 1.0)

        Args:
            value (str): value for IDD Field `Number of People Schedule Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `number_of_people_schedule_name` or None if not set

        """
        return self["Number of People Schedule Name"]

    @number_of_people_schedule_name.setter
    def number_of_people_schedule_name(self, value=None):
        """Corresponds to IDD field `Number of People Schedule Name`"""
        self["Number of People Schedule Name"] = value

    @property
    def number_of_people_calculation_method(self):
        """field `Number of People Calculation Method`

        |  The entered calculation method is used to create the maximum number of people
        |  for this set of attributes (i.e. sensible fraction, schedule, etc)
        |  Choices: People -- simply enter number of occupants.
        |  People per Zone Floor Area -- enter the number to apply.  Value * Floor Area = Number of people
        |  Zone Floor Area per Person -- enter the number to apply.  Floor Area / Value = Number of people
        |  Default value: People

        Args:
            value (str): value for IDD Field `Number of People Calculation Method`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `number_of_people_calculation_method` or None if not set

        """
        return self["Number of People Calculation Method"]

    @number_of_people_calculation_method.setter
    def number_of_people_calculation_method(self, value="People"):
        """Corresponds to IDD field `Number of People Calculation Method`"""
        self["Number of People Calculation Method"] = value

    @property
    def number_of_people(self):
        """field `Number of People`

        Args:
            value (float): value for IDD Field `Number of People`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `number_of_people` or None if not set

        """
        return self["Number of People"]

    @number_of_people.setter
    def number_of_people(self, value=None):
        """Corresponds to IDD field `Number of People`"""
        self["Number of People"] = value

    @property
    def people_per_zone_floor_area(self):
        """field `People per Zone Floor Area`

        |  Units: person/m2

        Args:
            value (float): value for IDD Field `People per Zone Floor Area`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `people_per_zone_floor_area` or None if not set

        """
        return self["People per Zone Floor Area"]

    @people_per_zone_floor_area.setter
    def people_per_zone_floor_area(self, value=None):
        """Corresponds to IDD field `People per Zone Floor Area`"""
        self["People per Zone Floor Area"] = value

    @property
    def zone_floor_area_per_person(self):
        """field `Zone Floor Area per Person`

        |  Units: m2/person

        Args:
            value (float): value for IDD Field `Zone Floor Area per Person`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `zone_floor_area_per_person` or None if not set

        """
        return self["Zone Floor Area per Person"]

    @zone_floor_area_per_person.setter
    def zone_floor_area_per_person(self, value=None):
        """Corresponds to IDD field `Zone Floor Area per Person`"""
        self["Zone Floor Area per Person"] = value

    @property
    def fraction_radiant(self):
        """field `Fraction Radiant`

        |  value <= 1.0

        Args:
            value (float): value for IDD Field `Fraction Radiant`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `fraction_radiant` or None if not set

        """
        return self["Fraction Radiant"]

    @fraction_radiant.setter
    def fraction_radiant(self, value=None):
        """Corresponds to IDD field `Fraction Radiant`"""
        self["Fraction Radiant"] = value

    @property
    def sensible_heat_fraction(self):
        """field `Sensible Heat Fraction`

        |  if input, overrides program calculated sensible/latent split
        |  Default value: "autocalculate"
        |  value <= 1.0

        Args:
            value (float or "Autocalculate"): value for IDD Field `Sensible Heat Fraction`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float or "Autocalculate": the value of `sensible_heat_fraction` or None if not set

        """
        return self["Sensible Heat Fraction"]

    @sensible_heat_fraction.setter
    def sensible_heat_fraction(self, value="autocalculate"):
        """Corresponds to IDD field `Sensible Heat Fraction`"""
        self["Sensible Heat Fraction"] = value

    @property
    def activity_level_schedule_name(self):
        """field `Activity Level Schedule Name`

        |  Note that W has to be converted to mets in TC routine
        |  units in schedule are W/person

        Args:
            value (str): value for IDD Field `Activity Level Schedule Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `activity_level_schedule_name` or None if not set

        """
        return self["Activity Level Schedule Name"]

    @activity_level_schedule_name.setter
    def activity_level_schedule_name(self, value=None):
        """Corresponds to IDD field `Activity Level Schedule Name`"""
        self["Activity Level Schedule Name"] = value

    @property
    def carbon_dioxide_generation_rate(self):
        """field `Carbon Dioxide Generation Rate`

        |  CO2 generation rate per unit of activity level.
        |  The default value is obtained from ASHRAE Std 62.1 at 0.0084 cfm/met/person over
        |  the general adult population.
        |  Units: m3/s-W
        |  Default value: 3.82e-08
        |  value <= 3.82e-07

        Args:
            value (float): value for IDD Field `Carbon Dioxide Generation Rate`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `carbon_dioxide_generation_rate` or None if not set

        """
        return self["Carbon Dioxide Generation Rate"]

    @carbon_dioxide_generation_rate.setter
    def carbon_dioxide_generation_rate(self, value=3.82e-08):
        """Corresponds to IDD field `Carbon Dioxide Generation Rate`"""
        self["Carbon Dioxide Generation Rate"] = value

    @property
    def enable_ashrae_55_comfort_warnings(self):
        """field `Enable ASHRAE 55 Comfort Warnings`

        |  Default value: No

        Args:
            value (str): value for IDD Field `Enable ASHRAE 55 Comfort Warnings`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `enable_ashrae_55_comfort_warnings` or None if not set

        """
        return self["Enable ASHRAE 55 Comfort Warnings"]

    @enable_ashrae_55_comfort_warnings.setter
    def enable_ashrae_55_comfort_warnings(self, value="No"):
        """Corresponds to IDD field `Enable ASHRAE 55 Comfort Warnings`"""
        self["Enable ASHRAE 55 Comfort Warnings"] = value

    @property
    def mean_radiant_temperature_calculation_type(self):
        """field `Mean Radiant Temperature Calculation Type`

        |  optional (only required for thermal comfort runs)
        |  Default value: ZoneAveraged

        Args:
            value (str): value for IDD Field `Mean Radiant Temperature Calculation Type`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `mean_radiant_temperature_calculation_type` or None if not set

        """
        return self["Mean Radiant Temperature Calculation Type"]

    @mean_radiant_temperature_calculation_type.setter
    def mean_radiant_temperature_calculation_type(self, value="ZoneAveraged"):
        """Corresponds to IDD field `Mean Radiant Temperature Calculation
        Type`"""
        self["Mean Radiant Temperature Calculation Type"] = value

    @property
    def surface_name_or_angle_factor_list_name(self):
        """field `Surface Name/Angle Factor List Name`

        |  optional (only required for thermal comfort runs)

        Args:
            value (str): value for IDD Field `Surface Name/Angle Factor List Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `surface_name_or_angle_factor_list_name` or None if not set

        """
        return self["Surface Name/Angle Factor List Name"]

    @surface_name_or_angle_factor_list_name.setter
    def surface_name_or_angle_factor_list_name(self, value=None):
        """Corresponds to IDD field `Surface Name/Angle Factor List Name`"""
        self["Surface Name/Angle Factor List Name"] = value

    @property
    def work_efficiency_schedule_name(self):
        """field `Work Efficiency Schedule Name`

        |  units in schedule are 0.0 to 1.0
        |  optional (only required for thermal comfort runs)

        Args:
            value (str): value for IDD Field `Work Efficiency Schedule Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `work_efficiency_schedule_name` or None if not set

        """
        return self["Work Efficiency Schedule Name"]

    @work_efficiency_schedule_name.setter
    def work_efficiency_schedule_name(self, value=None):
        """Corresponds to IDD field `Work Efficiency Schedule Name`"""
        self["Work Efficiency Schedule Name"] = value

    @property
    def clothing_insulation_calculation_method(self):
        """field `Clothing Insulation Calculation Method`

        |  Default value: ClothingInsulationSchedule

        Args:
            value (str): value for IDD Field `Clothing Insulation Calculation Method`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `clothing_insulation_calculation_method` or None if not set

        """
        return self["Clothing Insulation Calculation Method"]

    @clothing_insulation_calculation_method.setter
    def clothing_insulation_calculation_method(
            self,
            value="ClothingInsulationSchedule"):
        """Corresponds to IDD field `Clothing Insulation Calculation Method`"""
        self["Clothing Insulation Calculation Method"] = value

    @property
    def clothing_insulation_calculation_method_schedule_name(self):
        """field `Clothing Insulation Calculation Method Schedule Name`

        |  a schedule value of 1 for the Scheduled method, and 2 for the DynamicClothingModelASHRAE55 method

        Args:
            value (str): value for IDD Field `Clothing Insulation Calculation Method Schedule Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `clothing_insulation_calculation_method_schedule_name` or None if not set

        """
        return self["Clothing Insulation Calculation Method Schedule Name"]

    @clothing_insulation_calculation_method_schedule_name.setter
    def clothing_insulation_calculation_method_schedule_name(self, value=None):
        """Corresponds to IDD field `Clothing Insulation Calculation Method
        Schedule Name`"""
        self["Clothing Insulation Calculation Method Schedule Name"] = value

    @property
    def clothing_insulation_schedule_name(self):
        """field `Clothing Insulation Schedule Name`

        |  use "Clo" from ASHRAE or Thermal Comfort guides
        |  optional (only required for thermal comfort runs)

        Args:
            value (str): value for IDD Field `Clothing Insulation Schedule Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `clothing_insulation_schedule_name` or None if not set

        """
        return self["Clothing Insulation Schedule Name"]

    @clothing_insulation_schedule_name.setter
    def clothing_insulation_schedule_name(self, value=None):
        """Corresponds to IDD field `Clothing Insulation Schedule Name`"""
        self["Clothing Insulation Schedule Name"] = value

    @property
    def air_velocity_schedule_name(self):
        """field `Air Velocity Schedule Name`

        |  units in the schedule are m/s
        |  optional (only required for thermal comfort runs)

        Args:
            value (str): value for IDD Field `Air Velocity Schedule Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `air_velocity_schedule_name` or None if not set

        """
        return self["Air Velocity Schedule Name"]

    @air_velocity_schedule_name.setter
    def air_velocity_schedule_name(self, value=None):
        """Corresponds to IDD field `Air Velocity Schedule Name`"""
        self["Air Velocity Schedule Name"] = value

    @property
    def thermal_comfort_model_1_type(self):
        """field `Thermal Comfort Model 1 Type`

        |  optional (only needed for people thermal comfort results reporting)

        Args:
            value (str): value for IDD Field `Thermal Comfort Model 1 Type`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `thermal_comfort_model_1_type` or None if not set

        """
        return self["Thermal Comfort Model 1 Type"]

    @thermal_comfort_model_1_type.setter
    def thermal_comfort_model_1_type(self, value=None):
        """Corresponds to IDD field `Thermal Comfort Model 1 Type`"""
        self["Thermal Comfort Model 1 Type"] = value

    @property
    def thermal_comfort_model_2_type(self):
        """field `Thermal Comfort Model 2 Type`

        |  optional (second type of thermal comfort model and results reporting)

        Args:
            value (str): value for IDD Field `Thermal Comfort Model 2 Type`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `thermal_comfort_model_2_type` or None if not set

        """
        return self["Thermal Comfort Model 2 Type"]

    @thermal_comfort_model_2_type.setter
    def thermal_comfort_model_2_type(self, value=None):
        """Corresponds to IDD field `Thermal Comfort Model 2 Type`"""
        self["Thermal Comfort Model 2 Type"] = value

    @property
    def thermal_comfort_model_3_type(self):
        """field `Thermal Comfort Model 3 Type`

        |  optional (third thermal comfort model and report type)

        Args:
            value (str): value for IDD Field `Thermal Comfort Model 3 Type`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `thermal_comfort_model_3_type` or None if not set

        """
        return self["Thermal Comfort Model 3 Type"]

    @thermal_comfort_model_3_type.setter
    def thermal_comfort_model_3_type(self, value=None):
        """Corresponds to IDD field `Thermal Comfort Model 3 Type`"""
        self["Thermal Comfort Model 3 Type"] = value

    @property
    def thermal_comfort_model_4_type(self):
        """field `Thermal Comfort Model 4 Type`

        |  optional (fourth thermal comfort model and report type)

        Args:
            value (str): value for IDD Field `Thermal Comfort Model 4 Type`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `thermal_comfort_model_4_type` or None if not set

        """
        return self["Thermal Comfort Model 4 Type"]

    @thermal_comfort_model_4_type.setter
    def thermal_comfort_model_4_type(self, value=None):
        """Corresponds to IDD field `Thermal Comfort Model 4 Type`"""
        self["Thermal Comfort Model 4 Type"] = value

    @property
    def thermal_comfort_model_5_type(self):
        """field `Thermal Comfort Model 5 Type`

        |  optional (fifth thermal comfort model and report type)

        Args:
            value (str): value for IDD Field `Thermal Comfort Model 5 Type`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `thermal_comfort_model_5_type` or None if not set

        """
        return self["Thermal Comfort Model 5 Type"]

    @thermal_comfort_model_5_type.setter
    def thermal_comfort_model_5_type(self, value=None):
        """Corresponds to IDD field `Thermal Comfort Model 5 Type`"""
        self["Thermal Comfort Model 5 Type"] = value




class ComfortViewFactorAngles(DataObject):

    """Corresponds to IDD object `ComfortViewFactorAngles` Used to specify
    radiant view factors for thermal comfort calculations."""
    _schema = {'extensible-fields': OrderedDict(),
               'fields': OrderedDict([(u'name',
                                       {'name': u'Name',
                                        'pyname': u'name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'alpha'}),
                                      (u'zone name',
                                       {'name': u'Zone Name',
                                        'pyname': u'zone_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'surface 1 name',
                                       {'name': u'Surface 1 Name',
                                        'pyname': u'surface_1_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'angle factor 1',
                                       {'name': u'Angle Factor 1',
                                        'pyname': u'angle_factor_1',
                                        'maximum': 1.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'surface 2 name',
                                       {'name': u'Surface 2 Name',
                                        'pyname': u'surface_2_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'angle factor 2',
                                       {'name': u'Angle Factor 2',
                                        'pyname': u'angle_factor_2',
                                        'maximum': 1.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'surface 3 name',
                                       {'name': u'Surface 3 Name',
                                        'pyname': u'surface_3_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'angle factor 3',
                                       {'name': u'Angle Factor 3',
                                        'pyname': u'angle_factor_3',
                                        'maximum': 1.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'surface 4 name',
                                       {'name': u'Surface 4 Name',
                                        'pyname': u'surface_4_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'angle factor 4',
                                       {'name': u'Angle Factor 4',
                                        'pyname': u'angle_factor_4',
                                        'maximum': 1.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'surface 5 name',
                                       {'name': u'Surface 5 Name',
                                        'pyname': u'surface_5_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'angle factor 5',
                                       {'name': u'Angle Factor 5',
                                        'pyname': u'angle_factor_5',
                                        'maximum': 1.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'surface 6 name',
                                       {'name': u'Surface 6 Name',
                                        'pyname': u'surface_6_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'angle factor 6',
                                       {'name': u'Angle Factor 6',
                                        'pyname': u'angle_factor_6',
                                        'maximum': 1.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'surface 7 name',
                                       {'name': u'Surface 7 Name',
                                        'pyname': u'surface_7_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'angle factor 7',
                                       {'name': u'Angle Factor 7',
                                        'pyname': u'angle_factor_7',
                                        'maximum': 1.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'surface 8 name',
                                       {'name': u'Surface 8 Name',
                                        'pyname': u'surface_8_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'angle factor 8',
                                       {'name': u'Angle Factor 8',
                                        'pyname': u'angle_factor_8',
                                        'maximum': 1.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'surface 9 name',
                                       {'name': u'Surface 9 Name',
                                        'pyname': u'surface_9_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'angle factor 9',
                                       {'name': u'Angle Factor 9',
                                        'pyname': u'angle_factor_9',
                                        'maximum': 1.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'surface 10 name',
                                       {'name': u'Surface 10 Name',
                                        'pyname': u'surface_10_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'angle factor 10',
                                       {'name': u'Angle Factor 10',
                                        'pyname': u'angle_factor_10',
                                        'maximum': 1.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'surface 11 name',
                                       {'name': u'Surface 11 Name',
                                        'pyname': u'surface_11_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'angle factor 11',
                                       {'name': u'Angle Factor 11',
                                        'pyname': u'angle_factor_11',
                                        'maximum': 1.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'surface 12 name',
                                       {'name': u'Surface 12 Name',
                                        'pyname': u'surface_12_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'angle factor 12',
                                       {'name': u'Angle Factor 12',
                                        'pyname': u'angle_factor_12',
                                        'maximum': 1.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'surface 13 name',
                                       {'name': u'Surface 13 Name',
                                        'pyname': u'surface_13_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'angle factor 13',
                                       {'name': u'Angle Factor 13',
                                        'pyname': u'angle_factor_13',
                                        'maximum': 1.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'surface 14 name',
                                       {'name': u'Surface 14 Name',
                                        'pyname': u'surface_14_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'angle factor 14',
                                       {'name': u'Angle Factor 14',
                                        'pyname': u'angle_factor_14',
                                        'maximum': 1.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'surface 15 name',
                                       {'name': u'Surface 15 Name',
                                        'pyname': u'surface_15_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'angle factor 15',
                                       {'name': u'Angle Factor 15',
                                        'pyname': u'angle_factor_15',
                                        'maximum': 1.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'surface 16 name',
                                       {'name': u'Surface 16 Name',
                                        'pyname': u'surface_16_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'angle factor 16',
                                       {'name': u'Angle Factor 16',
                                        'pyname': u'angle_factor_16',
                                        'maximum': 1.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'surface 17 name',
                                       {'name': u'Surface 17 Name',
                                        'pyname': u'surface_17_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'angle factor 17',
                                       {'name': u'Angle Factor 17',
                                        'pyname': u'angle_factor_17',
                                        'maximum': 1.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'surface 18 name',
                                       {'name': u'Surface 18 Name',
                                        'pyname': u'surface_18_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'angle factor 18',
                                       {'name': u'Angle Factor 18',
                                        'pyname': u'angle_factor_18',
                                        'maximum': 1.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'surface 19 name',
                                       {'name': u'Surface 19 Name',
                                        'pyname': u'surface_19_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'angle factor 19',
                                       {'name': u'Angle Factor 19',
                                        'pyname': u'angle_factor_19',
                                        'maximum': 1.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'surface 20 name',
                                       {'name': u'Surface 20 Name',
                                        'pyname': u'surface_20_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'angle factor 20',
                                       {'name': u'Angle Factor 20',
                                        'pyname': u'angle_factor_20',
                                        'maximum': 1.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real'})]),
               'format': None,
               'group': u'Internal Gains',
               'min-fields': 0,
               'name': u'ComfortViewFactorAngles',
               'pyname': u'ComfortViewFactorAngles',
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
    def zone_name(self):
        """field `Zone Name`

        Args:
            value (str): value for IDD Field `Zone Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `zone_name` or None if not set

        """
        return self["Zone Name"]

    @zone_name.setter
    def zone_name(self, value=None):
        """Corresponds to IDD field `Zone Name`"""
        self["Zone Name"] = value

    @property
    def surface_1_name(self):
        """field `Surface 1 Name`

        Args:
            value (str): value for IDD Field `Surface 1 Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `surface_1_name` or None if not set

        """
        return self["Surface 1 Name"]

    @surface_1_name.setter
    def surface_1_name(self, value=None):
        """Corresponds to IDD field `Surface 1 Name`"""
        self["Surface 1 Name"] = value

    @property
    def angle_factor_1(self):
        """field `Angle Factor 1`

        |  value <= 1.0

        Args:
            value (float): value for IDD Field `Angle Factor 1`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `angle_factor_1` or None if not set

        """
        return self["Angle Factor 1"]

    @angle_factor_1.setter
    def angle_factor_1(self, value=None):
        """Corresponds to IDD field `Angle Factor 1`"""
        self["Angle Factor 1"] = value

    @property
    def surface_2_name(self):
        """field `Surface 2 Name`

        Args:
            value (str): value for IDD Field `Surface 2 Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `surface_2_name` or None if not set

        """
        return self["Surface 2 Name"]

    @surface_2_name.setter
    def surface_2_name(self, value=None):
        """Corresponds to IDD field `Surface 2 Name`"""
        self["Surface 2 Name"] = value

    @property
    def angle_factor_2(self):
        """field `Angle Factor 2`

        |  value <= 1.0

        Args:
            value (float): value for IDD Field `Angle Factor 2`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `angle_factor_2` or None if not set

        """
        return self["Angle Factor 2"]

    @angle_factor_2.setter
    def angle_factor_2(self, value=None):
        """Corresponds to IDD field `Angle Factor 2`"""
        self["Angle Factor 2"] = value

    @property
    def surface_3_name(self):
        """field `Surface 3 Name`

        Args:
            value (str): value for IDD Field `Surface 3 Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `surface_3_name` or None if not set

        """
        return self["Surface 3 Name"]

    @surface_3_name.setter
    def surface_3_name(self, value=None):
        """Corresponds to IDD field `Surface 3 Name`"""
        self["Surface 3 Name"] = value

    @property
    def angle_factor_3(self):
        """field `Angle Factor 3`

        |  value <= 1.0

        Args:
            value (float): value for IDD Field `Angle Factor 3`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `angle_factor_3` or None if not set

        """
        return self["Angle Factor 3"]

    @angle_factor_3.setter
    def angle_factor_3(self, value=None):
        """Corresponds to IDD field `Angle Factor 3`"""
        self["Angle Factor 3"] = value

    @property
    def surface_4_name(self):
        """field `Surface 4 Name`

        Args:
            value (str): value for IDD Field `Surface 4 Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `surface_4_name` or None if not set

        """
        return self["Surface 4 Name"]

    @surface_4_name.setter
    def surface_4_name(self, value=None):
        """Corresponds to IDD field `Surface 4 Name`"""
        self["Surface 4 Name"] = value

    @property
    def angle_factor_4(self):
        """field `Angle Factor 4`

        |  value <= 1.0

        Args:
            value (float): value for IDD Field `Angle Factor 4`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `angle_factor_4` or None if not set

        """
        return self["Angle Factor 4"]

    @angle_factor_4.setter
    def angle_factor_4(self, value=None):
        """Corresponds to IDD field `Angle Factor 4`"""
        self["Angle Factor 4"] = value

    @property
    def surface_5_name(self):
        """field `Surface 5 Name`

        Args:
            value (str): value for IDD Field `Surface 5 Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `surface_5_name` or None if not set

        """
        return self["Surface 5 Name"]

    @surface_5_name.setter
    def surface_5_name(self, value=None):
        """Corresponds to IDD field `Surface 5 Name`"""
        self["Surface 5 Name"] = value

    @property
    def angle_factor_5(self):
        """field `Angle Factor 5`

        |  value <= 1.0

        Args:
            value (float): value for IDD Field `Angle Factor 5`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `angle_factor_5` or None if not set

        """
        return self["Angle Factor 5"]

    @angle_factor_5.setter
    def angle_factor_5(self, value=None):
        """Corresponds to IDD field `Angle Factor 5`"""
        self["Angle Factor 5"] = value

    @property
    def surface_6_name(self):
        """field `Surface 6 Name`

        Args:
            value (str): value for IDD Field `Surface 6 Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `surface_6_name` or None if not set

        """
        return self["Surface 6 Name"]

    @surface_6_name.setter
    def surface_6_name(self, value=None):
        """Corresponds to IDD field `Surface 6 Name`"""
        self["Surface 6 Name"] = value

    @property
    def angle_factor_6(self):
        """field `Angle Factor 6`

        |  value <= 1.0

        Args:
            value (float): value for IDD Field `Angle Factor 6`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `angle_factor_6` or None if not set

        """
        return self["Angle Factor 6"]

    @angle_factor_6.setter
    def angle_factor_6(self, value=None):
        """Corresponds to IDD field `Angle Factor 6`"""
        self["Angle Factor 6"] = value

    @property
    def surface_7_name(self):
        """field `Surface 7 Name`

        Args:
            value (str): value for IDD Field `Surface 7 Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `surface_7_name` or None if not set

        """
        return self["Surface 7 Name"]

    @surface_7_name.setter
    def surface_7_name(self, value=None):
        """Corresponds to IDD field `Surface 7 Name`"""
        self["Surface 7 Name"] = value

    @property
    def angle_factor_7(self):
        """field `Angle Factor 7`

        |  value <= 1.0

        Args:
            value (float): value for IDD Field `Angle Factor 7`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `angle_factor_7` or None if not set

        """
        return self["Angle Factor 7"]

    @angle_factor_7.setter
    def angle_factor_7(self, value=None):
        """Corresponds to IDD field `Angle Factor 7`"""
        self["Angle Factor 7"] = value

    @property
    def surface_8_name(self):
        """field `Surface 8 Name`

        Args:
            value (str): value for IDD Field `Surface 8 Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `surface_8_name` or None if not set

        """
        return self["Surface 8 Name"]

    @surface_8_name.setter
    def surface_8_name(self, value=None):
        """Corresponds to IDD field `Surface 8 Name`"""
        self["Surface 8 Name"] = value

    @property
    def angle_factor_8(self):
        """field `Angle Factor 8`

        |  value <= 1.0

        Args:
            value (float): value for IDD Field `Angle Factor 8`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `angle_factor_8` or None if not set

        """
        return self["Angle Factor 8"]

    @angle_factor_8.setter
    def angle_factor_8(self, value=None):
        """Corresponds to IDD field `Angle Factor 8`"""
        self["Angle Factor 8"] = value

    @property
    def surface_9_name(self):
        """field `Surface 9 Name`

        Args:
            value (str): value for IDD Field `Surface 9 Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `surface_9_name` or None if not set

        """
        return self["Surface 9 Name"]

    @surface_9_name.setter
    def surface_9_name(self, value=None):
        """Corresponds to IDD field `Surface 9 Name`"""
        self["Surface 9 Name"] = value

    @property
    def angle_factor_9(self):
        """field `Angle Factor 9`

        |  value <= 1.0

        Args:
            value (float): value for IDD Field `Angle Factor 9`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `angle_factor_9` or None if not set

        """
        return self["Angle Factor 9"]

    @angle_factor_9.setter
    def angle_factor_9(self, value=None):
        """Corresponds to IDD field `Angle Factor 9`"""
        self["Angle Factor 9"] = value

    @property
    def surface_10_name(self):
        """field `Surface 10 Name`

        Args:
            value (str): value for IDD Field `Surface 10 Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `surface_10_name` or None if not set

        """
        return self["Surface 10 Name"]

    @surface_10_name.setter
    def surface_10_name(self, value=None):
        """Corresponds to IDD field `Surface 10 Name`"""
        self["Surface 10 Name"] = value

    @property
    def angle_factor_10(self):
        """field `Angle Factor 10`

        |  value <= 1.0

        Args:
            value (float): value for IDD Field `Angle Factor 10`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `angle_factor_10` or None if not set

        """
        return self["Angle Factor 10"]

    @angle_factor_10.setter
    def angle_factor_10(self, value=None):
        """Corresponds to IDD field `Angle Factor 10`"""
        self["Angle Factor 10"] = value

    @property
    def surface_11_name(self):
        """field `Surface 11 Name`

        Args:
            value (str): value for IDD Field `Surface 11 Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `surface_11_name` or None if not set

        """
        return self["Surface 11 Name"]

    @surface_11_name.setter
    def surface_11_name(self, value=None):
        """Corresponds to IDD field `Surface 11 Name`"""
        self["Surface 11 Name"] = value

    @property
    def angle_factor_11(self):
        """field `Angle Factor 11`

        |  value <= 1.0

        Args:
            value (float): value for IDD Field `Angle Factor 11`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `angle_factor_11` or None if not set

        """
        return self["Angle Factor 11"]

    @angle_factor_11.setter
    def angle_factor_11(self, value=None):
        """Corresponds to IDD field `Angle Factor 11`"""
        self["Angle Factor 11"] = value

    @property
    def surface_12_name(self):
        """field `Surface 12 Name`

        Args:
            value (str): value for IDD Field `Surface 12 Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `surface_12_name` or None if not set

        """
        return self["Surface 12 Name"]

    @surface_12_name.setter
    def surface_12_name(self, value=None):
        """Corresponds to IDD field `Surface 12 Name`"""
        self["Surface 12 Name"] = value

    @property
    def angle_factor_12(self):
        """field `Angle Factor 12`

        |  value <= 1.0

        Args:
            value (float): value for IDD Field `Angle Factor 12`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `angle_factor_12` or None if not set

        """
        return self["Angle Factor 12"]

    @angle_factor_12.setter
    def angle_factor_12(self, value=None):
        """Corresponds to IDD field `Angle Factor 12`"""
        self["Angle Factor 12"] = value

    @property
    def surface_13_name(self):
        """field `Surface 13 Name`

        Args:
            value (str): value for IDD Field `Surface 13 Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `surface_13_name` or None if not set

        """
        return self["Surface 13 Name"]

    @surface_13_name.setter
    def surface_13_name(self, value=None):
        """Corresponds to IDD field `Surface 13 Name`"""
        self["Surface 13 Name"] = value

    @property
    def angle_factor_13(self):
        """field `Angle Factor 13`

        |  value <= 1.0

        Args:
            value (float): value for IDD Field `Angle Factor 13`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `angle_factor_13` or None if not set

        """
        return self["Angle Factor 13"]

    @angle_factor_13.setter
    def angle_factor_13(self, value=None):
        """Corresponds to IDD field `Angle Factor 13`"""
        self["Angle Factor 13"] = value

    @property
    def surface_14_name(self):
        """field `Surface 14 Name`

        Args:
            value (str): value for IDD Field `Surface 14 Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `surface_14_name` or None if not set

        """
        return self["Surface 14 Name"]

    @surface_14_name.setter
    def surface_14_name(self, value=None):
        """Corresponds to IDD field `Surface 14 Name`"""
        self["Surface 14 Name"] = value

    @property
    def angle_factor_14(self):
        """field `Angle Factor 14`

        |  value <= 1.0

        Args:
            value (float): value for IDD Field `Angle Factor 14`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `angle_factor_14` or None if not set

        """
        return self["Angle Factor 14"]

    @angle_factor_14.setter
    def angle_factor_14(self, value=None):
        """Corresponds to IDD field `Angle Factor 14`"""
        self["Angle Factor 14"] = value

    @property
    def surface_15_name(self):
        """field `Surface 15 Name`

        Args:
            value (str): value for IDD Field `Surface 15 Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `surface_15_name` or None if not set

        """
        return self["Surface 15 Name"]

    @surface_15_name.setter
    def surface_15_name(self, value=None):
        """Corresponds to IDD field `Surface 15 Name`"""
        self["Surface 15 Name"] = value

    @property
    def angle_factor_15(self):
        """field `Angle Factor 15`

        |  value <= 1.0

        Args:
            value (float): value for IDD Field `Angle Factor 15`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `angle_factor_15` or None if not set

        """
        return self["Angle Factor 15"]

    @angle_factor_15.setter
    def angle_factor_15(self, value=None):
        """Corresponds to IDD field `Angle Factor 15`"""
        self["Angle Factor 15"] = value

    @property
    def surface_16_name(self):
        """field `Surface 16 Name`

        Args:
            value (str): value for IDD Field `Surface 16 Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `surface_16_name` or None if not set

        """
        return self["Surface 16 Name"]

    @surface_16_name.setter
    def surface_16_name(self, value=None):
        """Corresponds to IDD field `Surface 16 Name`"""
        self["Surface 16 Name"] = value

    @property
    def angle_factor_16(self):
        """field `Angle Factor 16`

        |  value <= 1.0

        Args:
            value (float): value for IDD Field `Angle Factor 16`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `angle_factor_16` or None if not set

        """
        return self["Angle Factor 16"]

    @angle_factor_16.setter
    def angle_factor_16(self, value=None):
        """Corresponds to IDD field `Angle Factor 16`"""
        self["Angle Factor 16"] = value

    @property
    def surface_17_name(self):
        """field `Surface 17 Name`

        Args:
            value (str): value for IDD Field `Surface 17 Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `surface_17_name` or None if not set

        """
        return self["Surface 17 Name"]

    @surface_17_name.setter
    def surface_17_name(self, value=None):
        """Corresponds to IDD field `Surface 17 Name`"""
        self["Surface 17 Name"] = value

    @property
    def angle_factor_17(self):
        """field `Angle Factor 17`

        |  value <= 1.0

        Args:
            value (float): value for IDD Field `Angle Factor 17`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `angle_factor_17` or None if not set

        """
        return self["Angle Factor 17"]

    @angle_factor_17.setter
    def angle_factor_17(self, value=None):
        """Corresponds to IDD field `Angle Factor 17`"""
        self["Angle Factor 17"] = value

    @property
    def surface_18_name(self):
        """field `Surface 18 Name`

        Args:
            value (str): value for IDD Field `Surface 18 Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `surface_18_name` or None if not set

        """
        return self["Surface 18 Name"]

    @surface_18_name.setter
    def surface_18_name(self, value=None):
        """Corresponds to IDD field `Surface 18 Name`"""
        self["Surface 18 Name"] = value

    @property
    def angle_factor_18(self):
        """field `Angle Factor 18`

        |  value <= 1.0

        Args:
            value (float): value for IDD Field `Angle Factor 18`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `angle_factor_18` or None if not set

        """
        return self["Angle Factor 18"]

    @angle_factor_18.setter
    def angle_factor_18(self, value=None):
        """Corresponds to IDD field `Angle Factor 18`"""
        self["Angle Factor 18"] = value

    @property
    def surface_19_name(self):
        """field `Surface 19 Name`

        Args:
            value (str): value for IDD Field `Surface 19 Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `surface_19_name` or None if not set

        """
        return self["Surface 19 Name"]

    @surface_19_name.setter
    def surface_19_name(self, value=None):
        """Corresponds to IDD field `Surface 19 Name`"""
        self["Surface 19 Name"] = value

    @property
    def angle_factor_19(self):
        """field `Angle Factor 19`

        |  value <= 1.0

        Args:
            value (float): value for IDD Field `Angle Factor 19`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `angle_factor_19` or None if not set

        """
        return self["Angle Factor 19"]

    @angle_factor_19.setter
    def angle_factor_19(self, value=None):
        """Corresponds to IDD field `Angle Factor 19`"""
        self["Angle Factor 19"] = value

    @property
    def surface_20_name(self):
        """field `Surface 20 Name`

        Args:
            value (str): value for IDD Field `Surface 20 Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `surface_20_name` or None if not set

        """
        return self["Surface 20 Name"]

    @surface_20_name.setter
    def surface_20_name(self, value=None):
        """Corresponds to IDD field `Surface 20 Name`"""
        self["Surface 20 Name"] = value

    @property
    def angle_factor_20(self):
        """field `Angle Factor 20`

        |  value <= 1.0

        Args:
            value (float): value for IDD Field `Angle Factor 20`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `angle_factor_20` or None if not set

        """
        return self["Angle Factor 20"]

    @angle_factor_20.setter
    def angle_factor_20(self, value=None):
        """Corresponds to IDD field `Angle Factor 20`"""
        self["Angle Factor 20"] = value




class Lights(DataObject):

    """Corresponds to IDD object `Lights` Sets internal gains for lights in the
    zone.

    If you use a ZoneList in the Zone or ZoneList name field then this
    definition applies to all the zones in the ZoneList.

    """
    _schema = {'extensible-fields': OrderedDict(),
               'fields': OrderedDict([(u'name',
                                       {'name': u'Name',
                                        'pyname': u'name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'alpha'}),
                                      (u'zone or zonelist name',
                                       {'name': u'Zone or ZoneList Name',
                                        'pyname': u'zone_or_zonelist_name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'schedule name',
                                       {'name': u'Schedule Name',
                                        'pyname': u'schedule_name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'design level calculation method',
                                       {'name': u'Design Level Calculation Method',
                                        'pyname': u'design_level_calculation_method',
                                        'default': u'LightingLevel',
                                        'required-field': True,
                                        'autosizable': False,
                                        'accepted-values': [u'LightingLevel',
                                                            u'Watts/Area',
                                                            u'Watts/Person'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'lighting level',
                                       {'name': u'Lighting Level',
                                        'pyname': u'lighting_level',
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'W'}),
                                      (u'watts per zone floor area',
                                       {'name': u'Watts per Zone Floor Area',
                                        'pyname': u'watts_per_zone_floor_area',
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'W/m2'}),
                                      (u'watts per person',
                                       {'name': u'Watts per Person',
                                        'pyname': u'watts_per_person',
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'W/person'}),
                                      (u'return air fraction',
                                       {'name': u'Return Air Fraction',
                                        'pyname': u'return_air_fraction',
                                        'default': 0.0,
                                        'maximum': 1.0,
                                        'required-field': True,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'fraction radiant',
                                       {'name': u'Fraction Radiant',
                                        'pyname': u'fraction_radiant',
                                        'default': 0.0,
                                        'maximum': 1.0,
                                        'required-field': True,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'fraction visible',
                                       {'name': u'Fraction Visible',
                                        'pyname': u'fraction_visible',
                                        'default': 0.0,
                                        'maximum': 1.0,
                                        'required-field': True,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'fraction replaceable',
                                       {'name': u'Fraction Replaceable',
                                        'pyname': u'fraction_replaceable',
                                        'default': 1.0,
                                        'maximum': 1.0,
                                        'required-field': True,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'end-use subcategory',
                                       {'name': u'End-Use Subcategory',
                                        'pyname': u'enduse_subcategory',
                                        'default': u'General',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'alpha'}),
                                      (u'return air fraction calculated from plenum temperature',
                                       {'name': u'Return Air Fraction Calculated from Plenum Temperature',
                                        'pyname': u'return_air_fraction_calculated_from_plenum_temperature',
                                        'default': u'No',
                                        'required-field': False,
                                        'autosizable': False,
                                        'accepted-values': [u'Yes',
                                                            u'No'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'return air fraction function of plenum temperature coefficient 1',
                                       {'name': u'Return Air Fraction Function of Plenum Temperature Coefficient 1',
                                        'pyname': u'return_air_fraction_function_of_plenum_temperature_coefficient_1',
                                        'default': 0.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'return air fraction function of plenum temperature coefficient 2',
                                       {'name': u'Return Air Fraction Function of Plenum Temperature Coefficient 2',
                                        'pyname': u'return_air_fraction_function_of_plenum_temperature_coefficient_2',
                                        'default': 0.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'1/K'})]),
               'format': None,
               'group': u'Internal Gains',
               'min-fields': 10,
               'name': u'Lights',
               'pyname': u'Lights',
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
    def schedule_name(self):
        """field `Schedule Name`

        |  units in schedule should be fraction applied to design level of lights, generally (0.0 - 1.0)

        Args:
            value (str): value for IDD Field `Schedule Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `schedule_name` or None if not set

        """
        return self["Schedule Name"]

    @schedule_name.setter
    def schedule_name(self, value=None):
        """Corresponds to IDD field `Schedule Name`"""
        self["Schedule Name"] = value

    @property
    def design_level_calculation_method(self):
        """field `Design Level Calculation Method`

        |  The entered calculation method is used to create the maximum amount of lights
        |  for this set of attributes
        |  Choices: LightingLevel => Lighting Level -- simply enter watts of lights
        |  Watts/Area => Watts per Zone Floor Area -- enter the number to apply.  Value * Floor Area = Lights
        |  Watts/Person => Watts per Person -- enter the number to apply.  Value * Occupants = Lights
        |  Default value: LightingLevel

        Args:
            value (str): value for IDD Field `Design Level Calculation Method`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `design_level_calculation_method` or None if not set

        """
        return self["Design Level Calculation Method"]

    @design_level_calculation_method.setter
    def design_level_calculation_method(self, value="LightingLevel"):
        """Corresponds to IDD field `Design Level Calculation Method`"""
        self["Design Level Calculation Method"] = value

    @property
    def lighting_level(self):
        """field `Lighting Level`

        |  Units: W
        |  IP-Units: W

        Args:
            value (float): value for IDD Field `Lighting Level`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `lighting_level` or None if not set

        """
        return self["Lighting Level"]

    @lighting_level.setter
    def lighting_level(self, value=None):
        """Corresponds to IDD field `Lighting Level`"""
        self["Lighting Level"] = value

    @property
    def watts_per_zone_floor_area(self):
        """field `Watts per Zone Floor Area`

        |  Units: W/m2
        |  IP-Units: W/ft2

        Args:
            value (float): value for IDD Field `Watts per Zone Floor Area`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `watts_per_zone_floor_area` or None if not set

        """
        return self["Watts per Zone Floor Area"]

    @watts_per_zone_floor_area.setter
    def watts_per_zone_floor_area(self, value=None):
        """Corresponds to IDD field `Watts per Zone Floor Area`"""
        self["Watts per Zone Floor Area"] = value

    @property
    def watts_per_person(self):
        """field `Watts per Person`

        |  Units: W/person
        |  IP-Units: W/person

        Args:
            value (float): value for IDD Field `Watts per Person`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `watts_per_person` or None if not set

        """
        return self["Watts per Person"]

    @watts_per_person.setter
    def watts_per_person(self, value=None):
        """Corresponds to IDD field `Watts per Person`"""
        self["Watts per Person"] = value

    @property
    def return_air_fraction(self):
        """field `Return Air Fraction`

        |  Used only for sizing calculation if return-air-fraction
        |  coefficients are specified.
        |  value <= 1.0

        Args:
            value (float): value for IDD Field `Return Air Fraction`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `return_air_fraction` or None if not set

        """
        return self["Return Air Fraction"]

    @return_air_fraction.setter
    def return_air_fraction(self, value=None):
        """Corresponds to IDD field `Return Air Fraction`"""
        self["Return Air Fraction"] = value

    @property
    def fraction_radiant(self):
        """field `Fraction Radiant`

        |  value <= 1.0

        Args:
            value (float): value for IDD Field `Fraction Radiant`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `fraction_radiant` or None if not set

        """
        return self["Fraction Radiant"]

    @fraction_radiant.setter
    def fraction_radiant(self, value=None):
        """Corresponds to IDD field `Fraction Radiant`"""
        self["Fraction Radiant"] = value

    @property
    def fraction_visible(self):
        """field `Fraction Visible`

        |  value <= 1.0

        Args:
            value (float): value for IDD Field `Fraction Visible`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `fraction_visible` or None if not set

        """
        return self["Fraction Visible"]

    @fraction_visible.setter
    def fraction_visible(self, value=None):
        """Corresponds to IDD field `Fraction Visible`"""
        self["Fraction Visible"] = value

    @property
    def fraction_replaceable(self):
        """field `Fraction Replaceable`

        |  For Daylighting:Controls and Daylighting:DElight:Controls,
        |  must be 0 or 1:  0 = no dimming control, 1 = full dimming control
        |  Default value: 1.0
        |  value <= 1.0

        Args:
            value (float): value for IDD Field `Fraction Replaceable`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `fraction_replaceable` or None if not set

        """
        return self["Fraction Replaceable"]

    @fraction_replaceable.setter
    def fraction_replaceable(self, value=1.0):
        """Corresponds to IDD field `Fraction Replaceable`"""
        self["Fraction Replaceable"] = value

    @property
    def enduse_subcategory(self):
        """field `End-Use Subcategory`

        |  Default value: General

        Args:
            value (str): value for IDD Field `End-Use Subcategory`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `enduse_subcategory` or None if not set
        """
        return self["End-Use Subcategory"]

    @enduse_subcategory.setter
    def enduse_subcategory(self, value="General"):
        """  Corresponds to IDD field `End-Use Subcategory`

        """
        self["End-Use Subcategory"] = value

    @property
    def return_air_fraction_calculated_from_plenum_temperature(self):
        """field `Return Air Fraction Calculated from Plenum Temperature`

        |  Default value: No

        Args:
            value (str): value for IDD Field `Return Air Fraction Calculated from Plenum Temperature`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `return_air_fraction_calculated_from_plenum_temperature` or None if not set

        """
        return self["Return Air Fraction Calculated from Plenum Temperature"]

    @return_air_fraction_calculated_from_plenum_temperature.setter
    def return_air_fraction_calculated_from_plenum_temperature(
            self,
            value="No"):
        """Corresponds to IDD field `Return Air Fraction Calculated from Plenum
        Temperature`"""
        self["Return Air Fraction Calculated from Plenum Temperature"] = value

    @property
    def return_air_fraction_function_of_plenum_temperature_coefficient_1(self):
        """field `Return Air Fraction Function of Plenum Temperature
        Coefficient 1`

        |  Used only if Return Air Fraction Is Calculated from Plenum Temperature = Yes
        |  Equation is Return Air Fraction = Coefficient#1 - Coefficient#2 X PlenumTemp(degC)

        Args:
            value (float): value for IDD Field `Return Air Fraction Function of Plenum Temperature Coefficient 1`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `return_air_fraction_function_of_plenum_temperature_coefficient_1` or None if not set

        """
        return self[
            "Return Air Fraction Function of Plenum Temperature Coefficient 1"]

    @return_air_fraction_function_of_plenum_temperature_coefficient_1.setter
    def return_air_fraction_function_of_plenum_temperature_coefficient_1(
            self,
            value=None):
        """Corresponds to IDD field `Return Air Fraction Function of Plenum
        Temperature Coefficient 1`"""
        self[
            "Return Air Fraction Function of Plenum Temperature Coefficient 1"] = value

    @property
    def return_air_fraction_function_of_plenum_temperature_coefficient_2(self):
        """field `Return Air Fraction Function of Plenum Temperature
        Coefficient 2`

        |  Used only if Return Air Fraction Is Calculated from Plenum Temperature = Yes
        |  Equation is Return Air Fraction = Coefficient#1 - Coefficient#2 X PlenumTemp(degC)
        |  Units: 1/K

        Args:
            value (float): value for IDD Field `Return Air Fraction Function of Plenum Temperature Coefficient 2`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `return_air_fraction_function_of_plenum_temperature_coefficient_2` or None if not set

        """
        return self[
            "Return Air Fraction Function of Plenum Temperature Coefficient 2"]

    @return_air_fraction_function_of_plenum_temperature_coefficient_2.setter
    def return_air_fraction_function_of_plenum_temperature_coefficient_2(
            self,
            value=None):
        """Corresponds to IDD field `Return Air Fraction Function of Plenum
        Temperature Coefficient 2`"""
        self[
            "Return Air Fraction Function of Plenum Temperature Coefficient 2"] = value




class ElectricEquipment(DataObject):

    """Corresponds to IDD object `ElectricEquipment` Sets internal gains for
    electric equipment in the zone.

    If you use a ZoneList in the Zone or ZoneList name field then this
    definition applies to all the zones in the ZoneList.

    """
    _schema = {'extensible-fields': OrderedDict(),
               'fields': OrderedDict([(u'name',
                                       {'name': u'Name',
                                        'pyname': u'name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'alpha'}),
                                      (u'zone or zonelist name',
                                       {'name': u'Zone or ZoneList Name',
                                        'pyname': u'zone_or_zonelist_name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'schedule name',
                                       {'name': u'Schedule Name',
                                        'pyname': u'schedule_name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'design level calculation method',
                                       {'name': u'Design Level Calculation Method',
                                        'pyname': u'design_level_calculation_method',
                                        'default': u'EquipmentLevel',
                                        'required-field': True,
                                        'autosizable': False,
                                        'accepted-values': [u'EquipmentLevel',
                                                            u'Watts/Area',
                                                            u'Watts/Person'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'design level',
                                       {'name': u'Design Level',
                                        'pyname': u'design_level',
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'W'}),
                                      (u'watts per zone floor area',
                                       {'name': u'Watts per Zone Floor Area',
                                        'pyname': u'watts_per_zone_floor_area',
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'W/m2'}),
                                      (u'watts per person',
                                       {'name': u'Watts per Person',
                                        'pyname': u'watts_per_person',
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'W/person'}),
                                      (u'fraction latent',
                                       {'name': u'Fraction Latent',
                                        'pyname': u'fraction_latent',
                                        'default': 0.0,
                                        'maximum': 1.0,
                                        'required-field': True,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'fraction radiant',
                                       {'name': u'Fraction Radiant',
                                        'pyname': u'fraction_radiant',
                                        'default': 0.0,
                                        'maximum': 1.0,
                                        'required-field': True,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'fraction lost',
                                       {'name': u'Fraction Lost',
                                        'pyname': u'fraction_lost',
                                        'default': 0.0,
                                        'maximum': 1.0,
                                        'required-field': True,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'end-use subcategory',
                                       {'name': u'End-Use Subcategory',
                                        'pyname': u'enduse_subcategory',
                                        'default': u'General',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'alpha'})]),
               'format': None,
               'group': u'Internal Gains',
               'min-fields': 0,
               'name': u'ElectricEquipment',
               'pyname': u'ElectricEquipment',
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
    def schedule_name(self):
        """field `Schedule Name`

        |  units in schedule should be fraction applied to design level of electric equipment, generally (0.0 - 1.0)

        Args:
            value (str): value for IDD Field `Schedule Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `schedule_name` or None if not set

        """
        return self["Schedule Name"]

    @schedule_name.setter
    def schedule_name(self, value=None):
        """Corresponds to IDD field `Schedule Name`"""
        self["Schedule Name"] = value

    @property
    def design_level_calculation_method(self):
        """field `Design Level Calculation Method`

        |  The entered calculation method is used to create the maximum amount of electric equipment
        |  for this set of attributes
        |  Choices: EquipmentLevel => Equipment Level -- simply enter watts of equipment
        |  Watts/Area => Watts per Zone Floor Area -- enter the number to apply.  Value * Floor Area = Equipment Level
        |  Watts/Person => Watts per Person -- enter the number to apply.  Value * Occupants = Equipment Level
        |  Default value: EquipmentLevel

        Args:
            value (str): value for IDD Field `Design Level Calculation Method`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `design_level_calculation_method` or None if not set

        """
        return self["Design Level Calculation Method"]

    @design_level_calculation_method.setter
    def design_level_calculation_method(self, value="EquipmentLevel"):
        """Corresponds to IDD field `Design Level Calculation Method`"""
        self["Design Level Calculation Method"] = value

    @property
    def design_level(self):
        """field `Design Level`

        |  Units: W
        |  IP-Units: W

        Args:
            value (float): value for IDD Field `Design Level`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `design_level` or None if not set

        """
        return self["Design Level"]

    @design_level.setter
    def design_level(self, value=None):
        """Corresponds to IDD field `Design Level`"""
        self["Design Level"] = value

    @property
    def watts_per_zone_floor_area(self):
        """field `Watts per Zone Floor Area`

        |  Units: W/m2
        |  IP-Units: W/ft2

        Args:
            value (float): value for IDD Field `Watts per Zone Floor Area`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `watts_per_zone_floor_area` or None if not set

        """
        return self["Watts per Zone Floor Area"]

    @watts_per_zone_floor_area.setter
    def watts_per_zone_floor_area(self, value=None):
        """Corresponds to IDD field `Watts per Zone Floor Area`"""
        self["Watts per Zone Floor Area"] = value

    @property
    def watts_per_person(self):
        """field `Watts per Person`

        |  Units: W/person
        |  IP-Units: W/person

        Args:
            value (float): value for IDD Field `Watts per Person`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `watts_per_person` or None if not set

        """
        return self["Watts per Person"]

    @watts_per_person.setter
    def watts_per_person(self, value=None):
        """Corresponds to IDD field `Watts per Person`"""
        self["Watts per Person"] = value

    @property
    def fraction_latent(self):
        """field `Fraction Latent`

        |  value <= 1.0

        Args:
            value (float): value for IDD Field `Fraction Latent`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `fraction_latent` or None if not set

        """
        return self["Fraction Latent"]

    @fraction_latent.setter
    def fraction_latent(self, value=None):
        """Corresponds to IDD field `Fraction Latent`"""
        self["Fraction Latent"] = value

    @property
    def fraction_radiant(self):
        """field `Fraction Radiant`

        |  value <= 1.0

        Args:
            value (float): value for IDD Field `Fraction Radiant`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `fraction_radiant` or None if not set

        """
        return self["Fraction Radiant"]

    @fraction_radiant.setter
    def fraction_radiant(self, value=None):
        """Corresponds to IDD field `Fraction Radiant`"""
        self["Fraction Radiant"] = value

    @property
    def fraction_lost(self):
        """field `Fraction Lost`

        |  value <= 1.0

        Args:
            value (float): value for IDD Field `Fraction Lost`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `fraction_lost` or None if not set

        """
        return self["Fraction Lost"]

    @fraction_lost.setter
    def fraction_lost(self, value=None):
        """Corresponds to IDD field `Fraction Lost`"""
        self["Fraction Lost"] = value

    @property
    def enduse_subcategory(self):
        """field `End-Use Subcategory`

        |  Default value: General

        Args:
            value (str): value for IDD Field `End-Use Subcategory`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `enduse_subcategory` or None if not set
        """
        return self["End-Use Subcategory"]

    @enduse_subcategory.setter
    def enduse_subcategory(self, value="General"):
        """  Corresponds to IDD field `End-Use Subcategory`

        """
        self["End-Use Subcategory"] = value




class GasEquipment(DataObject):

    """Corresponds to IDD object `GasEquipment` Sets internal gains and
    contaminant rates for gas equipment in the zone.

    If you use a ZoneList in the Zone name field then this definition
    applies to all those zones.

    """
    _schema = {'extensible-fields': OrderedDict(),
               'fields': OrderedDict([(u'name',
                                       {'name': u'Name',
                                        'pyname': u'name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'alpha'}),
                                      (u'zone or zonelist name',
                                       {'name': u'Zone or ZoneList Name',
                                        'pyname': u'zone_or_zonelist_name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'schedule name',
                                       {'name': u'Schedule Name',
                                        'pyname': u'schedule_name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'design level calculation method',
                                       {'name': u'Design Level Calculation Method',
                                        'pyname': u'design_level_calculation_method',
                                        'default': u'EquipmentLevel',
                                        'required-field': True,
                                        'autosizable': False,
                                        'accepted-values': [u'EquipmentLevel',
                                                            u'Watts/Area',
                                                            u'Watts/Person',
                                                            u'Power/Area',
                                                            u'Power/Person'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'design level',
                                       {'name': u'Design Level',
                                        'pyname': u'design_level',
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'W'}),
                                      (u'power per zone floor area',
                                       {'name': u'Power per Zone Floor Area',
                                        'pyname': u'power_per_zone_floor_area',
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'W/m2'}),
                                      (u'power per person',
                                       {'name': u'Power per Person',
                                        'pyname': u'power_per_person',
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'W/Person'}),
                                      (u'fraction latent',
                                       {'name': u'Fraction Latent',
                                        'pyname': u'fraction_latent',
                                        'default': 0.0,
                                        'maximum': 1.0,
                                        'required-field': True,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'fraction radiant',
                                       {'name': u'Fraction Radiant',
                                        'pyname': u'fraction_radiant',
                                        'default': 0.0,
                                        'maximum': 1.0,
                                        'required-field': True,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'fraction lost',
                                       {'name': u'Fraction Lost',
                                        'pyname': u'fraction_lost',
                                        'default': 0.0,
                                        'maximum': 1.0,
                                        'required-field': True,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'carbon dioxide generation rate',
                                       {'name': u'Carbon Dioxide Generation Rate',
                                        'pyname': u'carbon_dioxide_generation_rate',
                                        'default': 0.0,
                                        'maximum': 4e-07,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'm3/s-W'}),
                                      (u'end-use subcategory',
                                       {'name': u'End-Use Subcategory',
                                        'pyname': u'enduse_subcategory',
                                        'default': u'General',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'alpha'})]),
               'format': None,
               'group': u'Internal Gains',
               'min-fields': 0,
               'name': u'GasEquipment',
               'pyname': u'GasEquipment',
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
    def schedule_name(self):
        """field `Schedule Name`

        |  units in Schedule should be fraction applied to design level of gas equipment, generally (0.0 - 1.0)

        Args:
            value (str): value for IDD Field `Schedule Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `schedule_name` or None if not set

        """
        return self["Schedule Name"]

    @schedule_name.setter
    def schedule_name(self, value=None):
        """Corresponds to IDD field `Schedule Name`"""
        self["Schedule Name"] = value

    @property
    def design_level_calculation_method(self):
        """field `Design Level Calculation Method`

        |  The entered calculation method is used to create the maximum amount of gas equipment
        |  for this set of attributes
        |  Choices: EquipmentLevel => Design Level -- simply enter power input of equipment
        |  Watts/Area or Power/Area => Power per Zone Floor Area -- enter the number to apply.  Value * Floor Area = Equipment Level
        |  Watts/Person or Power/Person => Power per Person -- enter the number to apply.  Value * Occupants = Equipment Level
        |  Default value: EquipmentLevel

        Args:
            value (str): value for IDD Field `Design Level Calculation Method`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `design_level_calculation_method` or None if not set

        """
        return self["Design Level Calculation Method"]

    @design_level_calculation_method.setter
    def design_level_calculation_method(self, value="EquipmentLevel"):
        """Corresponds to IDD field `Design Level Calculation Method`"""
        self["Design Level Calculation Method"] = value

    @property
    def design_level(self):
        """field `Design Level`

        |  Units: W
        |  IP-Units: Btu/h

        Args:
            value (float): value for IDD Field `Design Level`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `design_level` or None if not set

        """
        return self["Design Level"]

    @design_level.setter
    def design_level(self, value=None):
        """Corresponds to IDD field `Design Level`"""
        self["Design Level"] = value

    @property
    def power_per_zone_floor_area(self):
        """field `Power per Zone Floor Area`

        |  Units: W/m2
        |  IP-Units: Btu/h-ft2

        Args:
            value (float): value for IDD Field `Power per Zone Floor Area`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `power_per_zone_floor_area` or None if not set

        """
        return self["Power per Zone Floor Area"]

    @power_per_zone_floor_area.setter
    def power_per_zone_floor_area(self, value=None):
        """Corresponds to IDD field `Power per Zone Floor Area`"""
        self["Power per Zone Floor Area"] = value

    @property
    def power_per_person(self):
        """field `Power per Person`

        |  Units: W/Person
        |  IP-Units: Btu/h-person

        Args:
            value (float): value for IDD Field `Power per Person`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `power_per_person` or None if not set

        """
        return self["Power per Person"]

    @power_per_person.setter
    def power_per_person(self, value=None):
        """Corresponds to IDD field `Power per Person`"""
        self["Power per Person"] = value

    @property
    def fraction_latent(self):
        """field `Fraction Latent`

        |  value <= 1.0

        Args:
            value (float): value for IDD Field `Fraction Latent`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `fraction_latent` or None if not set

        """
        return self["Fraction Latent"]

    @fraction_latent.setter
    def fraction_latent(self, value=None):
        """Corresponds to IDD field `Fraction Latent`"""
        self["Fraction Latent"] = value

    @property
    def fraction_radiant(self):
        """field `Fraction Radiant`

        |  value <= 1.0

        Args:
            value (float): value for IDD Field `Fraction Radiant`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `fraction_radiant` or None if not set

        """
        return self["Fraction Radiant"]

    @fraction_radiant.setter
    def fraction_radiant(self, value=None):
        """Corresponds to IDD field `Fraction Radiant`"""
        self["Fraction Radiant"] = value

    @property
    def fraction_lost(self):
        """field `Fraction Lost`

        |  value <= 1.0

        Args:
            value (float): value for IDD Field `Fraction Lost`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `fraction_lost` or None if not set

        """
        return self["Fraction Lost"]

    @fraction_lost.setter
    def fraction_lost(self, value=None):
        """Corresponds to IDD field `Fraction Lost`"""
        self["Fraction Lost"] = value

    @property
    def carbon_dioxide_generation_rate(self):
        """field `Carbon Dioxide Generation Rate`

        |  CO2 generation rate per unit of power input
        |  The default value assumes the equipment is fully vented.
        |  For unvented equipment, a suggested value is 3.45E-8 m3/s-W. This value is
        |  converted from a natural gas CO2 emission rate of 117 lbs CO2 per million Btu.
        |  The maximum value assumes to be 10 times of the recommended value.
        |  Units: m3/s-W
        |  IP-Units: (ft3/min)/(Btu/h)
        |  value <= 4e-07

        Args:
            value (float): value for IDD Field `Carbon Dioxide Generation Rate`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `carbon_dioxide_generation_rate` or None if not set

        """
        return self["Carbon Dioxide Generation Rate"]

    @carbon_dioxide_generation_rate.setter
    def carbon_dioxide_generation_rate(self, value=None):
        """Corresponds to IDD field `Carbon Dioxide Generation Rate`"""
        self["Carbon Dioxide Generation Rate"] = value

    @property
    def enduse_subcategory(self):
        """field `End-Use Subcategory`

        |  Default value: General

        Args:
            value (str): value for IDD Field `End-Use Subcategory`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `enduse_subcategory` or None if not set
        """
        return self["End-Use Subcategory"]

    @enduse_subcategory.setter
    def enduse_subcategory(self, value="General"):
        """  Corresponds to IDD field `End-Use Subcategory`

        """
        self["End-Use Subcategory"] = value




class HotWaterEquipment(DataObject):

    """Corresponds to IDD object `HotWaterEquipment` Sets internal gains for
    hot water equipment in the zone.

    If you use a ZoneList in the Zone name field then this definition
    applies to all those zones.

    """
    _schema = {'extensible-fields': OrderedDict(),
               'fields': OrderedDict([(u'name',
                                       {'name': u'Name',
                                        'pyname': u'name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'alpha'}),
                                      (u'zone or zonelist name',
                                       {'name': u'Zone or ZoneList Name',
                                        'pyname': u'zone_or_zonelist_name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'schedule name',
                                       {'name': u'Schedule Name',
                                        'pyname': u'schedule_name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'design level calculation method',
                                       {'name': u'Design Level Calculation Method',
                                        'pyname': u'design_level_calculation_method',
                                        'default': u'EquipmentLevel',
                                        'required-field': True,
                                        'autosizable': False,
                                        'accepted-values': [u'EquipmentLevel',
                                                            u'Watts/Area',
                                                            u'Watts/Person',
                                                            u'Power/Area',
                                                            u'Power/Person'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'design level',
                                       {'name': u'Design Level',
                                        'pyname': u'design_level',
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'W'}),
                                      (u'power per zone floor area',
                                       {'name': u'Power per Zone Floor Area',
                                        'pyname': u'power_per_zone_floor_area',
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'W/m2'}),
                                      (u'power per person',
                                       {'name': u'Power per Person',
                                        'pyname': u'power_per_person',
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'W/Person'}),
                                      (u'fraction latent',
                                       {'name': u'Fraction Latent',
                                        'pyname': u'fraction_latent',
                                        'default': 0.0,
                                        'maximum': 1.0,
                                        'required-field': True,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'fraction radiant',
                                       {'name': u'Fraction Radiant',
                                        'pyname': u'fraction_radiant',
                                        'default': 0.0,
                                        'maximum': 1.0,
                                        'required-field': True,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'fraction lost',
                                       {'name': u'Fraction Lost',
                                        'pyname': u'fraction_lost',
                                        'default': 0.0,
                                        'maximum': 1.0,
                                        'required-field': True,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'end-use subcategory',
                                       {'name': u'End-Use Subcategory',
                                        'pyname': u'enduse_subcategory',
                                        'default': u'General',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'alpha'})]),
               'format': None,
               'group': u'Internal Gains',
               'min-fields': 0,
               'name': u'HotWaterEquipment',
               'pyname': u'HotWaterEquipment',
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
    def schedule_name(self):
        """field `Schedule Name`

        |  units in Schedule should be fraction applied to design level of hot water equipment, generally (0.0 - 1.0)

        Args:
            value (str): value for IDD Field `Schedule Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `schedule_name` or None if not set

        """
        return self["Schedule Name"]

    @schedule_name.setter
    def schedule_name(self, value=None):
        """Corresponds to IDD field `Schedule Name`"""
        self["Schedule Name"] = value

    @property
    def design_level_calculation_method(self):
        """field `Design Level Calculation Method`

        |  The entered calculation method is used to create the maximum amount of hot water equipment
        |  for this set of attributes
        |  Choices: EquipmentLevel => Design Level -- simply enter power input of equipment
        |  Watts/Area or Power/Area => Power per Zone Floor Area -- enter the number to apply.  Value * Floor Area = Equipment Level
        |  Watts/Person or Power/Person => Power per Person -- enter the number to apply.  Value * Occupants = Equipment Level
        |  Default value: EquipmentLevel

        Args:
            value (str): value for IDD Field `Design Level Calculation Method`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `design_level_calculation_method` or None if not set

        """
        return self["Design Level Calculation Method"]

    @design_level_calculation_method.setter
    def design_level_calculation_method(self, value="EquipmentLevel"):
        """Corresponds to IDD field `Design Level Calculation Method`"""
        self["Design Level Calculation Method"] = value

    @property
    def design_level(self):
        """field `Design Level`

        |  Units: W
        |  IP-Units: Btu/h

        Args:
            value (float): value for IDD Field `Design Level`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `design_level` or None if not set

        """
        return self["Design Level"]

    @design_level.setter
    def design_level(self, value=None):
        """Corresponds to IDD field `Design Level`"""
        self["Design Level"] = value

    @property
    def power_per_zone_floor_area(self):
        """field `Power per Zone Floor Area`

        |  Units: W/m2
        |  IP-Units: Btu/h-ft2

        Args:
            value (float): value for IDD Field `Power per Zone Floor Area`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `power_per_zone_floor_area` or None if not set

        """
        return self["Power per Zone Floor Area"]

    @power_per_zone_floor_area.setter
    def power_per_zone_floor_area(self, value=None):
        """Corresponds to IDD field `Power per Zone Floor Area`"""
        self["Power per Zone Floor Area"] = value

    @property
    def power_per_person(self):
        """field `Power per Person`

        |  Units: W/Person
        |  IP-Units: Btu/h-person

        Args:
            value (float): value for IDD Field `Power per Person`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `power_per_person` or None if not set

        """
        return self["Power per Person"]

    @power_per_person.setter
    def power_per_person(self, value=None):
        """Corresponds to IDD field `Power per Person`"""
        self["Power per Person"] = value

    @property
    def fraction_latent(self):
        """field `Fraction Latent`

        |  value <= 1.0

        Args:
            value (float): value for IDD Field `Fraction Latent`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `fraction_latent` or None if not set

        """
        return self["Fraction Latent"]

    @fraction_latent.setter
    def fraction_latent(self, value=None):
        """Corresponds to IDD field `Fraction Latent`"""
        self["Fraction Latent"] = value

    @property
    def fraction_radiant(self):
        """field `Fraction Radiant`

        |  value <= 1.0

        Args:
            value (float): value for IDD Field `Fraction Radiant`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `fraction_radiant` or None if not set

        """
        return self["Fraction Radiant"]

    @fraction_radiant.setter
    def fraction_radiant(self, value=None):
        """Corresponds to IDD field `Fraction Radiant`"""
        self["Fraction Radiant"] = value

    @property
    def fraction_lost(self):
        """field `Fraction Lost`

        |  value <= 1.0

        Args:
            value (float): value for IDD Field `Fraction Lost`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `fraction_lost` or None if not set

        """
        return self["Fraction Lost"]

    @fraction_lost.setter
    def fraction_lost(self, value=None):
        """Corresponds to IDD field `Fraction Lost`"""
        self["Fraction Lost"] = value

    @property
    def enduse_subcategory(self):
        """field `End-Use Subcategory`

        |  Default value: General

        Args:
            value (str): value for IDD Field `End-Use Subcategory`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `enduse_subcategory` or None if not set
        """
        return self["End-Use Subcategory"]

    @enduse_subcategory.setter
    def enduse_subcategory(self, value="General"):
        """  Corresponds to IDD field `End-Use Subcategory`

        """
        self["End-Use Subcategory"] = value




class SteamEquipment(DataObject):

    """Corresponds to IDD object `SteamEquipment` Sets internal gains for steam
    equipment in the zone."""
    _schema = {'extensible-fields': OrderedDict(),
               'fields': OrderedDict([(u'name',
                                       {'name': u'Name',
                                        'pyname': u'name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'alpha'}),
                                      (u'zone or zonelist name',
                                       {'name': u'Zone or ZoneList Name',
                                        'pyname': u'zone_or_zonelist_name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'schedule name',
                                       {'name': u'Schedule Name',
                                        'pyname': u'schedule_name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'design level calculation method',
                                       {'name': u'Design Level Calculation Method',
                                        'pyname': u'design_level_calculation_method',
                                        'default': u'EquipmentLevel',
                                        'required-field': True,
                                        'autosizable': False,
                                        'accepted-values': [u'EquipmentLevel',
                                                            u'Watts/Area',
                                                            u'Watts/Person',
                                                            u'Power/Area',
                                                            u'Power/Person'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'design level',
                                       {'name': u'Design Level',
                                        'pyname': u'design_level',
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'W'}),
                                      (u'power per zone floor area',
                                       {'name': u'Power per Zone Floor Area',
                                        'pyname': u'power_per_zone_floor_area',
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'W/m2'}),
                                      (u'power per person',
                                       {'name': u'Power per Person',
                                        'pyname': u'power_per_person',
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'W/Person'}),
                                      (u'fraction latent',
                                       {'name': u'Fraction Latent',
                                        'pyname': u'fraction_latent',
                                        'default': 0.0,
                                        'maximum': 1.0,
                                        'required-field': True,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'fraction radiant',
                                       {'name': u'Fraction Radiant',
                                        'pyname': u'fraction_radiant',
                                        'default': 0.0,
                                        'maximum': 1.0,
                                        'required-field': True,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'fraction lost',
                                       {'name': u'Fraction Lost',
                                        'pyname': u'fraction_lost',
                                        'default': 0.0,
                                        'maximum': 1.0,
                                        'required-field': True,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'end-use subcategory',
                                       {'name': u'End-Use Subcategory',
                                        'pyname': u'enduse_subcategory',
                                        'default': u'General',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'alpha'})]),
               'format': None,
               'group': u'Internal Gains',
               'min-fields': 0,
               'name': u'SteamEquipment',
               'pyname': u'SteamEquipment',
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
    def schedule_name(self):
        """field `Schedule Name`

        |  units in Schedule should be fraction applied to design level of steam equipment, generally (0.0 - 1.0)

        Args:
            value (str): value for IDD Field `Schedule Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `schedule_name` or None if not set

        """
        return self["Schedule Name"]

    @schedule_name.setter
    def schedule_name(self, value=None):
        """Corresponds to IDD field `Schedule Name`"""
        self["Schedule Name"] = value

    @property
    def design_level_calculation_method(self):
        """field `Design Level Calculation Method`

        |  The entered calculation method is used to create the maximum amount of steam equipment
        |  for this set of attributes
        |  Choices: EquipmentLevel => Design Level -- simply enter power input of equipment
        |  Watts/Area or Power/Area => Power per Zone Floor Area -- enter the number to apply.  Value * Floor Area = Equipment Level
        |  Watts/Person or Power/Person => Power per Person -- enter the number to apply.  Value * Occupants = Equipment Level
        |  Default value: EquipmentLevel

        Args:
            value (str): value for IDD Field `Design Level Calculation Method`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `design_level_calculation_method` or None if not set

        """
        return self["Design Level Calculation Method"]

    @design_level_calculation_method.setter
    def design_level_calculation_method(self, value="EquipmentLevel"):
        """Corresponds to IDD field `Design Level Calculation Method`"""
        self["Design Level Calculation Method"] = value

    @property
    def design_level(self):
        """field `Design Level`

        |  Units: W
        |  IP-Units: Btu/h

        Args:
            value (float): value for IDD Field `Design Level`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `design_level` or None if not set

        """
        return self["Design Level"]

    @design_level.setter
    def design_level(self, value=None):
        """Corresponds to IDD field `Design Level`"""
        self["Design Level"] = value

    @property
    def power_per_zone_floor_area(self):
        """field `Power per Zone Floor Area`

        |  Units: W/m2
        |  IP-Units: Btu/h-ft2

        Args:
            value (float): value for IDD Field `Power per Zone Floor Area`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `power_per_zone_floor_area` or None if not set

        """
        return self["Power per Zone Floor Area"]

    @power_per_zone_floor_area.setter
    def power_per_zone_floor_area(self, value=None):
        """Corresponds to IDD field `Power per Zone Floor Area`"""
        self["Power per Zone Floor Area"] = value

    @property
    def power_per_person(self):
        """field `Power per Person`

        |  Units: W/Person
        |  IP-Units: Btu/h-person

        Args:
            value (float): value for IDD Field `Power per Person`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `power_per_person` or None if not set

        """
        return self["Power per Person"]

    @power_per_person.setter
    def power_per_person(self, value=None):
        """Corresponds to IDD field `Power per Person`"""
        self["Power per Person"] = value

    @property
    def fraction_latent(self):
        """field `Fraction Latent`

        |  value <= 1.0

        Args:
            value (float): value for IDD Field `Fraction Latent`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `fraction_latent` or None if not set

        """
        return self["Fraction Latent"]

    @fraction_latent.setter
    def fraction_latent(self, value=None):
        """Corresponds to IDD field `Fraction Latent`"""
        self["Fraction Latent"] = value

    @property
    def fraction_radiant(self):
        """field `Fraction Radiant`

        |  value <= 1.0

        Args:
            value (float): value for IDD Field `Fraction Radiant`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `fraction_radiant` or None if not set

        """
        return self["Fraction Radiant"]

    @fraction_radiant.setter
    def fraction_radiant(self, value=None):
        """Corresponds to IDD field `Fraction Radiant`"""
        self["Fraction Radiant"] = value

    @property
    def fraction_lost(self):
        """field `Fraction Lost`

        |  value <= 1.0

        Args:
            value (float): value for IDD Field `Fraction Lost`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `fraction_lost` or None if not set

        """
        return self["Fraction Lost"]

    @fraction_lost.setter
    def fraction_lost(self, value=None):
        """Corresponds to IDD field `Fraction Lost`"""
        self["Fraction Lost"] = value

    @property
    def enduse_subcategory(self):
        """field `End-Use Subcategory`

        |  Default value: General

        Args:
            value (str): value for IDD Field `End-Use Subcategory`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `enduse_subcategory` or None if not set
        """
        return self["End-Use Subcategory"]

    @enduse_subcategory.setter
    def enduse_subcategory(self, value="General"):
        """  Corresponds to IDD field `End-Use Subcategory`

        """
        self["End-Use Subcategory"] = value




class OtherEquipment(DataObject):

    """Corresponds to IDD object `OtherEquipment` Sets internal gains or losses
    for "other" equipment in the zone."""
    _schema = {'extensible-fields': OrderedDict(),
               'fields': OrderedDict([(u'name',
                                       {'name': u'Name',
                                        'pyname': u'name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'alpha'}),
                                      (u'zone or zonelist name',
                                       {'name': u'Zone or ZoneList Name',
                                        'pyname': u'zone_or_zonelist_name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'schedule name',
                                       {'name': u'Schedule Name',
                                        'pyname': u'schedule_name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'design level calculation method',
                                       {'name': u'Design Level Calculation Method',
                                        'pyname': u'design_level_calculation_method',
                                        'default': u'EquipmentLevel',
                                        'required-field': True,
                                        'autosizable': False,
                                        'accepted-values': [u'EquipmentLevel',
                                                            u'Watts/Area',
                                                            u'Watts/Person',
                                                            u'Power/Area',
                                                            u'Power/Person'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'design level',
                                       {'name': u'Design Level',
                                        'pyname': u'design_level',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'W'}),
                                      (u'power per zone floor area',
                                       {'name': u'Power per Zone Floor Area',
                                        'pyname': u'power_per_zone_floor_area',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'W/m2'}),
                                      (u'power per person',
                                       {'name': u'Power per Person',
                                        'pyname': u'power_per_person',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'W/Person'}),
                                      (u'fraction latent',
                                       {'name': u'Fraction Latent',
                                        'pyname': u'fraction_latent',
                                        'default': 0.0,
                                        'maximum': 1.0,
                                        'required-field': True,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'fraction radiant',
                                       {'name': u'Fraction Radiant',
                                        'pyname': u'fraction_radiant',
                                        'default': 0.0,
                                        'maximum': 1.0,
                                        'required-field': True,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'fraction lost',
                                       {'name': u'Fraction Lost',
                                        'pyname': u'fraction_lost',
                                        'default': 0.0,
                                        'maximum': 1.0,
                                        'required-field': True,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real'})]),
               'format': None,
               'group': u'Internal Gains',
               'min-fields': 0,
               'name': u'OtherEquipment',
               'pyname': u'OtherEquipment',
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
    def schedule_name(self):
        """field `Schedule Name`

        |  units in Schedule should be fraction applied to design level of other equipment, generally (0.0 - 1.0)

        Args:
            value (str): value for IDD Field `Schedule Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `schedule_name` or None if not set

        """
        return self["Schedule Name"]

    @schedule_name.setter
    def schedule_name(self, value=None):
        """Corresponds to IDD field `Schedule Name`"""
        self["Schedule Name"] = value

    @property
    def design_level_calculation_method(self):
        """field `Design Level Calculation Method`

        |  The entered calculation method is used to create the maximum amount of other equipment.
        |  to set a loss, use a negative value in the following fields.
        |  for this set of attributes
        |  Choices: EquipmentLevel => Design Level -- simply enter power input of equipment
        |  Watts/Area or Power/Area => Power per Zone Floor Area -- enter the number to apply.  Value * Floor Area = Equipment Level
        |  Watts/Person or Power/Person => Power per Person -- enter the number to apply.  Value * Occupants = Equipment Level
        |  Default value: EquipmentLevel

        Args:
            value (str): value for IDD Field `Design Level Calculation Method`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `design_level_calculation_method` or None if not set

        """
        return self["Design Level Calculation Method"]

    @design_level_calculation_method.setter
    def design_level_calculation_method(self, value="EquipmentLevel"):
        """Corresponds to IDD field `Design Level Calculation Method`"""
        self["Design Level Calculation Method"] = value

    @property
    def design_level(self):
        """field `Design Level`

        |  Units: W
        |  IP-Units: Btu/h

        Args:
            value (float): value for IDD Field `Design Level`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `design_level` or None if not set

        """
        return self["Design Level"]

    @design_level.setter
    def design_level(self, value=None):
        """Corresponds to IDD field `Design Level`"""
        self["Design Level"] = value

    @property
    def power_per_zone_floor_area(self):
        """field `Power per Zone Floor Area`

        |  Units: W/m2
        |  IP-Units: Btu/h-ft2

        Args:
            value (float): value for IDD Field `Power per Zone Floor Area`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `power_per_zone_floor_area` or None if not set

        """
        return self["Power per Zone Floor Area"]

    @power_per_zone_floor_area.setter
    def power_per_zone_floor_area(self, value=None):
        """Corresponds to IDD field `Power per Zone Floor Area`"""
        self["Power per Zone Floor Area"] = value

    @property
    def power_per_person(self):
        """field `Power per Person`

        |  Units: W/Person
        |  IP-Units: Btu/h-person

        Args:
            value (float): value for IDD Field `Power per Person`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `power_per_person` or None if not set

        """
        return self["Power per Person"]

    @power_per_person.setter
    def power_per_person(self, value=None):
        """Corresponds to IDD field `Power per Person`"""
        self["Power per Person"] = value

    @property
    def fraction_latent(self):
        """field `Fraction Latent`

        |  value <= 1.0

        Args:
            value (float): value for IDD Field `Fraction Latent`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `fraction_latent` or None if not set

        """
        return self["Fraction Latent"]

    @fraction_latent.setter
    def fraction_latent(self, value=None):
        """Corresponds to IDD field `Fraction Latent`"""
        self["Fraction Latent"] = value

    @property
    def fraction_radiant(self):
        """field `Fraction Radiant`

        |  value <= 1.0

        Args:
            value (float): value for IDD Field `Fraction Radiant`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `fraction_radiant` or None if not set

        """
        return self["Fraction Radiant"]

    @fraction_radiant.setter
    def fraction_radiant(self, value=None):
        """Corresponds to IDD field `Fraction Radiant`"""
        self["Fraction Radiant"] = value

    @property
    def fraction_lost(self):
        """field `Fraction Lost`

        |  value <= 1.0

        Args:
            value (float): value for IDD Field `Fraction Lost`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `fraction_lost` or None if not set

        """
        return self["Fraction Lost"]

    @fraction_lost.setter
    def fraction_lost(self, value=None):
        """Corresponds to IDD field `Fraction Lost`"""
        self["Fraction Lost"] = value




class ElectricEquipmentIteAirCooled(DataObject):

    """ Corresponds to IDD object `ElectricEquipment:ITE:AirCooled`
        This object describes air-cooled electric information technology equipment (ITE) which has
        variable power consumption as a function of loading and temperature.
    """
    _schema = {'extensible-fields': OrderedDict(),
               'fields': OrderedDict([(u'name',
                                       {'name': u'Name',
                                        'pyname': u'name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'alpha'}),
                                      (u'zone name',
                                       {'name': u'Zone Name',
                                        'pyname': u'zone_name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'design power input calculation method',
                                       {'name': u'Design Power Input Calculation Method',
                                        'pyname': u'design_power_input_calculation_method',
                                        'default': u'Watts/Unit',
                                        'required-field': True,
                                        'autosizable': False,
                                        'accepted-values': [u'Watts/Unit',
                                                            u'Watts/Area'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'watts per unit',
                                       {'name': u'Watts per Unit',
                                        'pyname': u'watts_per_unit',
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'W'}),
                                      (u'number of units',
                                       {'name': u'Number of Units',
                                        'pyname': u'number_of_units',
                                        'default': 1.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'watts per zone floor area',
                                       {'name': u'Watts per Zone Floor Area',
                                        'pyname': u'watts_per_zone_floor_area',
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'W/m2'}),
                                      (u'design power input schedule name',
                                       {'name': u'Design Power Input Schedule Name',
                                        'pyname': u'design_power_input_schedule_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'cpu loading  schedule name',
                                       {'name': u'CPU Loading  Schedule Name',
                                        'pyname': u'cpu_loading_schedule_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'cpu power input function of loading and air temperature curve name',
                                       {'name': u'CPU Power Input Function of Loading and Air Temperature Curve Name',
                                        'pyname': u'cpu_power_input_function_of_loading_and_air_temperature_curve_name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'design fan power input fraction',
                                       {'name': u'Design Fan Power Input Fraction',
                                        'pyname': u'design_fan_power_input_fraction',
                                        'default': 0.0,
                                        'maximum': 1.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'design fan air flow rate per power input',
                                       {'name': u'Design Fan Air Flow Rate per Power Input',
                                        'pyname': u'design_fan_air_flow_rate_per_power_input',
                                        'required-field': True,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'm3/s-W'}),
                                      (u'air flow function of loading and air temperature curve name',
                                       {'name': u'Air Flow Function of Loading and Air Temperature Curve Name',
                                        'pyname': u'air_flow_function_of_loading_and_air_temperature_curve_name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'fan power input function of flow curve name',
                                       {'name': u'Fan Power Input Function of Flow Curve Name',
                                        'pyname': u'fan_power_input_function_of_flow_curve_name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'design entering air temperature',
                                       {'name': u'Design Entering Air Temperature',
                                        'pyname': u'design_entering_air_temperature',
                                        'default': 15.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'C'}),
                                      (u'environmental class',
                                       {'name': u'Environmental Class',
                                        'pyname': u'environmental_class',
                                        'default': u'None',
                                        'required-field': False,
                                        'autosizable': False,
                                        'accepted-values': [u'None',
                                                            u'A1',
                                                            u'A2',
                                                            u'A3',
                                                            u'A4',
                                                            u'B',
                                                            u'C'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'air inlet connection type',
                                       {'name': u'Air Inlet Connection Type',
                                        'pyname': u'air_inlet_connection_type',
                                        'default': u'AdjustedSupply',
                                        'required-field': False,
                                        'autosizable': False,
                                        'accepted-values': [u'AdjustedSupply',
                                                            u'ZoneAirNode',
                                                            u'RoomAirModel'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'air inlet room air model node name',
                                       {'name': u'Air Inlet Room Air Model Node Name',
                                        'pyname': u'air_inlet_room_air_model_node_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'air outlet room air model node name',
                                       {'name': u'Air Outlet Room Air Model Node Name',
                                        'pyname': u'air_outlet_room_air_model_node_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'supply air node name',
                                       {'name': u'Supply Air Node Name',
                                        'pyname': u'supply_air_node_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'node'}),
                                      (u'design recirculation fraction',
                                       {'name': u'Design Recirculation Fraction',
                                        'pyname': u'design_recirculation_fraction',
                                        'default': 0.0,
                                        'maximum': 0.5,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'recirculation function of loading and supply temperature curve name',
                                       {'name': u'Recirculation Function of Loading and Supply Temperature Curve Name',
                                        'pyname': u'recirculation_function_of_loading_and_supply_temperature_curve_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'design electric power supply efficiency',
                                       {'name': u'Design Electric Power Supply Efficiency',
                                        'pyname': u'design_electric_power_supply_efficiency',
                                        'default': 1.0,
                                        'minimum>': 0.0,
                                        'maximum': 1.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'electric power supply efficiency function of part load ratio curve name',
                                       {'name': u'Electric Power Supply Efficiency Function of Part Load Ratio Curve Name',
                                        'pyname': u'electric_power_supply_efficiency_function_of_part_load_ratio_curve_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'fraction of electric power supply losses to zone',
                                       {'name': u'Fraction of Electric Power Supply Losses to Zone',
                                        'pyname': u'fraction_of_electric_power_supply_losses_to_zone',
                                        'default': 1.0,
                                        'maximum': 1.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'cpu end-use subcategory',
                                       {'name': u'CPU End-Use Subcategory',
                                        'pyname': u'cpu_enduse_subcategory',
                                        'default': u'ITE-CPU',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'alpha'}),
                                      (u'fan end-use subcategory',
                                       {'name': u'Fan End-Use Subcategory',
                                        'pyname': u'fan_enduse_subcategory',
                                        'default': u'ITE-Fans',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'alpha'}),
                                      (u'electric power supply end-use subcategory',
                                       {'name': u'Electric Power Supply End-Use Subcategory',
                                        'pyname': u'electric_power_supply_enduse_subcategory',
                                        'default': u'ITE-UPS',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'alpha'})]),
               'format': None,
               'group': u'Internal Gains',
               'min-fields': 27,
               'name': u'ElectricEquipment:ITE:AirCooled',
               'pyname': u'ElectricEquipmentIteAirCooled',
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
    def zone_name(self):
        """field `Zone Name`

        Args:
            value (str): value for IDD Field `Zone Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `zone_name` or None if not set

        """
        return self["Zone Name"]

    @zone_name.setter
    def zone_name(self, value=None):
        """Corresponds to IDD field `Zone Name`"""
        self["Zone Name"] = value

    @property
    def design_power_input_calculation_method(self):
        """field `Design Power Input Calculation Method`

        |  The entered calculation method is used to specify the design power input
        |  Watts/Unit => Watts per Unit -- Design Power = Watts per Unit * Number of Units
        |  Watts/Area => Watts per Zone Floor Area -- Design Power = Watts per Zone Floor Area * Floor Area
        |  Default value: Watts/Unit

        Args:
            value (str): value for IDD Field `Design Power Input Calculation Method`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `design_power_input_calculation_method` or None if not set

        """
        return self["Design Power Input Calculation Method"]

    @design_power_input_calculation_method.setter
    def design_power_input_calculation_method(self, value="Watts/Unit"):
        """Corresponds to IDD field `Design Power Input Calculation Method`"""
        self["Design Power Input Calculation Method"] = value

    @property
    def watts_per_unit(self):
        """field `Watts per Unit`

        |  Units: W
        |  IP-Units: W

        Args:
            value (float): value for IDD Field `Watts per Unit`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `watts_per_unit` or None if not set

        """
        return self["Watts per Unit"]

    @watts_per_unit.setter
    def watts_per_unit(self, value=None):
        """Corresponds to IDD field `Watts per Unit`"""
        self["Watts per Unit"] = value

    @property
    def number_of_units(self):
        """field `Number of Units`

        |  Default value: 1.0

        Args:
            value (float): value for IDD Field `Number of Units`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `number_of_units` or None if not set

        """
        return self["Number of Units"]

    @number_of_units.setter
    def number_of_units(self, value=1.0):
        """Corresponds to IDD field `Number of Units`"""
        self["Number of Units"] = value

    @property
    def watts_per_zone_floor_area(self):
        """field `Watts per Zone Floor Area`

        |  Units: W/m2
        |  IP-Units: W/ft2

        Args:
            value (float): value for IDD Field `Watts per Zone Floor Area`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `watts_per_zone_floor_area` or None if not set

        """
        return self["Watts per Zone Floor Area"]

    @watts_per_zone_floor_area.setter
    def watts_per_zone_floor_area(self, value=None):
        """Corresponds to IDD field `Watts per Zone Floor Area`"""
        self["Watts per Zone Floor Area"] = value

    @property
    def design_power_input_schedule_name(self):
        """field `Design Power Input Schedule Name`

        |  Operating schedule for this equipment, fraction applied to the design power input,
        |  generally (0.0 - 1.0)
        |  If this field is blank, the schedule is assumed to always be 1.0.

        Args:
            value (str): value for IDD Field `Design Power Input Schedule Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `design_power_input_schedule_name` or None if not set

        """
        return self["Design Power Input Schedule Name"]

    @design_power_input_schedule_name.setter
    def design_power_input_schedule_name(self, value=None):
        """Corresponds to IDD field `Design Power Input Schedule Name`"""
        self["Design Power Input Schedule Name"] = value

    @property
    def cpu_loading_schedule_name(self):
        """field `CPU Loading  Schedule Name`

        |  CPU loading schedule for this equipment as a fraction from 0.0 (idle) to 1.0 (full load).
        |  If this field is blank, the schedule is assumed to always be 1.0.

        Args:
            value (str): value for IDD Field `CPU Loading  Schedule Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `cpu_loading_schedule_name` or None if not set

        """
        return self["CPU Loading  Schedule Name"]

    @cpu_loading_schedule_name.setter
    def cpu_loading_schedule_name(self, value=None):
        """Corresponds to IDD field `CPU Loading  Schedule Name`"""
        self["CPU Loading  Schedule Name"] = value

    @property
    def cpu_power_input_function_of_loading_and_air_temperature_curve_name(
            self):
        """field `CPU Power Input Function of Loading and Air Temperature Curve
        Name`

        |  The name of a two-variable curve or table lookup object which modifies the CPU power
        |  input as a function of CPU loading (x) and air inlet node temperature (y).
        |  This curve (table) should equal 1.0 at design conditions (CPU loading = 1.0 and
        |  Design Entering Air Temperature).

        Args:
            value (str): value for IDD Field `CPU Power Input Function of Loading and Air Temperature Curve Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `cpu_power_input_function_of_loading_and_air_temperature_curve_name` or None if not set

        """
        return self[
            "CPU Power Input Function of Loading and Air Temperature Curve Name"]

    @cpu_power_input_function_of_loading_and_air_temperature_curve_name.setter
    def cpu_power_input_function_of_loading_and_air_temperature_curve_name(
            self,
            value=None):
        """Corresponds to IDD field `CPU Power Input Function of Loading and
        Air Temperature Curve Name`"""
        self[
            "CPU Power Input Function of Loading and Air Temperature Curve Name"] = value

    @property
    def design_fan_power_input_fraction(self):
        """field `Design Fan Power Input Fraction`

        |  The fraction of the total power input at design conditions which is for the cooling fan(s)
        |  value <= 1.0

        Args:
            value (float): value for IDD Field `Design Fan Power Input Fraction`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `design_fan_power_input_fraction` or None if not set

        """
        return self["Design Fan Power Input Fraction"]

    @design_fan_power_input_fraction.setter
    def design_fan_power_input_fraction(self, value=None):
        """Corresponds to IDD field `Design Fan Power Input Fraction`"""
        self["Design Fan Power Input Fraction"] = value

    @property
    def design_fan_air_flow_rate_per_power_input(self):
        """field `Design Fan Air Flow Rate per Power Input`

        |  The cooling fan air flow rate per total electric power input at design conditions
        |  Units: m3/s-W

        Args:
            value (float): value for IDD Field `Design Fan Air Flow Rate per Power Input`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `design_fan_air_flow_rate_per_power_input` or None if not set

        """
        return self["Design Fan Air Flow Rate per Power Input"]

    @design_fan_air_flow_rate_per_power_input.setter
    def design_fan_air_flow_rate_per_power_input(self, value=None):
        """Corresponds to IDD field `Design Fan Air Flow Rate per Power
        Input`"""
        self["Design Fan Air Flow Rate per Power Input"] = value

    @property
    def air_flow_function_of_loading_and_air_temperature_curve_name(self):
        """field `Air Flow Function of Loading and Air Temperature Curve Name`

        |  The name of a two-variable curve or table lookup object which modifies the cooling
        |  air flow rate as a function of CPU loading (x) and air inlet node temperature (y).
        |  This curve (table) should equal 1.0 at design conditions (CPU loading = 1.0 and
        |  Design Entering Air Temperature).

        Args:
            value (str): value for IDD Field `Air Flow Function of Loading and Air Temperature Curve Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `air_flow_function_of_loading_and_air_temperature_curve_name` or None if not set

        """
        return self[
            "Air Flow Function of Loading and Air Temperature Curve Name"]

    @air_flow_function_of_loading_and_air_temperature_curve_name.setter
    def air_flow_function_of_loading_and_air_temperature_curve_name(
            self,
            value=None):
        """Corresponds to IDD field `Air Flow Function of Loading and Air
        Temperature Curve Name`"""
        self[
            "Air Flow Function of Loading and Air Temperature Curve Name"] = value

    @property
    def fan_power_input_function_of_flow_curve_name(self):
        """field `Fan Power Input Function of Flow Curve Name`

        |  The name of a single-variable curve or table lookup object which modifies the cooling
        |  fan power as a function of flow fraction (x).
        |  This curve (table) should equal 1.0 at a flow fraction of 1.0.

        Args:
            value (str): value for IDD Field `Fan Power Input Function of Flow Curve Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `fan_power_input_function_of_flow_curve_name` or None if not set

        """
        return self["Fan Power Input Function of Flow Curve Name"]

    @fan_power_input_function_of_flow_curve_name.setter
    def fan_power_input_function_of_flow_curve_name(self, value=None):
        """Corresponds to IDD field `Fan Power Input Function of Flow Curve
        Name`"""
        self["Fan Power Input Function of Flow Curve Name"] = value

    @property
    def design_entering_air_temperature(self):
        """field `Design Entering Air Temperature`

        |  The entering air temperature at design conditions.
        |  Units: C
        |  Default value: 15.0

        Args:
            value (float): value for IDD Field `Design Entering Air Temperature`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `design_entering_air_temperature` or None if not set

        """
        return self["Design Entering Air Temperature"]

    @design_entering_air_temperature.setter
    def design_entering_air_temperature(self, value=15.0):
        """Corresponds to IDD field `Design Entering Air Temperature`"""
        self["Design Entering Air Temperature"] = value

    @property
    def environmental_class(self):
        """field `Environmental Class`

        |  Specifies the allowable operating conditions for the air inlet conditions.
        |  Used for reporting time outside allowable conditions.
        |  Default value: None

        Args:
            value (str): value for IDD Field `Environmental Class`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `environmental_class` or None if not set

        """
        return self["Environmental Class"]

    @environmental_class.setter
    def environmental_class(self, value="None"):
        """Corresponds to IDD field `Environmental Class`"""
        self["Environmental Class"] = value

    @property
    def air_inlet_connection_type(self):
        """field `Air Inlet Connection Type`

        |  Specifies the type of connection between the zone and the ITE air inlet node.
        |  AdjustedSupply = ITE inlet temperature will be the current Supply Air Node temperature
        |  adjusted by the current recirculation fraction.
        |  All heat output is added to the zone air heat balance as a convective gain.
        |  ZoneAirNode = ITE air inlet condition is  the average zone condition.
        |  All heat output is added to the zone air heat balance as a convective gain.
        |  RoomAirModel = ITE air inlet and outlet are connected to room air model nodes.
        |  Default value: AdjustedSupply

        Args:
            value (str): value for IDD Field `Air Inlet Connection Type`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `air_inlet_connection_type` or None if not set

        """
        return self["Air Inlet Connection Type"]

    @air_inlet_connection_type.setter
    def air_inlet_connection_type(self, value="AdjustedSupply"):
        """Corresponds to IDD field `Air Inlet Connection Type`"""
        self["Air Inlet Connection Type"] = value

    @property
    def air_inlet_room_air_model_node_name(self):
        """field `Air Inlet Room Air Model Node Name`

        |  Name of a RoomAir:Node object which is connected to the ITE air inlet.

        Args:
            value (str): value for IDD Field `Air Inlet Room Air Model Node Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `air_inlet_room_air_model_node_name` or None if not set

        """
        return self["Air Inlet Room Air Model Node Name"]

    @air_inlet_room_air_model_node_name.setter
    def air_inlet_room_air_model_node_name(self, value=None):
        """Corresponds to IDD field `Air Inlet Room Air Model Node Name`"""
        self["Air Inlet Room Air Model Node Name"] = value

    @property
    def air_outlet_room_air_model_node_name(self):
        """field `Air Outlet Room Air Model Node Name`

        |  Name of a RoomAir:Node object which is connected to the ITE air outlet.

        Args:
            value (str): value for IDD Field `Air Outlet Room Air Model Node Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `air_outlet_room_air_model_node_name` or None if not set

        """
        return self["Air Outlet Room Air Model Node Name"]

    @air_outlet_room_air_model_node_name.setter
    def air_outlet_room_air_model_node_name(self, value=None):
        """Corresponds to IDD field `Air Outlet Room Air Model Node Name`"""
        self["Air Outlet Room Air Model Node Name"] = value

    @property
    def supply_air_node_name(self):
        """field `Supply Air Node Name`

        |  Name of the supply air inlet node serving this ITE. Required if the
        |  Air Node Connection Type = AdjustedSupply. Also required if reporting of
        |  Supply Heat Index is desired.

        Args:
            value (str): value for IDD Field `Supply Air Node Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `supply_air_node_name` or None if not set

        """
        return self["Supply Air Node Name"]

    @supply_air_node_name.setter
    def supply_air_node_name(self, value=None):
        """Corresponds to IDD field `Supply Air Node Name`"""
        self["Supply Air Node Name"] = value

    @property
    def design_recirculation_fraction(self):
        """field `Design Recirculation Fraction`

        |  The recirculation fraction for this equipment at design conditions. This field is used only
        |  if the Air Node Connection Type = AdjustedSupply. The default is 0.0 (no recirculation).
        |  value <= 0.5

        Args:
            value (float): value for IDD Field `Design Recirculation Fraction`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `design_recirculation_fraction` or None if not set

        """
        return self["Design Recirculation Fraction"]

    @design_recirculation_fraction.setter
    def design_recirculation_fraction(self, value=None):
        """Corresponds to IDD field `Design Recirculation Fraction`"""
        self["Design Recirculation Fraction"] = value

    @property
    def recirculation_function_of_loading_and_supply_temperature_curve_name(
            self):
        """field `Recirculation Function of Loading and Supply Temperature
        Curve Name`

        |  The name of a two-variable curve or table lookup object which modifies the recirculation
        |  fractionas a function of CPU loading (x) and supply air node temperature (y).
        |  This curve (table) should equal 1.0 at design conditions (CPU loading = 1.0 and
        |  Design Entering Air Temperature).This field is used only if the
        |  Air Node Connection Type = AdjustedSupply. If this curve is left blank, then the curve
        |  is assumed to always equal 1.0.

        Args:
            value (str): value for IDD Field `Recirculation Function of Loading and Supply Temperature Curve Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `recirculation_function_of_loading_and_supply_temperature_curve_name` or None if not set

        """
        return self[
            "Recirculation Function of Loading and Supply Temperature Curve Name"]

    @recirculation_function_of_loading_and_supply_temperature_curve_name.setter
    def recirculation_function_of_loading_and_supply_temperature_curve_name(
            self,
            value=None):
        """Corresponds to IDD field `Recirculation Function of Loading and
        Supply Temperature Curve Name`"""
        self[
            "Recirculation Function of Loading and Supply Temperature Curve Name"] = value

    @property
    def design_electric_power_supply_efficiency(self):
        """field `Design Electric Power Supply Efficiency`

        |  The efficiency of the power supply system serving this ITE
        |  Default value: 1.0
        |  value <= 1.0

        Args:
            value (float): value for IDD Field `Design Electric Power Supply Efficiency`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `design_electric_power_supply_efficiency` or None if not set

        """
        return self["Design Electric Power Supply Efficiency"]

    @design_electric_power_supply_efficiency.setter
    def design_electric_power_supply_efficiency(self, value=1.0):
        """Corresponds to IDD field `Design Electric Power Supply
        Efficiency`"""
        self["Design Electric Power Supply Efficiency"] = value

    @property
    def electric_power_supply_efficiency_function_of_part_load_ratio_curve_name(
            self):
        """field `Electric Power Supply Efficiency Function of Part Load Ratio
        Curve Name`

        |  The name of a single-variable curve or table lookup object which modifies the electric
        |  power supply efficiency as a function of part-load ratio (x).
        |  This curve (table) should equal 1.0 at full load (PLR = 1.0).
        |  If this curve is left blank, then the curve is assumed to always equal 1.0.

        Args:
            value (str): value for IDD Field `Electric Power Supply Efficiency Function of Part Load Ratio Curve Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `electric_power_supply_efficiency_function_of_part_load_ratio_curve_name` or None if not set

        """
        return self[
            "Electric Power Supply Efficiency Function of Part Load Ratio Curve Name"]

    @electric_power_supply_efficiency_function_of_part_load_ratio_curve_name.setter
    def electric_power_supply_efficiency_function_of_part_load_ratio_curve_name(
            self,
            value=None):
        """Corresponds to IDD field `Electric Power Supply Efficiency Function
        of Part Load Ratio Curve Name`"""
        self[
            "Electric Power Supply Efficiency Function of Part Load Ratio Curve Name"] = value

    @property
    def fraction_of_electric_power_supply_losses_to_zone(self):
        """field `Fraction of Electric Power Supply Losses to Zone`

        |  Fraction of the electric power supply losses which are a heat gain to the zone
        |  If this field is <1.0, the remainder of the losses are assumed to be lost to the outdoors.
        |  Default value: 1.0
        |  value <= 1.0

        Args:
            value (float): value for IDD Field `Fraction of Electric Power Supply Losses to Zone`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `fraction_of_electric_power_supply_losses_to_zone` or None if not set

        """
        return self["Fraction of Electric Power Supply Losses to Zone"]

    @fraction_of_electric_power_supply_losses_to_zone.setter
    def fraction_of_electric_power_supply_losses_to_zone(self, value=1.0):
        """Corresponds to IDD field `Fraction of Electric Power Supply Losses
        to Zone`"""
        self["Fraction of Electric Power Supply Losses to Zone"] = value

    @property
    def cpu_enduse_subcategory(self):
        """field `CPU End-Use Subcategory`

        |  Default value: ITE-CPU

        Args:
            value (str): value for IDD Field `CPU End-Use Subcategory`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `cpu_enduse_subcategory` or None if not set
        """
        return self["CPU End-Use Subcategory"]

    @cpu_enduse_subcategory.setter
    def cpu_enduse_subcategory(self, value="ITE-CPU"):
        """  Corresponds to IDD field `CPU End-Use Subcategory`

        """
        self["CPU End-Use Subcategory"] = value

    @property
    def fan_enduse_subcategory(self):
        """field `Fan End-Use Subcategory`

        |  Default value: ITE-Fans

        Args:
            value (str): value for IDD Field `Fan End-Use Subcategory`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `fan_enduse_subcategory` or None if not set
        """
        return self["Fan End-Use Subcategory"]

    @fan_enduse_subcategory.setter
    def fan_enduse_subcategory(self, value="ITE-Fans"):
        """  Corresponds to IDD field `Fan End-Use Subcategory`

        """
        self["Fan End-Use Subcategory"] = value

    @property
    def electric_power_supply_enduse_subcategory(self):
        """field `Electric Power Supply End-Use Subcategory`

        |  Default value: ITE-UPS

        Args:
            value (str): value for IDD Field `Electric Power Supply End-Use Subcategory`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `electric_power_supply_enduse_subcategory` or None if not set
        """
        return self["Electric Power Supply End-Use Subcategory"]

    @electric_power_supply_enduse_subcategory.setter
    def electric_power_supply_enduse_subcategory(self, value="ITE-UPS"):
        """  Corresponds to IDD field `Electric Power Supply End-Use Subcategory`

        """
        self["Electric Power Supply End-Use Subcategory"] = value




class ZoneBaseboardOutdoorTemperatureControlled(DataObject):

    """ Corresponds to IDD object `ZoneBaseboard:OutdoorTemperatureControlled`
        Specifies outside temperature-controlled electric baseboard heating.
    """
    _schema = {'extensible-fields': OrderedDict(),
               'fields': OrderedDict([(u'name',
                                       {'name': u'Name',
                                        'pyname': u'name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'alpha'}),
                                      (u'zone name',
                                       {'name': u'Zone Name',
                                        'pyname': u'zone_name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'schedule name',
                                       {'name': u'Schedule Name',
                                        'pyname': u'schedule_name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'capacity at low temperature',
                                       {'name': u'Capacity at Low Temperature',
                                        'pyname': u'capacity_at_low_temperature',
                                        'minimum>': 0.0,
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'W'}),
                                      (u'low temperature',
                                       {'name': u'Low Temperature',
                                        'pyname': u'low_temperature',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'C'}),
                                      (u'capacity at high temperature',
                                       {'name': u'Capacity at High Temperature',
                                        'pyname': u'capacity_at_high_temperature',
                                        'required-field': True,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'W'}),
                                      (u'high temperature',
                                       {'name': u'High Temperature',
                                        'pyname': u'high_temperature',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'C'}),
                                      (u'fraction radiant',
                                       {'name': u'Fraction Radiant',
                                        'pyname': u'fraction_radiant',
                                        'default': 0.0,
                                        'maximum': 1.0,
                                        'required-field': True,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'end-use subcategory',
                                       {'name': u'End-Use Subcategory',
                                        'pyname': u'enduse_subcategory',
                                        'default': u'General',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'alpha'})]),
               'format': None,
               'group': u'Internal Gains',
               'min-fields': 0,
               'name': u'ZoneBaseboard:OutdoorTemperatureControlled',
               'pyname': u'ZoneBaseboardOutdoorTemperatureControlled',
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
    def zone_name(self):
        """field `Zone Name`

        Args:
            value (str): value for IDD Field `Zone Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `zone_name` or None if not set

        """
        return self["Zone Name"]

    @zone_name.setter
    def zone_name(self, value=None):
        """Corresponds to IDD field `Zone Name`"""
        self["Zone Name"] = value

    @property
    def schedule_name(self):
        """field `Schedule Name`

        |  units in Schedule should be fraction applied to capacity of the baseboard heat equipment, generally (0.0 - 1.0)

        Args:
            value (str): value for IDD Field `Schedule Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `schedule_name` or None if not set

        """
        return self["Schedule Name"]

    @schedule_name.setter
    def schedule_name(self, value=None):
        """Corresponds to IDD field `Schedule Name`"""
        self["Schedule Name"] = value

    @property
    def capacity_at_low_temperature(self):
        """field `Capacity at Low Temperature`

        |  Units: W

        Args:
            value (float): value for IDD Field `Capacity at Low Temperature`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `capacity_at_low_temperature` or None if not set

        """
        return self["Capacity at Low Temperature"]

    @capacity_at_low_temperature.setter
    def capacity_at_low_temperature(self, value=None):
        """Corresponds to IDD field `Capacity at Low Temperature`"""
        self["Capacity at Low Temperature"] = value

    @property
    def low_temperature(self):
        """field `Low Temperature`

        |  Units: C

        Args:
            value (float): value for IDD Field `Low Temperature`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `low_temperature` or None if not set

        """
        return self["Low Temperature"]

    @low_temperature.setter
    def low_temperature(self, value=None):
        """Corresponds to IDD field `Low Temperature`"""
        self["Low Temperature"] = value

    @property
    def capacity_at_high_temperature(self):
        """field `Capacity at High Temperature`

        |  Units: W

        Args:
            value (float): value for IDD Field `Capacity at High Temperature`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `capacity_at_high_temperature` or None if not set

        """
        return self["Capacity at High Temperature"]

    @capacity_at_high_temperature.setter
    def capacity_at_high_temperature(self, value=None):
        """Corresponds to IDD field `Capacity at High Temperature`"""
        self["Capacity at High Temperature"] = value

    @property
    def high_temperature(self):
        """field `High Temperature`

        |  Units: C

        Args:
            value (float): value for IDD Field `High Temperature`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `high_temperature` or None if not set

        """
        return self["High Temperature"]

    @high_temperature.setter
    def high_temperature(self, value=None):
        """Corresponds to IDD field `High Temperature`"""
        self["High Temperature"] = value

    @property
    def fraction_radiant(self):
        """field `Fraction Radiant`

        |  value <= 1.0

        Args:
            value (float): value for IDD Field `Fraction Radiant`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `fraction_radiant` or None if not set

        """
        return self["Fraction Radiant"]

    @fraction_radiant.setter
    def fraction_radiant(self, value=None):
        """Corresponds to IDD field `Fraction Radiant`"""
        self["Fraction Radiant"] = value

    @property
    def enduse_subcategory(self):
        """field `End-Use Subcategory`

        |  Default value: General

        Args:
            value (str): value for IDD Field `End-Use Subcategory`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `enduse_subcategory` or None if not set
        """
        return self["End-Use Subcategory"]

    @enduse_subcategory.setter
    def enduse_subcategory(self, value="General"):
        """  Corresponds to IDD field `End-Use Subcategory`

        """
        self["End-Use Subcategory"] = value




class SwimmingPoolIndoor(DataObject):

    """ Corresponds to IDD object `SwimmingPool:Indoor`
    """
    _schema = {'extensible-fields': OrderedDict(),
               'fields': OrderedDict([(u'name',
                                       {'name': u'Name',
                                        'pyname': u'name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'alpha'}),
                                      (u'surface name',
                                       {'name': u'Surface Name',
                                        'pyname': u'surface_name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'average depth',
                                       {'name': u'Average Depth',
                                        'pyname': u'average_depth',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'm'}),
                                      (u'activity factor schedule name',
                                       {'name': u'Activity Factor Schedule Name',
                                        'pyname': u'activity_factor_schedule_name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'make-up water supply schedule name',
                                       {'name': u'Make-up Water Supply Schedule Name',
                                        'pyname': u'makeup_water_supply_schedule_name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'cover schedule name',
                                       {'name': u'Cover Schedule Name',
                                        'pyname': u'cover_schedule_name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'cover evaporation factor',
                                       {'name': u'Cover Evaporation Factor',
                                        'pyname': u'cover_evaporation_factor',
                                        'default': 0.0,
                                        'maximum': 1.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'cover convection factor',
                                       {'name': u'Cover Convection Factor',
                                        'pyname': u'cover_convection_factor',
                                        'default': 0.0,
                                        'maximum': 1.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'cover short-wavelength radiation factor',
                                       {'name': u'Cover Short-Wavelength Radiation Factor',
                                        'pyname': u'cover_shortwavelength_radiation_factor',
                                        'default': 0.0,
                                        'maximum': 1.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'cover long-wavelength radiation factor',
                                       {'name': u'Cover Long-Wavelength Radiation Factor',
                                        'pyname': u'cover_longwavelength_radiation_factor',
                                        'default': 0.0,
                                        'maximum': 1.0,
                                        'required-field': True,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'pool water inlet node',
                                       {'name': u'Pool Water Inlet Node',
                                        'pyname': u'pool_water_inlet_node',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'node'}),
                                      (u'pool water outlet node',
                                       {'name': u'Pool Water Outlet Node',
                                        'pyname': u'pool_water_outlet_node',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'node'}),
                                      (u'pool heating system maximum water flow rate',
                                       {'name': u'Pool Heating System Maximum Water Flow Rate',
                                        'pyname': u'pool_heating_system_maximum_water_flow_rate',
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'm3/s'}),
                                      (u'pool miscellaneous equipment power',
                                       {'name': u'Pool Miscellaneous Equipment Power',
                                        'pyname': u'pool_miscellaneous_equipment_power',
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'W/(m3/s)'}),
                                      (u'setpoint temperature schedule',
                                       {'name': u'Setpoint Temperature Schedule',
                                        'pyname': u'setpoint_temperature_schedule',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'maximum number of people',
                                       {'name': u'Maximum Number of People',
                                        'pyname': u'maximum_number_of_people',
                                        'required-field': True,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': 'real'}),
                                      (u'people schedule',
                                       {'name': u'People Schedule',
                                        'pyname': u'people_schedule',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'people heat gain schedule',
                                       {'name': u'People Heat Gain Schedule',
                                        'pyname': u'people_heat_gain_schedule',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'})]),
               'format': None,
               'group': u'Internal Gains',
               'min-fields': 0,
               'name': u'SwimmingPool:Indoor',
               'pyname': u'SwimmingPoolIndoor',
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
    def surface_name(self):
        """field `Surface Name`

        |  To be matched with a construction in this input file

        Args:
            value (str): value for IDD Field `Surface Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `surface_name` or None if not set

        """
        return self["Surface Name"]

    @surface_name.setter
    def surface_name(self, value=None):
        """Corresponds to IDD field `Surface Name`"""
        self["Surface Name"] = value

    @property
    def average_depth(self):
        """field `Average Depth`

        |  Units: m

        Args:
            value (float): value for IDD Field `Average Depth`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `average_depth` or None if not set

        """
        return self["Average Depth"]

    @average_depth.setter
    def average_depth(self, value=None):
        """Corresponds to IDD field `Average Depth`"""
        self["Average Depth"] = value

    @property
    def activity_factor_schedule_name(self):
        """field `Activity Factor Schedule Name`

        Args:
            value (str): value for IDD Field `Activity Factor Schedule Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `activity_factor_schedule_name` or None if not set

        """
        return self["Activity Factor Schedule Name"]

    @activity_factor_schedule_name.setter
    def activity_factor_schedule_name(self, value=None):
        """Corresponds to IDD field `Activity Factor Schedule Name`"""
        self["Activity Factor Schedule Name"] = value

    @property
    def makeup_water_supply_schedule_name(self):
        """field `Make-up Water Supply Schedule Name`


        Args:
            value (str): value for IDD Field `Make-up Water Supply Schedule Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `makeup_water_supply_schedule_name` or None if not set
        """
        return self["Make-up Water Supply Schedule Name"]

    @makeup_water_supply_schedule_name.setter
    def makeup_water_supply_schedule_name(self, value=None):
        """  Corresponds to IDD field `Make-up Water Supply Schedule Name`

        """
        self["Make-up Water Supply Schedule Name"] = value

    @property
    def cover_schedule_name(self):
        """field `Cover Schedule Name`

        Args:
            value (str): value for IDD Field `Cover Schedule Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `cover_schedule_name` or None if not set

        """
        return self["Cover Schedule Name"]

    @cover_schedule_name.setter
    def cover_schedule_name(self, value=None):
        """Corresponds to IDD field `Cover Schedule Name`"""
        self["Cover Schedule Name"] = value

    @property
    def cover_evaporation_factor(self):
        """field `Cover Evaporation Factor`

        |  value <= 1.0

        Args:
            value (float): value for IDD Field `Cover Evaporation Factor`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `cover_evaporation_factor` or None if not set

        """
        return self["Cover Evaporation Factor"]

    @cover_evaporation_factor.setter
    def cover_evaporation_factor(self, value=None):
        """Corresponds to IDD field `Cover Evaporation Factor`"""
        self["Cover Evaporation Factor"] = value

    @property
    def cover_convection_factor(self):
        """field `Cover Convection Factor`

        |  value <= 1.0

        Args:
            value (float): value for IDD Field `Cover Convection Factor`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `cover_convection_factor` or None if not set

        """
        return self["Cover Convection Factor"]

    @cover_convection_factor.setter
    def cover_convection_factor(self, value=None):
        """Corresponds to IDD field `Cover Convection Factor`"""
        self["Cover Convection Factor"] = value

    @property
    def cover_shortwavelength_radiation_factor(self):
        """field `Cover Short-Wavelength Radiation Factor`

        |  value <= 1.0

        Args:
            value (float): value for IDD Field `Cover Short-Wavelength Radiation Factor`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `cover_shortwavelength_radiation_factor` or None if not set
        """
        return self["Cover Short-Wavelength Radiation Factor"]

    @cover_shortwavelength_radiation_factor.setter
    def cover_shortwavelength_radiation_factor(self, value=None):
        """  Corresponds to IDD field `Cover Short-Wavelength Radiation Factor`

        """
        self["Cover Short-Wavelength Radiation Factor"] = value

    @property
    def cover_longwavelength_radiation_factor(self):
        """field `Cover Long-Wavelength Radiation Factor`

        |  value <= 1.0

        Args:
            value (float): value for IDD Field `Cover Long-Wavelength Radiation Factor`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `cover_longwavelength_radiation_factor` or None if not set
        """
        return self["Cover Long-Wavelength Radiation Factor"]

    @cover_longwavelength_radiation_factor.setter
    def cover_longwavelength_radiation_factor(self, value=None):
        """  Corresponds to IDD field `Cover Long-Wavelength Radiation Factor`

        """
        self["Cover Long-Wavelength Radiation Factor"] = value

    @property
    def pool_water_inlet_node(self):
        """field `Pool Water Inlet Node`

        Args:
            value (str): value for IDD Field `Pool Water Inlet Node`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `pool_water_inlet_node` or None if not set

        """
        return self["Pool Water Inlet Node"]

    @pool_water_inlet_node.setter
    def pool_water_inlet_node(self, value=None):
        """Corresponds to IDD field `Pool Water Inlet Node`"""
        self["Pool Water Inlet Node"] = value

    @property
    def pool_water_outlet_node(self):
        """field `Pool Water Outlet Node`

        Args:
            value (str): value for IDD Field `Pool Water Outlet Node`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `pool_water_outlet_node` or None if not set

        """
        return self["Pool Water Outlet Node"]

    @pool_water_outlet_node.setter
    def pool_water_outlet_node(self, value=None):
        """Corresponds to IDD field `Pool Water Outlet Node`"""
        self["Pool Water Outlet Node"] = value

    @property
    def pool_heating_system_maximum_water_flow_rate(self):
        """field `Pool Heating System Maximum Water Flow Rate`

        |  Units: m3/s

        Args:
            value (float): value for IDD Field `Pool Heating System Maximum Water Flow Rate`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `pool_heating_system_maximum_water_flow_rate` or None if not set

        """
        return self["Pool Heating System Maximum Water Flow Rate"]

    @pool_heating_system_maximum_water_flow_rate.setter
    def pool_heating_system_maximum_water_flow_rate(self, value=None):
        """Corresponds to IDD field `Pool Heating System Maximum Water Flow
        Rate`"""
        self["Pool Heating System Maximum Water Flow Rate"] = value

    @property
    def pool_miscellaneous_equipment_power(self):
        """field `Pool Miscellaneous Equipment Power`

        |  Power input per pool water flow rate
        |  Units: W/(m3/s)

        Args:
            value (float): value for IDD Field `Pool Miscellaneous Equipment Power`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `pool_miscellaneous_equipment_power` or None if not set

        """
        return self["Pool Miscellaneous Equipment Power"]

    @pool_miscellaneous_equipment_power.setter
    def pool_miscellaneous_equipment_power(self, value=None):
        """Corresponds to IDD field `Pool Miscellaneous Equipment Power`"""
        self["Pool Miscellaneous Equipment Power"] = value

    @property
    def setpoint_temperature_schedule(self):
        """field `Setpoint Temperature Schedule`

        Args:
            value (str): value for IDD Field `Setpoint Temperature Schedule`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `setpoint_temperature_schedule` or None if not set

        """
        return self["Setpoint Temperature Schedule"]

    @setpoint_temperature_schedule.setter
    def setpoint_temperature_schedule(self, value=None):
        """Corresponds to IDD field `Setpoint Temperature Schedule`"""
        self["Setpoint Temperature Schedule"] = value

    @property
    def maximum_number_of_people(self):
        """field `Maximum Number of People`

        Args:
            value (float): value for IDD Field `Maximum Number of People`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `maximum_number_of_people` or None if not set

        """
        return self["Maximum Number of People"]

    @maximum_number_of_people.setter
    def maximum_number_of_people(self, value=None):
        """Corresponds to IDD field `Maximum Number of People`"""
        self["Maximum Number of People"] = value

    @property
    def people_schedule(self):
        """field `People Schedule`

        Args:
            value (str): value for IDD Field `People Schedule`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `people_schedule` or None if not set

        """
        return self["People Schedule"]

    @people_schedule.setter
    def people_schedule(self, value=None):
        """Corresponds to IDD field `People Schedule`"""
        self["People Schedule"] = value

    @property
    def people_heat_gain_schedule(self):
        """field `People Heat Gain Schedule`

        Args:
            value (str): value for IDD Field `People Heat Gain Schedule`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `people_heat_gain_schedule` or None if not set

        """
        return self["People Heat Gain Schedule"]

    @people_heat_gain_schedule.setter
    def people_heat_gain_schedule(self, value=None):
        """Corresponds to IDD field `People Heat Gain Schedule`"""
        self["People Heat Gain Schedule"] = value




class ZoneContaminantSourceAndSinkCarbonDioxide(DataObject):

    """ Corresponds to IDD object `ZoneContaminantSourceAndSink:CarbonDioxide`
        Represents internal CO2 gains and sinks in the zone.
    """
    _schema = {'extensible-fields': OrderedDict(),
               'fields': OrderedDict([(u'name',
                                       {'name': u'Name',
                                        'pyname': u'name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'alpha'}),
                                      (u'zone name',
                                       {'name': u'Zone Name',
                                        'pyname': u'zone_name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'design generation rate',
                                       {'name': u'Design Generation Rate',
                                        'pyname': u'design_generation_rate',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'm3/s'}),
                                      (u'schedule name',
                                       {'name': u'Schedule Name',
                                        'pyname': u'schedule_name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'})]),
               'format': None,
               'group': u'Internal Gains',
               'min-fields': 0,
               'name': u'ZoneContaminantSourceAndSink:CarbonDioxide',
               'pyname': u'ZoneContaminantSourceAndSinkCarbonDioxide',
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
    def zone_name(self):
        """field `Zone Name`

        Args:
            value (str): value for IDD Field `Zone Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `zone_name` or None if not set

        """
        return self["Zone Name"]

    @zone_name.setter
    def zone_name(self, value=None):
        """Corresponds to IDD field `Zone Name`"""
        self["Zone Name"] = value

    @property
    def design_generation_rate(self):
        """field `Design Generation Rate`

        |  Positive values represent sources and negative values represent sinks.
        |  Units: m3/s

        Args:
            value (float): value for IDD Field `Design Generation Rate`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `design_generation_rate` or None if not set

        """
        return self["Design Generation Rate"]

    @design_generation_rate.setter
    def design_generation_rate(self, value=None):
        """Corresponds to IDD field `Design Generation Rate`"""
        self["Design Generation Rate"] = value

    @property
    def schedule_name(self):
        """field `Schedule Name`

        |  Value in this schedule should be a fraction (generally 0.0 - 1.0) applied to the Design Generation Rate

        Args:
            value (str): value for IDD Field `Schedule Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `schedule_name` or None if not set

        """
        return self["Schedule Name"]

    @schedule_name.setter
    def schedule_name(self, value=None):
        """Corresponds to IDD field `Schedule Name`"""
        self["Schedule Name"] = value




class ZoneContaminantSourceAndSinkGenericConstant(DataObject):

    """ Corresponds to IDD object `ZoneContaminantSourceAndSink:Generic:Constant`
        Sets internal generic contaminant gains and sinks in a zone with constant values.
    """
    _schema = {'extensible-fields': OrderedDict(),
               'fields': OrderedDict([(u'name',
                                       {'name': u'Name',
                                        'pyname': u'name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'alpha'}),
                                      (u'zone name',
                                       {'name': u'Zone Name',
                                        'pyname': u'zone_name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'design generation rate',
                                       {'name': u'Design Generation Rate',
                                        'pyname': u'design_generation_rate',
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'm3/s'}),
                                      (u'generation schedule name',
                                       {'name': u'Generation Schedule Name',
                                        'pyname': u'generation_schedule_name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'design removal coefficient',
                                       {'name': u'Design Removal Coefficient',
                                        'pyname': u'design_removal_coefficient',
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'm3/s'}),
                                      (u'removal schedule name',
                                       {'name': u'Removal Schedule Name',
                                        'pyname': u'removal_schedule_name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'})]),
               'format': None,
               'group': u'Internal Gains',
               'min-fields': 0,
               'name': u'ZoneContaminantSourceAndSink:Generic:Constant',
               'pyname': u'ZoneContaminantSourceAndSinkGenericConstant',
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
    def zone_name(self):
        """field `Zone Name`

        Args:
            value (str): value for IDD Field `Zone Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `zone_name` or None if not set

        """
        return self["Zone Name"]

    @zone_name.setter
    def zone_name(self, value=None):
        """Corresponds to IDD field `Zone Name`"""
        self["Zone Name"] = value

    @property
    def design_generation_rate(self):
        """field `Design Generation Rate`

        |  The values represent source.
        |  Units: m3/s

        Args:
            value (float): value for IDD Field `Design Generation Rate`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `design_generation_rate` or None if not set

        """
        return self["Design Generation Rate"]

    @design_generation_rate.setter
    def design_generation_rate(self, value=None):
        """Corresponds to IDD field `Design Generation Rate`"""
        self["Design Generation Rate"] = value

    @property
    def generation_schedule_name(self):
        """field `Generation Schedule Name`

        |  Value in this schedule should be a fraction (generally 0.0 - 1.0) applied to the Design Generation Rate

        Args:
            value (str): value for IDD Field `Generation Schedule Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `generation_schedule_name` or None if not set

        """
        return self["Generation Schedule Name"]

    @generation_schedule_name.setter
    def generation_schedule_name(self, value=None):
        """Corresponds to IDD field `Generation Schedule Name`"""
        self["Generation Schedule Name"] = value

    @property
    def design_removal_coefficient(self):
        """field `Design Removal Coefficient`

        |  The value represent sink.
        |  Units: m3/s

        Args:
            value (float): value for IDD Field `Design Removal Coefficient`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `design_removal_coefficient` or None if not set

        """
        return self["Design Removal Coefficient"]

    @design_removal_coefficient.setter
    def design_removal_coefficient(self, value=None):
        """Corresponds to IDD field `Design Removal Coefficient`"""
        self["Design Removal Coefficient"] = value

    @property
    def removal_schedule_name(self):
        """field `Removal Schedule Name`

        |  Value in this schedule should be a fraction (generally 0.0 - 1.0) applied to the
        |  Design removal Coefficient

        Args:
            value (str): value for IDD Field `Removal Schedule Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `removal_schedule_name` or None if not set

        """
        return self["Removal Schedule Name"]

    @removal_schedule_name.setter
    def removal_schedule_name(self, value=None):
        """Corresponds to IDD field `Removal Schedule Name`"""
        self["Removal Schedule Name"] = value




class SurfaceContaminantSourceAndSinkGenericPressureDriven(DataObject):

    """ Corresponds to IDD object `SurfaceContaminantSourceAndSink:Generic:PressureDriven`
        Simulate generic contaminant source driven by the pressure difference across a surface.
    """
    _schema = {'extensible-fields': OrderedDict(),
               'fields': OrderedDict([(u'name',
                                       {'name': u'Name',
                                        'pyname': u'name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'alpha'}),
                                      (u'surface name',
                                       {'name': u'Surface Name',
                                        'pyname': u'surface_name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'design generation rate coefficient',
                                       {'name': u'Design Generation Rate Coefficient',
                                        'pyname': u'design_generation_rate_coefficient',
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'm3/s'}),
                                      (u'generation schedule name',
                                       {'name': u'Generation Schedule Name',
                                        'pyname': u'generation_schedule_name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'generation exponent',
                                       {'name': u'Generation Exponent',
                                        'pyname': u'generation_exponent',
                                        'minimum>': 0.0,
                                        'maximum': 1.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'dimensionless'})]),
               'format': None,
               'group': u'Internal Gains',
               'min-fields': 0,
               'name': u'SurfaceContaminantSourceAndSink:Generic:PressureDriven',
               'pyname': u'SurfaceContaminantSourceAndSinkGenericPressureDriven',
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
    def surface_name(self):
        """field `Surface Name`

        Args:
            value (str): value for IDD Field `Surface Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `surface_name` or None if not set

        """
        return self["Surface Name"]

    @surface_name.setter
    def surface_name(self, value=None):
        """Corresponds to IDD field `Surface Name`"""
        self["Surface Name"] = value

    @property
    def design_generation_rate_coefficient(self):
        """field `Design Generation Rate Coefficient`

        |  Units: m3/s

        Args:
            value (float): value for IDD Field `Design Generation Rate Coefficient`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `design_generation_rate_coefficient` or None if not set

        """
        return self["Design Generation Rate Coefficient"]

    @design_generation_rate_coefficient.setter
    def design_generation_rate_coefficient(self, value=None):
        """Corresponds to IDD field `Design Generation Rate Coefficient`"""
        self["Design Generation Rate Coefficient"] = value

    @property
    def generation_schedule_name(self):
        """field `Generation Schedule Name`

        |  Value in this schedule should be a fraction (generally 0.0 - 1.0) applied to the
        |  Design Generation Rate Coefficient

        Args:
            value (str): value for IDD Field `Generation Schedule Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `generation_schedule_name` or None if not set

        """
        return self["Generation Schedule Name"]

    @generation_schedule_name.setter
    def generation_schedule_name(self, value=None):
        """Corresponds to IDD field `Generation Schedule Name`"""
        self["Generation Schedule Name"] = value

    @property
    def generation_exponent(self):
        """field `Generation Exponent`

        |  Units: dimensionless
        |  value <= 1.0

        Args:
            value (float): value for IDD Field `Generation Exponent`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `generation_exponent` or None if not set

        """
        return self["Generation Exponent"]

    @generation_exponent.setter
    def generation_exponent(self, value=None):
        """Corresponds to IDD field `Generation Exponent`"""
        self["Generation Exponent"] = value




class ZoneContaminantSourceAndSinkGenericCutoffModel(DataObject):

    """ Corresponds to IDD object `ZoneContaminantSourceAndSink:Generic:CutoffModel`
        Simulate generic contaminant source driven by the cutoff concentration model.
    """
    _schema = {'extensible-fields': OrderedDict(),
               'fields': OrderedDict([(u'name',
                                       {'name': u'Name',
                                        'pyname': u'name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'alpha'}),
                                      (u'zone name',
                                       {'name': u'Zone Name',
                                        'pyname': u'zone_name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'design generation rate coefficient',
                                       {'name': u'Design Generation Rate Coefficient',
                                        'pyname': u'design_generation_rate_coefficient',
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'm3/s'}),
                                      (u'schedule name',
                                       {'name': u'Schedule Name',
                                        'pyname': u'schedule_name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'cutoff generic contaminant at which emission ceases',
                                       {'name': u'Cutoff Generic Contaminant at which Emission Ceases',
                                        'pyname': u'cutoff_generic_contaminant_at_which_emission_ceases',
                                        'minimum>': 0.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'ppm'})]),
               'format': None,
               'group': u'Internal Gains',
               'min-fields': 0,
               'name': u'ZoneContaminantSourceAndSink:Generic:CutoffModel',
               'pyname': u'ZoneContaminantSourceAndSinkGenericCutoffModel',
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
    def zone_name(self):
        """field `Zone Name`

        Args:
            value (str): value for IDD Field `Zone Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `zone_name` or None if not set

        """
        return self["Zone Name"]

    @zone_name.setter
    def zone_name(self, value=None):
        """Corresponds to IDD field `Zone Name`"""
        self["Zone Name"] = value

    @property
    def design_generation_rate_coefficient(self):
        """field `Design Generation Rate Coefficient`

        |  Units: m3/s

        Args:
            value (float): value for IDD Field `Design Generation Rate Coefficient`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `design_generation_rate_coefficient` or None if not set

        """
        return self["Design Generation Rate Coefficient"]

    @design_generation_rate_coefficient.setter
    def design_generation_rate_coefficient(self, value=None):
        """Corresponds to IDD field `Design Generation Rate Coefficient`"""
        self["Design Generation Rate Coefficient"] = value

    @property
    def schedule_name(self):
        """field `Schedule Name`

        |  Value in this schedule should be a fraction (generally 0.0 - 1.0) applied to the
        |  Design Generation Rate Coefficient

        Args:
            value (str): value for IDD Field `Schedule Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `schedule_name` or None if not set

        """
        return self["Schedule Name"]

    @schedule_name.setter
    def schedule_name(self, value=None):
        """Corresponds to IDD field `Schedule Name`"""
        self["Schedule Name"] = value

    @property
    def cutoff_generic_contaminant_at_which_emission_ceases(self):
        """field `Cutoff Generic Contaminant at which Emission Ceases`

        |  When the zone concentration level is greater than the cutoff level, emission stops,
        |  and the source level is zero.
        |  Units: ppm

        Args:
            value (float): value for IDD Field `Cutoff Generic Contaminant at which Emission Ceases`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `cutoff_generic_contaminant_at_which_emission_ceases` or None if not set

        """
        return self["Cutoff Generic Contaminant at which Emission Ceases"]

    @cutoff_generic_contaminant_at_which_emission_ceases.setter
    def cutoff_generic_contaminant_at_which_emission_ceases(self, value=None):
        """Corresponds to IDD field `Cutoff Generic Contaminant at which
        Emission Ceases`"""
        self["Cutoff Generic Contaminant at which Emission Ceases"] = value




class ZoneContaminantSourceAndSinkGenericDecaySource(DataObject):

    """ Corresponds to IDD object `ZoneContaminantSourceAndSink:Generic:DecaySource`
        Simulate generic contaminant source driven by the cutoff concentration model.
    """
    _schema = {'extensible-fields': OrderedDict(),
               'fields': OrderedDict([(u'name',
                                       {'name': u'Name',
                                        'pyname': u'name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'alpha'}),
                                      (u'zone name',
                                       {'name': u'Zone Name',
                                        'pyname': u'zone_name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'initial emission rate',
                                       {'name': u'Initial Emission Rate',
                                        'pyname': u'initial_emission_rate',
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'm3/s'}),
                                      (u'schedule name',
                                       {'name': u'Schedule Name',
                                        'pyname': u'schedule_name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'delay time constant',
                                       {'name': u'Delay Time Constant',
                                        'pyname': u'delay_time_constant',
                                        'minimum>': 0.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u's'})]),
               'format': None,
               'group': u'Internal Gains',
               'min-fields': 0,
               'name': u'ZoneContaminantSourceAndSink:Generic:DecaySource',
               'pyname': u'ZoneContaminantSourceAndSinkGenericDecaySource',
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
    def zone_name(self):
        """field `Zone Name`

        Args:
            value (str): value for IDD Field `Zone Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `zone_name` or None if not set

        """
        return self["Zone Name"]

    @zone_name.setter
    def zone_name(self, value=None):
        """Corresponds to IDD field `Zone Name`"""
        self["Zone Name"] = value

    @property
    def initial_emission_rate(self):
        """field `Initial Emission Rate`

        |  Units: m3/s

        Args:
            value (float): value for IDD Field `Initial Emission Rate`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `initial_emission_rate` or None if not set

        """
        return self["Initial Emission Rate"]

    @initial_emission_rate.setter
    def initial_emission_rate(self, value=None):
        """Corresponds to IDD field `Initial Emission Rate`"""
        self["Initial Emission Rate"] = value

    @property
    def schedule_name(self):
        """field `Schedule Name`

        |  Value in this schedule should be a fraction (generally 0.0 - 1.0) applied to the
        |  Initial Emission Rate. When the value is equal to 1.0, the time will be reset to
        |  zero.

        Args:
            value (str): value for IDD Field `Schedule Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `schedule_name` or None if not set

        """
        return self["Schedule Name"]

    @schedule_name.setter
    def schedule_name(self, value=None):
        """Corresponds to IDD field `Schedule Name`"""
        self["Schedule Name"] = value

    @property
    def delay_time_constant(self):
        """field `Delay Time Constant`

        |  Units: s

        Args:
            value (float): value for IDD Field `Delay Time Constant`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `delay_time_constant` or None if not set

        """
        return self["Delay Time Constant"]

    @delay_time_constant.setter
    def delay_time_constant(self, value=None):
        """Corresponds to IDD field `Delay Time Constant`"""
        self["Delay Time Constant"] = value




class SurfaceContaminantSourceAndSinkGenericBoundaryLayerDiffusion(DataObject):

    """ Corresponds to IDD object `SurfaceContaminantSourceAndSink:Generic:BoundaryLayerDiffusion`
        Simulate generic contaminant source driven by the boundary layer diffusion controlled model.
    """
    _schema = {'extensible-fields': OrderedDict(),
               'fields': OrderedDict([(u'name',
                                       {'name': u'Name',
                                        'pyname': u'name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'alpha'}),
                                      (u'surface name',
                                       {'name': u'Surface Name',
                                        'pyname': u'surface_name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'mass transfer coefficient',
                                       {'name': u'Mass Transfer Coefficient',
                                        'pyname': u'mass_transfer_coefficient',
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'm/s'}),
                                      (u'schedule name',
                                       {'name': u'Schedule Name',
                                        'pyname': u'schedule_name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'henry adsorption constant or partition coefficient',
                                       {'name': u'Henry adsorption constant or partition coefficient',
                                        'pyname': u'henry_adsorption_constant_or_partition_coefficient',
                                        'minimum>': 0.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'dimensionless'})]),
               'format': None,
               'group': u'Internal Gains',
               'min-fields': 0,
               'name': u'SurfaceContaminantSourceAndSink:Generic:BoundaryLayerDiffusion',
               'pyname': u'SurfaceContaminantSourceAndSinkGenericBoundaryLayerDiffusion',
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
    def surface_name(self):
        """field `Surface Name`

        Args:
            value (str): value for IDD Field `Surface Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `surface_name` or None if not set

        """
        return self["Surface Name"]

    @surface_name.setter
    def surface_name(self, value=None):
        """Corresponds to IDD field `Surface Name`"""
        self["Surface Name"] = value

    @property
    def mass_transfer_coefficient(self):
        """field `Mass Transfer Coefficient`

        |  Units: m/s

        Args:
            value (float): value for IDD Field `Mass Transfer Coefficient`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `mass_transfer_coefficient` or None if not set

        """
        return self["Mass Transfer Coefficient"]

    @mass_transfer_coefficient.setter
    def mass_transfer_coefficient(self, value=None):
        """Corresponds to IDD field `Mass Transfer Coefficient`"""
        self["Mass Transfer Coefficient"] = value

    @property
    def schedule_name(self):
        """field `Schedule Name`

        |  Value in this schedule should be a fraction (generally 0.0 - 1.0) applied to the
        |  Initial Emission Rate. When the value is equal to 1.0, the time will be reset to
        |  zero.

        Args:
            value (str): value for IDD Field `Schedule Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `schedule_name` or None if not set

        """
        return self["Schedule Name"]

    @schedule_name.setter
    def schedule_name(self, value=None):
        """Corresponds to IDD field `Schedule Name`"""
        self["Schedule Name"] = value

    @property
    def henry_adsorption_constant_or_partition_coefficient(self):
        """field `Henry adsorption constant or partition coefficient`

        |  Units: dimensionless

        Args:
            value (float): value for IDD Field `Henry adsorption constant or partition coefficient`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `henry_adsorption_constant_or_partition_coefficient` or None if not set

        """
        return self["Henry adsorption constant or partition coefficient"]

    @henry_adsorption_constant_or_partition_coefficient.setter
    def henry_adsorption_constant_or_partition_coefficient(self, value=None):
        """Corresponds to IDD field `Henry adsorption constant or partition
        coefficient`"""
        self["Henry adsorption constant or partition coefficient"] = value




class SurfaceContaminantSourceAndSinkGenericDepositionVelocitySink(DataObject):

    """ Corresponds to IDD object `SurfaceContaminantSourceAndSink:Generic:DepositionVelocitySink`
        Simulate generic contaminant source driven by the boundary layer diffusion controlled model.
    """
    _schema = {'extensible-fields': OrderedDict(),
               'fields': OrderedDict([(u'name',
                                       {'name': u'Name',
                                        'pyname': u'name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'alpha'}),
                                      (u'surface name',
                                       {'name': u'Surface Name',
                                        'pyname': u'surface_name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'deposition velocity',
                                       {'name': u'Deposition Velocity',
                                        'pyname': u'deposition_velocity',
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'm/s'}),
                                      (u'schedule name',
                                       {'name': u'Schedule Name',
                                        'pyname': u'schedule_name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'})]),
               'format': None,
               'group': u'Internal Gains',
               'min-fields': 0,
               'name': u'SurfaceContaminantSourceAndSink:Generic:DepositionVelocitySink',
               'pyname': u'SurfaceContaminantSourceAndSinkGenericDepositionVelocitySink',
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
    def surface_name(self):
        """field `Surface Name`

        Args:
            value (str): value for IDD Field `Surface Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `surface_name` or None if not set

        """
        return self["Surface Name"]

    @surface_name.setter
    def surface_name(self, value=None):
        """Corresponds to IDD field `Surface Name`"""
        self["Surface Name"] = value

    @property
    def deposition_velocity(self):
        """field `Deposition Velocity`

        |  Units: m/s

        Args:
            value (float): value for IDD Field `Deposition Velocity`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `deposition_velocity` or None if not set

        """
        return self["Deposition Velocity"]

    @deposition_velocity.setter
    def deposition_velocity(self, value=None):
        """Corresponds to IDD field `Deposition Velocity`"""
        self["Deposition Velocity"] = value

    @property
    def schedule_name(self):
        """field `Schedule Name`

        |  Value in this schedule should be a fraction (generally 0.0 - 1.0) applied to the
        |  Initial Emission Rate. When the value is equal to 1.0, the time will be reset to
        |  zero.

        Args:
            value (str): value for IDD Field `Schedule Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `schedule_name` or None if not set

        """
        return self["Schedule Name"]

    @schedule_name.setter
    def schedule_name(self, value=None):
        """Corresponds to IDD field `Schedule Name`"""
        self["Schedule Name"] = value




class ZoneContaminantSourceAndSinkGenericDepositionRateSink(DataObject):

    """ Corresponds to IDD object `ZoneContaminantSourceAndSink:Generic:DepositionRateSink`
        Simulate generic contaminant source driven by the boundary layer diffusion controlled model.
    """
    _schema = {'extensible-fields': OrderedDict(),
               'fields': OrderedDict([(u'name',
                                       {'name': u'Name',
                                        'pyname': u'name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'alpha'}),
                                      (u'zone name',
                                       {'name': u'Zone Name',
                                        'pyname': u'zone_name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'deposition rate',
                                       {'name': u'Deposition Rate',
                                        'pyname': u'deposition_rate',
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'm/s'}),
                                      (u'schedule name',
                                       {'name': u'Schedule Name',
                                        'pyname': u'schedule_name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'})]),
               'format': None,
               'group': u'Internal Gains',
               'min-fields': 0,
               'name': u'ZoneContaminantSourceAndSink:Generic:DepositionRateSink',
               'pyname': u'ZoneContaminantSourceAndSinkGenericDepositionRateSink',
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
    def zone_name(self):
        """field `Zone Name`

        Args:
            value (str): value for IDD Field `Zone Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `zone_name` or None if not set

        """
        return self["Zone Name"]

    @zone_name.setter
    def zone_name(self, value=None):
        """Corresponds to IDD field `Zone Name`"""
        self["Zone Name"] = value

    @property
    def deposition_rate(self):
        """field `Deposition Rate`

        |  Units: m/s

        Args:
            value (float): value for IDD Field `Deposition Rate`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `deposition_rate` or None if not set

        """
        return self["Deposition Rate"]

    @deposition_rate.setter
    def deposition_rate(self, value=None):
        """Corresponds to IDD field `Deposition Rate`"""
        self["Deposition Rate"] = value

    @property
    def schedule_name(self):
        """field `Schedule Name`

        |  Value in this schedule should be a fraction (generally 0.0 - 1.0) applied to the
        |  Initial Emission Rate. When the value is equal to 1.0, the time will be reset to
        |  zero.

        Args:
            value (str): value for IDD Field `Schedule Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `schedule_name` or None if not set

        """
        return self["Schedule Name"]

    @schedule_name.setter
    def schedule_name(self, value=None):
        """Corresponds to IDD field `Schedule Name`"""
        self["Schedule Name"] = value


