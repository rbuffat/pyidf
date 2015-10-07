""" Data objects in group "Zone Airflow"
"""

from collections import OrderedDict
import logging
from pyidf.helper import DataObject

logger = logging.getLogger("pyidf")
logger.addHandler(logging.NullHandler())



class ZoneInfiltrationDesignFlowRate(DataObject):

    """ Corresponds to IDD object `ZoneInfiltration:DesignFlowRate`
        Infiltration is specified as a design level which is modified by a Schedule fraction, temperature difference and wind speed:
        Infiltration=Idesign * FSchedule * (A + B*|(Tzone-Todb)| + C*WindSpd + D * WindSpd**2)
        If you use a ZoneList in the Zone or ZoneList name field then this definition applies
        to all the zones in the ZoneList.
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
                                      (u'design flow rate calculation method',
                                       {'name': u'Design Flow Rate Calculation Method',
                                        'pyname': u'design_flow_rate_calculation_method',
                                        'default': u'Flow/Zone',
                                        'required-field': True,
                                        'autosizable': False,
                                        'accepted-values': [u'Flow/Zone',
                                                            u'Flow/Area',
                                                            u'Flow/ExteriorArea',
                                                            u'Flow/ExteriorWallArea',
                                                            u'AirChanges/Hour'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'design flow rate',
                                       {'name': u'Design Flow Rate',
                                        'pyname': u'design_flow_rate',
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'm3/s'}),
                                      (u'flow per zone floor area',
                                       {'name': u'Flow per Zone Floor Area',
                                        'pyname': u'flow_per_zone_floor_area',
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'm3/s-m2'}),
                                      (u'flow per exterior surface area',
                                       {'name': u'Flow per Exterior Surface Area',
                                        'pyname': u'flow_per_exterior_surface_area',
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'm3/s-m2'}),
                                      (u'air changes per hour',
                                       {'name': u'Air Changes per Hour',
                                        'pyname': u'air_changes_per_hour',
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'1/hr'}),
                                      (u'constant term coefficient',
                                       {'name': u'Constant Term Coefficient',
                                        'pyname': u'constant_term_coefficient',
                                        'default': 1.0,
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'temperature term coefficient',
                                       {'name': u'Temperature Term Coefficient',
                                        'pyname': u'temperature_term_coefficient',
                                        'default': 0.0,
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'velocity term coefficient',
                                       {'name': u'Velocity Term Coefficient',
                                        'pyname': u'velocity_term_coefficient',
                                        'default': 0.0,
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'velocity squared term coefficient',
                                       {'name': u'Velocity Squared Term Coefficient',
                                        'pyname': u'velocity_squared_term_coefficient',
                                        'default': 0.0,
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real'})]),
               'format': None,
               'group': u'Zone Airflow',
               'min-fields': 12,
               'name': u'ZoneInfiltration:DesignFlowRate',
               'pyname': u'ZoneInfiltrationDesignFlowRate',
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
    def design_flow_rate_calculation_method(self):
        """field `Design Flow Rate Calculation Method`

        |  The entered calculation method is used to create the maximum amount of infiltration
        |  for this set of attributes
        |  Choices: Flow/Zone => Design Flow Rate -- simply enter Design Flow Rate
        |  Flow/Area => Flow per Zone Floor Area - Value * Floor Area (zone) = Design Flow Rate
        |  Flow/ExteriorArea => Flow per Exterior Surface Area - Value * Exterior Surface Area (zone) = Design Flow Rate
        |  Flow/ExteriorWallArea => Flow per Exterior Surface Area - Value * Exterior Wall Surface Area (zone) = Design Flow Rate
        |  AirChanges/Hour => Air Changes per Hour - Value * Floor Volume (zone) adjusted for m3/s = Design Volume Flow Rate
        |  "Idesign" in Equation is the result.
        |  Default value: Flow/Zone

        Args:
            value (str): value for IDD Field `Design Flow Rate Calculation Method`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `design_flow_rate_calculation_method` or None if not set

        """
        return self["Design Flow Rate Calculation Method"]

    @design_flow_rate_calculation_method.setter
    def design_flow_rate_calculation_method(self, value="Flow/Zone"):
        """Corresponds to IDD field `Design Flow Rate Calculation Method`"""
        self["Design Flow Rate Calculation Method"] = value

    @property
    def design_flow_rate(self):
        """field `Design Flow Rate`

        |  Units: m3/s
        |  IP-Units: ft3/min

        Args:
            value (float): value for IDD Field `Design Flow Rate`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `design_flow_rate` or None if not set

        """
        return self["Design Flow Rate"]

    @design_flow_rate.setter
    def design_flow_rate(self, value=None):
        """Corresponds to IDD field `Design Flow Rate`"""
        self["Design Flow Rate"] = value

    @property
    def flow_per_zone_floor_area(self):
        """field `Flow per Zone Floor Area`

        |  Units: m3/s-m2

        Args:
            value (float): value for IDD Field `Flow per Zone Floor Area`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `flow_per_zone_floor_area` or None if not set

        """
        return self["Flow per Zone Floor Area"]

    @flow_per_zone_floor_area.setter
    def flow_per_zone_floor_area(self, value=None):
        """Corresponds to IDD field `Flow per Zone Floor Area`"""
        self["Flow per Zone Floor Area"] = value

    @property
    def flow_per_exterior_surface_area(self):
        """field `Flow per Exterior Surface Area`

        |  use key Flow/ExteriorArea for all exterior surface area
        |  use key Flow/ExteriorWallArea to include only exterior wall area
        |  Units: m3/s-m2

        Args:
            value (float): value for IDD Field `Flow per Exterior Surface Area`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `flow_per_exterior_surface_area` or None if not set

        """
        return self["Flow per Exterior Surface Area"]

    @flow_per_exterior_surface_area.setter
    def flow_per_exterior_surface_area(self, value=None):
        """Corresponds to IDD field `Flow per Exterior Surface Area`"""
        self["Flow per Exterior Surface Area"] = value

    @property
    def air_changes_per_hour(self):
        """field `Air Changes per Hour`

        |  Units: 1/hr

        Args:
            value (float): value for IDD Field `Air Changes per Hour`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `air_changes_per_hour` or None if not set

        """
        return self["Air Changes per Hour"]

    @air_changes_per_hour.setter
    def air_changes_per_hour(self, value=None):
        """Corresponds to IDD field `Air Changes per Hour`"""
        self["Air Changes per Hour"] = value

    @property
    def constant_term_coefficient(self):
        """field `Constant Term Coefficient`

        |  "A" in Equation
        |  Default value: 1.0

        Args:
            value (float): value for IDD Field `Constant Term Coefficient`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `constant_term_coefficient` or None if not set

        """
        return self["Constant Term Coefficient"]

    @constant_term_coefficient.setter
    def constant_term_coefficient(self, value=1.0):
        """Corresponds to IDD field `Constant Term Coefficient`"""
        self["Constant Term Coefficient"] = value

    @property
    def temperature_term_coefficient(self):
        """field `Temperature Term Coefficient`

        |  "B" in Equation

        Args:
            value (float): value for IDD Field `Temperature Term Coefficient`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `temperature_term_coefficient` or None if not set

        """
        return self["Temperature Term Coefficient"]

    @temperature_term_coefficient.setter
    def temperature_term_coefficient(self, value=None):
        """Corresponds to IDD field `Temperature Term Coefficient`"""
        self["Temperature Term Coefficient"] = value

    @property
    def velocity_term_coefficient(self):
        """field `Velocity Term Coefficient`

        |  "C" in Equation

        Args:
            value (float): value for IDD Field `Velocity Term Coefficient`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `velocity_term_coefficient` or None if not set

        """
        return self["Velocity Term Coefficient"]

    @velocity_term_coefficient.setter
    def velocity_term_coefficient(self, value=None):
        """Corresponds to IDD field `Velocity Term Coefficient`"""
        self["Velocity Term Coefficient"] = value

    @property
    def velocity_squared_term_coefficient(self):
        """field `Velocity Squared Term Coefficient`

        |  "D" in Equation

        Args:
            value (float): value for IDD Field `Velocity Squared Term Coefficient`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `velocity_squared_term_coefficient` or None if not set

        """
        return self["Velocity Squared Term Coefficient"]

    @velocity_squared_term_coefficient.setter
    def velocity_squared_term_coefficient(self, value=None):
        """Corresponds to IDD field `Velocity Squared Term Coefficient`"""
        self["Velocity Squared Term Coefficient"] = value




class ZoneInfiltrationEffectiveLeakageArea(DataObject):

    """ Corresponds to IDD object `ZoneInfiltration:EffectiveLeakageArea`
        Infiltration is specified as effective leakage area at 4 Pa, schedule fraction, stack and wind coefficients, and
        is a function of temperature difference and wind speed:
        Infiltration=FSchedule * (AL /1000) SQRT(Cs*|(Tzone-Todb)| +  Cw*WindSpd**2 )
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
                                      (u'effective air leakage area',
                                       {'name': u'Effective Air Leakage Area',
                                        'pyname': u'effective_air_leakage_area',
                                        'minimum>': 0.0,
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'cm2'}),
                                      (u'stack coefficient',
                                       {'name': u'Stack Coefficient',
                                        'pyname': u'stack_coefficient',
                                        'minimum>': 0.0,
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'wind coefficient',
                                       {'name': u'Wind Coefficient',
                                        'pyname': u'wind_coefficient',
                                        'minimum>': 0.0,
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real'})]),
               'format': None,
               'group': u'Zone Airflow',
               'min-fields': 6,
               'name': u'ZoneInfiltration:EffectiveLeakageArea',
               'pyname': u'ZoneInfiltrationEffectiveLeakageArea',
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
    def effective_air_leakage_area(self):
        """field `Effective Air Leakage Area`

        |  "AL" in Equation
        |  units are cm2 (square centimeters)
        |  Units: cm2

        Args:
            value (float): value for IDD Field `Effective Air Leakage Area`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `effective_air_leakage_area` or None if not set

        """
        return self["Effective Air Leakage Area"]

    @effective_air_leakage_area.setter
    def effective_air_leakage_area(self, value=None):
        """Corresponds to IDD field `Effective Air Leakage Area`"""
        self["Effective Air Leakage Area"] = value

    @property
    def stack_coefficient(self):
        """field `Stack Coefficient`

        |  "Cs" in Equation

        Args:
            value (float): value for IDD Field `Stack Coefficient`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `stack_coefficient` or None if not set

        """
        return self["Stack Coefficient"]

    @stack_coefficient.setter
    def stack_coefficient(self, value=None):
        """Corresponds to IDD field `Stack Coefficient`"""
        self["Stack Coefficient"] = value

    @property
    def wind_coefficient(self):
        """field `Wind Coefficient`

        |  "Cw" in Equation

        Args:
            value (float): value for IDD Field `Wind Coefficient`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `wind_coefficient` or None if not set

        """
        return self["Wind Coefficient"]

    @wind_coefficient.setter
    def wind_coefficient(self, value=None):
        """Corresponds to IDD field `Wind Coefficient`"""
        self["Wind Coefficient"] = value




class ZoneInfiltrationFlowCoefficient(DataObject):

    """ Corresponds to IDD object `ZoneInfiltration:FlowCoefficient`
        Infiltration is specified as flow coefficient, schedule fraction, stack and wind coefficients, and
        is a function of temperature difference and wind speed:
        Infiltration=FSchedule * SQRT( (c * Cs*|(Tzone-Todb)|**n)**2 + (c* Cw*(s * WindSpd)**2n)**2 )
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
                                      (u'flow coefficient',
                                       {'name': u'Flow Coefficient',
                                        'pyname': u'flow_coefficient',
                                        'minimum>': 0.0,
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'stack coefficient',
                                       {'name': u'Stack Coefficient',
                                        'pyname': u'stack_coefficient',
                                        'minimum>': 0.0,
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'pressure exponent',
                                       {'name': u'Pressure Exponent',
                                        'pyname': u'pressure_exponent',
                                        'default': 0.67,
                                        'minimum>': 0.0,
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'wind coefficient',
                                       {'name': u'Wind Coefficient',
                                        'pyname': u'wind_coefficient',
                                        'minimum>': 0.0,
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'shelter factor',
                                       {'name': u'Shelter Factor',
                                        'pyname': u'shelter_factor',
                                        'minimum>': 0.0,
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real'})]),
               'format': None,
               'group': u'Zone Airflow',
               'min-fields': 8,
               'name': u'ZoneInfiltration:FlowCoefficient',
               'pyname': u'ZoneInfiltrationFlowCoefficient',
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
    def flow_coefficient(self):
        """field `Flow Coefficient`

        |  "c" in Equation

        Args:
            value (float): value for IDD Field `Flow Coefficient`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `flow_coefficient` or None if not set

        """
        return self["Flow Coefficient"]

    @flow_coefficient.setter
    def flow_coefficient(self, value=None):
        """Corresponds to IDD field `Flow Coefficient`"""
        self["Flow Coefficient"] = value

    @property
    def stack_coefficient(self):
        """field `Stack Coefficient`

        |  "Cs" in Equation

        Args:
            value (float): value for IDD Field `Stack Coefficient`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `stack_coefficient` or None if not set

        """
        return self["Stack Coefficient"]

    @stack_coefficient.setter
    def stack_coefficient(self, value=None):
        """Corresponds to IDD field `Stack Coefficient`"""
        self["Stack Coefficient"] = value

    @property
    def pressure_exponent(self):
        """field `Pressure Exponent`

        |  "n" in Equation
        |  Default value: 0.67

        Args:
            value (float): value for IDD Field `Pressure Exponent`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `pressure_exponent` or None if not set

        """
        return self["Pressure Exponent"]

    @pressure_exponent.setter
    def pressure_exponent(self, value=0.67):
        """Corresponds to IDD field `Pressure Exponent`"""
        self["Pressure Exponent"] = value

    @property
    def wind_coefficient(self):
        """field `Wind Coefficient`

        |  "Cw" in Equation

        Args:
            value (float): value for IDD Field `Wind Coefficient`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `wind_coefficient` or None if not set

        """
        return self["Wind Coefficient"]

    @wind_coefficient.setter
    def wind_coefficient(self, value=None):
        """Corresponds to IDD field `Wind Coefficient`"""
        self["Wind Coefficient"] = value

    @property
    def shelter_factor(self):
        """field `Shelter Factor`

        |  "s" in Equation

        Args:
            value (float): value for IDD Field `Shelter Factor`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `shelter_factor` or None if not set

        """
        return self["Shelter Factor"]

    @shelter_factor.setter
    def shelter_factor(self, value=None):
        """Corresponds to IDD field `Shelter Factor`"""
        self["Shelter Factor"] = value




class ZoneVentilationDesignFlowRate(DataObject):

    """ Corresponds to IDD object `ZoneVentilation:DesignFlowRate`
        Ventilation is specified as a design level which is modified by a schedule fraction, temperature difference and wind speed:
        Ventilation=Vdesign * Fschedule * (A + B*|(Tzone-Todb)| + C*WindSpd + D * WindSpd**2)
        If you use a ZoneList in the Zone or ZoneList name field then this definition applies
        to all the zones in the ZoneList.
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
                                      (u'design flow rate calculation method',
                                       {'name': u'Design Flow Rate Calculation Method',
                                        'pyname': u'design_flow_rate_calculation_method',
                                        'default': u'Flow/Zone',
                                        'required-field': True,
                                        'autosizable': False,
                                        'accepted-values': [u'Flow/Zone',
                                                            u'Flow/Area',
                                                            u'Flow/Person',
                                                            u'AirChanges/Hour'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'design flow rate',
                                       {'name': u'Design Flow Rate',
                                        'pyname': u'design_flow_rate',
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'm3/s'}),
                                      (u'flow rate per zone floor area',
                                       {'name': u'Flow Rate per Zone Floor Area',
                                        'pyname': u'flow_rate_per_zone_floor_area',
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'm3/s-m2'}),
                                      (u'flow rate per person',
                                       {'name': u'Flow Rate per Person',
                                        'pyname': u'flow_rate_per_person',
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'm3/s-person'}),
                                      (u'air changes per hour',
                                       {'name': u'Air Changes per Hour',
                                        'pyname': u'air_changes_per_hour',
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'1/hr'}),
                                      (u'ventilation type',
                                       {'name': u'Ventilation Type',
                                        'pyname': u'ventilation_type',
                                        'default': u'Natural',
                                        'required-field': True,
                                        'autosizable': False,
                                        'accepted-values': [u'Natural',
                                                            u'Intake',
                                                            u'Exhaust',
                                                            u'Balanced'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'fan pressure rise',
                                       {'name': u'Fan Pressure Rise',
                                        'pyname': u'fan_pressure_rise',
                                        'default': 0.0,
                                        'required-field': True,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'Pa'}),
                                      (u'fan total efficiency',
                                       {'name': u'Fan Total Efficiency',
                                        'pyname': u'fan_total_efficiency',
                                        'default': 1.0,
                                        'minimum>': 0.0,
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'constant term coefficient',
                                       {'name': u'Constant Term Coefficient',
                                        'pyname': u'constant_term_coefficient',
                                        'default': 1.0,
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'temperature term coefficient',
                                       {'name': u'Temperature Term Coefficient',
                                        'pyname': u'temperature_term_coefficient',
                                        'default': 0.0,
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'velocity term coefficient',
                                       {'name': u'Velocity Term Coefficient',
                                        'pyname': u'velocity_term_coefficient',
                                        'default': 0.0,
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'velocity squared term coefficient',
                                       {'name': u'Velocity Squared Term Coefficient',
                                        'pyname': u'velocity_squared_term_coefficient',
                                        'default': 0.0,
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'minimum indoor temperature',
                                       {'name': u'Minimum Indoor Temperature',
                                        'pyname': u'minimum_indoor_temperature',
                                        'default': -100.0,
                                        'maximum': 100.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': -100.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'C'}),
                                      (u'minimum indoor temperature schedule name',
                                       {'name': u'Minimum Indoor Temperature Schedule Name',
                                        'pyname': u'minimum_indoor_temperature_schedule_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'maximum indoor temperature',
                                       {'name': u'Maximum Indoor Temperature',
                                        'pyname': u'maximum_indoor_temperature',
                                        'default': 100.0,
                                        'maximum': 100.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': -100.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'C'}),
                                      (u'maximum indoor temperature schedule name',
                                       {'name': u'Maximum Indoor Temperature Schedule Name',
                                        'pyname': u'maximum_indoor_temperature_schedule_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'delta temperature',
                                       {'name': u'Delta Temperature',
                                        'pyname': u'delta_temperature',
                                        'default': -100.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': -100.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'deltaC'}),
                                      (u'delta temperature schedule name',
                                       {'name': u'Delta Temperature Schedule Name',
                                        'pyname': u'delta_temperature_schedule_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'minimum outdoor temperature',
                                       {'name': u'Minimum Outdoor Temperature',
                                        'pyname': u'minimum_outdoor_temperature',
                                        'default': -100.0,
                                        'maximum': 100.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': -100.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'C'}),
                                      (u'minimum outdoor temperature schedule name',
                                       {'name': u'Minimum Outdoor Temperature Schedule Name',
                                        'pyname': u'minimum_outdoor_temperature_schedule_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'maximum outdoor temperature',
                                       {'name': u'Maximum Outdoor Temperature',
                                        'pyname': u'maximum_outdoor_temperature',
                                        'default': 100.0,
                                        'maximum': 100.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': -100.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'C'}),
                                      (u'maximum outdoor temperature schedule name',
                                       {'name': u'Maximum Outdoor Temperature Schedule Name',
                                        'pyname': u'maximum_outdoor_temperature_schedule_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'maximum wind speed',
                                       {'name': u'Maximum Wind Speed',
                                        'pyname': u'maximum_wind_speed',
                                        'default': 40.0,
                                        'maximum': 40.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'm/s'})]),
               'format': None,
               'group': u'Zone Airflow',
               'min-fields': 15,
               'name': u'ZoneVentilation:DesignFlowRate',
               'pyname': u'ZoneVentilationDesignFlowRate',
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
    def design_flow_rate_calculation_method(self):
        """field `Design Flow Rate Calculation Method`

        |  The entered calculation method is used to create the maximum amount of ventilation
        |  for this set of attributes
        |  Choices: Flow/Zone => Design Flow Rate -- simply enter Design Flow Rate
        |  Flow/Area => Flow Rate per Zone Floor Area - Value * Floor Area (zone) = Design Flow Rate
        |  Flow/Person => Flow Rate per Person - Value * #people = Design Flow Rate
        |  AirChanges/Hour => Air Changes per Hour - Value * Floor Volume (zone) adjusted for m3/s = Design Volume Flow Rate
        |  "Vdesign" in Equation is the result.
        |  Default value: Flow/Zone

        Args:
            value (str): value for IDD Field `Design Flow Rate Calculation Method`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `design_flow_rate_calculation_method` or None if not set

        """
        return self["Design Flow Rate Calculation Method"]

    @design_flow_rate_calculation_method.setter
    def design_flow_rate_calculation_method(self, value="Flow/Zone"):
        """Corresponds to IDD field `Design Flow Rate Calculation Method`"""
        self["Design Flow Rate Calculation Method"] = value

    @property
    def design_flow_rate(self):
        """field `Design Flow Rate`

        |  Units: m3/s

        Args:
            value (float): value for IDD Field `Design Flow Rate`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `design_flow_rate` or None if not set

        """
        return self["Design Flow Rate"]

    @design_flow_rate.setter
    def design_flow_rate(self, value=None):
        """Corresponds to IDD field `Design Flow Rate`"""
        self["Design Flow Rate"] = value

    @property
    def flow_rate_per_zone_floor_area(self):
        """field `Flow Rate per Zone Floor Area`

        |  Units: m3/s-m2

        Args:
            value (float): value for IDD Field `Flow Rate per Zone Floor Area`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `flow_rate_per_zone_floor_area` or None if not set

        """
        return self["Flow Rate per Zone Floor Area"]

    @flow_rate_per_zone_floor_area.setter
    def flow_rate_per_zone_floor_area(self, value=None):
        """Corresponds to IDD field `Flow Rate per Zone Floor Area`"""
        self["Flow Rate per Zone Floor Area"] = value

    @property
    def flow_rate_per_person(self):
        """field `Flow Rate per Person`

        |  Units: m3/s-person

        Args:
            value (float): value for IDD Field `Flow Rate per Person`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `flow_rate_per_person` or None if not set

        """
        return self["Flow Rate per Person"]

    @flow_rate_per_person.setter
    def flow_rate_per_person(self, value=None):
        """Corresponds to IDD field `Flow Rate per Person`"""
        self["Flow Rate per Person"] = value

    @property
    def air_changes_per_hour(self):
        """field `Air Changes per Hour`

        |  Units: 1/hr

        Args:
            value (float): value for IDD Field `Air Changes per Hour`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `air_changes_per_hour` or None if not set

        """
        return self["Air Changes per Hour"]

    @air_changes_per_hour.setter
    def air_changes_per_hour(self, value=None):
        """Corresponds to IDD field `Air Changes per Hour`"""
        self["Air Changes per Hour"] = value

    @property
    def ventilation_type(self):
        """field `Ventilation Type`

        |  Default value: Natural

        Args:
            value (str): value for IDD Field `Ventilation Type`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `ventilation_type` or None if not set

        """
        return self["Ventilation Type"]

    @ventilation_type.setter
    def ventilation_type(self, value="Natural"):
        """Corresponds to IDD field `Ventilation Type`"""
        self["Ventilation Type"] = value

    @property
    def fan_pressure_rise(self):
        """field `Fan Pressure Rise`

        |  pressure rise across the fan
        |  Units: Pa

        Args:
            value (float): value for IDD Field `Fan Pressure Rise`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `fan_pressure_rise` or None if not set

        """
        return self["Fan Pressure Rise"]

    @fan_pressure_rise.setter
    def fan_pressure_rise(self, value=None):
        """Corresponds to IDD field `Fan Pressure Rise`"""
        self["Fan Pressure Rise"] = value

    @property
    def fan_total_efficiency(self):
        """field `Fan Total Efficiency`

        |  Default value: 1.0

        Args:
            value (float): value for IDD Field `Fan Total Efficiency`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `fan_total_efficiency` or None if not set

        """
        return self["Fan Total Efficiency"]

    @fan_total_efficiency.setter
    def fan_total_efficiency(self, value=1.0):
        """Corresponds to IDD field `Fan Total Efficiency`"""
        self["Fan Total Efficiency"] = value

    @property
    def constant_term_coefficient(self):
        """field `Constant Term Coefficient`

        |  "A" in Equation
        |  Default value: 1.0

        Args:
            value (float): value for IDD Field `Constant Term Coefficient`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `constant_term_coefficient` or None if not set

        """
        return self["Constant Term Coefficient"]

    @constant_term_coefficient.setter
    def constant_term_coefficient(self, value=1.0):
        """Corresponds to IDD field `Constant Term Coefficient`"""
        self["Constant Term Coefficient"] = value

    @property
    def temperature_term_coefficient(self):
        """field `Temperature Term Coefficient`

        |  "B" in Equation

        Args:
            value (float): value for IDD Field `Temperature Term Coefficient`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `temperature_term_coefficient` or None if not set

        """
        return self["Temperature Term Coefficient"]

    @temperature_term_coefficient.setter
    def temperature_term_coefficient(self, value=None):
        """Corresponds to IDD field `Temperature Term Coefficient`"""
        self["Temperature Term Coefficient"] = value

    @property
    def velocity_term_coefficient(self):
        """field `Velocity Term Coefficient`

        |  "C" in Equation

        Args:
            value (float): value for IDD Field `Velocity Term Coefficient`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `velocity_term_coefficient` or None if not set

        """
        return self["Velocity Term Coefficient"]

    @velocity_term_coefficient.setter
    def velocity_term_coefficient(self, value=None):
        """Corresponds to IDD field `Velocity Term Coefficient`"""
        self["Velocity Term Coefficient"] = value

    @property
    def velocity_squared_term_coefficient(self):
        """field `Velocity Squared Term Coefficient`

        |  "D" in Equation

        Args:
            value (float): value for IDD Field `Velocity Squared Term Coefficient`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `velocity_squared_term_coefficient` or None if not set

        """
        return self["Velocity Squared Term Coefficient"]

    @velocity_squared_term_coefficient.setter
    def velocity_squared_term_coefficient(self, value=None):
        """Corresponds to IDD field `Velocity Squared Term Coefficient`"""
        self["Velocity Squared Term Coefficient"] = value

    @property
    def minimum_indoor_temperature(self):
        """field `Minimum Indoor Temperature`

        |  this is the indoor temperature below which ventilation is shutoff
        |  Units: C
        |  Default value: -100.0
        |  value >= -100.0
        |  value <= 100.0

        Args:
            value (float): value for IDD Field `Minimum Indoor Temperature`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `minimum_indoor_temperature` or None if not set

        """
        return self["Minimum Indoor Temperature"]

    @minimum_indoor_temperature.setter
    def minimum_indoor_temperature(self, value=-100.0):
        """Corresponds to IDD field `Minimum Indoor Temperature`"""
        self["Minimum Indoor Temperature"] = value

    @property
    def minimum_indoor_temperature_schedule_name(self):
        """field `Minimum Indoor Temperature Schedule Name`

        |  This schedule contains the indoor temperature versus time below which
        |  ventilation is shutoff.

        Args:
            value (str): value for IDD Field `Minimum Indoor Temperature Schedule Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `minimum_indoor_temperature_schedule_name` or None if not set

        """
        return self["Minimum Indoor Temperature Schedule Name"]

    @minimum_indoor_temperature_schedule_name.setter
    def minimum_indoor_temperature_schedule_name(self, value=None):
        """Corresponds to IDD field `Minimum Indoor Temperature Schedule
        Name`"""
        self["Minimum Indoor Temperature Schedule Name"] = value

    @property
    def maximum_indoor_temperature(self):
        """field `Maximum Indoor Temperature`

        |  this is the indoor temperature above which ventilation is shutoff
        |  Units: C
        |  Default value: 100.0
        |  value >= -100.0
        |  value <= 100.0

        Args:
            value (float): value for IDD Field `Maximum Indoor Temperature`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `maximum_indoor_temperature` or None if not set

        """
        return self["Maximum Indoor Temperature"]

    @maximum_indoor_temperature.setter
    def maximum_indoor_temperature(self, value=100.0):
        """Corresponds to IDD field `Maximum Indoor Temperature`"""
        self["Maximum Indoor Temperature"] = value

    @property
    def maximum_indoor_temperature_schedule_name(self):
        """field `Maximum Indoor Temperature Schedule Name`

        |  This schedule contains the indoor temperature versus time above which
        |  ventilation is shutoff.

        Args:
            value (str): value for IDD Field `Maximum Indoor Temperature Schedule Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `maximum_indoor_temperature_schedule_name` or None if not set

        """
        return self["Maximum Indoor Temperature Schedule Name"]

    @maximum_indoor_temperature_schedule_name.setter
    def maximum_indoor_temperature_schedule_name(self, value=None):
        """Corresponds to IDD field `Maximum Indoor Temperature Schedule
        Name`"""
        self["Maximum Indoor Temperature Schedule Name"] = value

    @property
    def delta_temperature(self):
        """field `Delta Temperature`

        |  This is the temperature differential between indoor and outdoor below which ventilation is shutoff.
        |  If ((IndoorTemp - OutdoorTemp) < DeltaTemperature) then ventilation is not allowed.
        |  For example, if delta temperature is 2C, ventilation is assumed to be available if the outside air temperature
        |  is at least 2C cooler than the zone air temperature. The values for this field can include negative numbers.
        |  This allows ventilation to occur even if the outdoor temperature is above the indoor temperature.
        |  Units: deltaC
        |  Default value: -100.0
        |  value >= -100.0

        Args:
            value (float): value for IDD Field `Delta Temperature`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `delta_temperature` or None if not set

        """
        return self["Delta Temperature"]

    @delta_temperature.setter
    def delta_temperature(self, value=-100.0):
        """Corresponds to IDD field `Delta Temperature`"""
        self["Delta Temperature"] = value

    @property
    def delta_temperature_schedule_name(self):
        """field `Delta Temperature Schedule Name`

        |  This schedule contains the temperature differential between indoor and outdoor
        |  versus time below which ventilation is shutoff.

        Args:
            value (str): value for IDD Field `Delta Temperature Schedule Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `delta_temperature_schedule_name` or None if not set

        """
        return self["Delta Temperature Schedule Name"]

    @delta_temperature_schedule_name.setter
    def delta_temperature_schedule_name(self, value=None):
        """Corresponds to IDD field `Delta Temperature Schedule Name`"""
        self["Delta Temperature Schedule Name"] = value

    @property
    def minimum_outdoor_temperature(self):
        """field `Minimum Outdoor Temperature`

        |  this is the outdoor temperature below which ventilation is shutoff
        |  Units: C
        |  Default value: -100.0
        |  value >= -100.0
        |  value <= 100.0

        Args:
            value (float): value for IDD Field `Minimum Outdoor Temperature`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `minimum_outdoor_temperature` or None if not set

        """
        return self["Minimum Outdoor Temperature"]

    @minimum_outdoor_temperature.setter
    def minimum_outdoor_temperature(self, value=-100.0):
        """Corresponds to IDD field `Minimum Outdoor Temperature`"""
        self["Minimum Outdoor Temperature"] = value

    @property
    def minimum_outdoor_temperature_schedule_name(self):
        """field `Minimum Outdoor Temperature Schedule Name`

        |  This schedule contains the outdoor temperature versus time below which
        |  ventilation is shutoff.

        Args:
            value (str): value for IDD Field `Minimum Outdoor Temperature Schedule Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `minimum_outdoor_temperature_schedule_name` or None if not set

        """
        return self["Minimum Outdoor Temperature Schedule Name"]

    @minimum_outdoor_temperature_schedule_name.setter
    def minimum_outdoor_temperature_schedule_name(self, value=None):
        """Corresponds to IDD field `Minimum Outdoor Temperature Schedule
        Name`"""
        self["Minimum Outdoor Temperature Schedule Name"] = value

    @property
    def maximum_outdoor_temperature(self):
        """field `Maximum Outdoor Temperature`

        |  this is the outdoor temperature above which ventilation is shutoff
        |  Units: C
        |  Default value: 100.0
        |  value >= -100.0
        |  value <= 100.0

        Args:
            value (float): value for IDD Field `Maximum Outdoor Temperature`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `maximum_outdoor_temperature` or None if not set

        """
        return self["Maximum Outdoor Temperature"]

    @maximum_outdoor_temperature.setter
    def maximum_outdoor_temperature(self, value=100.0):
        """Corresponds to IDD field `Maximum Outdoor Temperature`"""
        self["Maximum Outdoor Temperature"] = value

    @property
    def maximum_outdoor_temperature_schedule_name(self):
        """field `Maximum Outdoor Temperature Schedule Name`

        |  This schedule contains the outdoor temperature versus time above which
        |  ventilation is shutoff.

        Args:
            value (str): value for IDD Field `Maximum Outdoor Temperature Schedule Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `maximum_outdoor_temperature_schedule_name` or None if not set

        """
        return self["Maximum Outdoor Temperature Schedule Name"]

    @maximum_outdoor_temperature_schedule_name.setter
    def maximum_outdoor_temperature_schedule_name(self, value=None):
        """Corresponds to IDD field `Maximum Outdoor Temperature Schedule
        Name`"""
        self["Maximum Outdoor Temperature Schedule Name"] = value

    @property
    def maximum_wind_speed(self):
        """field `Maximum Wind Speed`

        |  this is the outdoor wind speed above which ventilation is shutoff
        |  Units: m/s
        |  Default value: 40.0
        |  value <= 40.0

        Args:
            value (float): value for IDD Field `Maximum Wind Speed`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `maximum_wind_speed` or None if not set

        """
        return self["Maximum Wind Speed"]

    @maximum_wind_speed.setter
    def maximum_wind_speed(self, value=40.0):
        """Corresponds to IDD field `Maximum Wind Speed`"""
        self["Maximum Wind Speed"] = value




class ZoneVentilationWindandStackOpenArea(DataObject):

    """ Corresponds to IDD object `ZoneVentilation:WindandStackOpenArea`
        This object is specified as natural ventilation driven by wind and stack effect only:
        Ventilation Wind = Cw * Opening Area * Schedule * WindSpd
        Ventilation Stack = Cd * Opening Area * Schedule * SQRT(2*g*DH*(|(Tzone-Todb)|/Tzone))
        Total Ventilation = SQRT((Ventilation Wind)^2 + (Ventilation Stack)^2)
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
                                      (u'opening area',
                                       {'name': u'Opening Area',
                                        'pyname': u'opening_area',
                                        'default': 0.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'm2'}),
                                      (u'opening area fraction schedule name',
                                       {'name': u'Opening Area Fraction Schedule Name',
                                        'pyname': u'opening_area_fraction_schedule_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'opening effectiveness',
                                       {'name': u'Opening Effectiveness',
                                        'pyname': u'opening_effectiveness',
                                        'default': 'Autocalculate',
                                        'maximum': 1.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': True,
                                        'type': u'real',
                                        'unit': u'dimensionless'}),
                                      (u'effective angle',
                                       {'name': u'Effective Angle',
                                        'pyname': u'effective_angle',
                                        'default': 0.0,
                                        'maximum<': 360.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'deg'}),
                                      (u'height difference',
                                       {'name': u'Height Difference',
                                        'pyname': u'height_difference',
                                        'default': 0.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'm'}),
                                      (u'discharge coefficient for opening',
                                       {'name': u'Discharge Coefficient for Opening',
                                        'pyname': u'discharge_coefficient_for_opening',
                                        'default': 'Autocalculate',
                                        'maximum': 1.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': True,
                                        'type': 'real'}),
                                      (u'minimum indoor temperature',
                                       {'name': u'Minimum Indoor Temperature',
                                        'pyname': u'minimum_indoor_temperature',
                                        'default': -100.0,
                                        'maximum': 100.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': -100.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'C'}),
                                      (u'minimum indoor temperature schedule name',
                                       {'name': u'Minimum Indoor Temperature Schedule Name',
                                        'pyname': u'minimum_indoor_temperature_schedule_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'maximum indoor temperature',
                                       {'name': u'Maximum Indoor Temperature',
                                        'pyname': u'maximum_indoor_temperature',
                                        'default': 100.0,
                                        'maximum': 100.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': -100.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'C'}),
                                      (u'maximum indoor temperature schedule name',
                                       {'name': u'Maximum Indoor Temperature Schedule Name',
                                        'pyname': u'maximum_indoor_temperature_schedule_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'delta temperature',
                                       {'name': u'Delta Temperature',
                                        'pyname': u'delta_temperature',
                                        'default': -100.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': -100.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'deltaC'}),
                                      (u'delta temperature schedule name',
                                       {'name': u'Delta Temperature Schedule Name',
                                        'pyname': u'delta_temperature_schedule_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'minimum outdoor temperature',
                                       {'name': u'Minimum Outdoor Temperature',
                                        'pyname': u'minimum_outdoor_temperature',
                                        'default': -100.0,
                                        'maximum': 100.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': -100.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'C'}),
                                      (u'minimum outdoor temperature schedule name',
                                       {'name': u'Minimum Outdoor Temperature Schedule Name',
                                        'pyname': u'minimum_outdoor_temperature_schedule_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'maximum outdoor temperature',
                                       {'name': u'Maximum Outdoor Temperature',
                                        'pyname': u'maximum_outdoor_temperature',
                                        'default': 100.0,
                                        'maximum': 100.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': -100.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'C'}),
                                      (u'maximum outdoor temperature schedule name',
                                       {'name': u'Maximum Outdoor Temperature Schedule Name',
                                        'pyname': u'maximum_outdoor_temperature_schedule_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'maximum wind speed',
                                       {'name': u'Maximum Wind Speed',
                                        'pyname': u'maximum_wind_speed',
                                        'default': 40.0,
                                        'maximum': 40.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'm/s'})]),
               'format': None,
               'group': u'Zone Airflow',
               'min-fields': 8,
               'name': u'ZoneVentilation:WindandStackOpenArea',
               'pyname': u'ZoneVentilationWindandStackOpenArea',
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
    def opening_area(self):
        """field `Opening Area`

        |  This is the opening area used to calculate stack effect and wind driven ventilation.
        |  Units: m2

        Args:
            value (float): value for IDD Field `Opening Area`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `opening_area` or None if not set

        """
        return self["Opening Area"]

    @opening_area.setter
    def opening_area(self, value=None):
        """Corresponds to IDD field `Opening Area`"""
        self["Opening Area"] = value

    @property
    def opening_area_fraction_schedule_name(self):
        """field `Opening Area Fraction Schedule Name`

        |  This schedule contains the fraction values applied to the opening area given in the previous
        |  input field (0.0 - 1.0).

        Args:
            value (str): value for IDD Field `Opening Area Fraction Schedule Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `opening_area_fraction_schedule_name` or None if not set

        """
        return self["Opening Area Fraction Schedule Name"]

    @opening_area_fraction_schedule_name.setter
    def opening_area_fraction_schedule_name(self, value=None):
        """Corresponds to IDD field `Opening Area Fraction Schedule Name`"""
        self["Opening Area Fraction Schedule Name"] = value

    @property
    def opening_effectiveness(self):
        """field `Opening Effectiveness`

        |  This field is used to calculate wind driven ventilation.
        |  "Cw" in the wind-driven equation and the maximum value is 1.0.
        |  When the input is Autocalculate, the program calculates Cw based on an angle between
        |  wind direction and effective angle
        |  Cw = 0.55 at angle = 0, and Cw = 0.3 at angle=180
        |  Linear interpolation is used to calculate Cw based on the above two values.
        |  Units: dimensionless
        |  Default value: "Autocalculate"
        |  value <= 1.0

        Args:
            value (float or "Autocalculate"): value for IDD Field `Opening Effectiveness`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float or "Autocalculate": the value of `opening_effectiveness` or None if not set

        """
        return self["Opening Effectiveness"]

    @opening_effectiveness.setter
    def opening_effectiveness(self, value="Autocalculate"):
        """Corresponds to IDD field `Opening Effectiveness`"""
        self["Opening Effectiveness"] = value

    @property
    def effective_angle(self):
        """field `Effective Angle`

        |  This field is defined as normal angle of the opening area and is used when input
        |  field Opening Effectiveness = Autocalculate.
        |  Units: deg
        |  value < 360.0

        Args:
            value (float): value for IDD Field `Effective Angle`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `effective_angle` or None if not set

        """
        return self["Effective Angle"]

    @effective_angle.setter
    def effective_angle(self, value=None):
        """Corresponds to IDD field `Effective Angle`"""
        self["Effective Angle"] = value

    @property
    def height_difference(self):
        """field `Height Difference`

        |  This is the height difference between the midpoint of an opening and
        |  the neutral pressure level.
        |  "DH" in the stack equation.
        |  Units: m

        Args:
            value (float): value for IDD Field `Height Difference`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `height_difference` or None if not set

        """
        return self["Height Difference"]

    @height_difference.setter
    def height_difference(self, value=None):
        """Corresponds to IDD field `Height Difference`"""
        self["Height Difference"] = value

    @property
    def discharge_coefficient_for_opening(self):
        """field `Discharge Coefficient for Opening`

        |  This is the discharge coefficient used to calculate stack effect.
        |  "Cd" in the stack equation and the maximum value is 1.0.
        |  When the input is Autocalculate, the following equation is used to calculate the
        |  coefficient:
        |  Cd = 0.4 + 0.0045*|(Tzone-Todb)|
        |  Default value: "Autocalculate"
        |  value <= 1.0

        Args:
            value (float or "Autocalculate"): value for IDD Field `Discharge Coefficient for Opening`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float or "Autocalculate": the value of `discharge_coefficient_for_opening` or None if not set

        """
        return self["Discharge Coefficient for Opening"]

    @discharge_coefficient_for_opening.setter
    def discharge_coefficient_for_opening(self, value="Autocalculate"):
        """Corresponds to IDD field `Discharge Coefficient for Opening`"""
        self["Discharge Coefficient for Opening"] = value

    @property
    def minimum_indoor_temperature(self):
        """field `Minimum Indoor Temperature`

        |  This is the indoor temperature below which ventilation is shutoff.
        |  Units: C
        |  Default value: -100.0
        |  value >= -100.0
        |  value <= 100.0

        Args:
            value (float): value for IDD Field `Minimum Indoor Temperature`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `minimum_indoor_temperature` or None if not set

        """
        return self["Minimum Indoor Temperature"]

    @minimum_indoor_temperature.setter
    def minimum_indoor_temperature(self, value=-100.0):
        """Corresponds to IDD field `Minimum Indoor Temperature`"""
        self["Minimum Indoor Temperature"] = value

    @property
    def minimum_indoor_temperature_schedule_name(self):
        """field `Minimum Indoor Temperature Schedule Name`

        |  This schedule contains the indoor temperature versus time below which
        |  ventilation is shutoff.

        Args:
            value (str): value for IDD Field `Minimum Indoor Temperature Schedule Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `minimum_indoor_temperature_schedule_name` or None if not set

        """
        return self["Minimum Indoor Temperature Schedule Name"]

    @minimum_indoor_temperature_schedule_name.setter
    def minimum_indoor_temperature_schedule_name(self, value=None):
        """Corresponds to IDD field `Minimum Indoor Temperature Schedule
        Name`"""
        self["Minimum Indoor Temperature Schedule Name"] = value

    @property
    def maximum_indoor_temperature(self):
        """field `Maximum Indoor Temperature`

        |  This is the indoor temperature above which ventilation is shutoff.
        |  Units: C
        |  Default value: 100.0
        |  value >= -100.0
        |  value <= 100.0

        Args:
            value (float): value for IDD Field `Maximum Indoor Temperature`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `maximum_indoor_temperature` or None if not set

        """
        return self["Maximum Indoor Temperature"]

    @maximum_indoor_temperature.setter
    def maximum_indoor_temperature(self, value=100.0):
        """Corresponds to IDD field `Maximum Indoor Temperature`"""
        self["Maximum Indoor Temperature"] = value

    @property
    def maximum_indoor_temperature_schedule_name(self):
        """field `Maximum Indoor Temperature Schedule Name`

        |  This schedule contains the indoor temperature versus time above which
        |  ventilation is shutoff.

        Args:
            value (str): value for IDD Field `Maximum Indoor Temperature Schedule Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `maximum_indoor_temperature_schedule_name` or None if not set

        """
        return self["Maximum Indoor Temperature Schedule Name"]

    @maximum_indoor_temperature_schedule_name.setter
    def maximum_indoor_temperature_schedule_name(self, value=None):
        """Corresponds to IDD field `Maximum Indoor Temperature Schedule
        Name`"""
        self["Maximum Indoor Temperature Schedule Name"] = value

    @property
    def delta_temperature(self):
        """field `Delta Temperature`

        |  This is the temperature differential between indoor and outdoor below
        |  which ventilation is shutoff.
        |  Units: deltaC
        |  Default value: -100.0
        |  value >= -100.0

        Args:
            value (float): value for IDD Field `Delta Temperature`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `delta_temperature` or None if not set

        """
        return self["Delta Temperature"]

    @delta_temperature.setter
    def delta_temperature(self, value=-100.0):
        """Corresponds to IDD field `Delta Temperature`"""
        self["Delta Temperature"] = value

    @property
    def delta_temperature_schedule_name(self):
        """field `Delta Temperature Schedule Name`

        |  This schedule contains the temperature differential between indoor and outdoor
        |  versus time below which ventilation is shutoff.

        Args:
            value (str): value for IDD Field `Delta Temperature Schedule Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `delta_temperature_schedule_name` or None if not set

        """
        return self["Delta Temperature Schedule Name"]

    @delta_temperature_schedule_name.setter
    def delta_temperature_schedule_name(self, value=None):
        """Corresponds to IDD field `Delta Temperature Schedule Name`"""
        self["Delta Temperature Schedule Name"] = value

    @property
    def minimum_outdoor_temperature(self):
        """field `Minimum Outdoor Temperature`

        |  This is the outdoor temperature below which ventilation is shutoff.
        |  Units: C
        |  Default value: -100.0
        |  value >= -100.0
        |  value <= 100.0

        Args:
            value (float): value for IDD Field `Minimum Outdoor Temperature`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `minimum_outdoor_temperature` or None if not set

        """
        return self["Minimum Outdoor Temperature"]

    @minimum_outdoor_temperature.setter
    def minimum_outdoor_temperature(self, value=-100.0):
        """Corresponds to IDD field `Minimum Outdoor Temperature`"""
        self["Minimum Outdoor Temperature"] = value

    @property
    def minimum_outdoor_temperature_schedule_name(self):
        """field `Minimum Outdoor Temperature Schedule Name`

        |  This schedule contains the outdoor temperature versus time below which
        |  ventilation is shutoff.

        Args:
            value (str): value for IDD Field `Minimum Outdoor Temperature Schedule Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `minimum_outdoor_temperature_schedule_name` or None if not set

        """
        return self["Minimum Outdoor Temperature Schedule Name"]

    @minimum_outdoor_temperature_schedule_name.setter
    def minimum_outdoor_temperature_schedule_name(self, value=None):
        """Corresponds to IDD field `Minimum Outdoor Temperature Schedule
        Name`"""
        self["Minimum Outdoor Temperature Schedule Name"] = value

    @property
    def maximum_outdoor_temperature(self):
        """field `Maximum Outdoor Temperature`

        |  This is the outdoor temperature above which ventilation is shutoff.
        |  Units: C
        |  Default value: 100.0
        |  value >= -100.0
        |  value <= 100.0

        Args:
            value (float): value for IDD Field `Maximum Outdoor Temperature`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `maximum_outdoor_temperature` or None if not set

        """
        return self["Maximum Outdoor Temperature"]

    @maximum_outdoor_temperature.setter
    def maximum_outdoor_temperature(self, value=100.0):
        """Corresponds to IDD field `Maximum Outdoor Temperature`"""
        self["Maximum Outdoor Temperature"] = value

    @property
    def maximum_outdoor_temperature_schedule_name(self):
        """field `Maximum Outdoor Temperature Schedule Name`

        |  This schedule contains the outdoor temperature versus time above which
        |  ventilation is shutoff.

        Args:
            value (str): value for IDD Field `Maximum Outdoor Temperature Schedule Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `maximum_outdoor_temperature_schedule_name` or None if not set

        """
        return self["Maximum Outdoor Temperature Schedule Name"]

    @maximum_outdoor_temperature_schedule_name.setter
    def maximum_outdoor_temperature_schedule_name(self, value=None):
        """Corresponds to IDD field `Maximum Outdoor Temperature Schedule
        Name`"""
        self["Maximum Outdoor Temperature Schedule Name"] = value

    @property
    def maximum_wind_speed(self):
        """field `Maximum Wind Speed`

        |  This is the outdoor wind speed above which ventilation is shutoff.
        |  Units: m/s
        |  Default value: 40.0
        |  value <= 40.0

        Args:
            value (float): value for IDD Field `Maximum Wind Speed`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `maximum_wind_speed` or None if not set

        """
        return self["Maximum Wind Speed"]

    @maximum_wind_speed.setter
    def maximum_wind_speed(self, value=40.0):
        """Corresponds to IDD field `Maximum Wind Speed`"""
        self["Maximum Wind Speed"] = value




class ZoneAirBalanceOutdoorAir(DataObject):

    """ Corresponds to IDD object `ZoneAirBalance:OutdoorAir`
        Provide a combined zone outdoor air flow by including interactions between
        mechanical ventilation, infiltration and duct leakage.
        This object will combine outdoor flows from all ZoneInfiltration and
        ZoneVentilation objects in the same zone. Balanced flows will be summed, while
        unbalanced flows will be added in quadrature.
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
                                      (u'air balance method',
                                       {'name': u'Air Balance Method',
                                        'pyname': u'air_balance_method',
                                        'default': u'Quadrature',
                                        'required-field': False,
                                        'autosizable': False,
                                        'accepted-values': [u'Quadrature',
                                                            u'None'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'induced outdoor air due to unbalanced duct leakage',
                                       {'name': u'Induced Outdoor Air Due to Unbalanced Duct Leakage',
                                        'pyname': u'induced_outdoor_air_due_to_unbalanced_duct_leakage',
                                        'default': 0.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'm3/s'}),
                                      (u'induced outdoor air schedule name',
                                       {'name': u'Induced Outdoor Air Schedule Name',
                                        'pyname': u'induced_outdoor_air_schedule_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'})]),
               'format': None,
               'group': u'Zone Airflow',
               'min-fields': 0,
               'name': u'ZoneAirBalance:OutdoorAir',
               'pyname': u'ZoneAirBalanceOutdoorAir',
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
    def air_balance_method(self):
        """field `Air Balance Method`

        |  None: Only perform simple calculations without using a combined zone outdoor air.
        |  Quadrature: A combined outdoor air is used in the quadrature sum.
        |  Default value: Quadrature

        Args:
            value (str): value for IDD Field `Air Balance Method`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `air_balance_method` or None if not set

        """
        return self["Air Balance Method"]

    @air_balance_method.setter
    def air_balance_method(self, value="Quadrature"):
        """Corresponds to IDD field `Air Balance Method`"""
        self["Air Balance Method"] = value

    @property
    def induced_outdoor_air_due_to_unbalanced_duct_leakage(self):
        """field `Induced Outdoor Air Due to Unbalanced Duct Leakage`

        |  Units: m3/s

        Args:
            value (float): value for IDD Field `Induced Outdoor Air Due to Unbalanced Duct Leakage`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `induced_outdoor_air_due_to_unbalanced_duct_leakage` or None if not set

        """
        return self["Induced Outdoor Air Due to Unbalanced Duct Leakage"]

    @induced_outdoor_air_due_to_unbalanced_duct_leakage.setter
    def induced_outdoor_air_due_to_unbalanced_duct_leakage(self, value=None):
        """Corresponds to IDD field `Induced Outdoor Air Due to Unbalanced Duct
        Leakage`"""
        self["Induced Outdoor Air Due to Unbalanced Duct Leakage"] = value

    @property
    def induced_outdoor_air_schedule_name(self):
        """field `Induced Outdoor Air Schedule Name`

        |  This schedule contains the fraction values applied to the Induced Outdoor Air given in the
        |  previous input field (0.0 - 1.0).

        Args:
            value (str): value for IDD Field `Induced Outdoor Air Schedule Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `induced_outdoor_air_schedule_name` or None if not set

        """
        return self["Induced Outdoor Air Schedule Name"]

    @induced_outdoor_air_schedule_name.setter
    def induced_outdoor_air_schedule_name(self, value=None):
        """Corresponds to IDD field `Induced Outdoor Air Schedule Name`"""
        self["Induced Outdoor Air Schedule Name"] = value




class ZoneMixing(DataObject):

    """Corresponds to IDD object `ZoneMixing` ZoneMixing is a simple air
    exchange from one zone to another.

    Note that this statement only affects the energy balance of the
    "receiving" zone and will not produce any effect on the "source"
    zone. Mixing statements can be complementary and include multiple
    zones, but the balancing of flows between zones is left to the
    user's discretion.

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
                                      (u'design flow rate calculation method',
                                       {'name': u'Design Flow Rate Calculation Method',
                                        'pyname': u'design_flow_rate_calculation_method',
                                        'default': u'Flow/Zone',
                                        'required-field': True,
                                        'autosizable': False,
                                        'accepted-values': [u'Flow/Zone',
                                                            u'Flow/Area',
                                                            u'Flow/Person',
                                                            u'AirChanges/Hour'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'design flow rate',
                                       {'name': u'Design Flow Rate',
                                        'pyname': u'design_flow_rate',
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'm3/s'}),
                                      (u'flow rate per zone floor area',
                                       {'name': u'Flow Rate per Zone Floor Area',
                                        'pyname': u'flow_rate_per_zone_floor_area',
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'm3/s-m2'}),
                                      (u'flow rate per person',
                                       {'name': u'Flow Rate per Person',
                                        'pyname': u'flow_rate_per_person',
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'm3/s-person'}),
                                      (u'air changes per hour',
                                       {'name': u'Air Changes per Hour',
                                        'pyname': u'air_changes_per_hour',
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'1/hr'}),
                                      (u'source zone name',
                                       {'name': u'Source Zone Name',
                                        'pyname': u'source_zone_name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'delta temperature',
                                       {'name': u'Delta Temperature',
                                        'pyname': u'delta_temperature',
                                        'default': 0.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'deltaC'}),
                                      (u'delta temperature schedule name',
                                       {'name': u'Delta Temperature Schedule Name',
                                        'pyname': u'delta_temperature_schedule_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'minimum zone temperature schedule name',
                                       {'name': u'Minimum Zone Temperature Schedule Name',
                                        'pyname': u'minimum_zone_temperature_schedule_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'maximum zone temperature schedule name',
                                       {'name': u'Maximum Zone Temperature Schedule Name',
                                        'pyname': u'maximum_zone_temperature_schedule_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'minimum source zone temperature schedule name',
                                       {'name': u'Minimum Source Zone Temperature Schedule Name',
                                        'pyname': u'minimum_source_zone_temperature_schedule_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'maximum source zone temperature schedule name',
                                       {'name': u'Maximum Source Zone Temperature Schedule Name',
                                        'pyname': u'maximum_source_zone_temperature_schedule_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'minimum outdoor temperature schedule name',
                                       {'name': u'Minimum Outdoor Temperature Schedule Name',
                                        'pyname': u'minimum_outdoor_temperature_schedule_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'maximum outdoor temperature schedule name',
                                       {'name': u'Maximum Outdoor Temperature Schedule Name',
                                        'pyname': u'maximum_outdoor_temperature_schedule_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'})]),
               'format': None,
               'group': u'Zone Airflow',
               'min-fields': 9,
               'name': u'ZoneMixing',
               'pyname': u'ZoneMixing',
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
    def design_flow_rate_calculation_method(self):
        """field `Design Flow Rate Calculation Method`

        |  The entered calculation method is used to create the maximum amount of ventilation
        |  for this set of attributes
        |  Choices: Flow/Zone => Design Flow Rate -- simply enter Design Flow Rate
        |  Flow/Area => Flow Rate per Zone Floor Area - Value * Floor Area (zone) = Design Flow Rate
        |  Flow/Person => Flow Rate per Person - Value * #people = Design Flow Rate
        |  AirChanges/Hour => Air Changes per Hour - Value * Floor Volume (zone) adjusted for m3/s = Design Volume Flow Rate
        |  "Vdesign" in Equation is the result.
        |  Default value: Flow/Zone

        Args:
            value (str): value for IDD Field `Design Flow Rate Calculation Method`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `design_flow_rate_calculation_method` or None if not set

        """
        return self["Design Flow Rate Calculation Method"]

    @design_flow_rate_calculation_method.setter
    def design_flow_rate_calculation_method(self, value="Flow/Zone"):
        """Corresponds to IDD field `Design Flow Rate Calculation Method`"""
        self["Design Flow Rate Calculation Method"] = value

    @property
    def design_flow_rate(self):
        """field `Design Flow Rate`

        |  Units: m3/s

        Args:
            value (float): value for IDD Field `Design Flow Rate`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `design_flow_rate` or None if not set

        """
        return self["Design Flow Rate"]

    @design_flow_rate.setter
    def design_flow_rate(self, value=None):
        """Corresponds to IDD field `Design Flow Rate`"""
        self["Design Flow Rate"] = value

    @property
    def flow_rate_per_zone_floor_area(self):
        """field `Flow Rate per Zone Floor Area`

        |  Units: m3/s-m2

        Args:
            value (float): value for IDD Field `Flow Rate per Zone Floor Area`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `flow_rate_per_zone_floor_area` or None if not set

        """
        return self["Flow Rate per Zone Floor Area"]

    @flow_rate_per_zone_floor_area.setter
    def flow_rate_per_zone_floor_area(self, value=None):
        """Corresponds to IDD field `Flow Rate per Zone Floor Area`"""
        self["Flow Rate per Zone Floor Area"] = value

    @property
    def flow_rate_per_person(self):
        """field `Flow Rate per Person`

        |  Units: m3/s-person

        Args:
            value (float): value for IDD Field `Flow Rate per Person`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `flow_rate_per_person` or None if not set

        """
        return self["Flow Rate per Person"]

    @flow_rate_per_person.setter
    def flow_rate_per_person(self, value=None):
        """Corresponds to IDD field `Flow Rate per Person`"""
        self["Flow Rate per Person"] = value

    @property
    def air_changes_per_hour(self):
        """field `Air Changes per Hour`

        |  Units: 1/hr

        Args:
            value (float): value for IDD Field `Air Changes per Hour`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `air_changes_per_hour` or None if not set

        """
        return self["Air Changes per Hour"]

    @air_changes_per_hour.setter
    def air_changes_per_hour(self, value=None):
        """Corresponds to IDD field `Air Changes per Hour`"""
        self["Air Changes per Hour"] = value

    @property
    def source_zone_name(self):
        """field `Source Zone Name`

        Args:
            value (str): value for IDD Field `Source Zone Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `source_zone_name` or None if not set

        """
        return self["Source Zone Name"]

    @source_zone_name.setter
    def source_zone_name(self, value=None):
        """Corresponds to IDD field `Source Zone Name`"""
        self["Source Zone Name"] = value

    @property
    def delta_temperature(self):
        """field `Delta Temperature`

        |  This field contains the constant temperature differential between source and
        |  receiving zones below which mixing is shutoff.
        |  Units: deltaC

        Args:
            value (float): value for IDD Field `Delta Temperature`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `delta_temperature` or None if not set

        """
        return self["Delta Temperature"]

    @delta_temperature.setter
    def delta_temperature(self, value=None):
        """Corresponds to IDD field `Delta Temperature`"""
        self["Delta Temperature"] = value

    @property
    def delta_temperature_schedule_name(self):
        """field `Delta Temperature Schedule Name`

        |  This schedule contains the temperature differential between source and receiving
        |  zones versus time below which mixing is shutoff.

        Args:
            value (str): value for IDD Field `Delta Temperature Schedule Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `delta_temperature_schedule_name` or None if not set

        """
        return self["Delta Temperature Schedule Name"]

    @delta_temperature_schedule_name.setter
    def delta_temperature_schedule_name(self, value=None):
        """Corresponds to IDD field `Delta Temperature Schedule Name`"""
        self["Delta Temperature Schedule Name"] = value

    @property
    def minimum_zone_temperature_schedule_name(self):
        """field `Minimum Zone Temperature Schedule Name`

        |  This schedule contains the zone dry-bulb temperature versus time below which
        |  mixing is shutoff.

        Args:
            value (str): value for IDD Field `Minimum Zone Temperature Schedule Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `minimum_zone_temperature_schedule_name` or None if not set

        """
        return self["Minimum Zone Temperature Schedule Name"]

    @minimum_zone_temperature_schedule_name.setter
    def minimum_zone_temperature_schedule_name(self, value=None):
        """Corresponds to IDD field `Minimum Zone Temperature Schedule Name`"""
        self["Minimum Zone Temperature Schedule Name"] = value

    @property
    def maximum_zone_temperature_schedule_name(self):
        """field `Maximum Zone Temperature Schedule Name`

        |  This schedule contains the zone dry-bulb temperature versus time above which
        |  mixing is shutoff.

        Args:
            value (str): value for IDD Field `Maximum Zone Temperature Schedule Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `maximum_zone_temperature_schedule_name` or None if not set

        """
        return self["Maximum Zone Temperature Schedule Name"]

    @maximum_zone_temperature_schedule_name.setter
    def maximum_zone_temperature_schedule_name(self, value=None):
        """Corresponds to IDD field `Maximum Zone Temperature Schedule Name`"""
        self["Maximum Zone Temperature Schedule Name"] = value

    @property
    def minimum_source_zone_temperature_schedule_name(self):
        """field `Minimum Source Zone Temperature Schedule Name`

        |  This schedule contains the source zone dry-bulb temperature versus time below
        |  which mixing is shutoff.

        Args:
            value (str): value for IDD Field `Minimum Source Zone Temperature Schedule Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `minimum_source_zone_temperature_schedule_name` or None if not set

        """
        return self["Minimum Source Zone Temperature Schedule Name"]

    @minimum_source_zone_temperature_schedule_name.setter
    def minimum_source_zone_temperature_schedule_name(self, value=None):
        """Corresponds to IDD field `Minimum Source Zone Temperature Schedule
        Name`"""
        self["Minimum Source Zone Temperature Schedule Name"] = value

    @property
    def maximum_source_zone_temperature_schedule_name(self):
        """field `Maximum Source Zone Temperature Schedule Name`

        |  This schedule contains the source zone dry-bulb temperature versus time above
        |  which mixing is shutoff.

        Args:
            value (str): value for IDD Field `Maximum Source Zone Temperature Schedule Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `maximum_source_zone_temperature_schedule_name` or None if not set

        """
        return self["Maximum Source Zone Temperature Schedule Name"]

    @maximum_source_zone_temperature_schedule_name.setter
    def maximum_source_zone_temperature_schedule_name(self, value=None):
        """Corresponds to IDD field `Maximum Source Zone Temperature Schedule
        Name`"""
        self["Maximum Source Zone Temperature Schedule Name"] = value

    @property
    def minimum_outdoor_temperature_schedule_name(self):
        """field `Minimum Outdoor Temperature Schedule Name`

        |  This schedule contains the outdoor temperature versus time below which
        |  mixing is shutoff.

        Args:
            value (str): value for IDD Field `Minimum Outdoor Temperature Schedule Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `minimum_outdoor_temperature_schedule_name` or None if not set

        """
        return self["Minimum Outdoor Temperature Schedule Name"]

    @minimum_outdoor_temperature_schedule_name.setter
    def minimum_outdoor_temperature_schedule_name(self, value=None):
        """Corresponds to IDD field `Minimum Outdoor Temperature Schedule
        Name`"""
        self["Minimum Outdoor Temperature Schedule Name"] = value

    @property
    def maximum_outdoor_temperature_schedule_name(self):
        """field `Maximum Outdoor Temperature Schedule Name`

        |  This schedule contains the outdoor temperature versus time above which
        |  mixing is shutoff.

        Args:
            value (str): value for IDD Field `Maximum Outdoor Temperature Schedule Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `maximum_outdoor_temperature_schedule_name` or None if not set

        """
        return self["Maximum Outdoor Temperature Schedule Name"]

    @maximum_outdoor_temperature_schedule_name.setter
    def maximum_outdoor_temperature_schedule_name(self, value=None):
        """Corresponds to IDD field `Maximum Outdoor Temperature Schedule
        Name`"""
        self["Maximum Outdoor Temperature Schedule Name"] = value




class ZoneCrossMixing(DataObject):

    """Corresponds to IDD object `ZoneCrossMixing` ZoneCrossMixing exchanges an
    equal amount of air between two zones.

    Note that this statement affects the energy balance of both zones.

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
                                      (u'design flow rate calculation method',
                                       {'name': u'Design Flow Rate Calculation Method',
                                        'pyname': u'design_flow_rate_calculation_method',
                                        'default': u'Flow/Zone',
                                        'required-field': True,
                                        'autosizable': False,
                                        'accepted-values': [u'Flow/Zone',
                                                            u'Flow/Person',
                                                            u'Flow/Area',
                                                            u'AirChanges/Hour'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'design flow rate',
                                       {'name': u'Design Flow Rate',
                                        'pyname': u'design_flow_rate',
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'm3/s'}),
                                      (u'flow rate per zone floor area',
                                       {'name': u'Flow Rate per Zone Floor Area',
                                        'pyname': u'flow_rate_per_zone_floor_area',
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'm3/s-m2'}),
                                      (u'flow rate per person',
                                       {'name': u'Flow Rate per Person',
                                        'pyname': u'flow_rate_per_person',
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'm3/s-person'}),
                                      (u'air changes per hour',
                                       {'name': u'Air Changes per Hour',
                                        'pyname': u'air_changes_per_hour',
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'1/hr'}),
                                      (u'source zone name',
                                       {'name': u'Source Zone Name',
                                        'pyname': u'source_zone_name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'delta temperature',
                                       {'name': u'Delta Temperature',
                                        'pyname': u'delta_temperature',
                                        'default': 0.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'deltaC'}),
                                      (u'delta temperature schedule name',
                                       {'name': u'Delta Temperature Schedule Name',
                                        'pyname': u'delta_temperature_schedule_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'minimum zone temperature schedule name',
                                       {'name': u'Minimum Zone Temperature Schedule Name',
                                        'pyname': u'minimum_zone_temperature_schedule_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'maximum zone temperature schedule name',
                                       {'name': u'Maximum Zone Temperature Schedule Name',
                                        'pyname': u'maximum_zone_temperature_schedule_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'minimum source zone temperature schedule name',
                                       {'name': u'Minimum Source Zone Temperature Schedule Name',
                                        'pyname': u'minimum_source_zone_temperature_schedule_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'maximum source zone temperature schedule name',
                                       {'name': u'Maximum Source Zone Temperature Schedule Name',
                                        'pyname': u'maximum_source_zone_temperature_schedule_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'minimum outdoor temperature schedule name',
                                       {'name': u'Minimum Outdoor Temperature Schedule Name',
                                        'pyname': u'minimum_outdoor_temperature_schedule_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'maximum outdoor temperature schedule name',
                                       {'name': u'Maximum Outdoor Temperature Schedule Name',
                                        'pyname': u'maximum_outdoor_temperature_schedule_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'})]),
               'format': None,
               'group': u'Zone Airflow',
               'min-fields': 9,
               'name': u'ZoneCrossMixing',
               'pyname': u'ZoneCrossMixing',
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
    def design_flow_rate_calculation_method(self):
        """field `Design Flow Rate Calculation Method`

        |  The entered calculation method is used to create the maximum amount of ventilation
        |  for this set of attributes
        |  Choices: Flow/Zone => Design Flow Rate -- simply enter Design Flow Rate
        |  Flow/Area => Flow Rate per Zone Floor Area - Value * Floor Area (zone) = Design Flow Rate
        |  Flow/Person => Flow Rate per Person - Value * #people = Design Flow Rate
        |  AirChanges/Hour => Air Changes per Hour - Value * Floor Volume (zone) adjusted for m3/s = Design Volume Flow Rate
        |  "Vdesign" in Equation is the result.
        |  Default value: Flow/Zone

        Args:
            value (str): value for IDD Field `Design Flow Rate Calculation Method`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `design_flow_rate_calculation_method` or None if not set

        """
        return self["Design Flow Rate Calculation Method"]

    @design_flow_rate_calculation_method.setter
    def design_flow_rate_calculation_method(self, value="Flow/Zone"):
        """Corresponds to IDD field `Design Flow Rate Calculation Method`"""
        self["Design Flow Rate Calculation Method"] = value

    @property
    def design_flow_rate(self):
        """field `Design Flow Rate`

        |  Units: m3/s

        Args:
            value (float): value for IDD Field `Design Flow Rate`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `design_flow_rate` or None if not set

        """
        return self["Design Flow Rate"]

    @design_flow_rate.setter
    def design_flow_rate(self, value=None):
        """Corresponds to IDD field `Design Flow Rate`"""
        self["Design Flow Rate"] = value

    @property
    def flow_rate_per_zone_floor_area(self):
        """field `Flow Rate per Zone Floor Area`

        |  Units: m3/s-m2

        Args:
            value (float): value for IDD Field `Flow Rate per Zone Floor Area`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `flow_rate_per_zone_floor_area` or None if not set

        """
        return self["Flow Rate per Zone Floor Area"]

    @flow_rate_per_zone_floor_area.setter
    def flow_rate_per_zone_floor_area(self, value=None):
        """Corresponds to IDD field `Flow Rate per Zone Floor Area`"""
        self["Flow Rate per Zone Floor Area"] = value

    @property
    def flow_rate_per_person(self):
        """field `Flow Rate per Person`

        |  Units: m3/s-person

        Args:
            value (float): value for IDD Field `Flow Rate per Person`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `flow_rate_per_person` or None if not set

        """
        return self["Flow Rate per Person"]

    @flow_rate_per_person.setter
    def flow_rate_per_person(self, value=None):
        """Corresponds to IDD field `Flow Rate per Person`"""
        self["Flow Rate per Person"] = value

    @property
    def air_changes_per_hour(self):
        """field `Air Changes per Hour`

        |  Units: 1/hr

        Args:
            value (float): value for IDD Field `Air Changes per Hour`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `air_changes_per_hour` or None if not set

        """
        return self["Air Changes per Hour"]

    @air_changes_per_hour.setter
    def air_changes_per_hour(self, value=None):
        """Corresponds to IDD field `Air Changes per Hour`"""
        self["Air Changes per Hour"] = value

    @property
    def source_zone_name(self):
        """field `Source Zone Name`

        Args:
            value (str): value for IDD Field `Source Zone Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `source_zone_name` or None if not set

        """
        return self["Source Zone Name"]

    @source_zone_name.setter
    def source_zone_name(self, value=None):
        """Corresponds to IDD field `Source Zone Name`"""
        self["Source Zone Name"] = value

    @property
    def delta_temperature(self):
        """field `Delta Temperature`

        |  This field contains the constant temperature differential between source and
        |  receiving zones below which cross mixing is shutoff. This value must be greater
        |  than or equal to zero.
        |  Units: deltaC

        Args:
            value (float): value for IDD Field `Delta Temperature`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `delta_temperature` or None if not set

        """
        return self["Delta Temperature"]

    @delta_temperature.setter
    def delta_temperature(self, value=None):
        """Corresponds to IDD field `Delta Temperature`"""
        self["Delta Temperature"] = value

    @property
    def delta_temperature_schedule_name(self):
        """field `Delta Temperature Schedule Name`

        |  This schedule contains the temperature differential between source and receiving
        |  zones versus time below which cross mixing is shutoff.

        Args:
            value (str): value for IDD Field `Delta Temperature Schedule Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `delta_temperature_schedule_name` or None if not set

        """
        return self["Delta Temperature Schedule Name"]

    @delta_temperature_schedule_name.setter
    def delta_temperature_schedule_name(self, value=None):
        """Corresponds to IDD field `Delta Temperature Schedule Name`"""
        self["Delta Temperature Schedule Name"] = value

    @property
    def minimum_zone_temperature_schedule_name(self):
        """field `Minimum Zone Temperature Schedule Name`

        |  This schedule contains the indoor temperature versus time below which
        |  cross mixing is shutoff.

        Args:
            value (str): value for IDD Field `Minimum Zone Temperature Schedule Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `minimum_zone_temperature_schedule_name` or None if not set

        """
        return self["Minimum Zone Temperature Schedule Name"]

    @minimum_zone_temperature_schedule_name.setter
    def minimum_zone_temperature_schedule_name(self, value=None):
        """Corresponds to IDD field `Minimum Zone Temperature Schedule Name`"""
        self["Minimum Zone Temperature Schedule Name"] = value

    @property
    def maximum_zone_temperature_schedule_name(self):
        """field `Maximum Zone Temperature Schedule Name`

        |  This schedule contains the indoor temperature versus time above which
        |  cross mixing is shutoff.

        Args:
            value (str): value for IDD Field `Maximum Zone Temperature Schedule Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `maximum_zone_temperature_schedule_name` or None if not set

        """
        return self["Maximum Zone Temperature Schedule Name"]

    @maximum_zone_temperature_schedule_name.setter
    def maximum_zone_temperature_schedule_name(self, value=None):
        """Corresponds to IDD field `Maximum Zone Temperature Schedule Name`"""
        self["Maximum Zone Temperature Schedule Name"] = value

    @property
    def minimum_source_zone_temperature_schedule_name(self):
        """field `Minimum Source Zone Temperature Schedule Name`

        |  This schedule contains the source zone dry-bulb temperature versus time below
        |  which cross mixing is shutoff.

        Args:
            value (str): value for IDD Field `Minimum Source Zone Temperature Schedule Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `minimum_source_zone_temperature_schedule_name` or None if not set

        """
        return self["Minimum Source Zone Temperature Schedule Name"]

    @minimum_source_zone_temperature_schedule_name.setter
    def minimum_source_zone_temperature_schedule_name(self, value=None):
        """Corresponds to IDD field `Minimum Source Zone Temperature Schedule
        Name`"""
        self["Minimum Source Zone Temperature Schedule Name"] = value

    @property
    def maximum_source_zone_temperature_schedule_name(self):
        """field `Maximum Source Zone Temperature Schedule Name`

        |  This schedule contains the source zone dry-bulb temperature versus time above
        |  which cross mixing is shutoff.

        Args:
            value (str): value for IDD Field `Maximum Source Zone Temperature Schedule Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `maximum_source_zone_temperature_schedule_name` or None if not set

        """
        return self["Maximum Source Zone Temperature Schedule Name"]

    @maximum_source_zone_temperature_schedule_name.setter
    def maximum_source_zone_temperature_schedule_name(self, value=None):
        """Corresponds to IDD field `Maximum Source Zone Temperature Schedule
        Name`"""
        self["Maximum Source Zone Temperature Schedule Name"] = value

    @property
    def minimum_outdoor_temperature_schedule_name(self):
        """field `Minimum Outdoor Temperature Schedule Name`

        |  This schedule contains the outdoor temperature versus time below which
        |  cross mixing is shutoff.

        Args:
            value (str): value for IDD Field `Minimum Outdoor Temperature Schedule Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `minimum_outdoor_temperature_schedule_name` or None if not set

        """
        return self["Minimum Outdoor Temperature Schedule Name"]

    @minimum_outdoor_temperature_schedule_name.setter
    def minimum_outdoor_temperature_schedule_name(self, value=None):
        """Corresponds to IDD field `Minimum Outdoor Temperature Schedule
        Name`"""
        self["Minimum Outdoor Temperature Schedule Name"] = value

    @property
    def maximum_outdoor_temperature_schedule_name(self):
        """field `Maximum Outdoor Temperature Schedule Name`

        |  This schedule contains the outdoor temperature versus time above which
        |  cross mixing is shutoff.

        Args:
            value (str): value for IDD Field `Maximum Outdoor Temperature Schedule Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `maximum_outdoor_temperature_schedule_name` or None if not set

        """
        return self["Maximum Outdoor Temperature Schedule Name"]

    @maximum_outdoor_temperature_schedule_name.setter
    def maximum_outdoor_temperature_schedule_name(self, value=None):
        """Corresponds to IDD field `Maximum Outdoor Temperature Schedule
        Name`"""
        self["Maximum Outdoor Temperature Schedule Name"] = value




class ZoneRefrigerationDoorMixing(DataObject):

    """Corresponds to IDD object `ZoneRefrigerationDoorMixing` Refrigeration
    Door Mixing is used for an opening between two zones that are at the same
    elevation but have different air temperatures.

    In this case, the mixing air flow
    between the two zones is determined by the density difference between the two zones.
    This would typically be used between two zones in a refrigerated warehouse that are
    controlled at different temperatures.  It could also be used to model a door to a walk-in
    refrigerated space if that space were modeled as a zone instead of using the object Refrigeration:WalkIn.

    """
    _schema = {'extensible-fields': OrderedDict(),
               'fields': OrderedDict([(u'name',
                                       {'name': u'Name',
                                        'pyname': u'name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'alpha'}),
                                      (u'zone 1 name',
                                       {'name': u'Zone 1 Name',
                                        'pyname': u'zone_1_name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'zone 2 name',
                                       {'name': u'Zone 2 Name',
                                        'pyname': u'zone_2_name',
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
                                      (u'door height',
                                       {'name': u'Door Height',
                                        'pyname': u'door_height',
                                        'default': 3.0,
                                        'maximum': 50.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'm'}),
                                      (u'door area',
                                       {'name': u'Door Area',
                                        'pyname': u'door_area',
                                        'default': 9.0,
                                        'maximum': 400.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'm2'}),
                                      (u'door protection type',
                                       {'name': u'Door Protection Type',
                                        'pyname': u'door_protection_type',
                                        'default': u'None',
                                        'required-field': False,
                                        'autosizable': False,
                                        'accepted-values': [u'None',
                                                            u'AirCurtain',
                                                            u'StripCurtain'],
                                        'autocalculatable': False,
                                        'type': 'alpha'})]),
               'format': None,
               'group': u'Zone Airflow',
               'min-fields': 4,
               'name': u'ZoneRefrigerationDoorMixing',
               'pyname': u'ZoneRefrigerationDoorMixing',
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
    def zone_1_name(self):
        """field `Zone 1 Name`

        Args:
            value (str): value for IDD Field `Zone 1 Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `zone_1_name` or None if not set

        """
        return self["Zone 1 Name"]

    @zone_1_name.setter
    def zone_1_name(self, value=None):
        """Corresponds to IDD field `Zone 1 Name`"""
        self["Zone 1 Name"] = value

    @property
    def zone_2_name(self):
        """field `Zone 2 Name`

        Args:
            value (str): value for IDD Field `Zone 2 Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `zone_2_name` or None if not set

        """
        return self["Zone 2 Name"]

    @zone_2_name.setter
    def zone_2_name(self, value=None):
        """Corresponds to IDD field `Zone 2 Name`"""
        self["Zone 2 Name"] = value

    @property
    def schedule_name(self):
        """field `Schedule Name`

        |  This schedule defines the fraction of the time the refrigeration door is open
        |  For example, if the warehouse is closed at night and there are no door openings
        |  between two zones, the value for that time period would be 0.
        |  If doors were propped open, the value  over that time period would be 1.0
        |  If the doors were open about 20% of the time, the value over that period would be 0.2
        |  Schedule values must lie between 0 and 1.0

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
    def door_height(self):
        """field `Door Height`

        |  Units: m
        |  Default value: 3.0
        |  value <= 50.0

        Args:
            value (float): value for IDD Field `Door Height`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `door_height` or None if not set

        """
        return self["Door Height"]

    @door_height.setter
    def door_height(self, value=3.0):
        """Corresponds to IDD field `Door Height`"""
        self["Door Height"] = value

    @property
    def door_area(self):
        """field `Door Area`

        |  Units: m2
        |  Default value: 9.0
        |  value <= 400.0

        Args:
            value (float): value for IDD Field `Door Area`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `door_area` or None if not set

        """
        return self["Door Area"]

    @door_area.setter
    def door_area(self, value=9.0):
        """Corresponds to IDD field `Door Area`"""
        self["Door Area"] = value

    @property
    def door_protection_type(self):
        """field `Door Protection Type`

        |  Door protection can reduce the air flow through a refrigeration door
        |  The default value is "None"
        |  Choices: "None", "AirCurtain", and "StripCurtain"
        |  A strip curtain reduces the air flow more than an air curtain
        |  Default value: None

        Args:
            value (str): value for IDD Field `Door Protection Type`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `door_protection_type` or None if not set

        """
        return self["Door Protection Type"]

    @door_protection_type.setter
    def door_protection_type(self, value="None"):
        """Corresponds to IDD field `Door Protection Type`"""
        self["Door Protection Type"] = value




class ZoneEarthtube(DataObject):

    """ Corresponds to IDD object `ZoneEarthtube`
        Earth Tube is specified as a design level which is modified by a Schedule fraction, temperature difference and wind speed:
        Earthtube=Edesign * Fschedule * (A + B*|(Tzone-Todb)| + C*WindSpd + D * WindSpd**2)
    """
    _schema = {'extensible-fields': OrderedDict(),
               'fields': OrderedDict([(u'zone name',
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
                                      (u'design flow rate',
                                       {'name': u'Design Flow Rate',
                                        'pyname': u'design_flow_rate',
                                        'required-field': True,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'm3/s'}),
                                      (u'minimum zone temperature when cooling',
                                       {'name': u'Minimum Zone Temperature when Cooling',
                                        'pyname': u'minimum_zone_temperature_when_cooling',
                                        'maximum': 100.0,
                                        'required-field': True,
                                        'autosizable': False,
                                        'minimum': -100.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'C'}),
                                      (u'maximum zone temperature when heating',
                                       {'name': u'Maximum Zone Temperature when Heating',
                                        'pyname': u'maximum_zone_temperature_when_heating',
                                        'maximum': 100.0,
                                        'required-field': True,
                                        'autosizable': False,
                                        'minimum': -100.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'C'}),
                                      (u'delta temperature',
                                       {'name': u'Delta Temperature',
                                        'pyname': u'delta_temperature',
                                        'required-field': True,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'deltaC'}),
                                      (u'earthtube type',
                                       {'name': u'Earthtube Type',
                                        'pyname': u'earthtube_type',
                                        'default': u'Natural',
                                        'required-field': True,
                                        'autosizable': False,
                                        'accepted-values': [u'Natural',
                                                            u'Intake',
                                                            u'Exhaust'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'fan pressure rise',
                                       {'name': u'Fan Pressure Rise',
                                        'pyname': u'fan_pressure_rise',
                                        'default': 0.0,
                                        'required-field': True,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'Pa'}),
                                      (u'fan total efficiency',
                                       {'name': u'Fan Total Efficiency',
                                        'pyname': u'fan_total_efficiency',
                                        'default': 1.0,
                                        'minimum>': 0.0,
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'pipe radius',
                                       {'name': u'Pipe Radius',
                                        'pyname': u'pipe_radius',
                                        'default': 1.0,
                                        'minimum>': 0.0,
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'm'}),
                                      (u'pipe thickness',
                                       {'name': u'Pipe Thickness',
                                        'pyname': u'pipe_thickness',
                                        'default': 0.2,
                                        'minimum>': 0.0,
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'm'}),
                                      (u'pipe length',
                                       {'name': u'Pipe Length',
                                        'pyname': u'pipe_length',
                                        'default': 15.0,
                                        'minimum>': 0.0,
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'm'}),
                                      (u'pipe thermal conductivity',
                                       {'name': u'Pipe Thermal Conductivity',
                                        'pyname': u'pipe_thermal_conductivity',
                                        'default': 200.0,
                                        'minimum>': 0.0,
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'W/m-K'}),
                                      (u'pipe depth under ground surface',
                                       {'name': u'Pipe Depth Under Ground Surface',
                                        'pyname': u'pipe_depth_under_ground_surface',
                                        'default': 3.0,
                                        'minimum>': 0.0,
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'm'}),
                                      (u'soil condition',
                                       {'name': u'Soil Condition',
                                        'pyname': u'soil_condition',
                                        'default': u'HeavyAndDamp',
                                        'required-field': True,
                                        'autosizable': False,
                                        'accepted-values': [u'HeavyAndSaturated',
                                                            u'HeavyAndDamp',
                                                            u'HeavyAndDry',
                                                            u'LightAndDry'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'average soil surface temperature',
                                       {'name': u'Average Soil Surface Temperature',
                                        'pyname': u'average_soil_surface_temperature',
                                        'default': 0.0,
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'C'}),
                                      (u'amplitude of soil surface temperature',
                                       {'name': u'Amplitude of Soil Surface Temperature',
                                        'pyname': u'amplitude_of_soil_surface_temperature',
                                        'default': 0.0,
                                        'required-field': True,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'deltaC'}),
                                      (u'phase constant of soil surface temperature',
                                       {'name': u'Phase Constant of Soil Surface Temperature',
                                        'pyname': u'phase_constant_of_soil_surface_temperature',
                                        'default': 0.0,
                                        'required-field': True,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'days'}),
                                      (u'constant term flow coefficient',
                                       {'name': u'Constant Term Flow Coefficient',
                                        'pyname': u'constant_term_flow_coefficient',
                                        'default': 1.0,
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'temperature term flow coefficient',
                                       {'name': u'Temperature Term Flow Coefficient',
                                        'pyname': u'temperature_term_flow_coefficient',
                                        'default': 0.0,
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'velocity term flow coefficient',
                                       {'name': u'Velocity Term Flow Coefficient',
                                        'pyname': u'velocity_term_flow_coefficient',
                                        'default': 0.0,
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'velocity squared term flow coefficient',
                                       {'name': u'Velocity Squared Term Flow Coefficient',
                                        'pyname': u'velocity_squared_term_flow_coefficient',
                                        'default': 0.0,
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real'})]),
               'format': None,
               'group': u'Zone Airflow',
               'min-fields': 22,
               'name': u'ZoneEarthtube',
               'pyname': u'ZoneEarthtube',
               'required-object': False,
               'unique-object': False}

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
    def design_flow_rate(self):
        """field `Design Flow Rate`

        |  "Edesign" in Equation
        |  Units: m3/s

        Args:
            value (float): value for IDD Field `Design Flow Rate`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `design_flow_rate` or None if not set

        """
        return self["Design Flow Rate"]

    @design_flow_rate.setter
    def design_flow_rate(self, value=None):
        """Corresponds to IDD field `Design Flow Rate`"""
        self["Design Flow Rate"] = value

    @property
    def minimum_zone_temperature_when_cooling(self):
        """field `Minimum Zone Temperature when Cooling`

        |  this is the indoor temperature below which the earth tube is shut off
        |  Units: C
        |  value >= -100.0
        |  value <= 100.0

        Args:
            value (float): value for IDD Field `Minimum Zone Temperature when Cooling`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `minimum_zone_temperature_when_cooling` or None if not set

        """
        return self["Minimum Zone Temperature when Cooling"]

    @minimum_zone_temperature_when_cooling.setter
    def minimum_zone_temperature_when_cooling(self, value=None):
        """Corresponds to IDD field `Minimum Zone Temperature when Cooling`"""
        self["Minimum Zone Temperature when Cooling"] = value

    @property
    def maximum_zone_temperature_when_heating(self):
        """field `Maximum Zone Temperature when Heating`

        |  this is the indoor temperature above which the earth tube is shut off
        |  Units: C
        |  value >= -100.0
        |  value <= 100.0

        Args:
            value (float): value for IDD Field `Maximum Zone Temperature when Heating`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `maximum_zone_temperature_when_heating` or None if not set

        """
        return self["Maximum Zone Temperature when Heating"]

    @maximum_zone_temperature_when_heating.setter
    def maximum_zone_temperature_when_heating(self, value=None):
        """Corresponds to IDD field `Maximum Zone Temperature when Heating`"""
        self["Maximum Zone Temperature when Heating"] = value

    @property
    def delta_temperature(self):
        """field `Delta Temperature`

        |  This is the temperature difference between indoor and outdoor below which the earth tube is shut off
        |  Units: deltaC

        Args:
            value (float): value for IDD Field `Delta Temperature`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `delta_temperature` or None if not set

        """
        return self["Delta Temperature"]

    @delta_temperature.setter
    def delta_temperature(self, value=None):
        """Corresponds to IDD field `Delta Temperature`"""
        self["Delta Temperature"] = value

    @property
    def earthtube_type(self):
        """field `Earthtube Type`

        |  Default value: Natural

        Args:
            value (str): value for IDD Field `Earthtube Type`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `earthtube_type` or None if not set

        """
        return self["Earthtube Type"]

    @earthtube_type.setter
    def earthtube_type(self, value="Natural"):
        """Corresponds to IDD field `Earthtube Type`"""
        self["Earthtube Type"] = value

    @property
    def fan_pressure_rise(self):
        """field `Fan Pressure Rise`

        |  pressure rise across the fan
        |  Units: Pa

        Args:
            value (float): value for IDD Field `Fan Pressure Rise`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `fan_pressure_rise` or None if not set

        """
        return self["Fan Pressure Rise"]

    @fan_pressure_rise.setter
    def fan_pressure_rise(self, value=None):
        """Corresponds to IDD field `Fan Pressure Rise`"""
        self["Fan Pressure Rise"] = value

    @property
    def fan_total_efficiency(self):
        """field `Fan Total Efficiency`

        |  Default value: 1.0

        Args:
            value (float): value for IDD Field `Fan Total Efficiency`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `fan_total_efficiency` or None if not set

        """
        return self["Fan Total Efficiency"]

    @fan_total_efficiency.setter
    def fan_total_efficiency(self, value=1.0):
        """Corresponds to IDD field `Fan Total Efficiency`"""
        self["Fan Total Efficiency"] = value

    @property
    def pipe_radius(self):
        """field `Pipe Radius`

        |  Units: m
        |  Default value: 1.0

        Args:
            value (float): value for IDD Field `Pipe Radius`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `pipe_radius` or None if not set

        """
        return self["Pipe Radius"]

    @pipe_radius.setter
    def pipe_radius(self, value=1.0):
        """Corresponds to IDD field `Pipe Radius`"""
        self["Pipe Radius"] = value

    @property
    def pipe_thickness(self):
        """field `Pipe Thickness`

        |  Units: m
        |  Default value: 0.2

        Args:
            value (float): value for IDD Field `Pipe Thickness`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `pipe_thickness` or None if not set

        """
        return self["Pipe Thickness"]

    @pipe_thickness.setter
    def pipe_thickness(self, value=0.2):
        """Corresponds to IDD field `Pipe Thickness`"""
        self["Pipe Thickness"] = value

    @property
    def pipe_length(self):
        """field `Pipe Length`

        |  Units: m
        |  Default value: 15.0

        Args:
            value (float): value for IDD Field `Pipe Length`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `pipe_length` or None if not set

        """
        return self["Pipe Length"]

    @pipe_length.setter
    def pipe_length(self, value=15.0):
        """Corresponds to IDD field `Pipe Length`"""
        self["Pipe Length"] = value

    @property
    def pipe_thermal_conductivity(self):
        """field `Pipe Thermal Conductivity`

        |  Units: W/m-K
        |  Default value: 200.0

        Args:
            value (float): value for IDD Field `Pipe Thermal Conductivity`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `pipe_thermal_conductivity` or None if not set

        """
        return self["Pipe Thermal Conductivity"]

    @pipe_thermal_conductivity.setter
    def pipe_thermal_conductivity(self, value=200.0):
        """Corresponds to IDD field `Pipe Thermal Conductivity`"""
        self["Pipe Thermal Conductivity"] = value

    @property
    def pipe_depth_under_ground_surface(self):
        """field `Pipe Depth Under Ground Surface`

        |  Units: m
        |  Default value: 3.0

        Args:
            value (float): value for IDD Field `Pipe Depth Under Ground Surface`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `pipe_depth_under_ground_surface` or None if not set

        """
        return self["Pipe Depth Under Ground Surface"]

    @pipe_depth_under_ground_surface.setter
    def pipe_depth_under_ground_surface(self, value=3.0):
        """Corresponds to IDD field `Pipe Depth Under Ground Surface`"""
        self["Pipe Depth Under Ground Surface"] = value

    @property
    def soil_condition(self):
        """field `Soil Condition`

        |  Default value: HeavyAndDamp

        Args:
            value (str): value for IDD Field `Soil Condition`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `soil_condition` or None if not set

        """
        return self["Soil Condition"]

    @soil_condition.setter
    def soil_condition(self, value="HeavyAndDamp"):
        """Corresponds to IDD field `Soil Condition`"""
        self["Soil Condition"] = value

    @property
    def average_soil_surface_temperature(self):
        """field `Average Soil Surface Temperature`

        |  Units: C

        Args:
            value (float): value for IDD Field `Average Soil Surface Temperature`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `average_soil_surface_temperature` or None if not set

        """
        return self["Average Soil Surface Temperature"]

    @average_soil_surface_temperature.setter
    def average_soil_surface_temperature(self, value=None):
        """Corresponds to IDD field `Average Soil Surface Temperature`"""
        self["Average Soil Surface Temperature"] = value

    @property
    def amplitude_of_soil_surface_temperature(self):
        """field `Amplitude of Soil Surface Temperature`

        |  Units: deltaC

        Args:
            value (float): value for IDD Field `Amplitude of Soil Surface Temperature`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `amplitude_of_soil_surface_temperature` or None if not set

        """
        return self["Amplitude of Soil Surface Temperature"]

    @amplitude_of_soil_surface_temperature.setter
    def amplitude_of_soil_surface_temperature(self, value=None):
        """Corresponds to IDD field `Amplitude of Soil Surface Temperature`"""
        self["Amplitude of Soil Surface Temperature"] = value

    @property
    def phase_constant_of_soil_surface_temperature(self):
        """field `Phase Constant of Soil Surface Temperature`

        |  Units: days

        Args:
            value (float): value for IDD Field `Phase Constant of Soil Surface Temperature`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `phase_constant_of_soil_surface_temperature` or None if not set

        """
        return self["Phase Constant of Soil Surface Temperature"]

    @phase_constant_of_soil_surface_temperature.setter
    def phase_constant_of_soil_surface_temperature(self, value=None):
        """Corresponds to IDD field `Phase Constant of Soil Surface
        Temperature`"""
        self["Phase Constant of Soil Surface Temperature"] = value

    @property
    def constant_term_flow_coefficient(self):
        """field `Constant Term Flow Coefficient`

        |  "A" in Equation
        |  Default value: 1.0

        Args:
            value (float): value for IDD Field `Constant Term Flow Coefficient`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `constant_term_flow_coefficient` or None if not set

        """
        return self["Constant Term Flow Coefficient"]

    @constant_term_flow_coefficient.setter
    def constant_term_flow_coefficient(self, value=1.0):
        """Corresponds to IDD field `Constant Term Flow Coefficient`"""
        self["Constant Term Flow Coefficient"] = value

    @property
    def temperature_term_flow_coefficient(self):
        """field `Temperature Term Flow Coefficient`

        |  "B" in Equation

        Args:
            value (float): value for IDD Field `Temperature Term Flow Coefficient`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `temperature_term_flow_coefficient` or None if not set

        """
        return self["Temperature Term Flow Coefficient"]

    @temperature_term_flow_coefficient.setter
    def temperature_term_flow_coefficient(self, value=None):
        """Corresponds to IDD field `Temperature Term Flow Coefficient`"""
        self["Temperature Term Flow Coefficient"] = value

    @property
    def velocity_term_flow_coefficient(self):
        """field `Velocity Term Flow Coefficient`

        |  "C" in Equation

        Args:
            value (float): value for IDD Field `Velocity Term Flow Coefficient`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `velocity_term_flow_coefficient` or None if not set

        """
        return self["Velocity Term Flow Coefficient"]

    @velocity_term_flow_coefficient.setter
    def velocity_term_flow_coefficient(self, value=None):
        """Corresponds to IDD field `Velocity Term Flow Coefficient`"""
        self["Velocity Term Flow Coefficient"] = value

    @property
    def velocity_squared_term_flow_coefficient(self):
        """field `Velocity Squared Term Flow Coefficient`

        |  "D" in Equation

        Args:
            value (float): value for IDD Field `Velocity Squared Term Flow Coefficient`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `velocity_squared_term_flow_coefficient` or None if not set

        """
        return self["Velocity Squared Term Flow Coefficient"]

    @velocity_squared_term_flow_coefficient.setter
    def velocity_squared_term_flow_coefficient(self, value=None):
        """Corresponds to IDD field `Velocity Squared Term Flow Coefficient`"""
        self["Velocity Squared Term Flow Coefficient"] = value




class ZoneCoolTowerShower(DataObject):

    """ Corresponds to IDD object `ZoneCoolTower:Shower`
        A cooltower (sometimes referred to as a wind tower or a shower cooling tower)
        models passive downdraught evaporative cooling (PDEC) that is designed to capture the
        wind at the top of a tower and cool the outdoor air using water evaporation before
        delivering it to a space.
    """
    _schema = {'extensible-fields': OrderedDict(),
               'fields': OrderedDict([(u'name',
                                       {'name': u'Name',
                                        'pyname': u'name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'availability schedule name',
                                       {'name': u'Availability Schedule Name',
                                        'pyname': u'availability_schedule_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'zone name',
                                       {'name': u'Zone Name',
                                        'pyname': u'zone_name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'water supply storage tank name',
                                       {'name': u'Water Supply Storage Tank Name',
                                        'pyname': u'water_supply_storage_tank_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'flow control type',
                                       {'name': u'Flow Control Type',
                                        'pyname': u'flow_control_type',
                                        'default': u'WindDrivenFlow',
                                        'required-field': False,
                                        'autosizable': False,
                                        'accepted-values': [u'WaterFlowSchedule',
                                                            u'WindDrivenFlow'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'pump flow rate schedule name',
                                       {'name': u'Pump Flow Rate Schedule Name',
                                        'pyname': u'pump_flow_rate_schedule_name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'maximum water flow rate',
                                       {'name': u'Maximum Water Flow Rate',
                                        'pyname': u'maximum_water_flow_rate',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'm3/s'}),
                                      (u'effective tower height',
                                       {'name': u'Effective Tower Height',
                                        'pyname': u'effective_tower_height',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'm'}),
                                      (u'airflow outlet area',
                                       {'name': u'Airflow Outlet Area',
                                        'pyname': u'airflow_outlet_area',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'm2'}),
                                      (u'maximum air flow rate',
                                       {'name': u'Maximum Air Flow Rate',
                                        'pyname': u'maximum_air_flow_rate',
                                        'required-field': True,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'm3/s'}),
                                      (u'minimum indoor temperature',
                                       {'name': u'Minimum Indoor Temperature',
                                        'pyname': u'minimum_indoor_temperature',
                                        'maximum': 100.0,
                                        'required-field': True,
                                        'autosizable': False,
                                        'minimum': -100.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'C'}),
                                      (u'fraction of water loss',
                                       {'name': u'Fraction of Water Loss',
                                        'pyname': u'fraction_of_water_loss',
                                        'maximum': 1.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': 'real'}),
                                      (u'fraction of flow schedule',
                                       {'name': u'Fraction of Flow Schedule',
                                        'pyname': u'fraction_of_flow_schedule',
                                        'maximum': 1.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': 'real'}),
                                      (u'rated power consumption',
                                       {'name': u'Rated Power Consumption',
                                        'pyname': u'rated_power_consumption',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'W'})]),
               'format': None,
               'group': u'Zone Airflow',
               'min-fields': 0,
               'name': u'ZoneCoolTower:Shower',
               'pyname': u'ZoneCoolTowerShower',
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
    def availability_schedule_name(self):
        """field `Availability Schedule Name`

        |  Availability schedule name for this system. Schedule value > 0 means the system is available.
        |  If this field is blank, the system is always available.

        Args:
            value (str): value for IDD Field `Availability Schedule Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `availability_schedule_name` or None if not set

        """
        return self["Availability Schedule Name"]

    @availability_schedule_name.setter
    def availability_schedule_name(self, value=None):
        """Corresponds to IDD field `Availability Schedule Name`"""
        self["Availability Schedule Name"] = value

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
    def water_supply_storage_tank_name(self):
        """field `Water Supply Storage Tank Name`

        |  In case of stand alone tank or underground water, leave this input blank

        Args:
            value (str): value for IDD Field `Water Supply Storage Tank Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `water_supply_storage_tank_name` or None if not set

        """
        return self["Water Supply Storage Tank Name"]

    @water_supply_storage_tank_name.setter
    def water_supply_storage_tank_name(self, value=None):
        """Corresponds to IDD field `Water Supply Storage Tank Name`"""
        self["Water Supply Storage Tank Name"] = value

    @property
    def flow_control_type(self):
        """field `Flow Control Type`

        |  Water flow schedule should be selected when the water flow rate is known.
        |  Wind-driven flow should be selected when the water flow rate is unknown.
        |  Default value: WindDrivenFlow

        Args:
            value (str): value for IDD Field `Flow Control Type`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `flow_control_type` or None if not set

        """
        return self["Flow Control Type"]

    @flow_control_type.setter
    def flow_control_type(self, value="WindDrivenFlow"):
        """Corresponds to IDD field `Flow Control Type`"""
        self["Flow Control Type"] = value

    @property
    def pump_flow_rate_schedule_name(self):
        """field `Pump Flow Rate Schedule Name`

        Args:
            value (str): value for IDD Field `Pump Flow Rate Schedule Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `pump_flow_rate_schedule_name` or None if not set

        """
        return self["Pump Flow Rate Schedule Name"]

    @pump_flow_rate_schedule_name.setter
    def pump_flow_rate_schedule_name(self, value=None):
        """Corresponds to IDD field `Pump Flow Rate Schedule Name`"""
        self["Pump Flow Rate Schedule Name"] = value

    @property
    def maximum_water_flow_rate(self):
        """field `Maximum Water Flow Rate`

        |  Units: m3/s

        Args:
            value (float): value for IDD Field `Maximum Water Flow Rate`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `maximum_water_flow_rate` or None if not set

        """
        return self["Maximum Water Flow Rate"]

    @maximum_water_flow_rate.setter
    def maximum_water_flow_rate(self, value=None):
        """Corresponds to IDD field `Maximum Water Flow Rate`"""
        self["Maximum Water Flow Rate"] = value

    @property
    def effective_tower_height(self):
        """field `Effective Tower Height`

        |  This field is from either the spray or the wet pad to the top of the outlet.
        |  Units: m

        Args:
            value (float): value for IDD Field `Effective Tower Height`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `effective_tower_height` or None if not set

        """
        return self["Effective Tower Height"]

    @effective_tower_height.setter
    def effective_tower_height(self, value=None):
        """Corresponds to IDD field `Effective Tower Height`"""
        self["Effective Tower Height"] = value

    @property
    def airflow_outlet_area(self):
        """field `Airflow Outlet Area`

        |  User have to specify effective area when outlet area is relatively bigger than the cross sectional area
        |  of cooltower. If the number of outlet is more than one, assume the air passes through only one.
        |  Units: m2

        Args:
            value (float): value for IDD Field `Airflow Outlet Area`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `airflow_outlet_area` or None if not set

        """
        return self["Airflow Outlet Area"]

    @airflow_outlet_area.setter
    def airflow_outlet_area(self, value=None):
        """Corresponds to IDD field `Airflow Outlet Area`"""
        self["Airflow Outlet Area"] = value

    @property
    def maximum_air_flow_rate(self):
        """field `Maximum Air Flow Rate`

        |  Units: m3/s

        Args:
            value (float): value for IDD Field `Maximum Air Flow Rate`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `maximum_air_flow_rate` or None if not set

        """
        return self["Maximum Air Flow Rate"]

    @maximum_air_flow_rate.setter
    def maximum_air_flow_rate(self, value=None):
        """Corresponds to IDD field `Maximum Air Flow Rate`"""
        self["Maximum Air Flow Rate"] = value

    @property
    def minimum_indoor_temperature(self):
        """field `Minimum Indoor Temperature`

        |  This field is to specify the indoor temperature below which cooltower is shutoff.
        |  Units: C
        |  value >= -100.0
        |  value <= 100.0

        Args:
            value (float): value for IDD Field `Minimum Indoor Temperature`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `minimum_indoor_temperature` or None if not set

        """
        return self["Minimum Indoor Temperature"]

    @minimum_indoor_temperature.setter
    def minimum_indoor_temperature(self, value=None):
        """Corresponds to IDD field `Minimum Indoor Temperature`"""
        self["Minimum Indoor Temperature"] = value

    @property
    def fraction_of_water_loss(self):
        """field `Fraction of Water Loss`

        |  value <= 1.0

        Args:
            value (float): value for IDD Field `Fraction of Water Loss`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `fraction_of_water_loss` or None if not set

        """
        return self["Fraction of Water Loss"]

    @fraction_of_water_loss.setter
    def fraction_of_water_loss(self, value=None):
        """Corresponds to IDD field `Fraction of Water Loss`"""
        self["Fraction of Water Loss"] = value

    @property
    def fraction_of_flow_schedule(self):
        """field `Fraction of Flow Schedule`

        |  value <= 1.0

        Args:
            value (float): value for IDD Field `Fraction of Flow Schedule`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `fraction_of_flow_schedule` or None if not set

        """
        return self["Fraction of Flow Schedule"]

    @fraction_of_flow_schedule.setter
    def fraction_of_flow_schedule(self, value=None):
        """Corresponds to IDD field `Fraction of Flow Schedule`"""
        self["Fraction of Flow Schedule"] = value

    @property
    def rated_power_consumption(self):
        """field `Rated Power Consumption`

        |  Units: W

        Args:
            value (float): value for IDD Field `Rated Power Consumption`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `rated_power_consumption` or None if not set

        """
        return self["Rated Power Consumption"]

    @rated_power_consumption.setter
    def rated_power_consumption(self, value=None):
        """Corresponds to IDD field `Rated Power Consumption`"""
        self["Rated Power Consumption"] = value




class ZoneThermalChimney(DataObject):

    """Corresponds to IDD object `ZoneThermalChimney` A thermal chimney is a
    vertical shaft utilizing solar radiation to enhance natural ventilation.

    It consists of an absorber wall, air gap and glass cover with high
    solar transmissivity.

    """
    _schema = {'extensible-fields': OrderedDict(),
               'fields': OrderedDict([(u'name',
                                       {'name': u'Name',
                                        'pyname': u'name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'zone name',
                                       {'name': u'Zone Name',
                                        'pyname': u'zone_name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'availability schedule name',
                                       {'name': u'Availability Schedule Name',
                                        'pyname': u'availability_schedule_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'width of the absorber wall',
                                       {'name': u'Width of the Absorber Wall',
                                        'pyname': u'width_of_the_absorber_wall',
                                        'required-field': True,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'm'}),
                                      (u'cross sectional area of air channel outlet',
                                       {'name': u'Cross Sectional Area of Air Channel Outlet',
                                        'pyname': u'cross_sectional_area_of_air_channel_outlet',
                                        'required-field': True,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'm2'}),
                                      (u'discharge coefficient',
                                       {'name': u'Discharge Coefficient',
                                        'pyname': u'discharge_coefficient',
                                        'default': 0.8,
                                        'maximum': 1.0,
                                        'required-field': True,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'zone 1 name',
                                       {'name': u'Zone 1 Name',
                                        'pyname': u'zone_1_name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'distance from top of thermal chimney to inlet 1',
                                       {'name': u'Distance from Top of Thermal Chimney to Inlet 1',
                                        'pyname': u'distance_from_top_of_thermal_chimney_to_inlet_1',
                                        'required-field': True,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'm'}),
                                      (u'relative ratios of air flow rates passing through zone 1',
                                       {'name': u'Relative Ratios of Air Flow Rates Passing through Zone 1',
                                        'pyname': u'relative_ratios_of_air_flow_rates_passing_through_zone_1',
                                        'default': 1.0,
                                        'maximum': 1.0,
                                        'required-field': True,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'cross sectional areas of air channel inlet 1',
                                       {'name': u'Cross Sectional Areas of Air Channel Inlet 1',
                                        'pyname': u'cross_sectional_areas_of_air_channel_inlet_1',
                                        'required-field': True,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'm2'}),
                                      (u'zone 2 name',
                                       {'name': u'Zone 2 Name',
                                        'pyname': u'zone_2_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'distance from top of thermal chimney to inlet 2',
                                       {'name': u'Distance from Top of Thermal Chimney to Inlet 2',
                                        'pyname': u'distance_from_top_of_thermal_chimney_to_inlet_2',
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'm'}),
                                      (u'relative ratios of air flow rates passing through zone 2',
                                       {'name': u'Relative Ratios of Air Flow Rates Passing through Zone 2',
                                        'pyname': u'relative_ratios_of_air_flow_rates_passing_through_zone_2',
                                        'maximum': 1.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'cross sectional areas of air channel inlet 2',
                                       {'name': u'Cross Sectional Areas of Air Channel Inlet 2',
                                        'pyname': u'cross_sectional_areas_of_air_channel_inlet_2',
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'm2'}),
                                      (u'zone 3 name',
                                       {'name': u'Zone 3 Name',
                                        'pyname': u'zone_3_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'distance from top of thermal chimney to inlet 3',
                                       {'name': u'Distance from Top of Thermal Chimney to Inlet 3',
                                        'pyname': u'distance_from_top_of_thermal_chimney_to_inlet_3',
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'm'}),
                                      (u'relative ratios of air flow rates passing through zone 3',
                                       {'name': u'Relative Ratios of Air Flow Rates Passing through Zone 3',
                                        'pyname': u'relative_ratios_of_air_flow_rates_passing_through_zone_3',
                                        'maximum': 1.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'cross sectional areas of air channel inlet 3',
                                       {'name': u'Cross Sectional Areas of Air Channel Inlet 3',
                                        'pyname': u'cross_sectional_areas_of_air_channel_inlet_3',
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'm2'}),
                                      (u'zone 4 name',
                                       {'name': u'Zone 4 Name',
                                        'pyname': u'zone_4_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'distance from top of thermal chimney to inlet 4',
                                       {'name': u'Distance from Top of Thermal Chimney to Inlet 4',
                                        'pyname': u'distance_from_top_of_thermal_chimney_to_inlet_4',
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'm'}),
                                      (u'relative ratios of air flow rates passing through zone 4',
                                       {'name': u'Relative Ratios of Air Flow Rates Passing through Zone 4',
                                        'pyname': u'relative_ratios_of_air_flow_rates_passing_through_zone_4',
                                        'maximum': 1.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'cross sectional areas of air channel inlet 4',
                                       {'name': u'Cross Sectional Areas of Air Channel Inlet 4',
                                        'pyname': u'cross_sectional_areas_of_air_channel_inlet_4',
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'm2'}),
                                      (u'zone 5 name',
                                       {'name': u'Zone 5 Name',
                                        'pyname': u'zone_5_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'distance from top of thermal chimney to inlet 5',
                                       {'name': u'Distance from Top of Thermal Chimney to Inlet 5',
                                        'pyname': u'distance_from_top_of_thermal_chimney_to_inlet_5',
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'm'}),
                                      (u'relative ratios of air flow rates passing through zone 5',
                                       {'name': u'Relative Ratios of Air Flow Rates Passing through Zone 5',
                                        'pyname': u'relative_ratios_of_air_flow_rates_passing_through_zone_5',
                                        'maximum': 1.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'cross sectional areas of air channel inlet 5',
                                       {'name': u'Cross Sectional Areas of Air Channel Inlet 5',
                                        'pyname': u'cross_sectional_areas_of_air_channel_inlet_5',
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'm2'}),
                                      (u'zone 6 name',
                                       {'name': u'Zone 6 Name',
                                        'pyname': u'zone_6_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'distance from top of thermal chimney to inlet 6',
                                       {'name': u'Distance from Top of Thermal Chimney to Inlet 6',
                                        'pyname': u'distance_from_top_of_thermal_chimney_to_inlet_6',
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'm'}),
                                      (u'relative ratios of air flow rates passing through zone 6',
                                       {'name': u'Relative Ratios of Air Flow Rates Passing through Zone 6',
                                        'pyname': u'relative_ratios_of_air_flow_rates_passing_through_zone_6',
                                        'maximum': 1.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'cross sectional areas of air channel inlet 6',
                                       {'name': u'Cross Sectional Areas of Air Channel Inlet 6',
                                        'pyname': u'cross_sectional_areas_of_air_channel_inlet_6',
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'm2'}),
                                      (u'zone 7 name',
                                       {'name': u'Zone 7 Name',
                                        'pyname': u'zone_7_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'distance from top of thermal chimney to inlet 7',
                                       {'name': u'Distance from Top of Thermal Chimney to Inlet 7',
                                        'pyname': u'distance_from_top_of_thermal_chimney_to_inlet_7',
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'm'}),
                                      (u'relative ratios of air flow rates passing through zone 7',
                                       {'name': u'Relative Ratios of Air Flow Rates Passing through Zone 7',
                                        'pyname': u'relative_ratios_of_air_flow_rates_passing_through_zone_7',
                                        'maximum': 1.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'cross sectional areas of air channel inlet 7',
                                       {'name': u'Cross Sectional Areas of Air Channel Inlet 7',
                                        'pyname': u'cross_sectional_areas_of_air_channel_inlet_7',
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'm2'}),
                                      (u'zone 8 name',
                                       {'name': u'Zone 8 Name',
                                        'pyname': u'zone_8_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'distance from top of thermal chimney to inlet 8',
                                       {'name': u'Distance from Top of Thermal Chimney to Inlet 8',
                                        'pyname': u'distance_from_top_of_thermal_chimney_to_inlet_8',
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'm'}),
                                      (u'relative ratios of air flow rates passing through zone 8',
                                       {'name': u'Relative Ratios of Air Flow Rates Passing through Zone 8',
                                        'pyname': u'relative_ratios_of_air_flow_rates_passing_through_zone_8',
                                        'maximum': 1.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'cross sectional areas of air channel inlet 8',
                                       {'name': u'Cross Sectional Areas of Air Channel Inlet 8',
                                        'pyname': u'cross_sectional_areas_of_air_channel_inlet_8',
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'm2'}),
                                      (u'zone 9 name',
                                       {'name': u'Zone 9 Name',
                                        'pyname': u'zone_9_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'distance from top of thermal chimney to inlet 9',
                                       {'name': u'Distance from Top of Thermal Chimney to Inlet 9',
                                        'pyname': u'distance_from_top_of_thermal_chimney_to_inlet_9',
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'm'}),
                                      (u'relative ratios of air flow rates passing through zone 9',
                                       {'name': u'Relative Ratios of Air Flow Rates Passing through Zone 9',
                                        'pyname': u'relative_ratios_of_air_flow_rates_passing_through_zone_9',
                                        'maximum': 1.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'cross sectional areas of air channel inlet 9',
                                       {'name': u'Cross Sectional Areas of Air Channel Inlet 9',
                                        'pyname': u'cross_sectional_areas_of_air_channel_inlet_9',
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'm2'}),
                                      (u'zone 10 name',
                                       {'name': u'Zone 10 Name',
                                        'pyname': u'zone_10_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'distance from top of thermal chimney to inlet 10',
                                       {'name': u'Distance from Top of Thermal Chimney to Inlet 10',
                                        'pyname': u'distance_from_top_of_thermal_chimney_to_inlet_10',
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'm'}),
                                      (u'relative ratios of air flow rates passing through zone 10',
                                       {'name': u'Relative Ratios of Air Flow Rates Passing through Zone 10',
                                        'pyname': u'relative_ratios_of_air_flow_rates_passing_through_zone_10',
                                        'maximum': 1.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'cross sectional areas of air channel inlet 10',
                                       {'name': u'Cross Sectional Areas of Air Channel Inlet 10',
                                        'pyname': u'cross_sectional_areas_of_air_channel_inlet_10',
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'm2'}),
                                      (u'zone 11 name',
                                       {'name': u'Zone 11 Name',
                                        'pyname': u'zone_11_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'distance from top of thermal chimney to inlet 11',
                                       {'name': u'Distance from Top of Thermal Chimney to Inlet 11',
                                        'pyname': u'distance_from_top_of_thermal_chimney_to_inlet_11',
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'm'}),
                                      (u'relative ratios of air flow rates passing through zone 11',
                                       {'name': u'Relative Ratios of Air Flow Rates Passing through Zone 11',
                                        'pyname': u'relative_ratios_of_air_flow_rates_passing_through_zone_11',
                                        'maximum': 1.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'cross sectional areas of air channel inlet 11',
                                       {'name': u'Cross Sectional Areas of Air Channel Inlet 11',
                                        'pyname': u'cross_sectional_areas_of_air_channel_inlet_11',
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'm2'}),
                                      (u'zone 12 name',
                                       {'name': u'Zone 12 Name',
                                        'pyname': u'zone_12_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'distance from top of thermal chimney to inlet 12',
                                       {'name': u'Distance from Top of Thermal Chimney to Inlet 12',
                                        'pyname': u'distance_from_top_of_thermal_chimney_to_inlet_12',
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'm'}),
                                      (u'relative ratios of air flow rates passing through zone 12',
                                       {'name': u'Relative Ratios of Air Flow Rates Passing through Zone 12',
                                        'pyname': u'relative_ratios_of_air_flow_rates_passing_through_zone_12',
                                        'maximum': 1.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'cross sectional areas of air channel inlet 12',
                                       {'name': u'Cross Sectional Areas of Air Channel Inlet 12',
                                        'pyname': u'cross_sectional_areas_of_air_channel_inlet_12',
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'm2'}),
                                      (u'zone 13 name',
                                       {'name': u'Zone 13 Name',
                                        'pyname': u'zone_13_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'distance from top of thermal chimney to inlet 13',
                                       {'name': u'Distance from Top of Thermal Chimney to Inlet 13',
                                        'pyname': u'distance_from_top_of_thermal_chimney_to_inlet_13',
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'm'}),
                                      (u'relative ratios of air flow rates passing through zone 13',
                                       {'name': u'Relative Ratios of Air Flow Rates Passing through Zone 13',
                                        'pyname': u'relative_ratios_of_air_flow_rates_passing_through_zone_13',
                                        'maximum': 1.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'cross sectional areas of air channel inlet 13',
                                       {'name': u'Cross Sectional Areas of Air Channel Inlet 13',
                                        'pyname': u'cross_sectional_areas_of_air_channel_inlet_13',
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'm2'}),
                                      (u'zone 14 name',
                                       {'name': u'Zone 14 Name',
                                        'pyname': u'zone_14_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'distance from top of thermal chimney to inlet 14',
                                       {'name': u'Distance from Top of Thermal Chimney to Inlet 14',
                                        'pyname': u'distance_from_top_of_thermal_chimney_to_inlet_14',
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'm'}),
                                      (u'relative ratios of air flow rates passing through zone 14',
                                       {'name': u'Relative Ratios of Air Flow Rates Passing through Zone 14',
                                        'pyname': u'relative_ratios_of_air_flow_rates_passing_through_zone_14',
                                        'maximum': 1.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'cross sectional areas of air channel inlet 14',
                                       {'name': u'Cross Sectional Areas of Air Channel Inlet 14',
                                        'pyname': u'cross_sectional_areas_of_air_channel_inlet_14',
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'm2'}),
                                      (u'zone 15 name',
                                       {'name': u'Zone 15 Name',
                                        'pyname': u'zone_15_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'distance from top of thermal chimney to inlet 15',
                                       {'name': u'Distance from Top of Thermal Chimney to Inlet 15',
                                        'pyname': u'distance_from_top_of_thermal_chimney_to_inlet_15',
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'm'}),
                                      (u'relative ratios of air flow rates passing through zone 15',
                                       {'name': u'Relative Ratios of Air Flow Rates Passing through Zone 15',
                                        'pyname': u'relative_ratios_of_air_flow_rates_passing_through_zone_15',
                                        'maximum': 1.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'cross sectional areas of air channel inlet 15',
                                       {'name': u'Cross Sectional Areas of Air Channel Inlet 15',
                                        'pyname': u'cross_sectional_areas_of_air_channel_inlet_15',
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'm2'}),
                                      (u'zone 16 name',
                                       {'name': u'Zone 16 Name',
                                        'pyname': u'zone_16_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'distance from top of thermal chimney to inlet 16',
                                       {'name': u'Distance from Top of Thermal Chimney to Inlet 16',
                                        'pyname': u'distance_from_top_of_thermal_chimney_to_inlet_16',
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'm'}),
                                      (u'relative ratios of air flow rates passing through zone 16',
                                       {'name': u'Relative Ratios of Air Flow Rates Passing through Zone 16',
                                        'pyname': u'relative_ratios_of_air_flow_rates_passing_through_zone_16',
                                        'maximum': 1.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'cross sectional areas of air channel inlet 16',
                                       {'name': u'Cross Sectional Areas of Air Channel Inlet 16',
                                        'pyname': u'cross_sectional_areas_of_air_channel_inlet_16',
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'm2'}),
                                      (u'zone 17 name',
                                       {'name': u'Zone 17 Name',
                                        'pyname': u'zone_17_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'distance from top of thermal chimney to inlet 17',
                                       {'name': u'Distance from Top of Thermal Chimney to Inlet 17',
                                        'pyname': u'distance_from_top_of_thermal_chimney_to_inlet_17',
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'm'}),
                                      (u'relative ratios of air flow rates passing through zone 17',
                                       {'name': u'Relative Ratios of Air Flow Rates Passing through Zone 17',
                                        'pyname': u'relative_ratios_of_air_flow_rates_passing_through_zone_17',
                                        'maximum': 1.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'cross sectional areas of air channel inlet 17',
                                       {'name': u'Cross Sectional Areas of Air Channel Inlet 17',
                                        'pyname': u'cross_sectional_areas_of_air_channel_inlet_17',
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'm2'}),
                                      (u'zone 18 name',
                                       {'name': u'Zone 18 Name',
                                        'pyname': u'zone_18_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'distance from top of thermal chimney to inlet 18',
                                       {'name': u'Distance from Top of Thermal Chimney to Inlet 18',
                                        'pyname': u'distance_from_top_of_thermal_chimney_to_inlet_18',
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'm'}),
                                      (u'relative ratios of air flow rates passing through zone 18',
                                       {'name': u'Relative Ratios of Air Flow Rates Passing through Zone 18',
                                        'pyname': u'relative_ratios_of_air_flow_rates_passing_through_zone_18',
                                        'maximum': 1.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'cross sectional areas of air channel inlet 18',
                                       {'name': u'Cross Sectional Areas of Air Channel Inlet 18',
                                        'pyname': u'cross_sectional_areas_of_air_channel_inlet_18',
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'm2'}),
                                      (u'zone 19 name',
                                       {'name': u'Zone 19 Name',
                                        'pyname': u'zone_19_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'distance from top of thermal chimney to inlet 19',
                                       {'name': u'Distance from Top of Thermal Chimney to Inlet 19',
                                        'pyname': u'distance_from_top_of_thermal_chimney_to_inlet_19',
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'm'}),
                                      (u'relative ratios of air flow rates passing through zone 19',
                                       {'name': u'Relative Ratios of Air Flow Rates Passing through Zone 19',
                                        'pyname': u'relative_ratios_of_air_flow_rates_passing_through_zone_19',
                                        'maximum': 1.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'cross sectional areas of air channel inlet 19',
                                       {'name': u'Cross Sectional Areas of Air Channel Inlet 19',
                                        'pyname': u'cross_sectional_areas_of_air_channel_inlet_19',
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'm2'}),
                                      (u'zone 20 name',
                                       {'name': u'Zone 20 Name',
                                        'pyname': u'zone_20_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'distance from top of thermal chimney to inlet 20',
                                       {'name': u'Distance from Top of Thermal Chimney to Inlet 20',
                                        'pyname': u'distance_from_top_of_thermal_chimney_to_inlet_20',
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'm'}),
                                      (u'relative ratios of air flow rates passing through zone 20',
                                       {'name': u'Relative Ratios of Air Flow Rates Passing through Zone 20',
                                        'pyname': u'relative_ratios_of_air_flow_rates_passing_through_zone_20',
                                        'maximum': 1.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'cross sectional areas of air channel inlet 20',
                                       {'name': u'Cross Sectional Areas of Air Channel Inlet 20',
                                        'pyname': u'cross_sectional_areas_of_air_channel_inlet_20',
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'm2'})]),
               'format': None,
               'group': u'Zone Airflow',
               'min-fields': 10,
               'name': u'ZoneThermalChimney',
               'pyname': u'ZoneThermalChimney',
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

        |  Name of zone that is the thermal chimney

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
    def availability_schedule_name(self):
        """field `Availability Schedule Name`

        |  Availability schedule name for this system. Schedule value > 0 means the system is available.
        |  If this field is blank, the system is always available.

        Args:
            value (str): value for IDD Field `Availability Schedule Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `availability_schedule_name` or None if not set

        """
        return self["Availability Schedule Name"]

    @availability_schedule_name.setter
    def availability_schedule_name(self, value=None):
        """Corresponds to IDD field `Availability Schedule Name`"""
        self["Availability Schedule Name"] = value

    @property
    def width_of_the_absorber_wall(self):
        """field `Width of the Absorber Wall`

        |  Units: m

        Args:
            value (float): value for IDD Field `Width of the Absorber Wall`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `width_of_the_absorber_wall` or None if not set

        """
        return self["Width of the Absorber Wall"]

    @width_of_the_absorber_wall.setter
    def width_of_the_absorber_wall(self, value=None):
        """Corresponds to IDD field `Width of the Absorber Wall`"""
        self["Width of the Absorber Wall"] = value

    @property
    def cross_sectional_area_of_air_channel_outlet(self):
        """field `Cross Sectional Area of Air Channel Outlet`

        |  Units: m2

        Args:
            value (float): value for IDD Field `Cross Sectional Area of Air Channel Outlet`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `cross_sectional_area_of_air_channel_outlet` or None if not set

        """
        return self["Cross Sectional Area of Air Channel Outlet"]

    @cross_sectional_area_of_air_channel_outlet.setter
    def cross_sectional_area_of_air_channel_outlet(self, value=None):
        """Corresponds to IDD field `Cross Sectional Area of Air Channel
        Outlet`"""
        self["Cross Sectional Area of Air Channel Outlet"] = value

    @property
    def discharge_coefficient(self):
        """field `Discharge Coefficient`

        |  Default value: 0.8
        |  value <= 1.0

        Args:
            value (float): value for IDD Field `Discharge Coefficient`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `discharge_coefficient` or None if not set

        """
        return self["Discharge Coefficient"]

    @discharge_coefficient.setter
    def discharge_coefficient(self, value=0.8):
        """Corresponds to IDD field `Discharge Coefficient`"""
        self["Discharge Coefficient"] = value

    @property
    def zone_1_name(self):
        """field `Zone 1 Name`

        Args:
            value (str): value for IDD Field `Zone 1 Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `zone_1_name` or None if not set

        """
        return self["Zone 1 Name"]

    @zone_1_name.setter
    def zone_1_name(self, value=None):
        """Corresponds to IDD field `Zone 1 Name`"""
        self["Zone 1 Name"] = value

    @property
    def distance_from_top_of_thermal_chimney_to_inlet_1(self):
        """field `Distance from Top of Thermal Chimney to Inlet 1`

        |  Units: m

        Args:
            value (float): value for IDD Field `Distance from Top of Thermal Chimney to Inlet 1`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `distance_from_top_of_thermal_chimney_to_inlet_1` or None if not set

        """
        return self["Distance from Top of Thermal Chimney to Inlet 1"]

    @distance_from_top_of_thermal_chimney_to_inlet_1.setter
    def distance_from_top_of_thermal_chimney_to_inlet_1(self, value=None):
        """Corresponds to IDD field `Distance from Top of Thermal Chimney to
        Inlet 1`"""
        self["Distance from Top of Thermal Chimney to Inlet 1"] = value

    @property
    def relative_ratios_of_air_flow_rates_passing_through_zone_1(self):
        """field `Relative Ratios of Air Flow Rates Passing through Zone 1`

        |  Default value: 1.0
        |  value <= 1.0

        Args:
            value (float): value for IDD Field `Relative Ratios of Air Flow Rates Passing through Zone 1`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `relative_ratios_of_air_flow_rates_passing_through_zone_1` or None if not set

        """
        return self["Relative Ratios of Air Flow Rates Passing through Zone 1"]

    @relative_ratios_of_air_flow_rates_passing_through_zone_1.setter
    def relative_ratios_of_air_flow_rates_passing_through_zone_1(
            self,
            value=1.0):
        """Corresponds to IDD field `Relative Ratios of Air Flow Rates Passing
        through Zone 1`"""
        self[
            "Relative Ratios of Air Flow Rates Passing through Zone 1"] = value

    @property
    def cross_sectional_areas_of_air_channel_inlet_1(self):
        """field `Cross Sectional Areas of Air Channel Inlet 1`

        |  Units: m2

        Args:
            value (float): value for IDD Field `Cross Sectional Areas of Air Channel Inlet 1`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `cross_sectional_areas_of_air_channel_inlet_1` or None if not set

        """
        return self["Cross Sectional Areas of Air Channel Inlet 1"]

    @cross_sectional_areas_of_air_channel_inlet_1.setter
    def cross_sectional_areas_of_air_channel_inlet_1(self, value=None):
        """Corresponds to IDD field `Cross Sectional Areas of Air Channel Inlet
        1`"""
        self["Cross Sectional Areas of Air Channel Inlet 1"] = value

    @property
    def zone_2_name(self):
        """field `Zone 2 Name`

        Args:
            value (str): value for IDD Field `Zone 2 Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `zone_2_name` or None if not set

        """
        return self["Zone 2 Name"]

    @zone_2_name.setter
    def zone_2_name(self, value=None):
        """Corresponds to IDD field `Zone 2 Name`"""
        self["Zone 2 Name"] = value

    @property
    def distance_from_top_of_thermal_chimney_to_inlet_2(self):
        """field `Distance from Top of Thermal Chimney to Inlet 2`

        |  Units: m

        Args:
            value (float): value for IDD Field `Distance from Top of Thermal Chimney to Inlet 2`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `distance_from_top_of_thermal_chimney_to_inlet_2` or None if not set

        """
        return self["Distance from Top of Thermal Chimney to Inlet 2"]

    @distance_from_top_of_thermal_chimney_to_inlet_2.setter
    def distance_from_top_of_thermal_chimney_to_inlet_2(self, value=None):
        """Corresponds to IDD field `Distance from Top of Thermal Chimney to
        Inlet 2`"""
        self["Distance from Top of Thermal Chimney to Inlet 2"] = value

    @property
    def relative_ratios_of_air_flow_rates_passing_through_zone_2(self):
        """field `Relative Ratios of Air Flow Rates Passing through Zone 2`

        |  value <= 1.0

        Args:
            value (float): value for IDD Field `Relative Ratios of Air Flow Rates Passing through Zone 2`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `relative_ratios_of_air_flow_rates_passing_through_zone_2` or None if not set

        """
        return self["Relative Ratios of Air Flow Rates Passing through Zone 2"]

    @relative_ratios_of_air_flow_rates_passing_through_zone_2.setter
    def relative_ratios_of_air_flow_rates_passing_through_zone_2(
            self,
            value=None):
        """Corresponds to IDD field `Relative Ratios of Air Flow Rates Passing
        through Zone 2`"""
        self[
            "Relative Ratios of Air Flow Rates Passing through Zone 2"] = value

    @property
    def cross_sectional_areas_of_air_channel_inlet_2(self):
        """field `Cross Sectional Areas of Air Channel Inlet 2`

        |  Units: m2

        Args:
            value (float): value for IDD Field `Cross Sectional Areas of Air Channel Inlet 2`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `cross_sectional_areas_of_air_channel_inlet_2` or None if not set

        """
        return self["Cross Sectional Areas of Air Channel Inlet 2"]

    @cross_sectional_areas_of_air_channel_inlet_2.setter
    def cross_sectional_areas_of_air_channel_inlet_2(self, value=None):
        """Corresponds to IDD field `Cross Sectional Areas of Air Channel Inlet
        2`"""
        self["Cross Sectional Areas of Air Channel Inlet 2"] = value

    @property
    def zone_3_name(self):
        """field `Zone 3 Name`

        Args:
            value (str): value for IDD Field `Zone 3 Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `zone_3_name` or None if not set

        """
        return self["Zone 3 Name"]

    @zone_3_name.setter
    def zone_3_name(self, value=None):
        """Corresponds to IDD field `Zone 3 Name`"""
        self["Zone 3 Name"] = value

    @property
    def distance_from_top_of_thermal_chimney_to_inlet_3(self):
        """field `Distance from Top of Thermal Chimney to Inlet 3`

        |  Units: m

        Args:
            value (float): value for IDD Field `Distance from Top of Thermal Chimney to Inlet 3`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `distance_from_top_of_thermal_chimney_to_inlet_3` or None if not set

        """
        return self["Distance from Top of Thermal Chimney to Inlet 3"]

    @distance_from_top_of_thermal_chimney_to_inlet_3.setter
    def distance_from_top_of_thermal_chimney_to_inlet_3(self, value=None):
        """Corresponds to IDD field `Distance from Top of Thermal Chimney to
        Inlet 3`"""
        self["Distance from Top of Thermal Chimney to Inlet 3"] = value

    @property
    def relative_ratios_of_air_flow_rates_passing_through_zone_3(self):
        """field `Relative Ratios of Air Flow Rates Passing through Zone 3`

        |  value <= 1.0

        Args:
            value (float): value for IDD Field `Relative Ratios of Air Flow Rates Passing through Zone 3`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `relative_ratios_of_air_flow_rates_passing_through_zone_3` or None if not set

        """
        return self["Relative Ratios of Air Flow Rates Passing through Zone 3"]

    @relative_ratios_of_air_flow_rates_passing_through_zone_3.setter
    def relative_ratios_of_air_flow_rates_passing_through_zone_3(
            self,
            value=None):
        """Corresponds to IDD field `Relative Ratios of Air Flow Rates Passing
        through Zone 3`"""
        self[
            "Relative Ratios of Air Flow Rates Passing through Zone 3"] = value

    @property
    def cross_sectional_areas_of_air_channel_inlet_3(self):
        """field `Cross Sectional Areas of Air Channel Inlet 3`

        |  Units: m2

        Args:
            value (float): value for IDD Field `Cross Sectional Areas of Air Channel Inlet 3`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `cross_sectional_areas_of_air_channel_inlet_3` or None if not set

        """
        return self["Cross Sectional Areas of Air Channel Inlet 3"]

    @cross_sectional_areas_of_air_channel_inlet_3.setter
    def cross_sectional_areas_of_air_channel_inlet_3(self, value=None):
        """Corresponds to IDD field `Cross Sectional Areas of Air Channel Inlet
        3`"""
        self["Cross Sectional Areas of Air Channel Inlet 3"] = value

    @property
    def zone_4_name(self):
        """field `Zone 4 Name`

        Args:
            value (str): value for IDD Field `Zone 4 Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `zone_4_name` or None if not set

        """
        return self["Zone 4 Name"]

    @zone_4_name.setter
    def zone_4_name(self, value=None):
        """Corresponds to IDD field `Zone 4 Name`"""
        self["Zone 4 Name"] = value

    @property
    def distance_from_top_of_thermal_chimney_to_inlet_4(self):
        """field `Distance from Top of Thermal Chimney to Inlet 4`

        |  Units: m

        Args:
            value (float): value for IDD Field `Distance from Top of Thermal Chimney to Inlet 4`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `distance_from_top_of_thermal_chimney_to_inlet_4` or None if not set

        """
        return self["Distance from Top of Thermal Chimney to Inlet 4"]

    @distance_from_top_of_thermal_chimney_to_inlet_4.setter
    def distance_from_top_of_thermal_chimney_to_inlet_4(self, value=None):
        """Corresponds to IDD field `Distance from Top of Thermal Chimney to
        Inlet 4`"""
        self["Distance from Top of Thermal Chimney to Inlet 4"] = value

    @property
    def relative_ratios_of_air_flow_rates_passing_through_zone_4(self):
        """field `Relative Ratios of Air Flow Rates Passing through Zone 4`

        |  value <= 1.0

        Args:
            value (float): value for IDD Field `Relative Ratios of Air Flow Rates Passing through Zone 4`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `relative_ratios_of_air_flow_rates_passing_through_zone_4` or None if not set

        """
        return self["Relative Ratios of Air Flow Rates Passing through Zone 4"]

    @relative_ratios_of_air_flow_rates_passing_through_zone_4.setter
    def relative_ratios_of_air_flow_rates_passing_through_zone_4(
            self,
            value=None):
        """Corresponds to IDD field `Relative Ratios of Air Flow Rates Passing
        through Zone 4`"""
        self[
            "Relative Ratios of Air Flow Rates Passing through Zone 4"] = value

    @property
    def cross_sectional_areas_of_air_channel_inlet_4(self):
        """field `Cross Sectional Areas of Air Channel Inlet 4`

        |  Units: m2

        Args:
            value (float): value for IDD Field `Cross Sectional Areas of Air Channel Inlet 4`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `cross_sectional_areas_of_air_channel_inlet_4` or None if not set

        """
        return self["Cross Sectional Areas of Air Channel Inlet 4"]

    @cross_sectional_areas_of_air_channel_inlet_4.setter
    def cross_sectional_areas_of_air_channel_inlet_4(self, value=None):
        """Corresponds to IDD field `Cross Sectional Areas of Air Channel Inlet
        4`"""
        self["Cross Sectional Areas of Air Channel Inlet 4"] = value

    @property
    def zone_5_name(self):
        """field `Zone 5 Name`

        Args:
            value (str): value for IDD Field `Zone 5 Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `zone_5_name` or None if not set

        """
        return self["Zone 5 Name"]

    @zone_5_name.setter
    def zone_5_name(self, value=None):
        """Corresponds to IDD field `Zone 5 Name`"""
        self["Zone 5 Name"] = value

    @property
    def distance_from_top_of_thermal_chimney_to_inlet_5(self):
        """field `Distance from Top of Thermal Chimney to Inlet 5`

        |  Units: m

        Args:
            value (float): value for IDD Field `Distance from Top of Thermal Chimney to Inlet 5`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `distance_from_top_of_thermal_chimney_to_inlet_5` or None if not set

        """
        return self["Distance from Top of Thermal Chimney to Inlet 5"]

    @distance_from_top_of_thermal_chimney_to_inlet_5.setter
    def distance_from_top_of_thermal_chimney_to_inlet_5(self, value=None):
        """Corresponds to IDD field `Distance from Top of Thermal Chimney to
        Inlet 5`"""
        self["Distance from Top of Thermal Chimney to Inlet 5"] = value

    @property
    def relative_ratios_of_air_flow_rates_passing_through_zone_5(self):
        """field `Relative Ratios of Air Flow Rates Passing through Zone 5`

        |  value <= 1.0

        Args:
            value (float): value for IDD Field `Relative Ratios of Air Flow Rates Passing through Zone 5`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `relative_ratios_of_air_flow_rates_passing_through_zone_5` or None if not set

        """
        return self["Relative Ratios of Air Flow Rates Passing through Zone 5"]

    @relative_ratios_of_air_flow_rates_passing_through_zone_5.setter
    def relative_ratios_of_air_flow_rates_passing_through_zone_5(
            self,
            value=None):
        """Corresponds to IDD field `Relative Ratios of Air Flow Rates Passing
        through Zone 5`"""
        self[
            "Relative Ratios of Air Flow Rates Passing through Zone 5"] = value

    @property
    def cross_sectional_areas_of_air_channel_inlet_5(self):
        """field `Cross Sectional Areas of Air Channel Inlet 5`

        |  Units: m2

        Args:
            value (float): value for IDD Field `Cross Sectional Areas of Air Channel Inlet 5`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `cross_sectional_areas_of_air_channel_inlet_5` or None if not set

        """
        return self["Cross Sectional Areas of Air Channel Inlet 5"]

    @cross_sectional_areas_of_air_channel_inlet_5.setter
    def cross_sectional_areas_of_air_channel_inlet_5(self, value=None):
        """Corresponds to IDD field `Cross Sectional Areas of Air Channel Inlet
        5`"""
        self["Cross Sectional Areas of Air Channel Inlet 5"] = value

    @property
    def zone_6_name(self):
        """field `Zone 6 Name`

        Args:
            value (str): value for IDD Field `Zone 6 Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `zone_6_name` or None if not set

        """
        return self["Zone 6 Name"]

    @zone_6_name.setter
    def zone_6_name(self, value=None):
        """Corresponds to IDD field `Zone 6 Name`"""
        self["Zone 6 Name"] = value

    @property
    def distance_from_top_of_thermal_chimney_to_inlet_6(self):
        """field `Distance from Top of Thermal Chimney to Inlet 6`

        |  Units: m

        Args:
            value (float): value for IDD Field `Distance from Top of Thermal Chimney to Inlet 6`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `distance_from_top_of_thermal_chimney_to_inlet_6` or None if not set

        """
        return self["Distance from Top of Thermal Chimney to Inlet 6"]

    @distance_from_top_of_thermal_chimney_to_inlet_6.setter
    def distance_from_top_of_thermal_chimney_to_inlet_6(self, value=None):
        """Corresponds to IDD field `Distance from Top of Thermal Chimney to
        Inlet 6`"""
        self["Distance from Top of Thermal Chimney to Inlet 6"] = value

    @property
    def relative_ratios_of_air_flow_rates_passing_through_zone_6(self):
        """field `Relative Ratios of Air Flow Rates Passing through Zone 6`

        |  value <= 1.0

        Args:
            value (float): value for IDD Field `Relative Ratios of Air Flow Rates Passing through Zone 6`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `relative_ratios_of_air_flow_rates_passing_through_zone_6` or None if not set

        """
        return self["Relative Ratios of Air Flow Rates Passing through Zone 6"]

    @relative_ratios_of_air_flow_rates_passing_through_zone_6.setter
    def relative_ratios_of_air_flow_rates_passing_through_zone_6(
            self,
            value=None):
        """Corresponds to IDD field `Relative Ratios of Air Flow Rates Passing
        through Zone 6`"""
        self[
            "Relative Ratios of Air Flow Rates Passing through Zone 6"] = value

    @property
    def cross_sectional_areas_of_air_channel_inlet_6(self):
        """field `Cross Sectional Areas of Air Channel Inlet 6`

        |  Units: m2

        Args:
            value (float): value for IDD Field `Cross Sectional Areas of Air Channel Inlet 6`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `cross_sectional_areas_of_air_channel_inlet_6` or None if not set

        """
        return self["Cross Sectional Areas of Air Channel Inlet 6"]

    @cross_sectional_areas_of_air_channel_inlet_6.setter
    def cross_sectional_areas_of_air_channel_inlet_6(self, value=None):
        """Corresponds to IDD field `Cross Sectional Areas of Air Channel Inlet
        6`"""
        self["Cross Sectional Areas of Air Channel Inlet 6"] = value

    @property
    def zone_7_name(self):
        """field `Zone 7 Name`

        Args:
            value (str): value for IDD Field `Zone 7 Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `zone_7_name` or None if not set

        """
        return self["Zone 7 Name"]

    @zone_7_name.setter
    def zone_7_name(self, value=None):
        """Corresponds to IDD field `Zone 7 Name`"""
        self["Zone 7 Name"] = value

    @property
    def distance_from_top_of_thermal_chimney_to_inlet_7(self):
        """field `Distance from Top of Thermal Chimney to Inlet 7`

        |  Units: m

        Args:
            value (float): value for IDD Field `Distance from Top of Thermal Chimney to Inlet 7`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `distance_from_top_of_thermal_chimney_to_inlet_7` or None if not set

        """
        return self["Distance from Top of Thermal Chimney to Inlet 7"]

    @distance_from_top_of_thermal_chimney_to_inlet_7.setter
    def distance_from_top_of_thermal_chimney_to_inlet_7(self, value=None):
        """Corresponds to IDD field `Distance from Top of Thermal Chimney to
        Inlet 7`"""
        self["Distance from Top of Thermal Chimney to Inlet 7"] = value

    @property
    def relative_ratios_of_air_flow_rates_passing_through_zone_7(self):
        """field `Relative Ratios of Air Flow Rates Passing through Zone 7`

        |  value <= 1.0

        Args:
            value (float): value for IDD Field `Relative Ratios of Air Flow Rates Passing through Zone 7`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `relative_ratios_of_air_flow_rates_passing_through_zone_7` or None if not set

        """
        return self["Relative Ratios of Air Flow Rates Passing through Zone 7"]

    @relative_ratios_of_air_flow_rates_passing_through_zone_7.setter
    def relative_ratios_of_air_flow_rates_passing_through_zone_7(
            self,
            value=None):
        """Corresponds to IDD field `Relative Ratios of Air Flow Rates Passing
        through Zone 7`"""
        self[
            "Relative Ratios of Air Flow Rates Passing through Zone 7"] = value

    @property
    def cross_sectional_areas_of_air_channel_inlet_7(self):
        """field `Cross Sectional Areas of Air Channel Inlet 7`

        |  Units: m2

        Args:
            value (float): value for IDD Field `Cross Sectional Areas of Air Channel Inlet 7`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `cross_sectional_areas_of_air_channel_inlet_7` or None if not set

        """
        return self["Cross Sectional Areas of Air Channel Inlet 7"]

    @cross_sectional_areas_of_air_channel_inlet_7.setter
    def cross_sectional_areas_of_air_channel_inlet_7(self, value=None):
        """Corresponds to IDD field `Cross Sectional Areas of Air Channel Inlet
        7`"""
        self["Cross Sectional Areas of Air Channel Inlet 7"] = value

    @property
    def zone_8_name(self):
        """field `Zone 8 Name`

        Args:
            value (str): value for IDD Field `Zone 8 Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `zone_8_name` or None if not set

        """
        return self["Zone 8 Name"]

    @zone_8_name.setter
    def zone_8_name(self, value=None):
        """Corresponds to IDD field `Zone 8 Name`"""
        self["Zone 8 Name"] = value

    @property
    def distance_from_top_of_thermal_chimney_to_inlet_8(self):
        """field `Distance from Top of Thermal Chimney to Inlet 8`

        |  Units: m

        Args:
            value (float): value for IDD Field `Distance from Top of Thermal Chimney to Inlet 8`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `distance_from_top_of_thermal_chimney_to_inlet_8` or None if not set

        """
        return self["Distance from Top of Thermal Chimney to Inlet 8"]

    @distance_from_top_of_thermal_chimney_to_inlet_8.setter
    def distance_from_top_of_thermal_chimney_to_inlet_8(self, value=None):
        """Corresponds to IDD field `Distance from Top of Thermal Chimney to
        Inlet 8`"""
        self["Distance from Top of Thermal Chimney to Inlet 8"] = value

    @property
    def relative_ratios_of_air_flow_rates_passing_through_zone_8(self):
        """field `Relative Ratios of Air Flow Rates Passing through Zone 8`

        |  value <= 1.0

        Args:
            value (float): value for IDD Field `Relative Ratios of Air Flow Rates Passing through Zone 8`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `relative_ratios_of_air_flow_rates_passing_through_zone_8` or None if not set

        """
        return self["Relative Ratios of Air Flow Rates Passing through Zone 8"]

    @relative_ratios_of_air_flow_rates_passing_through_zone_8.setter
    def relative_ratios_of_air_flow_rates_passing_through_zone_8(
            self,
            value=None):
        """Corresponds to IDD field `Relative Ratios of Air Flow Rates Passing
        through Zone 8`"""
        self[
            "Relative Ratios of Air Flow Rates Passing through Zone 8"] = value

    @property
    def cross_sectional_areas_of_air_channel_inlet_8(self):
        """field `Cross Sectional Areas of Air Channel Inlet 8`

        |  Units: m2

        Args:
            value (float): value for IDD Field `Cross Sectional Areas of Air Channel Inlet 8`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `cross_sectional_areas_of_air_channel_inlet_8` or None if not set

        """
        return self["Cross Sectional Areas of Air Channel Inlet 8"]

    @cross_sectional_areas_of_air_channel_inlet_8.setter
    def cross_sectional_areas_of_air_channel_inlet_8(self, value=None):
        """Corresponds to IDD field `Cross Sectional Areas of Air Channel Inlet
        8`"""
        self["Cross Sectional Areas of Air Channel Inlet 8"] = value

    @property
    def zone_9_name(self):
        """field `Zone 9 Name`

        Args:
            value (str): value for IDD Field `Zone 9 Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `zone_9_name` or None if not set

        """
        return self["Zone 9 Name"]

    @zone_9_name.setter
    def zone_9_name(self, value=None):
        """Corresponds to IDD field `Zone 9 Name`"""
        self["Zone 9 Name"] = value

    @property
    def distance_from_top_of_thermal_chimney_to_inlet_9(self):
        """field `Distance from Top of Thermal Chimney to Inlet 9`

        |  Units: m

        Args:
            value (float): value for IDD Field `Distance from Top of Thermal Chimney to Inlet 9`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `distance_from_top_of_thermal_chimney_to_inlet_9` or None if not set

        """
        return self["Distance from Top of Thermal Chimney to Inlet 9"]

    @distance_from_top_of_thermal_chimney_to_inlet_9.setter
    def distance_from_top_of_thermal_chimney_to_inlet_9(self, value=None):
        """Corresponds to IDD field `Distance from Top of Thermal Chimney to
        Inlet 9`"""
        self["Distance from Top of Thermal Chimney to Inlet 9"] = value

    @property
    def relative_ratios_of_air_flow_rates_passing_through_zone_9(self):
        """field `Relative Ratios of Air Flow Rates Passing through Zone 9`

        |  value <= 1.0

        Args:
            value (float): value for IDD Field `Relative Ratios of Air Flow Rates Passing through Zone 9`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `relative_ratios_of_air_flow_rates_passing_through_zone_9` or None if not set

        """
        return self["Relative Ratios of Air Flow Rates Passing through Zone 9"]

    @relative_ratios_of_air_flow_rates_passing_through_zone_9.setter
    def relative_ratios_of_air_flow_rates_passing_through_zone_9(
            self,
            value=None):
        """Corresponds to IDD field `Relative Ratios of Air Flow Rates Passing
        through Zone 9`"""
        self[
            "Relative Ratios of Air Flow Rates Passing through Zone 9"] = value

    @property
    def cross_sectional_areas_of_air_channel_inlet_9(self):
        """field `Cross Sectional Areas of Air Channel Inlet 9`

        |  Units: m2

        Args:
            value (float): value for IDD Field `Cross Sectional Areas of Air Channel Inlet 9`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `cross_sectional_areas_of_air_channel_inlet_9` or None if not set

        """
        return self["Cross Sectional Areas of Air Channel Inlet 9"]

    @cross_sectional_areas_of_air_channel_inlet_9.setter
    def cross_sectional_areas_of_air_channel_inlet_9(self, value=None):
        """Corresponds to IDD field `Cross Sectional Areas of Air Channel Inlet
        9`"""
        self["Cross Sectional Areas of Air Channel Inlet 9"] = value

    @property
    def zone_10_name(self):
        """field `Zone 10 Name`

        Args:
            value (str): value for IDD Field `Zone 10 Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `zone_10_name` or None if not set

        """
        return self["Zone 10 Name"]

    @zone_10_name.setter
    def zone_10_name(self, value=None):
        """Corresponds to IDD field `Zone 10 Name`"""
        self["Zone 10 Name"] = value

    @property
    def distance_from_top_of_thermal_chimney_to_inlet_10(self):
        """field `Distance from Top of Thermal Chimney to Inlet 10`

        |  Units: m

        Args:
            value (float): value for IDD Field `Distance from Top of Thermal Chimney to Inlet 10`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `distance_from_top_of_thermal_chimney_to_inlet_10` or None if not set

        """
        return self["Distance from Top of Thermal Chimney to Inlet 10"]

    @distance_from_top_of_thermal_chimney_to_inlet_10.setter
    def distance_from_top_of_thermal_chimney_to_inlet_10(self, value=None):
        """Corresponds to IDD field `Distance from Top of Thermal Chimney to
        Inlet 10`"""
        self["Distance from Top of Thermal Chimney to Inlet 10"] = value

    @property
    def relative_ratios_of_air_flow_rates_passing_through_zone_10(self):
        """field `Relative Ratios of Air Flow Rates Passing through Zone 10`

        |  value <= 1.0

        Args:
            value (float): value for IDD Field `Relative Ratios of Air Flow Rates Passing through Zone 10`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `relative_ratios_of_air_flow_rates_passing_through_zone_10` or None if not set

        """
        return self[
            "Relative Ratios of Air Flow Rates Passing through Zone 10"]

    @relative_ratios_of_air_flow_rates_passing_through_zone_10.setter
    def relative_ratios_of_air_flow_rates_passing_through_zone_10(
            self,
            value=None):
        """Corresponds to IDD field `Relative Ratios of Air Flow Rates Passing
        through Zone 10`"""
        self[
            "Relative Ratios of Air Flow Rates Passing through Zone 10"] = value

    @property
    def cross_sectional_areas_of_air_channel_inlet_10(self):
        """field `Cross Sectional Areas of Air Channel Inlet 10`

        |  Units: m2

        Args:
            value (float): value for IDD Field `Cross Sectional Areas of Air Channel Inlet 10`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `cross_sectional_areas_of_air_channel_inlet_10` or None if not set

        """
        return self["Cross Sectional Areas of Air Channel Inlet 10"]

    @cross_sectional_areas_of_air_channel_inlet_10.setter
    def cross_sectional_areas_of_air_channel_inlet_10(self, value=None):
        """Corresponds to IDD field `Cross Sectional Areas of Air Channel Inlet
        10`"""
        self["Cross Sectional Areas of Air Channel Inlet 10"] = value

    @property
    def zone_11_name(self):
        """field `Zone 11 Name`

        Args:
            value (str): value for IDD Field `Zone 11 Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `zone_11_name` or None if not set

        """
        return self["Zone 11 Name"]

    @zone_11_name.setter
    def zone_11_name(self, value=None):
        """Corresponds to IDD field `Zone 11 Name`"""
        self["Zone 11 Name"] = value

    @property
    def distance_from_top_of_thermal_chimney_to_inlet_11(self):
        """field `Distance from Top of Thermal Chimney to Inlet 11`

        |  Units: m

        Args:
            value (float): value for IDD Field `Distance from Top of Thermal Chimney to Inlet 11`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `distance_from_top_of_thermal_chimney_to_inlet_11` or None if not set

        """
        return self["Distance from Top of Thermal Chimney to Inlet 11"]

    @distance_from_top_of_thermal_chimney_to_inlet_11.setter
    def distance_from_top_of_thermal_chimney_to_inlet_11(self, value=None):
        """Corresponds to IDD field `Distance from Top of Thermal Chimney to
        Inlet 11`"""
        self["Distance from Top of Thermal Chimney to Inlet 11"] = value

    @property
    def relative_ratios_of_air_flow_rates_passing_through_zone_11(self):
        """field `Relative Ratios of Air Flow Rates Passing through Zone 11`

        |  value <= 1.0

        Args:
            value (float): value for IDD Field `Relative Ratios of Air Flow Rates Passing through Zone 11`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `relative_ratios_of_air_flow_rates_passing_through_zone_11` or None if not set

        """
        return self[
            "Relative Ratios of Air Flow Rates Passing through Zone 11"]

    @relative_ratios_of_air_flow_rates_passing_through_zone_11.setter
    def relative_ratios_of_air_flow_rates_passing_through_zone_11(
            self,
            value=None):
        """Corresponds to IDD field `Relative Ratios of Air Flow Rates Passing
        through Zone 11`"""
        self[
            "Relative Ratios of Air Flow Rates Passing through Zone 11"] = value

    @property
    def cross_sectional_areas_of_air_channel_inlet_11(self):
        """field `Cross Sectional Areas of Air Channel Inlet 11`

        |  Units: m2

        Args:
            value (float): value for IDD Field `Cross Sectional Areas of Air Channel Inlet 11`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `cross_sectional_areas_of_air_channel_inlet_11` or None if not set

        """
        return self["Cross Sectional Areas of Air Channel Inlet 11"]

    @cross_sectional_areas_of_air_channel_inlet_11.setter
    def cross_sectional_areas_of_air_channel_inlet_11(self, value=None):
        """Corresponds to IDD field `Cross Sectional Areas of Air Channel Inlet
        11`"""
        self["Cross Sectional Areas of Air Channel Inlet 11"] = value

    @property
    def zone_12_name(self):
        """field `Zone 12 Name`

        Args:
            value (str): value for IDD Field `Zone 12 Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `zone_12_name` or None if not set

        """
        return self["Zone 12 Name"]

    @zone_12_name.setter
    def zone_12_name(self, value=None):
        """Corresponds to IDD field `Zone 12 Name`"""
        self["Zone 12 Name"] = value

    @property
    def distance_from_top_of_thermal_chimney_to_inlet_12(self):
        """field `Distance from Top of Thermal Chimney to Inlet 12`

        |  Units: m

        Args:
            value (float): value for IDD Field `Distance from Top of Thermal Chimney to Inlet 12`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `distance_from_top_of_thermal_chimney_to_inlet_12` or None if not set

        """
        return self["Distance from Top of Thermal Chimney to Inlet 12"]

    @distance_from_top_of_thermal_chimney_to_inlet_12.setter
    def distance_from_top_of_thermal_chimney_to_inlet_12(self, value=None):
        """Corresponds to IDD field `Distance from Top of Thermal Chimney to
        Inlet 12`"""
        self["Distance from Top of Thermal Chimney to Inlet 12"] = value

    @property
    def relative_ratios_of_air_flow_rates_passing_through_zone_12(self):
        """field `Relative Ratios of Air Flow Rates Passing through Zone 12`

        |  value <= 1.0

        Args:
            value (float): value for IDD Field `Relative Ratios of Air Flow Rates Passing through Zone 12`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `relative_ratios_of_air_flow_rates_passing_through_zone_12` or None if not set

        """
        return self[
            "Relative Ratios of Air Flow Rates Passing through Zone 12"]

    @relative_ratios_of_air_flow_rates_passing_through_zone_12.setter
    def relative_ratios_of_air_flow_rates_passing_through_zone_12(
            self,
            value=None):
        """Corresponds to IDD field `Relative Ratios of Air Flow Rates Passing
        through Zone 12`"""
        self[
            "Relative Ratios of Air Flow Rates Passing through Zone 12"] = value

    @property
    def cross_sectional_areas_of_air_channel_inlet_12(self):
        """field `Cross Sectional Areas of Air Channel Inlet 12`

        |  Units: m2

        Args:
            value (float): value for IDD Field `Cross Sectional Areas of Air Channel Inlet 12`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `cross_sectional_areas_of_air_channel_inlet_12` or None if not set

        """
        return self["Cross Sectional Areas of Air Channel Inlet 12"]

    @cross_sectional_areas_of_air_channel_inlet_12.setter
    def cross_sectional_areas_of_air_channel_inlet_12(self, value=None):
        """Corresponds to IDD field `Cross Sectional Areas of Air Channel Inlet
        12`"""
        self["Cross Sectional Areas of Air Channel Inlet 12"] = value

    @property
    def zone_13_name(self):
        """field `Zone 13 Name`

        Args:
            value (str): value for IDD Field `Zone 13 Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `zone_13_name` or None if not set

        """
        return self["Zone 13 Name"]

    @zone_13_name.setter
    def zone_13_name(self, value=None):
        """Corresponds to IDD field `Zone 13 Name`"""
        self["Zone 13 Name"] = value

    @property
    def distance_from_top_of_thermal_chimney_to_inlet_13(self):
        """field `Distance from Top of Thermal Chimney to Inlet 13`

        |  Units: m

        Args:
            value (float): value for IDD Field `Distance from Top of Thermal Chimney to Inlet 13`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `distance_from_top_of_thermal_chimney_to_inlet_13` or None if not set

        """
        return self["Distance from Top of Thermal Chimney to Inlet 13"]

    @distance_from_top_of_thermal_chimney_to_inlet_13.setter
    def distance_from_top_of_thermal_chimney_to_inlet_13(self, value=None):
        """Corresponds to IDD field `Distance from Top of Thermal Chimney to
        Inlet 13`"""
        self["Distance from Top of Thermal Chimney to Inlet 13"] = value

    @property
    def relative_ratios_of_air_flow_rates_passing_through_zone_13(self):
        """field `Relative Ratios of Air Flow Rates Passing through Zone 13`

        |  value <= 1.0

        Args:
            value (float): value for IDD Field `Relative Ratios of Air Flow Rates Passing through Zone 13`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `relative_ratios_of_air_flow_rates_passing_through_zone_13` or None if not set

        """
        return self[
            "Relative Ratios of Air Flow Rates Passing through Zone 13"]

    @relative_ratios_of_air_flow_rates_passing_through_zone_13.setter
    def relative_ratios_of_air_flow_rates_passing_through_zone_13(
            self,
            value=None):
        """Corresponds to IDD field `Relative Ratios of Air Flow Rates Passing
        through Zone 13`"""
        self[
            "Relative Ratios of Air Flow Rates Passing through Zone 13"] = value

    @property
    def cross_sectional_areas_of_air_channel_inlet_13(self):
        """field `Cross Sectional Areas of Air Channel Inlet 13`

        |  Units: m2

        Args:
            value (float): value for IDD Field `Cross Sectional Areas of Air Channel Inlet 13`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `cross_sectional_areas_of_air_channel_inlet_13` or None if not set

        """
        return self["Cross Sectional Areas of Air Channel Inlet 13"]

    @cross_sectional_areas_of_air_channel_inlet_13.setter
    def cross_sectional_areas_of_air_channel_inlet_13(self, value=None):
        """Corresponds to IDD field `Cross Sectional Areas of Air Channel Inlet
        13`"""
        self["Cross Sectional Areas of Air Channel Inlet 13"] = value

    @property
    def zone_14_name(self):
        """field `Zone 14 Name`

        Args:
            value (str): value for IDD Field `Zone 14 Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `zone_14_name` or None if not set

        """
        return self["Zone 14 Name"]

    @zone_14_name.setter
    def zone_14_name(self, value=None):
        """Corresponds to IDD field `Zone 14 Name`"""
        self["Zone 14 Name"] = value

    @property
    def distance_from_top_of_thermal_chimney_to_inlet_14(self):
        """field `Distance from Top of Thermal Chimney to Inlet 14`

        |  Units: m

        Args:
            value (float): value for IDD Field `Distance from Top of Thermal Chimney to Inlet 14`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `distance_from_top_of_thermal_chimney_to_inlet_14` or None if not set

        """
        return self["Distance from Top of Thermal Chimney to Inlet 14"]

    @distance_from_top_of_thermal_chimney_to_inlet_14.setter
    def distance_from_top_of_thermal_chimney_to_inlet_14(self, value=None):
        """Corresponds to IDD field `Distance from Top of Thermal Chimney to
        Inlet 14`"""
        self["Distance from Top of Thermal Chimney to Inlet 14"] = value

    @property
    def relative_ratios_of_air_flow_rates_passing_through_zone_14(self):
        """field `Relative Ratios of Air Flow Rates Passing through Zone 14`

        |  value <= 1.0

        Args:
            value (float): value for IDD Field `Relative Ratios of Air Flow Rates Passing through Zone 14`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `relative_ratios_of_air_flow_rates_passing_through_zone_14` or None if not set

        """
        return self[
            "Relative Ratios of Air Flow Rates Passing through Zone 14"]

    @relative_ratios_of_air_flow_rates_passing_through_zone_14.setter
    def relative_ratios_of_air_flow_rates_passing_through_zone_14(
            self,
            value=None):
        """Corresponds to IDD field `Relative Ratios of Air Flow Rates Passing
        through Zone 14`"""
        self[
            "Relative Ratios of Air Flow Rates Passing through Zone 14"] = value

    @property
    def cross_sectional_areas_of_air_channel_inlet_14(self):
        """field `Cross Sectional Areas of Air Channel Inlet 14`

        |  Units: m2

        Args:
            value (float): value for IDD Field `Cross Sectional Areas of Air Channel Inlet 14`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `cross_sectional_areas_of_air_channel_inlet_14` or None if not set

        """
        return self["Cross Sectional Areas of Air Channel Inlet 14"]

    @cross_sectional_areas_of_air_channel_inlet_14.setter
    def cross_sectional_areas_of_air_channel_inlet_14(self, value=None):
        """Corresponds to IDD field `Cross Sectional Areas of Air Channel Inlet
        14`"""
        self["Cross Sectional Areas of Air Channel Inlet 14"] = value

    @property
    def zone_15_name(self):
        """field `Zone 15 Name`

        Args:
            value (str): value for IDD Field `Zone 15 Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `zone_15_name` or None if not set

        """
        return self["Zone 15 Name"]

    @zone_15_name.setter
    def zone_15_name(self, value=None):
        """Corresponds to IDD field `Zone 15 Name`"""
        self["Zone 15 Name"] = value

    @property
    def distance_from_top_of_thermal_chimney_to_inlet_15(self):
        """field `Distance from Top of Thermal Chimney to Inlet 15`

        |  Units: m

        Args:
            value (float): value for IDD Field `Distance from Top of Thermal Chimney to Inlet 15`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `distance_from_top_of_thermal_chimney_to_inlet_15` or None if not set

        """
        return self["Distance from Top of Thermal Chimney to Inlet 15"]

    @distance_from_top_of_thermal_chimney_to_inlet_15.setter
    def distance_from_top_of_thermal_chimney_to_inlet_15(self, value=None):
        """Corresponds to IDD field `Distance from Top of Thermal Chimney to
        Inlet 15`"""
        self["Distance from Top of Thermal Chimney to Inlet 15"] = value

    @property
    def relative_ratios_of_air_flow_rates_passing_through_zone_15(self):
        """field `Relative Ratios of Air Flow Rates Passing through Zone 15`

        |  value <= 1.0

        Args:
            value (float): value for IDD Field `Relative Ratios of Air Flow Rates Passing through Zone 15`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `relative_ratios_of_air_flow_rates_passing_through_zone_15` or None if not set

        """
        return self[
            "Relative Ratios of Air Flow Rates Passing through Zone 15"]

    @relative_ratios_of_air_flow_rates_passing_through_zone_15.setter
    def relative_ratios_of_air_flow_rates_passing_through_zone_15(
            self,
            value=None):
        """Corresponds to IDD field `Relative Ratios of Air Flow Rates Passing
        through Zone 15`"""
        self[
            "Relative Ratios of Air Flow Rates Passing through Zone 15"] = value

    @property
    def cross_sectional_areas_of_air_channel_inlet_15(self):
        """field `Cross Sectional Areas of Air Channel Inlet 15`

        |  Units: m2

        Args:
            value (float): value for IDD Field `Cross Sectional Areas of Air Channel Inlet 15`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `cross_sectional_areas_of_air_channel_inlet_15` or None if not set

        """
        return self["Cross Sectional Areas of Air Channel Inlet 15"]

    @cross_sectional_areas_of_air_channel_inlet_15.setter
    def cross_sectional_areas_of_air_channel_inlet_15(self, value=None):
        """Corresponds to IDD field `Cross Sectional Areas of Air Channel Inlet
        15`"""
        self["Cross Sectional Areas of Air Channel Inlet 15"] = value

    @property
    def zone_16_name(self):
        """field `Zone 16 Name`

        Args:
            value (str): value for IDD Field `Zone 16 Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `zone_16_name` or None if not set

        """
        return self["Zone 16 Name"]

    @zone_16_name.setter
    def zone_16_name(self, value=None):
        """Corresponds to IDD field `Zone 16 Name`"""
        self["Zone 16 Name"] = value

    @property
    def distance_from_top_of_thermal_chimney_to_inlet_16(self):
        """field `Distance from Top of Thermal Chimney to Inlet 16`

        |  Units: m

        Args:
            value (float): value for IDD Field `Distance from Top of Thermal Chimney to Inlet 16`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `distance_from_top_of_thermal_chimney_to_inlet_16` or None if not set

        """
        return self["Distance from Top of Thermal Chimney to Inlet 16"]

    @distance_from_top_of_thermal_chimney_to_inlet_16.setter
    def distance_from_top_of_thermal_chimney_to_inlet_16(self, value=None):
        """Corresponds to IDD field `Distance from Top of Thermal Chimney to
        Inlet 16`"""
        self["Distance from Top of Thermal Chimney to Inlet 16"] = value

    @property
    def relative_ratios_of_air_flow_rates_passing_through_zone_16(self):
        """field `Relative Ratios of Air Flow Rates Passing through Zone 16`

        |  value <= 1.0

        Args:
            value (float): value for IDD Field `Relative Ratios of Air Flow Rates Passing through Zone 16`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `relative_ratios_of_air_flow_rates_passing_through_zone_16` or None if not set

        """
        return self[
            "Relative Ratios of Air Flow Rates Passing through Zone 16"]

    @relative_ratios_of_air_flow_rates_passing_through_zone_16.setter
    def relative_ratios_of_air_flow_rates_passing_through_zone_16(
            self,
            value=None):
        """Corresponds to IDD field `Relative Ratios of Air Flow Rates Passing
        through Zone 16`"""
        self[
            "Relative Ratios of Air Flow Rates Passing through Zone 16"] = value

    @property
    def cross_sectional_areas_of_air_channel_inlet_16(self):
        """field `Cross Sectional Areas of Air Channel Inlet 16`

        |  Units: m2

        Args:
            value (float): value for IDD Field `Cross Sectional Areas of Air Channel Inlet 16`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `cross_sectional_areas_of_air_channel_inlet_16` or None if not set

        """
        return self["Cross Sectional Areas of Air Channel Inlet 16"]

    @cross_sectional_areas_of_air_channel_inlet_16.setter
    def cross_sectional_areas_of_air_channel_inlet_16(self, value=None):
        """Corresponds to IDD field `Cross Sectional Areas of Air Channel Inlet
        16`"""
        self["Cross Sectional Areas of Air Channel Inlet 16"] = value

    @property
    def zone_17_name(self):
        """field `Zone 17 Name`

        Args:
            value (str): value for IDD Field `Zone 17 Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `zone_17_name` or None if not set

        """
        return self["Zone 17 Name"]

    @zone_17_name.setter
    def zone_17_name(self, value=None):
        """Corresponds to IDD field `Zone 17 Name`"""
        self["Zone 17 Name"] = value

    @property
    def distance_from_top_of_thermal_chimney_to_inlet_17(self):
        """field `Distance from Top of Thermal Chimney to Inlet 17`

        |  Units: m

        Args:
            value (float): value for IDD Field `Distance from Top of Thermal Chimney to Inlet 17`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `distance_from_top_of_thermal_chimney_to_inlet_17` or None if not set

        """
        return self["Distance from Top of Thermal Chimney to Inlet 17"]

    @distance_from_top_of_thermal_chimney_to_inlet_17.setter
    def distance_from_top_of_thermal_chimney_to_inlet_17(self, value=None):
        """Corresponds to IDD field `Distance from Top of Thermal Chimney to
        Inlet 17`"""
        self["Distance from Top of Thermal Chimney to Inlet 17"] = value

    @property
    def relative_ratios_of_air_flow_rates_passing_through_zone_17(self):
        """field `Relative Ratios of Air Flow Rates Passing through Zone 17`

        |  value <= 1.0

        Args:
            value (float): value for IDD Field `Relative Ratios of Air Flow Rates Passing through Zone 17`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `relative_ratios_of_air_flow_rates_passing_through_zone_17` or None if not set

        """
        return self[
            "Relative Ratios of Air Flow Rates Passing through Zone 17"]

    @relative_ratios_of_air_flow_rates_passing_through_zone_17.setter
    def relative_ratios_of_air_flow_rates_passing_through_zone_17(
            self,
            value=None):
        """Corresponds to IDD field `Relative Ratios of Air Flow Rates Passing
        through Zone 17`"""
        self[
            "Relative Ratios of Air Flow Rates Passing through Zone 17"] = value

    @property
    def cross_sectional_areas_of_air_channel_inlet_17(self):
        """field `Cross Sectional Areas of Air Channel Inlet 17`

        |  Units: m2

        Args:
            value (float): value for IDD Field `Cross Sectional Areas of Air Channel Inlet 17`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `cross_sectional_areas_of_air_channel_inlet_17` or None if not set

        """
        return self["Cross Sectional Areas of Air Channel Inlet 17"]

    @cross_sectional_areas_of_air_channel_inlet_17.setter
    def cross_sectional_areas_of_air_channel_inlet_17(self, value=None):
        """Corresponds to IDD field `Cross Sectional Areas of Air Channel Inlet
        17`"""
        self["Cross Sectional Areas of Air Channel Inlet 17"] = value

    @property
    def zone_18_name(self):
        """field `Zone 18 Name`

        Args:
            value (str): value for IDD Field `Zone 18 Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `zone_18_name` or None if not set

        """
        return self["Zone 18 Name"]

    @zone_18_name.setter
    def zone_18_name(self, value=None):
        """Corresponds to IDD field `Zone 18 Name`"""
        self["Zone 18 Name"] = value

    @property
    def distance_from_top_of_thermal_chimney_to_inlet_18(self):
        """field `Distance from Top of Thermal Chimney to Inlet 18`

        |  Units: m

        Args:
            value (float): value for IDD Field `Distance from Top of Thermal Chimney to Inlet 18`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `distance_from_top_of_thermal_chimney_to_inlet_18` or None if not set

        """
        return self["Distance from Top of Thermal Chimney to Inlet 18"]

    @distance_from_top_of_thermal_chimney_to_inlet_18.setter
    def distance_from_top_of_thermal_chimney_to_inlet_18(self, value=None):
        """Corresponds to IDD field `Distance from Top of Thermal Chimney to
        Inlet 18`"""
        self["Distance from Top of Thermal Chimney to Inlet 18"] = value

    @property
    def relative_ratios_of_air_flow_rates_passing_through_zone_18(self):
        """field `Relative Ratios of Air Flow Rates Passing through Zone 18`

        |  value <= 1.0

        Args:
            value (float): value for IDD Field `Relative Ratios of Air Flow Rates Passing through Zone 18`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `relative_ratios_of_air_flow_rates_passing_through_zone_18` or None if not set

        """
        return self[
            "Relative Ratios of Air Flow Rates Passing through Zone 18"]

    @relative_ratios_of_air_flow_rates_passing_through_zone_18.setter
    def relative_ratios_of_air_flow_rates_passing_through_zone_18(
            self,
            value=None):
        """Corresponds to IDD field `Relative Ratios of Air Flow Rates Passing
        through Zone 18`"""
        self[
            "Relative Ratios of Air Flow Rates Passing through Zone 18"] = value

    @property
    def cross_sectional_areas_of_air_channel_inlet_18(self):
        """field `Cross Sectional Areas of Air Channel Inlet 18`

        |  Units: m2

        Args:
            value (float): value for IDD Field `Cross Sectional Areas of Air Channel Inlet 18`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `cross_sectional_areas_of_air_channel_inlet_18` or None if not set

        """
        return self["Cross Sectional Areas of Air Channel Inlet 18"]

    @cross_sectional_areas_of_air_channel_inlet_18.setter
    def cross_sectional_areas_of_air_channel_inlet_18(self, value=None):
        """Corresponds to IDD field `Cross Sectional Areas of Air Channel Inlet
        18`"""
        self["Cross Sectional Areas of Air Channel Inlet 18"] = value

    @property
    def zone_19_name(self):
        """field `Zone 19 Name`

        Args:
            value (str): value for IDD Field `Zone 19 Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `zone_19_name` or None if not set

        """
        return self["Zone 19 Name"]

    @zone_19_name.setter
    def zone_19_name(self, value=None):
        """Corresponds to IDD field `Zone 19 Name`"""
        self["Zone 19 Name"] = value

    @property
    def distance_from_top_of_thermal_chimney_to_inlet_19(self):
        """field `Distance from Top of Thermal Chimney to Inlet 19`

        |  Units: m

        Args:
            value (float): value for IDD Field `Distance from Top of Thermal Chimney to Inlet 19`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `distance_from_top_of_thermal_chimney_to_inlet_19` or None if not set

        """
        return self["Distance from Top of Thermal Chimney to Inlet 19"]

    @distance_from_top_of_thermal_chimney_to_inlet_19.setter
    def distance_from_top_of_thermal_chimney_to_inlet_19(self, value=None):
        """Corresponds to IDD field `Distance from Top of Thermal Chimney to
        Inlet 19`"""
        self["Distance from Top of Thermal Chimney to Inlet 19"] = value

    @property
    def relative_ratios_of_air_flow_rates_passing_through_zone_19(self):
        """field `Relative Ratios of Air Flow Rates Passing through Zone 19`

        |  value <= 1.0

        Args:
            value (float): value for IDD Field `Relative Ratios of Air Flow Rates Passing through Zone 19`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `relative_ratios_of_air_flow_rates_passing_through_zone_19` or None if not set

        """
        return self[
            "Relative Ratios of Air Flow Rates Passing through Zone 19"]

    @relative_ratios_of_air_flow_rates_passing_through_zone_19.setter
    def relative_ratios_of_air_flow_rates_passing_through_zone_19(
            self,
            value=None):
        """Corresponds to IDD field `Relative Ratios of Air Flow Rates Passing
        through Zone 19`"""
        self[
            "Relative Ratios of Air Flow Rates Passing through Zone 19"] = value

    @property
    def cross_sectional_areas_of_air_channel_inlet_19(self):
        """field `Cross Sectional Areas of Air Channel Inlet 19`

        |  Units: m2

        Args:
            value (float): value for IDD Field `Cross Sectional Areas of Air Channel Inlet 19`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `cross_sectional_areas_of_air_channel_inlet_19` or None if not set

        """
        return self["Cross Sectional Areas of Air Channel Inlet 19"]

    @cross_sectional_areas_of_air_channel_inlet_19.setter
    def cross_sectional_areas_of_air_channel_inlet_19(self, value=None):
        """Corresponds to IDD field `Cross Sectional Areas of Air Channel Inlet
        19`"""
        self["Cross Sectional Areas of Air Channel Inlet 19"] = value

    @property
    def zone_20_name(self):
        """field `Zone 20 Name`

        Args:
            value (str): value for IDD Field `Zone 20 Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `zone_20_name` or None if not set

        """
        return self["Zone 20 Name"]

    @zone_20_name.setter
    def zone_20_name(self, value=None):
        """Corresponds to IDD field `Zone 20 Name`"""
        self["Zone 20 Name"] = value

    @property
    def distance_from_top_of_thermal_chimney_to_inlet_20(self):
        """field `Distance from Top of Thermal Chimney to Inlet 20`

        |  Units: m

        Args:
            value (float): value for IDD Field `Distance from Top of Thermal Chimney to Inlet 20`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `distance_from_top_of_thermal_chimney_to_inlet_20` or None if not set

        """
        return self["Distance from Top of Thermal Chimney to Inlet 20"]

    @distance_from_top_of_thermal_chimney_to_inlet_20.setter
    def distance_from_top_of_thermal_chimney_to_inlet_20(self, value=None):
        """Corresponds to IDD field `Distance from Top of Thermal Chimney to
        Inlet 20`"""
        self["Distance from Top of Thermal Chimney to Inlet 20"] = value

    @property
    def relative_ratios_of_air_flow_rates_passing_through_zone_20(self):
        """field `Relative Ratios of Air Flow Rates Passing through Zone 20`

        |  value <= 1.0

        Args:
            value (float): value for IDD Field `Relative Ratios of Air Flow Rates Passing through Zone 20`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `relative_ratios_of_air_flow_rates_passing_through_zone_20` or None if not set

        """
        return self[
            "Relative Ratios of Air Flow Rates Passing through Zone 20"]

    @relative_ratios_of_air_flow_rates_passing_through_zone_20.setter
    def relative_ratios_of_air_flow_rates_passing_through_zone_20(
            self,
            value=None):
        """Corresponds to IDD field `Relative Ratios of Air Flow Rates Passing
        through Zone 20`"""
        self[
            "Relative Ratios of Air Flow Rates Passing through Zone 20"] = value

    @property
    def cross_sectional_areas_of_air_channel_inlet_20(self):
        """field `Cross Sectional Areas of Air Channel Inlet 20`

        |  Units: m2

        Args:
            value (float): value for IDD Field `Cross Sectional Areas of Air Channel Inlet 20`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `cross_sectional_areas_of_air_channel_inlet_20` or None if not set

        """
        return self["Cross Sectional Areas of Air Channel Inlet 20"]

    @cross_sectional_areas_of_air_channel_inlet_20.setter
    def cross_sectional_areas_of_air_channel_inlet_20(self, value=None):
        """Corresponds to IDD field `Cross Sectional Areas of Air Channel Inlet
        20`"""
        self["Cross Sectional Areas of Air Channel Inlet 20"] = value


