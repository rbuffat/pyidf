""" Data objects in group "Zone HVAC Controls and Thermostats"
"""

from collections import OrderedDict
import logging
from pyidf.helper import DataObject

logger = logging.getLogger("pyidf")
logger.addHandler(logging.NullHandler())



class ZoneControlHumidistat(DataObject):

    """ Corresponds to IDD object `ZoneControl:Humidistat`
        Specifies zone relative humidity setpoint schedules for humidifying and dehumidifying.
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
                                      (u'humidifying relative humidity setpoint schedule name',
                                       {'name': u'Humidifying Relative Humidity Setpoint Schedule Name',
                                        'pyname': u'humidifying_relative_humidity_setpoint_schedule_name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'dehumidifying relative humidity setpoint schedule name',
                                       {'name': u'Dehumidifying Relative Humidity Setpoint Schedule Name',
                                        'pyname': u'dehumidifying_relative_humidity_setpoint_schedule_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'})]),
               'format': None,
               'group': u'Zone HVAC Controls and Thermostats',
               'min-fields': 3,
               'name': u'ZoneControl:Humidistat',
               'pyname': u'ZoneControlHumidistat',
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
    def humidifying_relative_humidity_setpoint_schedule_name(self):
        """field `Humidifying Relative Humidity Setpoint Schedule Name`

        |  hourly schedule values should be in Relative Humidity (percent)

        Args:
            value (str): value for IDD Field `Humidifying Relative Humidity Setpoint Schedule Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `humidifying_relative_humidity_setpoint_schedule_name` or None if not set

        """
        return self["Humidifying Relative Humidity Setpoint Schedule Name"]

    @humidifying_relative_humidity_setpoint_schedule_name.setter
    def humidifying_relative_humidity_setpoint_schedule_name(self, value=None):
        """Corresponds to IDD field `Humidifying Relative Humidity Setpoint
        Schedule Name`"""
        self["Humidifying Relative Humidity Setpoint Schedule Name"] = value

    @property
    def dehumidifying_relative_humidity_setpoint_schedule_name(self):
        """field `Dehumidifying Relative Humidity Setpoint Schedule Name`

        |  hourly schedule values should be in Relative Humidity (percent)

        Args:
            value (str): value for IDD Field `Dehumidifying Relative Humidity Setpoint Schedule Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `dehumidifying_relative_humidity_setpoint_schedule_name` or None if not set

        """
        return self["Dehumidifying Relative Humidity Setpoint Schedule Name"]

    @dehumidifying_relative_humidity_setpoint_schedule_name.setter
    def dehumidifying_relative_humidity_setpoint_schedule_name(
            self,
            value=None):
        """Corresponds to IDD field `Dehumidifying Relative Humidity Setpoint
        Schedule Name`"""
        self["Dehumidifying Relative Humidity Setpoint Schedule Name"] = value




class ZoneControlThermostat(DataObject):

    """ Corresponds to IDD object `ZoneControl:Thermostat`
        Define the Thermostat settings for a zone or list of zones.
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
                                        'type': 'alpha'}),
                                      (u'zone or zonelist name',
                                       {'name': u'Zone or ZoneList Name',
                                        'pyname': u'zone_or_zonelist_name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'control type schedule name',
                                       {'name': u'Control Type Schedule Name',
                                        'pyname': u'control_type_schedule_name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'control 1 object type',
                                       {'name': u'Control 1 Object Type',
                                        'pyname': u'control_1_object_type',
                                        'required-field': True,
                                        'autosizable': False,
                                        'accepted-values': [u'ThermostatSetpoint:SingleHeating',
                                                            u'ThermostatSetpoint:SingleCooling',
                                                            u'ThermostatSetpoint:SingleHeatingOrCooling',
                                                            u'ThermostatSetpoint:DualSetpoint'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'control 1 name',
                                       {'name': u'Control 1 Name',
                                        'pyname': u'control_1_name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'control 2 object type',
                                       {'name': u'Control 2 Object Type',
                                        'pyname': u'control_2_object_type',
                                        'required-field': False,
                                        'autosizable': False,
                                        'accepted-values': [u'ThermostatSetpoint:SingleHeating',
                                                            u'ThermostatSetpoint:SingleCooling',
                                                            u'ThermostatSetpoint:SingleHeatingOrCooling',
                                                            u'ThermostatSetpoint:DualSetpoint'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'control 2 name',
                                       {'name': u'Control 2 Name',
                                        'pyname': u'control_2_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'control 3 object type',
                                       {'name': u'Control 3 Object Type',
                                        'pyname': u'control_3_object_type',
                                        'required-field': False,
                                        'autosizable': False,
                                        'accepted-values': [u'ThermostatSetpoint:SingleHeating',
                                                            u'ThermostatSetpoint:SingleCooling',
                                                            u'ThermostatSetpoint:SingleHeatingOrCooling',
                                                            u'ThermostatSetpoint:DualSetpoint'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'control 3 name',
                                       {'name': u'Control 3 Name',
                                        'pyname': u'control_3_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'control 4 object type',
                                       {'name': u'Control 4 Object Type',
                                        'pyname': u'control_4_object_type',
                                        'required-field': False,
                                        'autosizable': False,
                                        'accepted-values': [u'ThermostatSetpoint:SingleHeating',
                                                            u'ThermostatSetpoint:SingleCooling',
                                                            u'ThermostatSetpoint:SingleHeatingOrCooling',
                                                            u'ThermostatSetpoint:DualSetpoint'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'control 4 name',
                                       {'name': u'Control 4 Name',
                                        'pyname': u'control_4_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'})]),
               'format': None,
               'group': u'Zone HVAC Controls and Thermostats',
               'min-fields': 0,
               'name': u'ZoneControl:Thermostat',
               'pyname': u'ZoneControlThermostat',
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
    def control_type_schedule_name(self):
        """field `Control Type Schedule Name`

        |  This schedule contains appropriate control types for thermostat.
        |  Control types are integers: 0 - Uncontrolled (floating, no thermostat), 1 = ThermostatSetpoint:SingleHeating,
        |  2 = ThermostatSetpoint:SingleCooling, 3 = ThermostatSetpoint:SingleHeatingOrCooling, 4 = ThermostatSetpoint:DualSetpoint

        Args:
            value (str): value for IDD Field `Control Type Schedule Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `control_type_schedule_name` or None if not set

        """
        return self["Control Type Schedule Name"]

    @control_type_schedule_name.setter
    def control_type_schedule_name(self, value=None):
        """Corresponds to IDD field `Control Type Schedule Name`"""
        self["Control Type Schedule Name"] = value

    @property
    def control_1_object_type(self):
        """field `Control 1 Object Type`

        Args:
            value (str): value for IDD Field `Control 1 Object Type`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `control_1_object_type` or None if not set

        """
        return self["Control 1 Object Type"]

    @control_1_object_type.setter
    def control_1_object_type(self, value=None):
        """Corresponds to IDD field `Control 1 Object Type`"""
        self["Control 1 Object Type"] = value

    @property
    def control_1_name(self):
        """field `Control 1 Name`

        |  Control names are names of individual control objects (e.g. ThermostatSetpoint:SingleHeating)
        |  Schedule values in these objects list actual setpoint temperatures for the control types

        Args:
            value (str): value for IDD Field `Control 1 Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `control_1_name` or None if not set

        """
        return self["Control 1 Name"]

    @control_1_name.setter
    def control_1_name(self, value=None):
        """Corresponds to IDD field `Control 1 Name`"""
        self["Control 1 Name"] = value

    @property
    def control_2_object_type(self):
        """field `Control 2 Object Type`

        Args:
            value (str): value for IDD Field `Control 2 Object Type`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `control_2_object_type` or None if not set

        """
        return self["Control 2 Object Type"]

    @control_2_object_type.setter
    def control_2_object_type(self, value=None):
        """Corresponds to IDD field `Control 2 Object Type`"""
        self["Control 2 Object Type"] = value

    @property
    def control_2_name(self):
        """field `Control 2 Name`

        |  Control names are names of individual control objects (e.g. ThermostatSetpoint:SingleHeating)
        |  Schedule values in these objects list actual setpoint temperatures for the control types

        Args:
            value (str): value for IDD Field `Control 2 Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `control_2_name` or None if not set

        """
        return self["Control 2 Name"]

    @control_2_name.setter
    def control_2_name(self, value=None):
        """Corresponds to IDD field `Control 2 Name`"""
        self["Control 2 Name"] = value

    @property
    def control_3_object_type(self):
        """field `Control 3 Object Type`

        Args:
            value (str): value for IDD Field `Control 3 Object Type`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `control_3_object_type` or None if not set

        """
        return self["Control 3 Object Type"]

    @control_3_object_type.setter
    def control_3_object_type(self, value=None):
        """Corresponds to IDD field `Control 3 Object Type`"""
        self["Control 3 Object Type"] = value

    @property
    def control_3_name(self):
        """field `Control 3 Name`

        |  Control names are names of individual control objects (e.g. ThermostatSetpoint:SingleHeating)
        |  Schedule values in these objects list actual setpoint temperatures for the control types

        Args:
            value (str): value for IDD Field `Control 3 Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `control_3_name` or None if not set

        """
        return self["Control 3 Name"]

    @control_3_name.setter
    def control_3_name(self, value=None):
        """Corresponds to IDD field `Control 3 Name`"""
        self["Control 3 Name"] = value

    @property
    def control_4_object_type(self):
        """field `Control 4 Object Type`

        Args:
            value (str): value for IDD Field `Control 4 Object Type`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `control_4_object_type` or None if not set

        """
        return self["Control 4 Object Type"]

    @control_4_object_type.setter
    def control_4_object_type(self, value=None):
        """Corresponds to IDD field `Control 4 Object Type`"""
        self["Control 4 Object Type"] = value

    @property
    def control_4_name(self):
        """field `Control 4 Name`

        |  Control names are names of individual control objects (e.g. ThermostatSetpoint:SingleHeating)
        |  Schedule values in these objects list actual setpoint temperatures for the control types

        Args:
            value (str): value for IDD Field `Control 4 Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `control_4_name` or None if not set

        """
        return self["Control 4 Name"]

    @control_4_name.setter
    def control_4_name(self, value=None):
        """Corresponds to IDD field `Control 4 Name`"""
        self["Control 4 Name"] = value




class ZoneControlThermostatOperativeTemperature(DataObject):

    """ Corresponds to IDD object `ZoneControl:Thermostat:OperativeTemperature`
        This object can be used with the ZoneList option on a thermostat or with one
        of the zones on that list (but you won't be able to use the object list to
        pick only one of those zones.  Thermostat names are <Zone Name> <global Thermostat name> internally.
    """
    _schema = {'extensible-fields': OrderedDict(),
               'fields': OrderedDict([(u'thermostat name',
                                       {'name': u'Thermostat Name',
                                        'pyname': u'thermostat_name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'radiative fraction input mode',
                                       {'name': u'Radiative Fraction Input Mode',
                                        'pyname': u'radiative_fraction_input_mode',
                                        'required-field': True,
                                        'autosizable': False,
                                        'accepted-values': [u'Constant',
                                                            u'Scheduled'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'fixed radiative fraction',
                                       {'name': u'Fixed Radiative Fraction',
                                        'pyname': u'fixed_radiative_fraction',
                                        'maximum<': 0.9,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': 'real'}),
                                      (u'radiative fraction schedule name',
                                       {'name': u'Radiative Fraction Schedule Name',
                                        'pyname': u'radiative_fraction_schedule_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'})]),
               'format': None,
               'group': u'Zone HVAC Controls and Thermostats',
               'min-fields': 0,
               'name': u'ZoneControl:Thermostat:OperativeTemperature',
               'pyname': u'ZoneControlThermostatOperativeTemperature',
               'required-object': False,
               'unique-object': False}

    @property
    def thermostat_name(self):
        """field `Thermostat Name`

        |  Enter the name of a ZoneControl:Thermostat object.
        |  This object modifies a ZoneControl:Thermostat object to add a
        |  radiative fraction.

        Args:
            value (str): value for IDD Field `Thermostat Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `thermostat_name` or None if not set

        """
        return self["Thermostat Name"]

    @thermostat_name.setter
    def thermostat_name(self, value=None):
        """Corresponds to IDD field `Thermostat Name`"""
        self["Thermostat Name"] = value

    @property
    def radiative_fraction_input_mode(self):
        """field `Radiative Fraction Input Mode`

        Args:
            value (str): value for IDD Field `Radiative Fraction Input Mode`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `radiative_fraction_input_mode` or None if not set

        """
        return self["Radiative Fraction Input Mode"]

    @radiative_fraction_input_mode.setter
    def radiative_fraction_input_mode(self, value=None):
        """Corresponds to IDD field `Radiative Fraction Input Mode`"""
        self["Radiative Fraction Input Mode"] = value

    @property
    def fixed_radiative_fraction(self):
        """field `Fixed Radiative Fraction`

        |  value < 0.9

        Args:
            value (float): value for IDD Field `Fixed Radiative Fraction`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `fixed_radiative_fraction` or None if not set

        """
        return self["Fixed Radiative Fraction"]

    @fixed_radiative_fraction.setter
    def fixed_radiative_fraction(self, value=None):
        """Corresponds to IDD field `Fixed Radiative Fraction`"""
        self["Fixed Radiative Fraction"] = value

    @property
    def radiative_fraction_schedule_name(self):
        """field `Radiative Fraction Schedule Name`

        |  Schedule values of 0.0 indicate no operative temperature control

        Args:
            value (str): value for IDD Field `Radiative Fraction Schedule Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `radiative_fraction_schedule_name` or None if not set

        """
        return self["Radiative Fraction Schedule Name"]

    @radiative_fraction_schedule_name.setter
    def radiative_fraction_schedule_name(self, value=None):
        """Corresponds to IDD field `Radiative Fraction Schedule Name`"""
        self["Radiative Fraction Schedule Name"] = value




class ZoneControlThermostatThermalComfort(DataObject):

    """ Corresponds to IDD object `ZoneControl:Thermostat:ThermalComfort`
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
                                        'type': 'alpha'}),
                                      (u'zone or zonelist name',
                                       {'name': u'Zone or ZoneList Name',
                                        'pyname': u'zone_or_zonelist_name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'averaging method',
                                       {'name': u'Averaging Method',
                                        'pyname': u'averaging_method',
                                        'default': u'PeopleAverage',
                                        'required-field': False,
                                        'autosizable': False,
                                        'accepted-values': [u'SpecificObject',
                                                            u'ObjectAverage',
                                                            u'PeopleAverage'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'specific people name',
                                       {'name': u'Specific People Name',
                                        'pyname': u'specific_people_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'minimum dry-bulb temperature setpoint',
                                       {'name': u'Minimum Dry-Bulb Temperature Setpoint',
                                        'pyname': u'minimum_drybulb_temperature_setpoint',
                                        'default': 0.0,
                                        'maximum': 50.0,
                                        'required-field': True,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'C'}),
                                      (u'maximum dry-bulb temperature setpoint',
                                       {'name': u'Maximum Dry-Bulb Temperature Setpoint',
                                        'pyname': u'maximum_drybulb_temperature_setpoint',
                                        'default': 50.0,
                                        'maximum': 50.0,
                                        'required-field': True,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'C'}),
                                      (u'thermal comfort control type schedule name',
                                       {'name': u'Thermal Comfort Control Type Schedule Name',
                                        'pyname': u'thermal_comfort_control_type_schedule_name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'thermal comfort control 1 object type',
                                       {'name': u'Thermal Comfort Control 1 Object Type',
                                        'pyname': u'thermal_comfort_control_1_object_type',
                                        'required-field': True,
                                        'autosizable': False,
                                        'accepted-values': [u'ThermostatSetpoint:ThermalComfort:Fanger:SingleHeating',
                                                            u'ThermostatSetpoint:ThermalComfort:Fanger:SingleCooling',
                                                            u'ThermostatSetpoint:ThermalComfort:Fanger:SingleHeatingOrCooling',
                                                            u'ThermostatSetpoint:ThermalComfort:Fanger:DualSetpoint'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'thermal comfort control 1 name',
                                       {'name': u'Thermal Comfort Control 1 Name',
                                        'pyname': u'thermal_comfort_control_1_name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'thermal comfort control 2 object type',
                                       {'name': u'Thermal Comfort Control 2 Object Type',
                                        'pyname': u'thermal_comfort_control_2_object_type',
                                        'required-field': False,
                                        'autosizable': False,
                                        'accepted-values': [u'ThermostatSetpoint:ThermalComfort:Fanger:SingleHeating',
                                                            u'ThermostatSetpoint:ThermalComfort:Fanger:SingleCooling',
                                                            u'ThermostatSetpoint:ThermalComfort:Fanger:SingleHeatingOrCooling',
                                                            u'ThermostatSetpoint:ThermalComfort:Fanger:DualSetpoint'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'thermal comfort control 2 name',
                                       {'name': u'Thermal Comfort Control 2 Name',
                                        'pyname': u'thermal_comfort_control_2_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'thermal comfort control 3 object type',
                                       {'name': u'Thermal Comfort Control 3 Object Type',
                                        'pyname': u'thermal_comfort_control_3_object_type',
                                        'required-field': False,
                                        'autosizable': False,
                                        'accepted-values': [u'ThermostatSetpoint:ThermalComfort:Fanger:SingleHeating',
                                                            u'ThermostatSetpoint:ThermalComfort:Fanger:SingleCooling',
                                                            u'ThermostatSetpoint:ThermalComfort:Fanger:SingleHeatingOrCooling',
                                                            u'ThermostatSetpoint:ThermalComfort:Fanger:DualSetpoint'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'thermal comfort control 3 name',
                                       {'name': u'Thermal Comfort Control 3 Name',
                                        'pyname': u'thermal_comfort_control_3_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'thermal comfort control 4 object type',
                                       {'name': u'Thermal Comfort Control 4 Object Type',
                                        'pyname': u'thermal_comfort_control_4_object_type',
                                        'required-field': False,
                                        'autosizable': False,
                                        'accepted-values': [u'ThermostatSetpoint:ThermalComfort:Fanger:SingleHeating',
                                                            u'ThermostatSetpoint:ThermalComfort:Fanger:SingleCooling',
                                                            u'ThermostatSetpoint:ThermalComfort:Fanger:SingleHeatingOrCooling',
                                                            u'ThermostatSetpoint:ThermalComfort:Fanger:DualSetpoint'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'thermal comfort control 4 name',
                                       {'name': u'Thermal Comfort Control 4 Name',
                                        'pyname': u'thermal_comfort_control_4_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'})]),
               'format': None,
               'group': u'Zone HVAC Controls and Thermostats',
               'min-fields': 9,
               'name': u'ZoneControl:Thermostat:ThermalComfort',
               'pyname': u'ZoneControlThermostatThermalComfort',
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
    def averaging_method(self):
        """field `Averaging Method`

        |  The method used to calculate thermal comfort dry-bulb temperature setpoint
        |  for multiple people objects in a zone
        |  Default value: PeopleAverage

        Args:
            value (str): value for IDD Field `Averaging Method`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `averaging_method` or None if not set

        """
        return self["Averaging Method"]

    @averaging_method.setter
    def averaging_method(self, value="PeopleAverage"):
        """Corresponds to IDD field `Averaging Method`"""
        self["Averaging Method"] = value

    @property
    def specific_people_name(self):
        """field `Specific People Name`

        |  Used only when Averaging Method = SpecificObject in the previous field.

        Args:
            value (str): value for IDD Field `Specific People Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `specific_people_name` or None if not set

        """
        return self["Specific People Name"]

    @specific_people_name.setter
    def specific_people_name(self, value=None):
        """Corresponds to IDD field `Specific People Name`"""
        self["Specific People Name"] = value

    @property
    def minimum_drybulb_temperature_setpoint(self):
        """field `Minimum Dry-Bulb Temperature Setpoint`

        |  Units: C
        |  value <= 50.0

        Args:
            value (float): value for IDD Field `Minimum Dry-Bulb Temperature Setpoint`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `minimum_drybulb_temperature_setpoint` or None if not set
        """
        return self["Minimum Dry-Bulb Temperature Setpoint"]

    @minimum_drybulb_temperature_setpoint.setter
    def minimum_drybulb_temperature_setpoint(self, value=None):
        """  Corresponds to IDD field `Minimum Dry-Bulb Temperature Setpoint`

        """
        self["Minimum Dry-Bulb Temperature Setpoint"] = value

    @property
    def maximum_drybulb_temperature_setpoint(self):
        """field `Maximum Dry-Bulb Temperature Setpoint`

        |  Units: C
        |  Default value: 50.0
        |  value <= 50.0

        Args:
            value (float): value for IDD Field `Maximum Dry-Bulb Temperature Setpoint`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `maximum_drybulb_temperature_setpoint` or None if not set
        """
        return self["Maximum Dry-Bulb Temperature Setpoint"]

    @maximum_drybulb_temperature_setpoint.setter
    def maximum_drybulb_temperature_setpoint(self, value=50.0):
        """  Corresponds to IDD field `Maximum Dry-Bulb Temperature Setpoint`

        """
        self["Maximum Dry-Bulb Temperature Setpoint"] = value

    @property
    def thermal_comfort_control_type_schedule_name(self):
        """field `Thermal Comfort Control Type Schedule Name`

        |  The Thermal Comfort Control Type Schedule contains values that are appropriate control types.
        |  Thermal Comfort Control types are integers: 0 - Uncontrolled (floating),
        |  1 = ThermostatSetpoint:ThermalComfort:Fanger:SingleHeating
        |  2 = ThermostatSetpoint:ThermalComfort:Fanger:SingleCooling
        |  3 = ThermostatSetpoint:ThermalComfort:Fanger:SingleHeatingOrCooling
        |  4 = ThermostatSetpoint:ThermalComfort:Fanger:DualSetpoint

        Args:
            value (str): value for IDD Field `Thermal Comfort Control Type Schedule Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `thermal_comfort_control_type_schedule_name` or None if not set

        """
        return self["Thermal Comfort Control Type Schedule Name"]

    @thermal_comfort_control_type_schedule_name.setter
    def thermal_comfort_control_type_schedule_name(self, value=None):
        """Corresponds to IDD field `Thermal Comfort Control Type Schedule
        Name`"""
        self["Thermal Comfort Control Type Schedule Name"] = value

    @property
    def thermal_comfort_control_1_object_type(self):
        """field `Thermal Comfort Control 1 Object Type`

        Args:
            value (str): value for IDD Field `Thermal Comfort Control 1 Object Type`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `thermal_comfort_control_1_object_type` or None if not set

        """
        return self["Thermal Comfort Control 1 Object Type"]

    @thermal_comfort_control_1_object_type.setter
    def thermal_comfort_control_1_object_type(self, value=None):
        """Corresponds to IDD field `Thermal Comfort Control 1 Object Type`"""
        self["Thermal Comfort Control 1 Object Type"] = value

    @property
    def thermal_comfort_control_1_name(self):
        """field `Thermal Comfort Control 1 Name`

        |  Control type names are names for individual control type objects.
        |  Schedule values in these objects list actual setpoint temperatures for the control types

        Args:
            value (str): value for IDD Field `Thermal Comfort Control 1 Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `thermal_comfort_control_1_name` or None if not set

        """
        return self["Thermal Comfort Control 1 Name"]

    @thermal_comfort_control_1_name.setter
    def thermal_comfort_control_1_name(self, value=None):
        """Corresponds to IDD field `Thermal Comfort Control 1 Name`"""
        self["Thermal Comfort Control 1 Name"] = value

    @property
    def thermal_comfort_control_2_object_type(self):
        """field `Thermal Comfort Control 2 Object Type`

        Args:
            value (str): value for IDD Field `Thermal Comfort Control 2 Object Type`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `thermal_comfort_control_2_object_type` or None if not set

        """
        return self["Thermal Comfort Control 2 Object Type"]

    @thermal_comfort_control_2_object_type.setter
    def thermal_comfort_control_2_object_type(self, value=None):
        """Corresponds to IDD field `Thermal Comfort Control 2 Object Type`"""
        self["Thermal Comfort Control 2 Object Type"] = value

    @property
    def thermal_comfort_control_2_name(self):
        """field `Thermal Comfort Control 2 Name`

        |  Control Type names are names for individual control type objects.
        |  Schedule values in these objects list actual setpoint temperatures for the control types

        Args:
            value (str): value for IDD Field `Thermal Comfort Control 2 Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `thermal_comfort_control_2_name` or None if not set

        """
        return self["Thermal Comfort Control 2 Name"]

    @thermal_comfort_control_2_name.setter
    def thermal_comfort_control_2_name(self, value=None):
        """Corresponds to IDD field `Thermal Comfort Control 2 Name`"""
        self["Thermal Comfort Control 2 Name"] = value

    @property
    def thermal_comfort_control_3_object_type(self):
        """field `Thermal Comfort Control 3 Object Type`

        Args:
            value (str): value for IDD Field `Thermal Comfort Control 3 Object Type`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `thermal_comfort_control_3_object_type` or None if not set

        """
        return self["Thermal Comfort Control 3 Object Type"]

    @thermal_comfort_control_3_object_type.setter
    def thermal_comfort_control_3_object_type(self, value=None):
        """Corresponds to IDD field `Thermal Comfort Control 3 Object Type`"""
        self["Thermal Comfort Control 3 Object Type"] = value

    @property
    def thermal_comfort_control_3_name(self):
        """field `Thermal Comfort Control 3 Name`

        |  Control type names are names for individual control type objects.
        |  Schedule values in these objects list actual setpoint temperatures for the control types

        Args:
            value (str): value for IDD Field `Thermal Comfort Control 3 Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `thermal_comfort_control_3_name` or None if not set

        """
        return self["Thermal Comfort Control 3 Name"]

    @thermal_comfort_control_3_name.setter
    def thermal_comfort_control_3_name(self, value=None):
        """Corresponds to IDD field `Thermal Comfort Control 3 Name`"""
        self["Thermal Comfort Control 3 Name"] = value

    @property
    def thermal_comfort_control_4_object_type(self):
        """field `Thermal Comfort Control 4 Object Type`

        Args:
            value (str): value for IDD Field `Thermal Comfort Control 4 Object Type`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `thermal_comfort_control_4_object_type` or None if not set

        """
        return self["Thermal Comfort Control 4 Object Type"]

    @thermal_comfort_control_4_object_type.setter
    def thermal_comfort_control_4_object_type(self, value=None):
        """Corresponds to IDD field `Thermal Comfort Control 4 Object Type`"""
        self["Thermal Comfort Control 4 Object Type"] = value

    @property
    def thermal_comfort_control_4_name(self):
        """field `Thermal Comfort Control 4 Name`

        |  Control type names are names for individual control type objects.
        |  Schedule values in these objects list actual setpoint temperatures for the control types

        Args:
            value (str): value for IDD Field `Thermal Comfort Control 4 Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `thermal_comfort_control_4_name` or None if not set

        """
        return self["Thermal Comfort Control 4 Name"]

    @thermal_comfort_control_4_name.setter
    def thermal_comfort_control_4_name(self, value=None):
        """Corresponds to IDD field `Thermal Comfort Control 4 Name`"""
        self["Thermal Comfort Control 4 Name"] = value




class ZoneControlThermostatTemperatureAndHumidity(DataObject):

    """ Corresponds to IDD object `ZoneControl:Thermostat:TemperatureAndHumidity`
        This object modifies a ZoneControl:Thermostat object to effect temperature control based on
        zone air humidity conditions.
    """
    _schema = {'extensible-fields': OrderedDict(),
               'fields': OrderedDict([(u'thermostat name',
                                       {'name': u'Thermostat Name',
                                        'pyname': u'thermostat_name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'dehumidifying relative humidity setpoint schedule name',
                                       {'name': u'Dehumidifying Relative Humidity Setpoint Schedule Name',
                                        'pyname': u'dehumidifying_relative_humidity_setpoint_schedule_name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'dehumidification control type',
                                       {'name': u'Dehumidification Control Type',
                                        'pyname': u'dehumidification_control_type',
                                        'default': u'Overcool',
                                        'required-field': False,
                                        'autosizable': False,
                                        'accepted-values': [u'Overcool',
                                                            u'None'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'overcool range input method',
                                       {'name': u'Overcool Range Input Method',
                                        'pyname': u'overcool_range_input_method',
                                        'default': u'Constant',
                                        'required-field': False,
                                        'autosizable': False,
                                        'accepted-values': [u'Constant',
                                                            u'Scheduled'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'overcool constant range',
                                       {'name': u'Overcool Constant Range',
                                        'pyname': u'overcool_constant_range',
                                        'default': 1.7,
                                        'maximum': 3.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'deltaC'}),
                                      (u'overcool range schedule name',
                                       {'name': u'Overcool Range Schedule Name',
                                        'pyname': u'overcool_range_schedule_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'overcool control ratio',
                                       {'name': u'Overcool Control Ratio',
                                        'pyname': u'overcool_control_ratio',
                                        'default': 3.6,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'percent/K'})]),
               'format': None,
               'group': u'Zone HVAC Controls and Thermostats',
               'min-fields': 2,
               'name': u'ZoneControl:Thermostat:TemperatureAndHumidity',
               'pyname': u'ZoneControlThermostatTemperatureAndHumidity',
               'required-object': False,
               'unique-object': False}

    @property
    def thermostat_name(self):
        """field `Thermostat Name`

        |  Enter the name of a ZoneControl:Thermostat object whose operation is to be modified to
        |  effect temperature control based on zone air humidity conditions. If the ZoneControl:
        |  Thermostat object references a ZoneList, simply enter the name of the ZoneControl:Thermostat
        |  object and this temperature and humidity thermostat control will be applied to all zones
        |  in the ZoneList. If the ZoneControl:Thermostat object references a ZoneList but it is
        |  desired that only a single zone within the ZoneList be controlled based on temperature and
        |  humidity control, then the name to be put here is <Zone Name> <Thermostat Name> where the
        |  Thermostat Name is the the name of the ZoneControl:Thermostat object.

        Args:
            value (str): value for IDD Field `Thermostat Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `thermostat_name` or None if not set

        """
        return self["Thermostat Name"]

    @thermostat_name.setter
    def thermostat_name(self, value=None):
        """Corresponds to IDD field `Thermostat Name`"""
        self["Thermostat Name"] = value

    @property
    def dehumidifying_relative_humidity_setpoint_schedule_name(self):
        """field `Dehumidifying Relative Humidity Setpoint Schedule Name`

        |  Schedule values should be in Relative Humidity (percent)

        Args:
            value (str): value for IDD Field `Dehumidifying Relative Humidity Setpoint Schedule Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `dehumidifying_relative_humidity_setpoint_schedule_name` or None if not set

        """
        return self["Dehumidifying Relative Humidity Setpoint Schedule Name"]

    @dehumidifying_relative_humidity_setpoint_schedule_name.setter
    def dehumidifying_relative_humidity_setpoint_schedule_name(
            self,
            value=None):
        """Corresponds to IDD field `Dehumidifying Relative Humidity Setpoint
        Schedule Name`"""
        self["Dehumidifying Relative Humidity Setpoint Schedule Name"] = value

    @property
    def dehumidification_control_type(self):
        """field `Dehumidification Control Type`

        |  Default value: Overcool

        Args:
            value (str): value for IDD Field `Dehumidification Control Type`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `dehumidification_control_type` or None if not set

        """
        return self["Dehumidification Control Type"]

    @dehumidification_control_type.setter
    def dehumidification_control_type(self, value="Overcool"):
        """Corresponds to IDD field `Dehumidification Control Type`"""
        self["Dehumidification Control Type"] = value

    @property
    def overcool_range_input_method(self):
        """field `Overcool Range Input Method`

        |  Default value: Constant

        Args:
            value (str): value for IDD Field `Overcool Range Input Method`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `overcool_range_input_method` or None if not set

        """
        return self["Overcool Range Input Method"]

    @overcool_range_input_method.setter
    def overcool_range_input_method(self, value="Constant"):
        """Corresponds to IDD field `Overcool Range Input Method`"""
        self["Overcool Range Input Method"] = value

    @property
    def overcool_constant_range(self):
        """field `Overcool Constant Range`

        |  Maximum Overcool temperature range for cooling setpoint reduction.
        |  Used with Dehumidification Control Type = Overcool.
        |  A value of 0.0 indicates no zone temperature overcooling will be provided to
        |  gain additional dehumidification.
        |  Units: deltaC
        |  Default value: 1.7
        |  value <= 3.0

        Args:
            value (float): value for IDD Field `Overcool Constant Range`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `overcool_constant_range` or None if not set

        """
        return self["Overcool Constant Range"]

    @overcool_constant_range.setter
    def overcool_constant_range(self, value=1.7):
        """Corresponds to IDD field `Overcool Constant Range`"""
        self["Overcool Constant Range"] = value

    @property
    def overcool_range_schedule_name(self):
        """field `Overcool Range Schedule Name`

        |  Schedule values of 0.0 indicates no zone temperature overcooling will be
        |  provided to gain additional dehumidification.
        |  Schedule values should be >= 0 and <= 3 (deltaC).

        Args:
            value (str): value for IDD Field `Overcool Range Schedule Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `overcool_range_schedule_name` or None if not set

        """
        return self["Overcool Range Schedule Name"]

    @overcool_range_schedule_name.setter
    def overcool_range_schedule_name(self, value=None):
        """Corresponds to IDD field `Overcool Range Schedule Name`"""
        self["Overcool Range Schedule Name"] = value

    @property
    def overcool_control_ratio(self):
        """field `Overcool Control Ratio`

        |  The value of this input field is used to adjust the cooling setpoint temperature
        |  (established by the associated ZoneControl:Thermostat object) downward based on the
        |  difference between the zone air relative humidity level and the dehumidifying
        |  relative humidity setpoint.
        |  Units: percent/K
        |  Default value: 3.6

        Args:
            value (float): value for IDD Field `Overcool Control Ratio`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `overcool_control_ratio` or None if not set

        """
        return self["Overcool Control Ratio"]

    @overcool_control_ratio.setter
    def overcool_control_ratio(self, value=3.6):
        """Corresponds to IDD field `Overcool Control Ratio`"""
        self["Overcool Control Ratio"] = value




class ThermostatSetpointSingleHeating(DataObject):

    """ Corresponds to IDD object `ThermostatSetpoint:SingleHeating`
        Used for a heating only thermostat. The setpoint can be scheduled and varied throughout
        the simulation but only heating is allowed with this control type.
    """
    _schema = {'extensible-fields': OrderedDict(),
               'fields': OrderedDict([(u'name',
                                       {'name': u'Name',
                                        'pyname': u'name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'alpha'}),
                                      (u'setpoint temperature schedule name',
                                       {'name': u'Setpoint Temperature Schedule Name',
                                        'pyname': u'setpoint_temperature_schedule_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'})]),
               'format': None,
               'group': u'Zone HVAC Controls and Thermostats',
               'min-fields': 0,
               'name': u'ThermostatSetpoint:SingleHeating',
               'pyname': u'ThermostatSetpointSingleHeating',
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
    def setpoint_temperature_schedule_name(self):
        """field `Setpoint Temperature Schedule Name`

        Args:
            value (str): value for IDD Field `Setpoint Temperature Schedule Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `setpoint_temperature_schedule_name` or None if not set

        """
        return self["Setpoint Temperature Schedule Name"]

    @setpoint_temperature_schedule_name.setter
    def setpoint_temperature_schedule_name(self, value=None):
        """Corresponds to IDD field `Setpoint Temperature Schedule Name`"""
        self["Setpoint Temperature Schedule Name"] = value




class ThermostatSetpointSingleCooling(DataObject):

    """ Corresponds to IDD object `ThermostatSetpoint:SingleCooling`
        Used for a cooling only thermostat. The setpoint can be scheduled and varied throughout
        the simulation but only cooling is allowed.
    """
    _schema = {'extensible-fields': OrderedDict(),
               'fields': OrderedDict([(u'name',
                                       {'name': u'Name',
                                        'pyname': u'name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'alpha'}),
                                      (u'setpoint temperature schedule name',
                                       {'name': u'Setpoint Temperature Schedule Name',
                                        'pyname': u'setpoint_temperature_schedule_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'})]),
               'format': None,
               'group': u'Zone HVAC Controls and Thermostats',
               'min-fields': 0,
               'name': u'ThermostatSetpoint:SingleCooling',
               'pyname': u'ThermostatSetpointSingleCooling',
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
    def setpoint_temperature_schedule_name(self):
        """field `Setpoint Temperature Schedule Name`

        Args:
            value (str): value for IDD Field `Setpoint Temperature Schedule Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `setpoint_temperature_schedule_name` or None if not set

        """
        return self["Setpoint Temperature Schedule Name"]

    @setpoint_temperature_schedule_name.setter
    def setpoint_temperature_schedule_name(self, value=None):
        """Corresponds to IDD field `Setpoint Temperature Schedule Name`"""
        self["Setpoint Temperature Schedule Name"] = value




class ThermostatSetpointSingleHeatingOrCooling(DataObject):

    """ Corresponds to IDD object `ThermostatSetpoint:SingleHeatingOrCooling`
        Used for a heating and cooling thermostat with a single setpoint. The setpoint can be
        scheduled and varied throughout the simulation for both heating and cooling.
    """
    _schema = {'extensible-fields': OrderedDict(),
               'fields': OrderedDict([(u'name',
                                       {'name': u'Name',
                                        'pyname': u'name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'alpha'}),
                                      (u'setpoint temperature schedule name',
                                       {'name': u'Setpoint Temperature Schedule Name',
                                        'pyname': u'setpoint_temperature_schedule_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'})]),
               'format': None,
               'group': u'Zone HVAC Controls and Thermostats',
               'min-fields': 0,
               'name': u'ThermostatSetpoint:SingleHeatingOrCooling',
               'pyname': u'ThermostatSetpointSingleHeatingOrCooling',
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
    def setpoint_temperature_schedule_name(self):
        """field `Setpoint Temperature Schedule Name`

        Args:
            value (str): value for IDD Field `Setpoint Temperature Schedule Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `setpoint_temperature_schedule_name` or None if not set

        """
        return self["Setpoint Temperature Schedule Name"]

    @setpoint_temperature_schedule_name.setter
    def setpoint_temperature_schedule_name(self, value=None):
        """Corresponds to IDD field `Setpoint Temperature Schedule Name`"""
        self["Setpoint Temperature Schedule Name"] = value




class ThermostatSetpointDualSetpoint(DataObject):

    """ Corresponds to IDD object `ThermostatSetpoint:DualSetpoint`
        Used for a heating and cooling thermostat with dual setpoints. The setpoints can be
        scheduled and varied throughout the simulation for both heating and cooling.
    """
    _schema = {'extensible-fields': OrderedDict(),
               'fields': OrderedDict([(u'name',
                                       {'name': u'Name',
                                        'pyname': u'name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'alpha'}),
                                      (u'heating setpoint temperature schedule name',
                                       {'name': u'Heating Setpoint Temperature Schedule Name',
                                        'pyname': u'heating_setpoint_temperature_schedule_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'cooling setpoint temperature schedule name',
                                       {'name': u'Cooling Setpoint Temperature Schedule Name',
                                        'pyname': u'cooling_setpoint_temperature_schedule_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'})]),
               'format': None,
               'group': u'Zone HVAC Controls and Thermostats',
               'min-fields': 0,
               'name': u'ThermostatSetpoint:DualSetpoint',
               'pyname': u'ThermostatSetpointDualSetpoint',
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
    def heating_setpoint_temperature_schedule_name(self):
        """field `Heating Setpoint Temperature Schedule Name`

        Args:
            value (str): value for IDD Field `Heating Setpoint Temperature Schedule Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `heating_setpoint_temperature_schedule_name` or None if not set

        """
        return self["Heating Setpoint Temperature Schedule Name"]

    @heating_setpoint_temperature_schedule_name.setter
    def heating_setpoint_temperature_schedule_name(self, value=None):
        """Corresponds to IDD field `Heating Setpoint Temperature Schedule
        Name`"""
        self["Heating Setpoint Temperature Schedule Name"] = value

    @property
    def cooling_setpoint_temperature_schedule_name(self):
        """field `Cooling Setpoint Temperature Schedule Name`

        Args:
            value (str): value for IDD Field `Cooling Setpoint Temperature Schedule Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `cooling_setpoint_temperature_schedule_name` or None if not set

        """
        return self["Cooling Setpoint Temperature Schedule Name"]

    @cooling_setpoint_temperature_schedule_name.setter
    def cooling_setpoint_temperature_schedule_name(self, value=None):
        """Corresponds to IDD field `Cooling Setpoint Temperature Schedule
        Name`"""
        self["Cooling Setpoint Temperature Schedule Name"] = value




class ThermostatSetpointThermalComfortFangerSingleHeating(DataObject):

    """ Corresponds to IDD object `ThermostatSetpoint:ThermalComfort:Fanger:SingleHeating`
        Used for heating only thermal comfort control. The PMV setpoint can be scheduled and
        varied throughout the simulation but only heating is allowed with this control type.
    """
    _schema = {'extensible-fields': OrderedDict(),
               'fields': OrderedDict([(u'name',
                                       {'name': u'Name',
                                        'pyname': u'name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'alpha'}),
                                      (u'fanger thermal comfort schedule name',
                                       {'name': u'Fanger Thermal Comfort Schedule Name',
                                        'pyname': u'fanger_thermal_comfort_schedule_name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'})]),
               'format': None,
               'group': u'Zone HVAC Controls and Thermostats',
               'min-fields': 2,
               'name': u'ThermostatSetpoint:ThermalComfort:Fanger:SingleHeating',
               'pyname': u'ThermostatSetpointThermalComfortFangerSingleHeating',
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
    def fanger_thermal_comfort_schedule_name(self):
        """field `Fanger Thermal Comfort Schedule Name`

        |  Schedule values should be Predicted Mean Vote (PMV)

        Args:
            value (str): value for IDD Field `Fanger Thermal Comfort Schedule Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `fanger_thermal_comfort_schedule_name` or None if not set

        """
        return self["Fanger Thermal Comfort Schedule Name"]

    @fanger_thermal_comfort_schedule_name.setter
    def fanger_thermal_comfort_schedule_name(self, value=None):
        """Corresponds to IDD field `Fanger Thermal Comfort Schedule Name`"""
        self["Fanger Thermal Comfort Schedule Name"] = value




class ThermostatSetpointThermalComfortFangerSingleCooling(DataObject):

    """ Corresponds to IDD object `ThermostatSetpoint:ThermalComfort:Fanger:SingleCooling`
        Used for cooling only thermal comfort control. The PMV setpoint can be scheduled and
        varied throughout the simulation but only cooling is allowed with this control type.
    """
    _schema = {'extensible-fields': OrderedDict(),
               'fields': OrderedDict([(u'name',
                                       {'name': u'Name',
                                        'pyname': u'name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'alpha'}),
                                      (u'fanger thermal comfort schedule name',
                                       {'name': u'Fanger Thermal Comfort Schedule Name',
                                        'pyname': u'fanger_thermal_comfort_schedule_name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'})]),
               'format': None,
               'group': u'Zone HVAC Controls and Thermostats',
               'min-fields': 2,
               'name': u'ThermostatSetpoint:ThermalComfort:Fanger:SingleCooling',
               'pyname': u'ThermostatSetpointThermalComfortFangerSingleCooling',
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
    def fanger_thermal_comfort_schedule_name(self):
        """field `Fanger Thermal Comfort Schedule Name`

        |  Schedule values should be Predicted Mean Vote (PMV)

        Args:
            value (str): value for IDD Field `Fanger Thermal Comfort Schedule Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `fanger_thermal_comfort_schedule_name` or None if not set

        """
        return self["Fanger Thermal Comfort Schedule Name"]

    @fanger_thermal_comfort_schedule_name.setter
    def fanger_thermal_comfort_schedule_name(self, value=None):
        """Corresponds to IDD field `Fanger Thermal Comfort Schedule Name`"""
        self["Fanger Thermal Comfort Schedule Name"] = value




class ThermostatSetpointThermalComfortFangerSingleHeatingOrCooling(DataObject):

    """ Corresponds to IDD object `ThermostatSetpoint:ThermalComfort:Fanger:SingleHeatingOrCooling`
        Used for heating and cooling thermal comfort control with a single setpoint. The PMV
        setpoint can be scheduled and varied throughout the simulation for both heating and
        cooling.
    """
    _schema = {'extensible-fields': OrderedDict(),
               'fields': OrderedDict([(u'name',
                                       {'name': u'Name',
                                        'pyname': u'name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'alpha'}),
                                      (u'fanger thermal comfort schedule name',
                                       {'name': u'Fanger Thermal Comfort Schedule Name',
                                        'pyname': u'fanger_thermal_comfort_schedule_name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'})]),
               'format': None,
               'group': u'Zone HVAC Controls and Thermostats',
               'min-fields': 2,
               'name': u'ThermostatSetpoint:ThermalComfort:Fanger:SingleHeatingOrCooling',
               'pyname': u'ThermostatSetpointThermalComfortFangerSingleHeatingOrCooling',
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
    def fanger_thermal_comfort_schedule_name(self):
        """field `Fanger Thermal Comfort Schedule Name`

        |  Schedule values should be Predicted Mean Vote (PMV)

        Args:
            value (str): value for IDD Field `Fanger Thermal Comfort Schedule Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `fanger_thermal_comfort_schedule_name` or None if not set

        """
        return self["Fanger Thermal Comfort Schedule Name"]

    @fanger_thermal_comfort_schedule_name.setter
    def fanger_thermal_comfort_schedule_name(self, value=None):
        """Corresponds to IDD field `Fanger Thermal Comfort Schedule Name`"""
        self["Fanger Thermal Comfort Schedule Name"] = value




class ThermostatSetpointThermalComfortFangerDualSetpoint(DataObject):

    """ Corresponds to IDD object `ThermostatSetpoint:ThermalComfort:Fanger:DualSetpoint`
        Used for heating and cooling thermal comfort control with dual setpoints. The PMV
        setpoints can be scheduled and varied throughout the simulation for both heating and
        cooling.
    """
    _schema = {'extensible-fields': OrderedDict(),
               'fields': OrderedDict([(u'name',
                                       {'name': u'Name',
                                        'pyname': u'name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'alpha'}),
                                      (u'fanger thermal comfort heating schedule name',
                                       {'name': u'Fanger Thermal Comfort Heating Schedule Name',
                                        'pyname': u'fanger_thermal_comfort_heating_schedule_name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'fanger thermal comfort cooling schedule name',
                                       {'name': u'Fanger Thermal Comfort Cooling Schedule Name',
                                        'pyname': u'fanger_thermal_comfort_cooling_schedule_name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'})]),
               'format': None,
               'group': u'Zone HVAC Controls and Thermostats',
               'min-fields': 3,
               'name': u'ThermostatSetpoint:ThermalComfort:Fanger:DualSetpoint',
               'pyname': u'ThermostatSetpointThermalComfortFangerDualSetpoint',
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
    def fanger_thermal_comfort_heating_schedule_name(self):
        """field `Fanger Thermal Comfort Heating Schedule Name`

        |  Schedule values should be Predicted Mean Vote (PMV)

        Args:
            value (str): value for IDD Field `Fanger Thermal Comfort Heating Schedule Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `fanger_thermal_comfort_heating_schedule_name` or None if not set

        """
        return self["Fanger Thermal Comfort Heating Schedule Name"]

    @fanger_thermal_comfort_heating_schedule_name.setter
    def fanger_thermal_comfort_heating_schedule_name(self, value=None):
        """Corresponds to IDD field `Fanger Thermal Comfort Heating Schedule
        Name`"""
        self["Fanger Thermal Comfort Heating Schedule Name"] = value

    @property
    def fanger_thermal_comfort_cooling_schedule_name(self):
        """field `Fanger Thermal Comfort Cooling Schedule Name`

        |  Schedule values should be Predicted Mean Vote (PMV)

        Args:
            value (str): value for IDD Field `Fanger Thermal Comfort Cooling Schedule Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `fanger_thermal_comfort_cooling_schedule_name` or None if not set

        """
        return self["Fanger Thermal Comfort Cooling Schedule Name"]

    @fanger_thermal_comfort_cooling_schedule_name.setter
    def fanger_thermal_comfort_cooling_schedule_name(self, value=None):
        """Corresponds to IDD field `Fanger Thermal Comfort Cooling Schedule
        Name`"""
        self["Fanger Thermal Comfort Cooling Schedule Name"] = value




class ZoneControlThermostatStagedDualSetpoint(DataObject):

    """ Corresponds to IDD object `ZoneControl:Thermostat:StagedDualSetpoint`
        Define the Thermostat StagedDualSetpoint settings for a zone or list of zones.
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
                                        'type': 'alpha'}),
                                      (u'zone or zonelist name',
                                       {'name': u'Zone or ZoneList Name',
                                        'pyname': u'zone_or_zonelist_name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'number of heating stages',
                                       {'name': u'Number of Heating Stages',
                                        'pyname': u'number_of_heating_stages',
                                        'maximum': 4,
                                        'required-field': True,
                                        'autosizable': False,
                                        'minimum': 1,
                                        'autocalculatable': False,
                                        'type': u'integer'}),
                                      (u'heating temperature setpoint schedule name',
                                       {'name': u'Heating Temperature Setpoint Schedule Name',
                                        'pyname': u'heating_temperature_setpoint_schedule_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'heating throttling temperature range',
                                       {'name': u'Heating Throttling Temperature Range',
                                        'pyname': u'heating_throttling_temperature_range',
                                        'default': 1.1,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': 'real',
                                        'unit': u'deltaC'}),
                                      (u'stage 1 heating temperature offset',
                                       {'name': u'Stage 1 Heating Temperature Offset',
                                        'pyname': u'stage_1_heating_temperature_offset',
                                        'maximum': 0.0,
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'deltaC'}),
                                      (u'stage 2 heating temperature offset',
                                       {'name': u'Stage 2 Heating Temperature Offset',
                                        'pyname': u'stage_2_heating_temperature_offset',
                                        'maximum': 0.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'deltaC'}),
                                      (u'stage 3 heating temperature offset',
                                       {'name': u'Stage 3 Heating Temperature Offset',
                                        'pyname': u'stage_3_heating_temperature_offset',
                                        'maximum': 0.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'deltaC'}),
                                      (u'stage 4 heating temperature offset',
                                       {'name': u'Stage 4 Heating Temperature Offset',
                                        'pyname': u'stage_4_heating_temperature_offset',
                                        'maximum': 0.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'deltaC'}),
                                      (u'number of cooling stages',
                                       {'name': u'Number of Cooling Stages',
                                        'pyname': u'number_of_cooling_stages',
                                        'maximum': 4,
                                        'required-field': True,
                                        'autosizable': False,
                                        'minimum': 1,
                                        'autocalculatable': False,
                                        'type': u'integer'}),
                                      (u'cooling temperature setpoint base schedule name',
                                       {'name': u'Cooling Temperature Setpoint Base Schedule Name',
                                        'pyname': u'cooling_temperature_setpoint_base_schedule_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'cooling throttling temperature range',
                                       {'name': u'Cooling Throttling Temperature Range',
                                        'pyname': u'cooling_throttling_temperature_range',
                                        'default': 1.1,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': 'real',
                                        'unit': u'deltaC'}),
                                      (u'stage 1 cooling temperature offset',
                                       {'name': u'Stage 1 Cooling Temperature Offset',
                                        'pyname': u'stage_1_cooling_temperature_offset',
                                        'required-field': True,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'deltaC'}),
                                      (u'stage 2 cooling temperature offset',
                                       {'name': u'Stage 2 Cooling Temperature Offset',
                                        'pyname': u'stage_2_cooling_temperature_offset',
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'deltaC'}),
                                      (u'stage 3 cooling temperature offset',
                                       {'name': u'Stage 3 Cooling Temperature Offset',
                                        'pyname': u'stage_3_cooling_temperature_offset',
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'deltaC'}),
                                      (u'stage 4 cooling temperature offset',
                                       {'name': u'Stage 4 Cooling Temperature Offset',
                                        'pyname': u'stage_4_cooling_temperature_offset',
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'deltaC'})]),
               'format': None,
               'group': u'Zone HVAC Controls and Thermostats',
               'min-fields': 0,
               'name': u'ZoneControl:Thermostat:StagedDualSetpoint',
               'pyname': u'ZoneControlThermostatStagedDualSetpoint',
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
    def number_of_heating_stages(self):
        """field `Number of Heating Stages`

        |  Enter the number of the following sets of data for heating temperature offset
        |  value >= 1
        |  value <= 4

        Args:
            value (int): value for IDD Field `Number of Heating Stages`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            int: the value of `number_of_heating_stages` or None if not set

        """
        return self["Number of Heating Stages"]

    @number_of_heating_stages.setter
    def number_of_heating_stages(self, value=None):
        """Corresponds to IDD field `Number of Heating Stages`"""
        self["Number of Heating Stages"] = value

    @property
    def heating_temperature_setpoint_schedule_name(self):
        """field `Heating Temperature Setpoint Schedule Name`

        Args:
            value (str): value for IDD Field `Heating Temperature Setpoint Schedule Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `heating_temperature_setpoint_schedule_name` or None if not set

        """
        return self["Heating Temperature Setpoint Schedule Name"]

    @heating_temperature_setpoint_schedule_name.setter
    def heating_temperature_setpoint_schedule_name(self, value=None):
        """Corresponds to IDD field `Heating Temperature Setpoint Schedule
        Name`"""
        self["Heating Temperature Setpoint Schedule Name"] = value

    @property
    def heating_throttling_temperature_range(self):
        """field `Heating Throttling Temperature Range`

        |  Units: deltaC
        |  Default value: 1.1

        Args:
            value (float): value for IDD Field `Heating Throttling Temperature Range`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `heating_throttling_temperature_range` or None if not set

        """
        return self["Heating Throttling Temperature Range"]

    @heating_throttling_temperature_range.setter
    def heating_throttling_temperature_range(self, value=1.1):
        """Corresponds to IDD field `Heating Throttling Temperature Range`"""
        self["Heating Throttling Temperature Range"] = value

    @property
    def stage_1_heating_temperature_offset(self):
        """field `Stage 1 Heating Temperature Offset`

        |  The heating temperature offset is used to determine heating stage number for
        |  multi stage equipment.
        |  When the temperature difference of the heating setpoint and the controlled zone
        |  temperature at previous time step is less than Stage 1 value and greater than
        |  Stage 2 value, the stage number is 1.
        |  Units: deltaC

        Args:
            value (float): value for IDD Field `Stage 1 Heating Temperature Offset`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `stage_1_heating_temperature_offset` or None if not set

        """
        return self["Stage 1 Heating Temperature Offset"]

    @stage_1_heating_temperature_offset.setter
    def stage_1_heating_temperature_offset(self, value=None):
        """Corresponds to IDD field `Stage 1 Heating Temperature Offset`"""
        self["Stage 1 Heating Temperature Offset"] = value

    @property
    def stage_2_heating_temperature_offset(self):
        """field `Stage 2 Heating Temperature Offset`

        |  The heating temperature offset is used to determine heating stage number for
        |  multi stage equipment.
        |  When the temperature difference of the heating setpoint and the controlled zone
        |  temperature at previous time step is less than Stage 2 value and greater than
        |  Stage 3 value, the stage number is 2.
        |  The value of this field has to be less the value at the previous field.
        |  Units: deltaC

        Args:
            value (float): value for IDD Field `Stage 2 Heating Temperature Offset`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `stage_2_heating_temperature_offset` or None if not set

        """
        return self["Stage 2 Heating Temperature Offset"]

    @stage_2_heating_temperature_offset.setter
    def stage_2_heating_temperature_offset(self, value=None):
        """Corresponds to IDD field `Stage 2 Heating Temperature Offset`"""
        self["Stage 2 Heating Temperature Offset"] = value

    @property
    def stage_3_heating_temperature_offset(self):
        """field `Stage 3 Heating Temperature Offset`

        |  The heating temperature offset is used to determine heating stage number for
        |  multi stage equipment.
        |  When the temperature difference of the heating setpoint and the controlled zone
        |  temperature at previous time step is less than Stage 3 value and greater than
        |  Stage 4 value, the stage number is 3.
        |  The value of this field has to be less the value at the previous field.
        |  Units: deltaC

        Args:
            value (float): value for IDD Field `Stage 3 Heating Temperature Offset`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `stage_3_heating_temperature_offset` or None if not set

        """
        return self["Stage 3 Heating Temperature Offset"]

    @stage_3_heating_temperature_offset.setter
    def stage_3_heating_temperature_offset(self, value=None):
        """Corresponds to IDD field `Stage 3 Heating Temperature Offset`"""
        self["Stage 3 Heating Temperature Offset"] = value

    @property
    def stage_4_heating_temperature_offset(self):
        """field `Stage 4 Heating Temperature Offset`

        |  The heating temperature offset is used to determine heating stage number for
        |  multi stage equipment.
        |  When the temperature difference of the heating setpoint and the controlled zone
        |  temperature at previous time step is less than Stage 4 value, the stage number is 4.
        |  The value of this field has to be less the value at the previous field.
        |  Units: deltaC

        Args:
            value (float): value for IDD Field `Stage 4 Heating Temperature Offset`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `stage_4_heating_temperature_offset` or None if not set

        """
        return self["Stage 4 Heating Temperature Offset"]

    @stage_4_heating_temperature_offset.setter
    def stage_4_heating_temperature_offset(self, value=None):
        """Corresponds to IDD field `Stage 4 Heating Temperature Offset`"""
        self["Stage 4 Heating Temperature Offset"] = value

    @property
    def number_of_cooling_stages(self):
        """field `Number of Cooling Stages`

        |  Enter the number of the following sets of data for cooling temperature offset
        |  value >= 1
        |  value <= 4

        Args:
            value (int): value for IDD Field `Number of Cooling Stages`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            int: the value of `number_of_cooling_stages` or None if not set

        """
        return self["Number of Cooling Stages"]

    @number_of_cooling_stages.setter
    def number_of_cooling_stages(self, value=None):
        """Corresponds to IDD field `Number of Cooling Stages`"""
        self["Number of Cooling Stages"] = value

    @property
    def cooling_temperature_setpoint_base_schedule_name(self):
        """field `Cooling Temperature Setpoint Base Schedule Name`

        Args:
            value (str): value for IDD Field `Cooling Temperature Setpoint Base Schedule Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `cooling_temperature_setpoint_base_schedule_name` or None if not set

        """
        return self["Cooling Temperature Setpoint Base Schedule Name"]

    @cooling_temperature_setpoint_base_schedule_name.setter
    def cooling_temperature_setpoint_base_schedule_name(self, value=None):
        """Corresponds to IDD field `Cooling Temperature Setpoint Base Schedule
        Name`"""
        self["Cooling Temperature Setpoint Base Schedule Name"] = value

    @property
    def cooling_throttling_temperature_range(self):
        """field `Cooling Throttling Temperature Range`

        |  Units: deltaC
        |  Default value: 1.1

        Args:
            value (float): value for IDD Field `Cooling Throttling Temperature Range`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `cooling_throttling_temperature_range` or None if not set

        """
        return self["Cooling Throttling Temperature Range"]

    @cooling_throttling_temperature_range.setter
    def cooling_throttling_temperature_range(self, value=1.1):
        """Corresponds to IDD field `Cooling Throttling Temperature Range`"""
        self["Cooling Throttling Temperature Range"] = value

    @property
    def stage_1_cooling_temperature_offset(self):
        """field `Stage 1 Cooling Temperature Offset`

        |  The cooling temperature offset is used to determine cooling stage number for
        |  multi stage equipment.
        |  When the temperature difference of the cooling setpoint and the controlled zone
        |  temperature at previous time step is greater than Stage 1 value and less than
        |  Stage 2 value, the stage number is 1.
        |  Units: deltaC

        Args:
            value (float): value for IDD Field `Stage 1 Cooling Temperature Offset`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `stage_1_cooling_temperature_offset` or None if not set

        """
        return self["Stage 1 Cooling Temperature Offset"]

    @stage_1_cooling_temperature_offset.setter
    def stage_1_cooling_temperature_offset(self, value=None):
        """Corresponds to IDD field `Stage 1 Cooling Temperature Offset`"""
        self["Stage 1 Cooling Temperature Offset"] = value

    @property
    def stage_2_cooling_temperature_offset(self):
        """field `Stage 2 Cooling Temperature Offset`

        |  The cooling temperature offset is used to determine cooling stage number for
        |  multi stage equipment.
        |  When the temperature difference of the cooling setpoint and the controlled zone
        |  temperature at previous time step is greater than Stage 2 value and less than
        |  Stage 3 value, the stage number is 2.
        |  The value of this field has to be greater than the value at the previous field.
        |  Units: deltaC

        Args:
            value (float): value for IDD Field `Stage 2 Cooling Temperature Offset`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `stage_2_cooling_temperature_offset` or None if not set

        """
        return self["Stage 2 Cooling Temperature Offset"]

    @stage_2_cooling_temperature_offset.setter
    def stage_2_cooling_temperature_offset(self, value=None):
        """Corresponds to IDD field `Stage 2 Cooling Temperature Offset`"""
        self["Stage 2 Cooling Temperature Offset"] = value

    @property
    def stage_3_cooling_temperature_offset(self):
        """field `Stage 3 Cooling Temperature Offset`

        |  The cooling temperature offset is used to determine cooling stage number for
        |  multi stage equipment.
        |  When the temperature difference of the cooling setpoint and the controlled zone
        |  temperature at previous time step is greater than Stage 3 value and less than
        |  Stage 4 value, the stage number is 3.
        |  The value of this field has to be greater than the value at the previous field.
        |  Units: deltaC

        Args:
            value (float): value for IDD Field `Stage 3 Cooling Temperature Offset`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `stage_3_cooling_temperature_offset` or None if not set

        """
        return self["Stage 3 Cooling Temperature Offset"]

    @stage_3_cooling_temperature_offset.setter
    def stage_3_cooling_temperature_offset(self, value=None):
        """Corresponds to IDD field `Stage 3 Cooling Temperature Offset`"""
        self["Stage 3 Cooling Temperature Offset"] = value

    @property
    def stage_4_cooling_temperature_offset(self):
        """field `Stage 4 Cooling Temperature Offset`

        |  The cooling temperature offset is used to determine cooling stage number for
        |  multi stage equipment.
        |  When the temperature difference of the cooling setpoint and the controlled zone
        |  temperature at previous time step is greater than Stage 4 value, the stage number is 4.
        |  The value of this field has to be greater than the value at the previous field.
        |  Units: deltaC

        Args:
            value (float): value for IDD Field `Stage 4 Cooling Temperature Offset`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `stage_4_cooling_temperature_offset` or None if not set

        """
        return self["Stage 4 Cooling Temperature Offset"]

    @stage_4_cooling_temperature_offset.setter
    def stage_4_cooling_temperature_offset(self, value=None):
        """Corresponds to IDD field `Stage 4 Cooling Temperature Offset`"""
        self["Stage 4 Cooling Temperature Offset"] = value




class ZoneControlContaminantController(DataObject):

    """ Corresponds to IDD object `ZoneControl:ContaminantController`
        Used to control a zone to a specified indoor level of CO2 or generic contaminants, or
        to specify minimum CO2 concentration schedule name for a zone.
    """
    _schema = {'extensible-fields': OrderedDict(),
               'fields': OrderedDict([(u'name',
                                       {'name': u'Name',
                                        'pyname': u'name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'controlled zone name',
                                       {'name': u'Controlled Zone Name',
                                        'pyname': u'controlled_zone_name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'carbon dioxide control availability schedule name',
                                       {'name': u'Carbon Dioxide Control Availability Schedule Name',
                                        'pyname': u'carbon_dioxide_control_availability_schedule_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'carbon dioxide setpoint schedule name',
                                       {'name': u'Carbon Dioxide Setpoint Schedule Name',
                                        'pyname': u'carbon_dioxide_setpoint_schedule_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'minimum carbon dioxide concentration schedule name',
                                       {'name': u'Minimum Carbon Dioxide Concentration Schedule Name',
                                        'pyname': u'minimum_carbon_dioxide_concentration_schedule_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'generic contaminant control availability schedule name',
                                       {'name': u'Generic Contaminant Control Availability Schedule Name',
                                        'pyname': u'generic_contaminant_control_availability_schedule_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'generic contaminant setpoint schedule name',
                                       {'name': u'Generic Contaminant Setpoint Schedule Name',
                                        'pyname': u'generic_contaminant_setpoint_schedule_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'})]),
               'format': None,
               'group': u'Zone HVAC Controls and Thermostats',
               'min-fields': 4,
               'name': u'ZoneControl:ContaminantController',
               'pyname': u'ZoneControlContaminantController',
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
    def controlled_zone_name(self):
        """field `Controlled Zone Name`

        Args:
            value (str): value for IDD Field `Controlled Zone Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `controlled_zone_name` or None if not set

        """
        return self["Controlled Zone Name"]

    @controlled_zone_name.setter
    def controlled_zone_name(self, value=None):
        """Corresponds to IDD field `Controlled Zone Name`"""
        self["Controlled Zone Name"] = value

    @property
    def carbon_dioxide_control_availability_schedule_name(self):
        """field `Carbon Dioxide Control Availability Schedule Name`

        |  Availability schedule name for CO2 controller. Schedule value > 0 means the CO2
        |  controller is enabled. If this field is blank, then CO2  controller is always enabled.

        Args:
            value (str): value for IDD Field `Carbon Dioxide Control Availability Schedule Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `carbon_dioxide_control_availability_schedule_name` or None if not set

        """
        return self["Carbon Dioxide Control Availability Schedule Name"]

    @carbon_dioxide_control_availability_schedule_name.setter
    def carbon_dioxide_control_availability_schedule_name(self, value=None):
        """Corresponds to IDD field `Carbon Dioxide Control Availability
        Schedule Name`"""
        self["Carbon Dioxide Control Availability Schedule Name"] = value

    @property
    def carbon_dioxide_setpoint_schedule_name(self):
        """field `Carbon Dioxide Setpoint Schedule Name`

        |  Schedule values should be carbon dioxide concentration in parts per million (ppm)

        Args:
            value (str): value for IDD Field `Carbon Dioxide Setpoint Schedule Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `carbon_dioxide_setpoint_schedule_name` or None if not set

        """
        return self["Carbon Dioxide Setpoint Schedule Name"]

    @carbon_dioxide_setpoint_schedule_name.setter
    def carbon_dioxide_setpoint_schedule_name(self, value=None):
        """Corresponds to IDD field `Carbon Dioxide Setpoint Schedule Name`"""
        self["Carbon Dioxide Setpoint Schedule Name"] = value

    @property
    def minimum_carbon_dioxide_concentration_schedule_name(self):
        """field `Minimum Carbon Dioxide Concentration Schedule Name`

        |  Schedule values should be carbon dioxide concentration in parts per
        |  million (ppm)
        |  This field is used when the field System Outdoor Air Method =
        |  ProportionalControlBasedonOccupancySchedule or ProportionalControlBasedOnDesignOccupancy
        |  in Controller:MechanicalVentilation

        Args:
            value (str): value for IDD Field `Minimum Carbon Dioxide Concentration Schedule Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `minimum_carbon_dioxide_concentration_schedule_name` or None if not set

        """
        return self["Minimum Carbon Dioxide Concentration Schedule Name"]

    @minimum_carbon_dioxide_concentration_schedule_name.setter
    def minimum_carbon_dioxide_concentration_schedule_name(self, value=None):
        """Corresponds to IDD field `Minimum Carbon Dioxide Concentration
        Schedule Name`"""
        self["Minimum Carbon Dioxide Concentration Schedule Name"] = value

    @property
    def generic_contaminant_control_availability_schedule_name(self):
        """field `Generic Contaminant Control Availability Schedule Name`

        |  Availability schedule name for generic contaminant controller. Schedule value > 0 means
        |  the generic contaminant controller is enabled. If this field is blank, then generic
        |  contaminant controller is always enabled.

        Args:
            value (str): value for IDD Field `Generic Contaminant Control Availability Schedule Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `generic_contaminant_control_availability_schedule_name` or None if not set

        """
        return self["Generic Contaminant Control Availability Schedule Name"]

    @generic_contaminant_control_availability_schedule_name.setter
    def generic_contaminant_control_availability_schedule_name(
            self,
            value=None):
        """Corresponds to IDD field `Generic Contaminant Control Availability
        Schedule Name`"""
        self["Generic Contaminant Control Availability Schedule Name"] = value

    @property
    def generic_contaminant_setpoint_schedule_name(self):
        """field `Generic Contaminant Setpoint Schedule Name`

        |  Schedule values should be generic contaminant concentration in parts per
        |  million (ppm)
        |  This field is used when the field System Outdoor Air Method =
        |  IndoorAirQualityProcedureGenericContaminant in Controller:MechanicalVentilation

        Args:
            value (str): value for IDD Field `Generic Contaminant Setpoint Schedule Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `generic_contaminant_setpoint_schedule_name` or None if not set

        """
        return self["Generic Contaminant Setpoint Schedule Name"]

    @generic_contaminant_setpoint_schedule_name.setter
    def generic_contaminant_setpoint_schedule_name(self, value=None):
        """Corresponds to IDD field `Generic Contaminant Setpoint Schedule
        Name`"""
        self["Generic Contaminant Setpoint Schedule Name"] = value


