""" Data objects in group "Location and Climate"
"""

from collections import OrderedDict
import logging
from pyidf.helper import DataObject

logger = logging.getLogger("pyidf")
logger.addHandler(logging.NullHandler())



class SiteLocation(DataObject):

    """ Corresponds to IDD object `Site:Location`
        Specifies the building's location. Only one location is allowed.
        Weather data file location, if it exists, will override this object.
    """
    _schema = {'extensible-fields': OrderedDict(),
               'fields': OrderedDict([(u'name',
                                       {'name': u'Name',
                                        'pyname': u'name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'alpha'}),
                                      (u'latitude',
                                       {'name': u'Latitude',
                                        'pyname': u'latitude',
                                        'default': 0.0,
                                        'maximum': 90.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': -90.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'deg'}),
                                      (u'longitude',
                                       {'name': u'Longitude',
                                        'pyname': u'longitude',
                                        'default': 0.0,
                                        'maximum': 180.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': -180.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'deg'}),
                                      (u'time zone',
                                       {'name': u'Time Zone',
                                        'pyname': u'time_zone',
                                        'default': 0.0,
                                        'maximum': 14.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': -12.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'hr'}),
                                      (u'elevation',
                                       {'name': u'Elevation',
                                        'pyname': u'elevation',
                                        'default': 0.0,
                                        'maximum<': 8900.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': -300.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'm'})]),
               'format': None,
               'group': u'Location and Climate',
               'min-fields': 5,
               'name': u'Site:Location',
               'pyname': u'SiteLocation',
               'required-object': False,
               'unique-object': True}

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
    def latitude(self):
        """field `Latitude`

        |  + is North, - is South, degree minutes represented in decimal (i.e. 30 minutes is .5)
        |  Units: deg
        |  value >= -90.0
        |  value <= 90.0

        Args:
            value (float): value for IDD Field `Latitude`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `latitude` or None if not set

        """
        return self["Latitude"]

    @latitude.setter
    def latitude(self, value=None):
        """Corresponds to IDD field `Latitude`"""
        self["Latitude"] = value

    @property
    def longitude(self):
        """field `Longitude`

        |  - is West, + is East, degree minutes represented in decimal (i.e. 30 minutes is .5)
        |  Units: deg
        |  value >= -180.0
        |  value <= 180.0

        Args:
            value (float): value for IDD Field `Longitude`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `longitude` or None if not set

        """
        return self["Longitude"]

    @longitude.setter
    def longitude(self, value=None):
        """Corresponds to IDD field `Longitude`"""
        self["Longitude"] = value

    @property
    def time_zone(self):
        """field `Time Zone`

        |  basic these limits on the WorldTimeZone Map (2003)
        |  Time relative to GMT. Decimal hours.
        |  Units: hr
        |  value >= -12.0
        |  value <= 14.0

        Args:
            value (float): value for IDD Field `Time Zone`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `time_zone` or None if not set

        """
        return self["Time Zone"]

    @time_zone.setter
    def time_zone(self, value=None):
        """Corresponds to IDD field `Time Zone`"""
        self["Time Zone"] = value

    @property
    def elevation(self):
        """field `Elevation`

        |  Units: m
        |  value >= -300.0
        |  value < 8900.0

        Args:
            value (float): value for IDD Field `Elevation`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `elevation` or None if not set

        """
        return self["Elevation"]

    @elevation.setter
    def elevation(self, value=None):
        """Corresponds to IDD field `Elevation`"""
        self["Elevation"] = value




class SizingPeriodDesignDay(DataObject):

    """ Corresponds to IDD object `SizingPeriod:DesignDay`
        The design day object creates the parameters for the program to create
        the 24 hour weather profile that can be used for sizing as well as
        running to test the other simulation parameters. Parameters in this
        include a date (month and day), a day type (which uses the appropriate
        schedules for either sizing or simple tests), min/max temperatures,
        wind speeds, and solar radiation values.
    """
    _schema = {'extensible-fields': OrderedDict(),
               'fields': OrderedDict([(u'name',
                                       {'name': u'Name',
                                        'pyname': u'name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'alpha'}),
                                      (u'month',
                                       {'name': u'Month',
                                        'pyname': u'month',
                                        'maximum': 12,
                                        'required-field': True,
                                        'autosizable': False,
                                        'minimum': 1,
                                        'autocalculatable': False,
                                        'type': u'integer'}),
                                      (u'day of month',
                                       {'name': u'Day of Month',
                                        'pyname': u'day_of_month',
                                        'maximum': 31,
                                        'required-field': True,
                                        'autosizable': False,
                                        'minimum': 1,
                                        'autocalculatable': False,
                                        'type': u'integer'}),
                                      (u'day type',
                                       {'name': u'Day Type',
                                        'pyname': u'day_type',
                                        'required-field': True,
                                        'autosizable': False,
                                        'accepted-values': [u'Sunday',
                                                            u'Monday',
                                                            u'Tuesday',
                                                            u'Wednesday',
                                                            u'Thursday',
                                                            u'Friday',
                                                            u'Saturday',
                                                            u'Holiday',
                                                            u'SummerDesignDay',
                                                            u'WinterDesignDay',
                                                            u'CustomDay1',
                                                            u'CustomDay2'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'maximum dry-bulb temperature',
                                       {'name': u'Maximum Dry-Bulb Temperature',
                                        'pyname': u'maximum_drybulb_temperature',
                                        'maximum': 70.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': -90.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'C'}),
                                      (u'daily dry-bulb temperature range',
                                       {'name': u'Daily Dry-Bulb Temperature Range',
                                        'pyname': u'daily_drybulb_temperature_range',
                                        'default': 0.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'deltaC'}),
                                      (u'dry-bulb temperature range modifier type',
                                       {'name': u'Dry-Bulb Temperature Range Modifier Type',
                                        'pyname': u'drybulb_temperature_range_modifier_type',
                                        'default': u'DefaultMultipliers',
                                        'required-field': False,
                                        'autosizable': False,
                                        'accepted-values': [u'MultiplierSchedule',
                                                            u'DifferenceSchedule',
                                                            u'TemperatureProfileSchedule',
                                                            u'DefaultMultipliers'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'dry-bulb temperature range modifier day schedule name',
                                       {'name': u'Dry-Bulb Temperature Range Modifier Day Schedule Name',
                                        'pyname': u'drybulb_temperature_range_modifier_day_schedule_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'humidity condition type',
                                       {'name': u'Humidity Condition Type',
                                        'pyname': u'humidity_condition_type',
                                        'default': u'WetBulb',
                                        'required-field': False,
                                        'autosizable': False,
                                        'accepted-values': [u'WetBulb',
                                                            u'DewPoint',
                                                            u'HumidityRatio',
                                                            u'Enthalpy',
                                                            u'RelativeHumiditySchedule',
                                                            u'WetBulbProfileMultiplierSchedule',
                                                            u'WetBulbProfileDifferenceSchedule',
                                                            u'WetBulbProfileDefaultMultipliers'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'wetbulb or dewpoint at maximum dry-bulb',
                                       {'name': u'Wetbulb or DewPoint at Maximum Dry-Bulb',
                                        'pyname': u'wetbulb_or_dewpoint_at_maximum_drybulb',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'C'}),
                                      (u'humidity condition day schedule name',
                                       {'name': u'Humidity Condition Day Schedule Name',
                                        'pyname': u'humidity_condition_day_schedule_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'humidity ratio at maximum dry-bulb',
                                       {'name': u'Humidity Ratio at Maximum Dry-Bulb',
                                        'pyname': u'humidity_ratio_at_maximum_drybulb',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'kgWater/kgDryAir'}),
                                      (u'enthalpy at maximum dry-bulb',
                                       {'name': u'Enthalpy at Maximum Dry-Bulb',
                                        'pyname': u'enthalpy_at_maximum_drybulb',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'J/kg'}),
                                      (u'daily wet-bulb temperature range',
                                       {'name': u'Daily Wet-Bulb Temperature Range',
                                        'pyname': u'daily_wetbulb_temperature_range',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': 'real',
                                        'unit': u'deltaC'}),
                                      (u'barometric pressure',
                                       {'name': u'Barometric Pressure',
                                        'pyname': u'barometric_pressure',
                                        'maximum': 120000.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 31000.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'Pa'}),
                                      (u'wind speed',
                                       {'name': u'Wind Speed',
                                        'pyname': u'wind_speed',
                                        'maximum': 40.0,
                                        'required-field': True,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'm/s'}),
                                      (u'wind direction',
                                       {'name': u'Wind Direction',
                                        'pyname': u'wind_direction',
                                        'maximum': 360.0,
                                        'required-field': True,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'deg'}),
                                      (u'rain indicator',
                                       {'name': u'Rain Indicator',
                                        'pyname': u'rain_indicator',
                                        'default': u'No',
                                        'required-field': False,
                                        'autosizable': False,
                                        'accepted-values': [u'Yes',
                                                            u'No'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'snow indicator',
                                       {'name': u'Snow Indicator',
                                        'pyname': u'snow_indicator',
                                        'default': u'No',
                                        'required-field': False,
                                        'autosizable': False,
                                        'accepted-values': [u'Yes',
                                                            u'No'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'daylight saving time indicator',
                                       {'name': u'Daylight Saving Time Indicator',
                                        'pyname': u'daylight_saving_time_indicator',
                                        'default': u'No',
                                        'required-field': False,
                                        'autosizable': False,
                                        'accepted-values': [u'Yes',
                                                            u'No'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'solar model indicator',
                                       {'name': u'Solar Model Indicator',
                                        'pyname': u'solar_model_indicator',
                                        'default': u'ASHRAEClearSky',
                                        'required-field': False,
                                        'autosizable': False,
                                        'accepted-values': [u'ASHRAEClearSky',
                                                            u'ZhangHuang',
                                                            u'Schedule',
                                                            u'ASHRAETau'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'beam solar day schedule name',
                                       {'name': u'Beam Solar Day Schedule Name',
                                        'pyname': u'beam_solar_day_schedule_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'diffuse solar day schedule name',
                                       {'name': u'Diffuse Solar Day Schedule Name',
                                        'pyname': u'diffuse_solar_day_schedule_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'ashrae clear sky optical depth for beam irradiance (taub)',
                                       {'name': u'ASHRAE Clear Sky Optical Depth for Beam Irradiance (taub)',
                                        'pyname': u'ashrae_clear_sky_optical_depth_for_beam_irradiance_taub',
                                        'default': 0.0,
                                        'maximum': 1.2,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': 'real',
                                        'unit': u'dimensionless'}),
                                      (u'ashrae clear sky optical depth for diffuse irradiance (taud)',
                                       {'name': u'ASHRAE Clear Sky Optical Depth for Diffuse Irradiance (taud)',
                                        'pyname': u'ashrae_clear_sky_optical_depth_for_diffuse_irradiance_taud',
                                        'default': 0.0,
                                        'maximum': 3.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': 'real',
                                        'unit': u'dimensionless'}),
                                      (u'sky clearness',
                                       {'name': u'Sky Clearness',
                                        'pyname': u'sky_clearness',
                                        'default': 0.0,
                                        'maximum': 1.2,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real'})]),
               'format': None,
               'group': u'Location and Climate',
               'min-fields': 0,
               'name': u'SizingPeriod:DesignDay',
               'pyname': u'SizingPeriodDesignDay',
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
    def month(self):
        """field `Month`

        |  value >= 1
        |  value <= 12

        Args:
            value (int): value for IDD Field `Month`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            int: the value of `month` or None if not set

        """
        return self["Month"]

    @month.setter
    def month(self, value=None):
        """Corresponds to IDD field `Month`"""
        self["Month"] = value

    @property
    def day_of_month(self):
        """field `Day of Month`

        |  must be valid for Month field
        |  value >= 1
        |  value <= 31

        Args:
            value (int): value for IDD Field `Day of Month`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            int: the value of `day_of_month` or None if not set

        """
        return self["Day of Month"]

    @day_of_month.setter
    def day_of_month(self, value=None):
        """Corresponds to IDD field `Day of Month`"""
        self["Day of Month"] = value

    @property
    def day_type(self):
        """field `Day Type`

        |  Day Type selects the schedules appropriate for this design day

        Args:
            value (str): value for IDD Field `Day Type`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `day_type` or None if not set

        """
        return self["Day Type"]

    @day_type.setter
    def day_type(self, value=None):
        """Corresponds to IDD field `Day Type`"""
        self["Day Type"] = value

    @property
    def maximum_drybulb_temperature(self):
        """field `Maximum Dry-Bulb Temperature`

        |  This field is required when field "Dry-Bulb Temperature Range Modifier Type"
        |  is not "TemperatureProfileSchedule".
        |  Units: C
        |  value >= -90.0
        |  value <= 70.0

        Args:
            value (float): value for IDD Field `Maximum Dry-Bulb Temperature`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `maximum_drybulb_temperature` or None if not set
        """
        return self["Maximum Dry-Bulb Temperature"]

    @maximum_drybulb_temperature.setter
    def maximum_drybulb_temperature(self, value=None):
        """  Corresponds to IDD field `Maximum Dry-Bulb Temperature`

        """
        self["Maximum Dry-Bulb Temperature"] = value

    @property
    def daily_drybulb_temperature_range(self):
        """field `Daily Dry-Bulb Temperature Range`

        |  Must still produce appropriate maximum dry-bulb (within range)
        |  This field is not needed if Dry-Bulb Temperature Range Modifier Type
        |  is "delta".
        |  Units: deltaC

        Args:
            value (float): value for IDD Field `Daily Dry-Bulb Temperature Range`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `daily_drybulb_temperature_range` or None if not set
        """
        return self["Daily Dry-Bulb Temperature Range"]

    @daily_drybulb_temperature_range.setter
    def daily_drybulb_temperature_range(self, value=None):
        """  Corresponds to IDD field `Daily Dry-Bulb Temperature Range`

        """
        self["Daily Dry-Bulb Temperature Range"] = value

    @property
    def drybulb_temperature_range_modifier_type(self):
        """field `Dry-Bulb Temperature Range Modifier Type`

        |  Type of modifier to the dry-bulb temperature calculated for the timestep
        |  Default value: DefaultMultipliers

        Args:
            value (str): value for IDD Field `Dry-Bulb Temperature Range Modifier Type`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `drybulb_temperature_range_modifier_type` or None if not set
        """
        return self["Dry-Bulb Temperature Range Modifier Type"]

    @drybulb_temperature_range_modifier_type.setter
    def drybulb_temperature_range_modifier_type(
            self,
            value="DefaultMultipliers"):
        """  Corresponds to IDD field `Dry-Bulb Temperature Range Modifier Type`

        """
        self["Dry-Bulb Temperature Range Modifier Type"] = value

    @property
    def drybulb_temperature_range_modifier_day_schedule_name(self):
        """field `Dry-Bulb Temperature Range Modifier Day Schedule Name`

        |  Only used when previous field is "MultiplierSchedule", "DifferenceSchedule" or
        |  "TemperatureProfileSchedule".
        |  For type "MultiplierSchedule"  the hour/time interval values should specify
        |  the fraction (0-1) of the dry-bulb temperature range to be subtracted
        |  from the maximum dry-bulb temperature for each timestep in the day
        |  For type "DifferenceSchedule" the values should specify a number to be subtracted
        |  from the maximum dry-bulb temperature for each timestep in the day.
        |  Note that numbers in the difference schedule cannot be negative as that
        |  would result in a higher maximum than the maximum previously specified.
        |  For type "TemperatureProfileSchedule" the values should specify the actual dry-bulb
        |  temperature for each timestep in the day.

        Args:
            value (str): value for IDD Field `Dry-Bulb Temperature Range Modifier Day Schedule Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `drybulb_temperature_range_modifier_day_schedule_name` or None if not set
        """
        return self["Dry-Bulb Temperature Range Modifier Day Schedule Name"]

    @drybulb_temperature_range_modifier_day_schedule_name.setter
    def drybulb_temperature_range_modifier_day_schedule_name(self, value=None):
        """  Corresponds to IDD field `Dry-Bulb Temperature Range Modifier Day Schedule Name`

        """
        self["Dry-Bulb Temperature Range Modifier Day Schedule Name"] = value

    @property
    def humidity_condition_type(self):
        """field `Humidity Condition Type`

        |  values/schedules indicated here and in subsequent fields create the humidity
        |  values in the 24 hour design day conditions profile.
        |  Default value: WetBulb

        Args:
            value (str): value for IDD Field `Humidity Condition Type`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `humidity_condition_type` or None if not set

        """
        return self["Humidity Condition Type"]

    @humidity_condition_type.setter
    def humidity_condition_type(self, value="WetBulb"):
        """Corresponds to IDD field `Humidity Condition Type`"""
        self["Humidity Condition Type"] = value

    @property
    def wetbulb_or_dewpoint_at_maximum_drybulb(self):
        """field `Wetbulb or DewPoint at Maximum Dry-Bulb`

        |  Wetbulb or dewpoint temperature coincident with the maximum temperature.
        |  Required only if field Humidity Condition Type is "Wetbulb", "Dewpoint",
        |  "WetBulbProfileMultiplierSchedule", "WetBulbProfileDifferenceSchedule",
        |  or "WetBulbProfileDefaultMultipliers"
        |  Units: C

        Args:
            value (float): value for IDD Field `Wetbulb or DewPoint at Maximum Dry-Bulb`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `wetbulb_or_dewpoint_at_maximum_drybulb` or None if not set
        """
        return self["Wetbulb or DewPoint at Maximum Dry-Bulb"]

    @wetbulb_or_dewpoint_at_maximum_drybulb.setter
    def wetbulb_or_dewpoint_at_maximum_drybulb(self, value=None):
        """  Corresponds to IDD field `Wetbulb or DewPoint at Maximum Dry-Bulb`

        """
        self["Wetbulb or DewPoint at Maximum Dry-Bulb"] = value

    @property
    def humidity_condition_day_schedule_name(self):
        """field `Humidity Condition Day Schedule Name`

        |  Only used when Humidity Condition Type is "RelativeHumiditySchedule",
        |  "WetBulbProfileMultiplierSchedule", or "WetBulbProfileDifferenceSchedule"
        |  For type "RelativeHumiditySchedule", the hour/time interval values should specify
        |  relative humidity (percent) from 0.0 to 100.0.
        |  For type "WetBulbProfileMultiplierSchedule" the hour/time interval values should specify
        |  the fraction (0-1) of the wet-bulb temperature range to be subtracted from the
        |  maximum wet-bulb temperature for each timestep in the day (units = Fraction)
        |  For type "WetBulbProfileDifferenceSchedule" the values should specify a number to be subtracted
        |  from the maximum wet-bulb temperature for each timestep in the day. (units = deltaC)

        Args:
            value (str): value for IDD Field `Humidity Condition Day Schedule Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `humidity_condition_day_schedule_name` or None if not set

        """
        return self["Humidity Condition Day Schedule Name"]

    @humidity_condition_day_schedule_name.setter
    def humidity_condition_day_schedule_name(self, value=None):
        """Corresponds to IDD field `Humidity Condition Day Schedule Name`"""
        self["Humidity Condition Day Schedule Name"] = value

    @property
    def humidity_ratio_at_maximum_drybulb(self):
        """field `Humidity Ratio at Maximum Dry-Bulb`

        |  Humidity ratio coincident with the maximum temperature (constant humidity ratio throughout day).
        |  Required only if field Humidity Condition Type is "HumidityRatio".
        |  Units: kgWater/kgDryAir

        Args:
            value (float): value for IDD Field `Humidity Ratio at Maximum Dry-Bulb`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `humidity_ratio_at_maximum_drybulb` or None if not set
        """
        return self["Humidity Ratio at Maximum Dry-Bulb"]

    @humidity_ratio_at_maximum_drybulb.setter
    def humidity_ratio_at_maximum_drybulb(self, value=None):
        """  Corresponds to IDD field `Humidity Ratio at Maximum Dry-Bulb`

        """
        self["Humidity Ratio at Maximum Dry-Bulb"] = value

    @property
    def enthalpy_at_maximum_drybulb(self):
        """field `Enthalpy at Maximum Dry-Bulb`

        |  Enthalpy coincident with the maximum temperature.
        |  Required only if field Humidity Condition Type is "Enthalpy".
        |  Units: J/kg

        Args:
            value (float): value for IDD Field `Enthalpy at Maximum Dry-Bulb`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `enthalpy_at_maximum_drybulb` or None if not set
        """
        return self["Enthalpy at Maximum Dry-Bulb"]

    @enthalpy_at_maximum_drybulb.setter
    def enthalpy_at_maximum_drybulb(self, value=None):
        """  Corresponds to IDD field `Enthalpy at Maximum Dry-Bulb`

        """
        self["Enthalpy at Maximum Dry-Bulb"] = value

    @property
    def daily_wetbulb_temperature_range(self):
        """field `Daily Wet-Bulb Temperature Range`

        |  Required only if Humidity Condition Type = "WetbulbProfileMultiplierSchedule" or
        |  "WetBulbProfileDefaultMultipliers"
        |  Units: deltaC

        Args:
            value (float): value for IDD Field `Daily Wet-Bulb Temperature Range`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `daily_wetbulb_temperature_range` or None if not set
        """
        return self["Daily Wet-Bulb Temperature Range"]

    @daily_wetbulb_temperature_range.setter
    def daily_wetbulb_temperature_range(self, value=None):
        """  Corresponds to IDD field `Daily Wet-Bulb Temperature Range`

        """
        self["Daily Wet-Bulb Temperature Range"] = value

    @property
    def barometric_pressure(self):
        """field `Barometric Pressure`

        |  This field's value is also checked against the calculated "standard barometric pressure"
        |  for the location.  If out of range (>10%) or blank, then is replaced by standard value.
        |  Units: Pa
        |  IP-Units: inHg
        |  value >= 31000.0
        |  value <= 120000.0

        Args:
            value (float): value for IDD Field `Barometric Pressure`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `barometric_pressure` or None if not set

        """
        return self["Barometric Pressure"]

    @barometric_pressure.setter
    def barometric_pressure(self, value=None):
        """Corresponds to IDD field `Barometric Pressure`"""
        self["Barometric Pressure"] = value

    @property
    def wind_speed(self):
        """field `Wind Speed`

        |  Units: m/s
        |  IP-Units: miles/hr
        |  value <= 40.0

        Args:
            value (float): value for IDD Field `Wind Speed`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `wind_speed` or None if not set

        """
        return self["Wind Speed"]

    @wind_speed.setter
    def wind_speed(self, value=None):
        """Corresponds to IDD field `Wind Speed`"""
        self["Wind Speed"] = value

    @property
    def wind_direction(self):
        """field `Wind Direction`

        |  North=0.0 East=90.0
        |  0 and 360 are the same direction.
        |  Units: deg
        |  value <= 360.0

        Args:
            value (float): value for IDD Field `Wind Direction`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `wind_direction` or None if not set

        """
        return self["Wind Direction"]

    @wind_direction.setter
    def wind_direction(self, value=None):
        """Corresponds to IDD field `Wind Direction`"""
        self["Wind Direction"] = value

    @property
    def rain_indicator(self):
        """field `Rain Indicator`

        |  Yes is raining (all day), No is not raining
        |  Default value: No

        Args:
            value (str): value for IDD Field `Rain Indicator`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `rain_indicator` or None if not set

        """
        return self["Rain Indicator"]

    @rain_indicator.setter
    def rain_indicator(self, value="No"):
        """Corresponds to IDD field `Rain Indicator`"""
        self["Rain Indicator"] = value

    @property
    def snow_indicator(self):
        """field `Snow Indicator`

        |  Yes is Snow on Ground, No is no Snow on Ground
        |  Default value: No

        Args:
            value (str): value for IDD Field `Snow Indicator`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `snow_indicator` or None if not set

        """
        return self["Snow Indicator"]

    @snow_indicator.setter
    def snow_indicator(self, value="No"):
        """Corresponds to IDD field `Snow Indicator`"""
        self["Snow Indicator"] = value

    @property
    def daylight_saving_time_indicator(self):
        """field `Daylight Saving Time Indicator`

        |  Yes -- use schedules modified for Daylight Saving Time Schedules.
        |  No - do not use schedules modified for Daylight Saving Time Schedules
        |  Default value: No

        Args:
            value (str): value for IDD Field `Daylight Saving Time Indicator`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `daylight_saving_time_indicator` or None if not set

        """
        return self["Daylight Saving Time Indicator"]

    @daylight_saving_time_indicator.setter
    def daylight_saving_time_indicator(self, value="No"):
        """Corresponds to IDD field `Daylight Saving Time Indicator`"""
        self["Daylight Saving Time Indicator"] = value

    @property
    def solar_model_indicator(self):
        """field `Solar Model Indicator`

        |  Default value: ASHRAEClearSky

        Args:
            value (str): value for IDD Field `Solar Model Indicator`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `solar_model_indicator` or None if not set

        """
        return self["Solar Model Indicator"]

    @solar_model_indicator.setter
    def solar_model_indicator(self, value="ASHRAEClearSky"):
        """Corresponds to IDD field `Solar Model Indicator`"""
        self["Solar Model Indicator"] = value

    @property
    def beam_solar_day_schedule_name(self):
        """field `Beam Solar Day Schedule Name`

        |  if Solar Model Indicator = Schedule, then beam schedule name (for day)

        Args:
            value (str): value for IDD Field `Beam Solar Day Schedule Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `beam_solar_day_schedule_name` or None if not set

        """
        return self["Beam Solar Day Schedule Name"]

    @beam_solar_day_schedule_name.setter
    def beam_solar_day_schedule_name(self, value=None):
        """Corresponds to IDD field `Beam Solar Day Schedule Name`"""
        self["Beam Solar Day Schedule Name"] = value

    @property
    def diffuse_solar_day_schedule_name(self):
        """field `Diffuse Solar Day Schedule Name`

        |  if Solar Model Indicator = Schedule, then diffuse schedule name (for day)

        Args:
            value (str): value for IDD Field `Diffuse Solar Day Schedule Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `diffuse_solar_day_schedule_name` or None if not set

        """
        return self["Diffuse Solar Day Schedule Name"]

    @diffuse_solar_day_schedule_name.setter
    def diffuse_solar_day_schedule_name(self, value=None):
        """Corresponds to IDD field `Diffuse Solar Day Schedule Name`"""
        self["Diffuse Solar Day Schedule Name"] = value

    @property
    def ashrae_clear_sky_optical_depth_for_beam_irradiance_taub(self):
        """field `ASHRAE Clear Sky Optical Depth for Beam Irradiance (taub)`

        |  Required if Solar Model Indicator = ASHRAETau
        |  Units: dimensionless
        |  value <= 1.2

        Args:
            value (float): value for IDD Field `ASHRAE Clear Sky Optical Depth for Beam Irradiance (taub)`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `ashrae_clear_sky_optical_depth_for_beam_irradiance_taub` or None if not set

        """
        return self[
            "ASHRAE Clear Sky Optical Depth for Beam Irradiance (taub)"]

    @ashrae_clear_sky_optical_depth_for_beam_irradiance_taub.setter
    def ashrae_clear_sky_optical_depth_for_beam_irradiance_taub(
            self,
            value=None):
        """Corresponds to IDD field `ASHRAE Clear Sky Optical Depth for Beam
        Irradiance (taub)`"""
        self[
            "ASHRAE Clear Sky Optical Depth for Beam Irradiance (taub)"] = value

    @property
    def ashrae_clear_sky_optical_depth_for_diffuse_irradiance_taud(self):
        """field `ASHRAE Clear Sky Optical Depth for Diffuse Irradiance (taud)`

        |  Required if Solar Model Indicator = ASHRAETau
        |  Units: dimensionless
        |  value <= 3.0

        Args:
            value (float): value for IDD Field `ASHRAE Clear Sky Optical Depth for Diffuse Irradiance (taud)`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `ashrae_clear_sky_optical_depth_for_diffuse_irradiance_taud` or None if not set

        """
        return self[
            "ASHRAE Clear Sky Optical Depth for Diffuse Irradiance (taud)"]

    @ashrae_clear_sky_optical_depth_for_diffuse_irradiance_taud.setter
    def ashrae_clear_sky_optical_depth_for_diffuse_irradiance_taud(
            self,
            value=None):
        """Corresponds to IDD field `ASHRAE Clear Sky Optical Depth for Diffuse
        Irradiance (taud)`"""
        self[
            "ASHRAE Clear Sky Optical Depth for Diffuse Irradiance (taud)"] = value

    @property
    def sky_clearness(self):
        """field `Sky Clearness`

        |  Used if Sky Model Indicator = ASHRAEClearSky or ZhangHuang
        |  0.0 is totally unclear, 1.0 is totally clear
        |  value <= 1.2

        Args:
            value (float): value for IDD Field `Sky Clearness`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `sky_clearness` or None if not set

        """
        return self["Sky Clearness"]

    @sky_clearness.setter
    def sky_clearness(self, value=None):
        """Corresponds to IDD field `Sky Clearness`"""
        self["Sky Clearness"] = value




class SizingPeriodWeatherFileDays(DataObject):

    """ Corresponds to IDD object `SizingPeriod:WeatherFileDays`
        Use a weather file period for design sizing calculations.
    """
    _schema = {'extensible-fields': OrderedDict(),
               'fields': OrderedDict([(u'name',
                                       {'name': u'Name',
                                        'pyname': u'name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'begin month',
                                       {'name': u'Begin Month',
                                        'pyname': u'begin_month',
                                        'maximum': 12,
                                        'required-field': True,
                                        'autosizable': False,
                                        'minimum': 1,
                                        'autocalculatable': False,
                                        'type': u'integer'}),
                                      (u'begin day of month',
                                       {'name': u'Begin Day of Month',
                                        'pyname': u'begin_day_of_month',
                                        'maximum': 31,
                                        'required-field': True,
                                        'autosizable': False,
                                        'minimum': 1,
                                        'autocalculatable': False,
                                        'type': u'integer'}),
                                      (u'end month',
                                       {'name': u'End Month',
                                        'pyname': u'end_month',
                                        'maximum': 12,
                                        'required-field': True,
                                        'autosizable': False,
                                        'minimum': 1,
                                        'autocalculatable': False,
                                        'type': u'integer'}),
                                      (u'end day of month',
                                       {'name': u'End Day of Month',
                                        'pyname': u'end_day_of_month',
                                        'maximum': 31,
                                        'required-field': True,
                                        'autosizable': False,
                                        'minimum': 1,
                                        'autocalculatable': False,
                                        'type': u'integer'}),
                                      (u'day of week for start day',
                                       {'name': u'Day of Week for Start Day',
                                        'pyname': u'day_of_week_for_start_day',
                                        'default': u'Monday',
                                        'required-field': False,
                                        'autosizable': False,
                                        'accepted-values': [u'Sunday',
                                                            u'Monday',
                                                            u'Tuesday',
                                                            u'Wednesday',
                                                            u'Thursday',
                                                            u'Friday',
                                                            u'Saturday',
                                                            u'SummerDesignDay',
                                                            u'WinterDesignDay',
                                                            u'CustomDay1',
                                                            u'CustomDay2'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'use weather file daylight saving period',
                                       {'name': u'Use Weather File Daylight Saving Period',
                                        'pyname': u'use_weather_file_daylight_saving_period',
                                        'default': u'Yes',
                                        'required-field': False,
                                        'autosizable': False,
                                        'accepted-values': [u'Yes',
                                                            u'No'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'use weather file rain and snow indicators',
                                       {'name': u'Use Weather File Rain and Snow Indicators',
                                        'pyname': u'use_weather_file_rain_and_snow_indicators',
                                        'default': u'Yes',
                                        'required-field': False,
                                        'autosizable': False,
                                        'accepted-values': [u'Yes',
                                                            u'No'],
                                        'autocalculatable': False,
                                        'type': 'alpha'})]),
               'format': None,
               'group': u'Location and Climate',
               'min-fields': 0,
               'name': u'SizingPeriod:WeatherFileDays',
               'pyname': u'SizingPeriodWeatherFileDays',
               'required-object': False,
               'unique-object': False}

    @property
    def name(self):
        """field `Name`

        |  user supplied name for reporting

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
    def begin_month(self):
        """field `Begin Month`

        |  value >= 1
        |  value <= 12

        Args:
            value (int): value for IDD Field `Begin Month`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            int: the value of `begin_month` or None if not set

        """
        return self["Begin Month"]

    @begin_month.setter
    def begin_month(self, value=None):
        """Corresponds to IDD field `Begin Month`"""
        self["Begin Month"] = value

    @property
    def begin_day_of_month(self):
        """field `Begin Day of Month`

        |  value >= 1
        |  value <= 31

        Args:
            value (int): value for IDD Field `Begin Day of Month`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            int: the value of `begin_day_of_month` or None if not set

        """
        return self["Begin Day of Month"]

    @begin_day_of_month.setter
    def begin_day_of_month(self, value=None):
        """Corresponds to IDD field `Begin Day of Month`"""
        self["Begin Day of Month"] = value

    @property
    def end_month(self):
        """field `End Month`

        |  value >= 1
        |  value <= 12

        Args:
            value (int): value for IDD Field `End Month`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            int: the value of `end_month` or None if not set

        """
        return self["End Month"]

    @end_month.setter
    def end_month(self, value=None):
        """Corresponds to IDD field `End Month`"""
        self["End Month"] = value

    @property
    def end_day_of_month(self):
        """field `End Day of Month`

        |  value >= 1
        |  value <= 31

        Args:
            value (int): value for IDD Field `End Day of Month`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            int: the value of `end_day_of_month` or None if not set

        """
        return self["End Day of Month"]

    @end_day_of_month.setter
    def end_day_of_month(self, value=None):
        """Corresponds to IDD field `End Day of Month`"""
        self["End Day of Month"] = value

    @property
    def day_of_week_for_start_day(self):
        """field `Day of Week for Start Day`

        |  =[|Sunday|Monday|Tuesday|Wednesday|Thursday|Friday|Saturday|SummerDesignDay|WinterDesignDay|
        |  |CustomDay1|CustomDay2];
        |  if you use SummerDesignDay or WinterDesignDay or the CustomDays then this will apply
        |  to the whole period; other days (i.e., Monday) will signify a start day and
        |  normal sequence of subsequent days
        |  Default value: Monday

        Args:
            value (str): value for IDD Field `Day of Week for Start Day`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `day_of_week_for_start_day` or None if not set

        """
        return self["Day of Week for Start Day"]

    @day_of_week_for_start_day.setter
    def day_of_week_for_start_day(self, value="Monday"):
        """Corresponds to IDD field `Day of Week for Start Day`"""
        self["Day of Week for Start Day"] = value

    @property
    def use_weather_file_daylight_saving_period(self):
        """field `Use Weather File Daylight Saving Period`

        |  If yes or blank, use daylight saving period as specified on Weatherfile.
        |  If no, do not use the daylight saving period as specified on the Weatherfile.
        |  Default value: Yes

        Args:
            value (str): value for IDD Field `Use Weather File Daylight Saving Period`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `use_weather_file_daylight_saving_period` or None if not set

        """
        return self["Use Weather File Daylight Saving Period"]

    @use_weather_file_daylight_saving_period.setter
    def use_weather_file_daylight_saving_period(self, value="Yes"):
        """Corresponds to IDD field `Use Weather File Daylight Saving
        Period`"""
        self["Use Weather File Daylight Saving Period"] = value

    @property
    def use_weather_file_rain_and_snow_indicators(self):
        """field `Use Weather File Rain and Snow Indicators`

        |  Default value: Yes

        Args:
            value (str): value for IDD Field `Use Weather File Rain and Snow Indicators`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `use_weather_file_rain_and_snow_indicators` or None if not set

        """
        return self["Use Weather File Rain and Snow Indicators"]

    @use_weather_file_rain_and_snow_indicators.setter
    def use_weather_file_rain_and_snow_indicators(self, value="Yes"):
        """Corresponds to IDD field `Use Weather File Rain and Snow
        Indicators`"""
        self["Use Weather File Rain and Snow Indicators"] = value




class SizingPeriodWeatherFileConditionType(DataObject):

    """ Corresponds to IDD object `SizingPeriod:WeatherFileConditionType`
        Use a weather file period for design sizing calculations.
        EPW weather files are created with typical and extreme periods
        created heuristically from the weather file data.  For more
        details on these periods, see AuxiliaryPrograms document.
    """
    _schema = {'extensible-fields': OrderedDict(),
               'fields': OrderedDict([(u'name',
                                       {'name': u'Name',
                                        'pyname': u'name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'period selection',
                                       {'name': u'Period Selection',
                                        'pyname': u'period_selection',
                                        'required-field': True,
                                        'autosizable': False,
                                        'accepted-values': [u'SummerExtreme',
                                                            u'SummerTypical',
                                                            u'WinterExtreme',
                                                            u'WinterTypical',
                                                            u'AutumnTypical',
                                                            u'SpringTypical',
                                                            u'WetSeason',
                                                            u'DrySeason',
                                                            u'NoDrySeason',
                                                            u'NoWetSeason',
                                                            u'TropicalHot',
                                                            u'TropicalCold',
                                                            u'NoDrySeasonMax',
                                                            u'NoDrySeasonMin',
                                                            u'NoWetSeasonMax',
                                                            u'NoWetSeasonMin'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'day of week for start day',
                                       {'name': u'Day of Week for Start Day',
                                        'pyname': u'day_of_week_for_start_day',
                                        'default': u'Monday',
                                        'required-field': False,
                                        'autosizable': False,
                                        'accepted-values': [u'Sunday',
                                                            u'Monday',
                                                            u'Tuesday',
                                                            u'Wednesday',
                                                            u'Thursday',
                                                            u'Friday',
                                                            u'Saturday',
                                                            u'SummerDesignDay',
                                                            u'WinterDesignDay',
                                                            u'CustomDay1',
                                                            u'CustomDay2'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'use weather file daylight saving period',
                                       {'name': u'Use Weather File Daylight Saving Period',
                                        'pyname': u'use_weather_file_daylight_saving_period',
                                        'default': u'Yes',
                                        'required-field': False,
                                        'autosizable': False,
                                        'accepted-values': [u'Yes',
                                                            u'No'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'use weather file rain and snow indicators',
                                       {'name': u'Use Weather File Rain and Snow Indicators',
                                        'pyname': u'use_weather_file_rain_and_snow_indicators',
                                        'default': u'Yes',
                                        'required-field': False,
                                        'autosizable': False,
                                        'accepted-values': [u'Yes',
                                                            u'No'],
                                        'autocalculatable': False,
                                        'type': 'alpha'})]),
               'format': None,
               'group': u'Location and Climate',
               'min-fields': 0,
               'name': u'SizingPeriod:WeatherFileConditionType',
               'pyname': u'SizingPeriodWeatherFileConditionType',
               'required-object': False,
               'unique-object': False}

    @property
    def name(self):
        """field `Name`

        |  user supplied name for reporting

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
    def period_selection(self):
        """field `Period Selection`

        |  Following is a list of all possible types of Extreme and Typical periods that
        |  might be identified in the Weather File. Not all possible types are available
        |  for all weather files.

        Args:
            value (str): value for IDD Field `Period Selection`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `period_selection` or None if not set

        """
        return self["Period Selection"]

    @period_selection.setter
    def period_selection(self, value=None):
        """Corresponds to IDD field `Period Selection`"""
        self["Period Selection"] = value

    @property
    def day_of_week_for_start_day(self):
        """field `Day of Week for Start Day`

        |  =[|Sunday|Monday|Tuesday|Wednesday|Thursday|Friday|Saturday|SummerDesignDay|WinterDesignDay|
        |  |CustomDay1|CustomDay2];
        |  if you use SummerDesignDay or WinterDesignDay or the CustomDays then this will apply
        |  to the whole period; other days (i.e., Monday) will signify a start day and
        |  normal sequence of subsequent days
        |  Default value: Monday

        Args:
            value (str): value for IDD Field `Day of Week for Start Day`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `day_of_week_for_start_day` or None if not set

        """
        return self["Day of Week for Start Day"]

    @day_of_week_for_start_day.setter
    def day_of_week_for_start_day(self, value="Monday"):
        """Corresponds to IDD field `Day of Week for Start Day`"""
        self["Day of Week for Start Day"] = value

    @property
    def use_weather_file_daylight_saving_period(self):
        """field `Use Weather File Daylight Saving Period`

        |  If yes or blank, use daylight saving period as specified on Weatherfile.
        |  If no, do not use the daylight saving period as specified on the Weatherfile.
        |  Default value: Yes

        Args:
            value (str): value for IDD Field `Use Weather File Daylight Saving Period`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `use_weather_file_daylight_saving_period` or None if not set

        """
        return self["Use Weather File Daylight Saving Period"]

    @use_weather_file_daylight_saving_period.setter
    def use_weather_file_daylight_saving_period(self, value="Yes"):
        """Corresponds to IDD field `Use Weather File Daylight Saving
        Period`"""
        self["Use Weather File Daylight Saving Period"] = value

    @property
    def use_weather_file_rain_and_snow_indicators(self):
        """field `Use Weather File Rain and Snow Indicators`

        |  Default value: Yes

        Args:
            value (str): value for IDD Field `Use Weather File Rain and Snow Indicators`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `use_weather_file_rain_and_snow_indicators` or None if not set

        """
        return self["Use Weather File Rain and Snow Indicators"]

    @use_weather_file_rain_and_snow_indicators.setter
    def use_weather_file_rain_and_snow_indicators(self, value="Yes"):
        """Corresponds to IDD field `Use Weather File Rain and Snow
        Indicators`"""
        self["Use Weather File Rain and Snow Indicators"] = value




class RunPeriod(DataObject):

    """Corresponds to IDD object `RunPeriod` Specified a range of dates and
    other parameters for a weather file simulation.

    Multiple run periods may be input, but they may not overlap.

    """
    _schema = {'extensible-fields': OrderedDict(),
               'fields': OrderedDict([(u'name',
                                       {'name': u'Name',
                                        'pyname': u'name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'begin month',
                                       {'name': u'Begin Month',
                                        'pyname': u'begin_month',
                                        'maximum': 12,
                                        'required-field': True,
                                        'autosizable': False,
                                        'minimum': 1,
                                        'autocalculatable': False,
                                        'type': u'integer'}),
                                      (u'begin day of month',
                                       {'name': u'Begin Day of Month',
                                        'pyname': u'begin_day_of_month',
                                        'maximum': 31,
                                        'required-field': True,
                                        'autosizable': False,
                                        'minimum': 1,
                                        'autocalculatable': False,
                                        'type': u'integer'}),
                                      (u'end month',
                                       {'name': u'End Month',
                                        'pyname': u'end_month',
                                        'maximum': 12,
                                        'required-field': True,
                                        'autosizable': False,
                                        'minimum': 1,
                                        'autocalculatable': False,
                                        'type': u'integer'}),
                                      (u'end day of month',
                                       {'name': u'End Day of Month',
                                        'pyname': u'end_day_of_month',
                                        'maximum': 31,
                                        'required-field': True,
                                        'autosizable': False,
                                        'minimum': 1,
                                        'autocalculatable': False,
                                        'type': u'integer'}),
                                      (u'day of week for start day',
                                       {'name': u'Day of Week for Start Day',
                                        'pyname': u'day_of_week_for_start_day',
                                        'default': u'UseWeatherFile',
                                        'required-field': False,
                                        'autosizable': False,
                                        'accepted-values': [u'Sunday',
                                                            u'Monday',
                                                            u'Tuesday',
                                                            u'Wednesday',
                                                            u'Thursday',
                                                            u'Friday',
                                                            u'Saturday',
                                                            u'UseWeatherFile'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'use weather file holidays and special days',
                                       {'name': u'Use Weather File Holidays and Special Days',
                                        'pyname': u'use_weather_file_holidays_and_special_days',
                                        'default': u'Yes',
                                        'required-field': False,
                                        'autosizable': False,
                                        'accepted-values': [u'Yes',
                                                            u'No'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'use weather file daylight saving period',
                                       {'name': u'Use Weather File Daylight Saving Period',
                                        'pyname': u'use_weather_file_daylight_saving_period',
                                        'default': u'Yes',
                                        'required-field': False,
                                        'autosizable': False,
                                        'accepted-values': [u'Yes',
                                                            u'No'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'apply weekend holiday rule',
                                       {'name': u'Apply Weekend Holiday Rule',
                                        'pyname': u'apply_weekend_holiday_rule',
                                        'default': u'No',
                                        'required-field': False,
                                        'autosizable': False,
                                        'accepted-values': [u'Yes',
                                                            u'No'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'use weather file rain indicators',
                                       {'name': u'Use Weather File Rain Indicators',
                                        'pyname': u'use_weather_file_rain_indicators',
                                        'default': u'Yes',
                                        'required-field': False,
                                        'autosizable': False,
                                        'accepted-values': [u'Yes',
                                                            u'No'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'use weather file snow indicators',
                                       {'name': u'Use Weather File Snow Indicators',
                                        'pyname': u'use_weather_file_snow_indicators',
                                        'default': u'Yes',
                                        'required-field': False,
                                        'autosizable': False,
                                        'accepted-values': [u'Yes',
                                                            u'No'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'number of times runperiod to be repeated',
                                       {'name': u'Number of Times Runperiod to be Repeated',
                                        'pyname': u'number_of_times_runperiod_to_be_repeated',
                                        'default': 1,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 1,
                                        'autocalculatable': False,
                                        'type': u'integer'}),
                                      (u'increment day of week on repeat',
                                       {'name': u'Increment Day of Week on repeat',
                                        'pyname': u'increment_day_of_week_on_repeat',
                                        'default': u'Yes',
                                        'required-field': False,
                                        'autosizable': False,
                                        'accepted-values': [u'Yes',
                                                            u'No'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'start year',
                                       {'name': u'Start Year',
                                        'pyname': u'start_year',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': 'real'})]),
               'format': None,
               'group': u'Location and Climate',
               'min-fields': 11,
               'name': u'RunPeriod',
               'pyname': u'RunPeriod',
               'required-object': False,
               'unique-object': False}

    @property
    def name(self):
        """field `Name`

        |  descriptive name (used in reporting mainly)
        |  if blank, weather file title is used.  if not blank, must be unique

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
    def begin_month(self):
        """field `Begin Month`

        |  value >= 1
        |  value <= 12

        Args:
            value (int): value for IDD Field `Begin Month`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            int: the value of `begin_month` or None if not set

        """
        return self["Begin Month"]

    @begin_month.setter
    def begin_month(self, value=None):
        """Corresponds to IDD field `Begin Month`"""
        self["Begin Month"] = value

    @property
    def begin_day_of_month(self):
        """field `Begin Day of Month`

        |  value >= 1
        |  value <= 31

        Args:
            value (int): value for IDD Field `Begin Day of Month`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            int: the value of `begin_day_of_month` or None if not set

        """
        return self["Begin Day of Month"]

    @begin_day_of_month.setter
    def begin_day_of_month(self, value=None):
        """Corresponds to IDD field `Begin Day of Month`"""
        self["Begin Day of Month"] = value

    @property
    def end_month(self):
        """field `End Month`

        |  value >= 1
        |  value <= 12

        Args:
            value (int): value for IDD Field `End Month`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            int: the value of `end_month` or None if not set

        """
        return self["End Month"]

    @end_month.setter
    def end_month(self, value=None):
        """Corresponds to IDD field `End Month`"""
        self["End Month"] = value

    @property
    def end_day_of_month(self):
        """field `End Day of Month`

        |  value >= 1
        |  value <= 31

        Args:
            value (int): value for IDD Field `End Day of Month`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            int: the value of `end_day_of_month` or None if not set

        """
        return self["End Day of Month"]

    @end_day_of_month.setter
    def end_day_of_month(self, value=None):
        """Corresponds to IDD field `End Day of Month`"""
        self["End Day of Month"] = value

    @property
    def day_of_week_for_start_day(self):
        """field `Day of Week for Start Day`

        |  =<blank - use WeatherFile>|Sunday|Monday|Tuesday|Wednesday|Thursday|Friday|Saturday];
        |  Default value: UseWeatherFile

        Args:
            value (str): value for IDD Field `Day of Week for Start Day`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `day_of_week_for_start_day` or None if not set

        """
        return self["Day of Week for Start Day"]

    @day_of_week_for_start_day.setter
    def day_of_week_for_start_day(self, value="UseWeatherFile"):
        """Corresponds to IDD field `Day of Week for Start Day`"""
        self["Day of Week for Start Day"] = value

    @property
    def use_weather_file_holidays_and_special_days(self):
        """field `Use Weather File Holidays and Special Days`

        |  If yes or blank, use holidays as specified on Weatherfile.
        |  If no, do not use the holidays specified on the Weatherfile.
        |  Note: You can still specify holidays/special days using the RunPeriodControl:SpecialDays object(s).
        |  Default value: Yes

        Args:
            value (str): value for IDD Field `Use Weather File Holidays and Special Days`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `use_weather_file_holidays_and_special_days` or None if not set

        """
        return self["Use Weather File Holidays and Special Days"]

    @use_weather_file_holidays_and_special_days.setter
    def use_weather_file_holidays_and_special_days(self, value="Yes"):
        """Corresponds to IDD field `Use Weather File Holidays and Special
        Days`"""
        self["Use Weather File Holidays and Special Days"] = value

    @property
    def use_weather_file_daylight_saving_period(self):
        """field `Use Weather File Daylight Saving Period`

        |  If yes or blank, use daylight saving period as specified on Weatherfile.
        |  If no, do not use the daylight saving period as specified on the Weatherfile.
        |  Default value: Yes

        Args:
            value (str): value for IDD Field `Use Weather File Daylight Saving Period`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `use_weather_file_daylight_saving_period` or None if not set

        """
        return self["Use Weather File Daylight Saving Period"]

    @use_weather_file_daylight_saving_period.setter
    def use_weather_file_daylight_saving_period(self, value="Yes"):
        """Corresponds to IDD field `Use Weather File Daylight Saving
        Period`"""
        self["Use Weather File Daylight Saving Period"] = value

    @property
    def apply_weekend_holiday_rule(self):
        """field `Apply Weekend Holiday Rule`

        |  if yes and single day holiday falls on weekend, "holiday" occurs on following Monday
        |  Default value: No

        Args:
            value (str): value for IDD Field `Apply Weekend Holiday Rule`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `apply_weekend_holiday_rule` or None if not set

        """
        return self["Apply Weekend Holiday Rule"]

    @apply_weekend_holiday_rule.setter
    def apply_weekend_holiday_rule(self, value="No"):
        """Corresponds to IDD field `Apply Weekend Holiday Rule`"""
        self["Apply Weekend Holiday Rule"] = value

    @property
    def use_weather_file_rain_indicators(self):
        """field `Use Weather File Rain Indicators`

        |  Default value: Yes

        Args:
            value (str): value for IDD Field `Use Weather File Rain Indicators`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `use_weather_file_rain_indicators` or None if not set

        """
        return self["Use Weather File Rain Indicators"]

    @use_weather_file_rain_indicators.setter
    def use_weather_file_rain_indicators(self, value="Yes"):
        """Corresponds to IDD field `Use Weather File Rain Indicators`"""
        self["Use Weather File Rain Indicators"] = value

    @property
    def use_weather_file_snow_indicators(self):
        """field `Use Weather File Snow Indicators`

        |  Default value: Yes

        Args:
            value (str): value for IDD Field `Use Weather File Snow Indicators`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `use_weather_file_snow_indicators` or None if not set

        """
        return self["Use Weather File Snow Indicators"]

    @use_weather_file_snow_indicators.setter
    def use_weather_file_snow_indicators(self, value="Yes"):
        """Corresponds to IDD field `Use Weather File Snow Indicators`"""
        self["Use Weather File Snow Indicators"] = value

    @property
    def number_of_times_runperiod_to_be_repeated(self):
        """field `Number of Times Runperiod to be Repeated`

        |  Default value: 1
        |  value >= 1

        Args:
            value (int): value for IDD Field `Number of Times Runperiod to be Repeated`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            int: the value of `number_of_times_runperiod_to_be_repeated` or None if not set

        """
        return self["Number of Times Runperiod to be Repeated"]

    @number_of_times_runperiod_to_be_repeated.setter
    def number_of_times_runperiod_to_be_repeated(self, value=1):
        """Corresponds to IDD field `Number of Times Runperiod to be
        Repeated`"""
        self["Number of Times Runperiod to be Repeated"] = value

    @property
    def increment_day_of_week_on_repeat(self):
        """field `Increment Day of Week on repeat`

        |  Default value: Yes

        Args:
            value (str): value for IDD Field `Increment Day of Week on repeat`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `increment_day_of_week_on_repeat` or None if not set

        """
        return self["Increment Day of Week on repeat"]

    @increment_day_of_week_on_repeat.setter
    def increment_day_of_week_on_repeat(self, value="Yes"):
        """Corresponds to IDD field `Increment Day of Week on repeat`"""
        self["Increment Day of Week on repeat"] = value

    @property
    def start_year(self):
        """field `Start Year`

        |  this is the start year for the start date.  If the leap year is "Yes" in the weather file header
        |  (that is HOLIDAYS/SPECIAL DAYS header first field), then any year which is a leap year will assume
        |  there will be a Feb 29. A repeat of this runperiod will automatically increment the year.

        Args:
            value (float): value for IDD Field `Start Year`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `start_year` or None if not set

        """
        return self["Start Year"]

    @start_year.setter
    def start_year(self, value=None):
        """Corresponds to IDD field `Start Year`"""
        self["Start Year"] = value




class RunPeriodCustomRange(DataObject):

    """ Corresponds to IDD object `RunPeriod:CustomRange`
        run simulation for a custom created weather file
    """
    _schema = {'extensible-fields': OrderedDict(),
               'fields': OrderedDict([(u'name',
                                       {'name': u'Name',
                                        'pyname': u'name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'begin month',
                                       {'name': u'Begin Month',
                                        'pyname': u'begin_month',
                                        'maximum': 12,
                                        'required-field': True,
                                        'autosizable': False,
                                        'minimum': 1,
                                        'autocalculatable': False,
                                        'type': u'integer'}),
                                      (u'begin day of month',
                                       {'name': u'Begin Day of Month',
                                        'pyname': u'begin_day_of_month',
                                        'maximum': 31,
                                        'required-field': True,
                                        'autosizable': False,
                                        'minimum': 1,
                                        'autocalculatable': False,
                                        'type': u'integer'}),
                                      (u'begin year',
                                       {'name': u'Begin Year',
                                        'pyname': u'begin_year',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': 'real'}),
                                      (u'end month',
                                       {'name': u'End Month',
                                        'pyname': u'end_month',
                                        'maximum': 12,
                                        'required-field': True,
                                        'autosizable': False,
                                        'minimum': 1,
                                        'autocalculatable': False,
                                        'type': u'integer'}),
                                      (u'end day of month',
                                       {'name': u'End Day of Month',
                                        'pyname': u'end_day_of_month',
                                        'maximum': 31,
                                        'required-field': True,
                                        'autosizable': False,
                                        'minimum': 1,
                                        'autocalculatable': False,
                                        'type': u'integer'}),
                                      (u'end year',
                                       {'name': u'End Year',
                                        'pyname': u'end_year',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': 'real'}),
                                      (u'day of week for start day',
                                       {'name': u'Day of Week for Start Day',
                                        'pyname': u'day_of_week_for_start_day',
                                        'default': u'UseWeatherFile',
                                        'required-field': False,
                                        'autosizable': False,
                                        'accepted-values': [u'Sunday',
                                                            u'Monday',
                                                            u'Tuesday',
                                                            u'Wednesday',
                                                            u'Thursday',
                                                            u'Friday',
                                                            u'Saturday',
                                                            u'UseWeatherFile'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'use weather file holidays and special days',
                                       {'name': u'Use Weather File Holidays and Special Days',
                                        'pyname': u'use_weather_file_holidays_and_special_days',
                                        'default': u'Yes',
                                        'required-field': False,
                                        'autosizable': False,
                                        'accepted-values': [u'Yes',
                                                            u'No'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'use weather file daylight saving period',
                                       {'name': u'Use Weather File Daylight Saving Period',
                                        'pyname': u'use_weather_file_daylight_saving_period',
                                        'default': u'Yes',
                                        'required-field': False,
                                        'autosizable': False,
                                        'accepted-values': [u'Yes',
                                                            u'No'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'apply weekend holiday rule',
                                       {'name': u'Apply Weekend Holiday Rule',
                                        'pyname': u'apply_weekend_holiday_rule',
                                        'default': u'No',
                                        'required-field': False,
                                        'autosizable': False,
                                        'accepted-values': [u'Yes',
                                                            u'No'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'use weather file rain indicators',
                                       {'name': u'Use Weather File Rain Indicators',
                                        'pyname': u'use_weather_file_rain_indicators',
                                        'default': u'Yes',
                                        'required-field': False,
                                        'autosizable': False,
                                        'accepted-values': [u'Yes',
                                                            u'No'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'use weather file snow indicators',
                                       {'name': u'Use Weather File Snow Indicators',
                                        'pyname': u'use_weather_file_snow_indicators',
                                        'default': u'Yes',
                                        'required-field': False,
                                        'autosizable': False,
                                        'accepted-values': [u'Yes',
                                                            u'No'],
                                        'autocalculatable': False,
                                        'type': 'alpha'})]),
               'format': None,
               'group': u'Location and Climate',
               'min-fields': 13,
               'name': u'RunPeriod:CustomRange',
               'pyname': u'RunPeriodCustomRange',
               'required-object': False,
               'unique-object': False}

    @property
    def name(self):
        """field `Name`

        |  descriptive name (used in reporting mainly)
        |  if blank, weather file title is used.  if not blank, must be unique

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
    def begin_month(self):
        """field `Begin Month`

        |  value >= 1
        |  value <= 12

        Args:
            value (int): value for IDD Field `Begin Month`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            int: the value of `begin_month` or None if not set

        """
        return self["Begin Month"]

    @begin_month.setter
    def begin_month(self, value=None):
        """Corresponds to IDD field `Begin Month`"""
        self["Begin Month"] = value

    @property
    def begin_day_of_month(self):
        """field `Begin Day of Month`

        |  value >= 1
        |  value <= 31

        Args:
            value (int): value for IDD Field `Begin Day of Month`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            int: the value of `begin_day_of_month` or None if not set

        """
        return self["Begin Day of Month"]

    @begin_day_of_month.setter
    def begin_day_of_month(self, value=None):
        """Corresponds to IDD field `Begin Day of Month`"""
        self["Begin Day of Month"] = value

    @property
    def begin_year(self):
        """field `Begin Year`

        |  must be start year of this date on weather file

        Args:
            value (float): value for IDD Field `Begin Year`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `begin_year` or None if not set

        """
        return self["Begin Year"]

    @begin_year.setter
    def begin_year(self, value=None):
        """Corresponds to IDD field `Begin Year`"""
        self["Begin Year"] = value

    @property
    def end_month(self):
        """field `End Month`

        |  value >= 1
        |  value <= 12

        Args:
            value (int): value for IDD Field `End Month`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            int: the value of `end_month` or None if not set

        """
        return self["End Month"]

    @end_month.setter
    def end_month(self, value=None):
        """Corresponds to IDD field `End Month`"""
        self["End Month"] = value

    @property
    def end_day_of_month(self):
        """field `End Day of Month`

        |  value >= 1
        |  value <= 31

        Args:
            value (int): value for IDD Field `End Day of Month`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            int: the value of `end_day_of_month` or None if not set

        """
        return self["End Day of Month"]

    @end_day_of_month.setter
    def end_day_of_month(self, value=None):
        """Corresponds to IDD field `End Day of Month`"""
        self["End Day of Month"] = value

    @property
    def end_year(self):
        """field `End Year`

        |  must be end year of this date on weather file

        Args:
            value (float): value for IDD Field `End Year`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `end_year` or None if not set

        """
        return self["End Year"]

    @end_year.setter
    def end_year(self, value=None):
        """Corresponds to IDD field `End Year`"""
        self["End Year"] = value

    @property
    def day_of_week_for_start_day(self):
        """field `Day of Week for Start Day`

        |  =<blank - use WeatherFile>|Sunday|Monday|Tuesday|Wednesday|Thursday|Friday|Saturday];
        |  Default value: UseWeatherFile

        Args:
            value (str): value for IDD Field `Day of Week for Start Day`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `day_of_week_for_start_day` or None if not set

        """
        return self["Day of Week for Start Day"]

    @day_of_week_for_start_day.setter
    def day_of_week_for_start_day(self, value="UseWeatherFile"):
        """Corresponds to IDD field `Day of Week for Start Day`"""
        self["Day of Week for Start Day"] = value

    @property
    def use_weather_file_holidays_and_special_days(self):
        """field `Use Weather File Holidays and Special Days`

        |  If yes or blank, use holidays as specified on Weatherfile.
        |  If no, do not use the holidays specified on the Weatherfile.
        |  Note: You can still specify holidays/special days using the RunPeriodControl:SpecialDays object(s).
        |  Default value: Yes

        Args:
            value (str): value for IDD Field `Use Weather File Holidays and Special Days`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `use_weather_file_holidays_and_special_days` or None if not set

        """
        return self["Use Weather File Holidays and Special Days"]

    @use_weather_file_holidays_and_special_days.setter
    def use_weather_file_holidays_and_special_days(self, value="Yes"):
        """Corresponds to IDD field `Use Weather File Holidays and Special
        Days`"""
        self["Use Weather File Holidays and Special Days"] = value

    @property
    def use_weather_file_daylight_saving_period(self):
        """field `Use Weather File Daylight Saving Period`

        |  If yes or blank, use daylight saving period as specified on Weatherfile.
        |  If no, do not use the daylight saving period as specified on the Weatherfile.
        |  Default value: Yes

        Args:
            value (str): value for IDD Field `Use Weather File Daylight Saving Period`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `use_weather_file_daylight_saving_period` or None if not set

        """
        return self["Use Weather File Daylight Saving Period"]

    @use_weather_file_daylight_saving_period.setter
    def use_weather_file_daylight_saving_period(self, value="Yes"):
        """Corresponds to IDD field `Use Weather File Daylight Saving
        Period`"""
        self["Use Weather File Daylight Saving Period"] = value

    @property
    def apply_weekend_holiday_rule(self):
        """field `Apply Weekend Holiday Rule`

        |  if yes and single day holiday falls on weekend, "holiday" occurs on following Monday
        |  Default value: No

        Args:
            value (str): value for IDD Field `Apply Weekend Holiday Rule`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `apply_weekend_holiday_rule` or None if not set

        """
        return self["Apply Weekend Holiday Rule"]

    @apply_weekend_holiday_rule.setter
    def apply_weekend_holiday_rule(self, value="No"):
        """Corresponds to IDD field `Apply Weekend Holiday Rule`"""
        self["Apply Weekend Holiday Rule"] = value

    @property
    def use_weather_file_rain_indicators(self):
        """field `Use Weather File Rain Indicators`

        |  Default value: Yes

        Args:
            value (str): value for IDD Field `Use Weather File Rain Indicators`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `use_weather_file_rain_indicators` or None if not set

        """
        return self["Use Weather File Rain Indicators"]

    @use_weather_file_rain_indicators.setter
    def use_weather_file_rain_indicators(self, value="Yes"):
        """Corresponds to IDD field `Use Weather File Rain Indicators`"""
        self["Use Weather File Rain Indicators"] = value

    @property
    def use_weather_file_snow_indicators(self):
        """field `Use Weather File Snow Indicators`

        |  Default value: Yes

        Args:
            value (str): value for IDD Field `Use Weather File Snow Indicators`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `use_weather_file_snow_indicators` or None if not set

        """
        return self["Use Weather File Snow Indicators"]

    @use_weather_file_snow_indicators.setter
    def use_weather_file_snow_indicators(self, value="Yes"):
        """Corresponds to IDD field `Use Weather File Snow Indicators`"""
        self["Use Weather File Snow Indicators"] = value




class RunPeriodControlSpecialDays(DataObject):

    """ Corresponds to IDD object `RunPeriodControl:SpecialDays`
        This object sets up holidays/special days to be used during weather file
        run periods.  (These are not used with SizingPeriod:* objects.)
        Depending on the value in the run period, days on the weather file may also
        be used.  However, the weather file specification will take precedence over
        any specification shown here.  (No error message on duplicate days or overlapping
        days).
    """
    _schema = {'extensible-fields': OrderedDict(),
               'fields': OrderedDict([(u'name',
                                       {'name': u'Name',
                                        'pyname': u'name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'start date',
                                       {'name': u'Start Date',
                                        'pyname': u'start_date',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'duration',
                                       {'name': u'Duration',
                                        'pyname': u'duration',
                                        'default': 1.0,
                                        'maximum': 366.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 1.0,
                                        'autocalculatable': False,
                                        'type': 'real',
                                        'unit': u'days'}),
                                      (u'special day type',
                                       {'name': u'Special Day Type',
                                        'pyname': u'special_day_type',
                                        'default': u'Holiday',
                                        'required-field': True,
                                        'autosizable': False,
                                        'accepted-values': [u'Holiday',
                                                            u'SummerDesignDay',
                                                            u'WinterDesignDay',
                                                            u'CustomDay1',
                                                            u'CustomDay2'],
                                        'autocalculatable': False,
                                        'type': 'alpha'})]),
               'format': None,
               'group': u'Location and Climate',
               'min-fields': 4,
               'name': u'RunPeriodControl:SpecialDays',
               'pyname': u'RunPeriodControlSpecialDays',
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
    def start_date(self):
        """field `Start Date`

        |  Dates can be several formats:
        |  <number>/<number>  (month/day)
        |  <number> <Month>
        |  <Month> <number>
        |  <Nth> <Weekday> in <Month)
        |  Last <WeekDay> in <Month>
        |  <Month> can be January, February, March, April, May, June, July, August, September, October, November, December
        |  Months can be the first 3 letters of the month
        |  <Weekday> can be Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday
        |  <Nth> can be 1 or 1st, 2 or 2nd, etc. up to 5(?)

        Args:
            value (str): value for IDD Field `Start Date`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `start_date` or None if not set

        """
        return self["Start Date"]

    @start_date.setter
    def start_date(self, value=None):
        """Corresponds to IDD field `Start Date`"""
        self["Start Date"] = value

    @property
    def duration(self):
        """field `Duration`

        |  Units: days
        |  Default value: 1.0
        |  value >= 1.0
        |  value <= 366.0

        Args:
            value (float): value for IDD Field `Duration`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `duration` or None if not set

        """
        return self["Duration"]

    @duration.setter
    def duration(self, value=1.0):
        """Corresponds to IDD field `Duration`"""
        self["Duration"] = value

    @property
    def special_day_type(self):
        """field `Special Day Type`

        |  Special Day Type selects the schedules appropriate for each day so labeled
        |  Default value: Holiday

        Args:
            value (str): value for IDD Field `Special Day Type`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `special_day_type` or None if not set

        """
        return self["Special Day Type"]

    @special_day_type.setter
    def special_day_type(self, value="Holiday"):
        """Corresponds to IDD field `Special Day Type`"""
        self["Special Day Type"] = value




class RunPeriodControlDaylightSavingTime(DataObject):

    """ Corresponds to IDD object `RunPeriodControl:DaylightSavingTime`
        This object sets up the daylight saving time period for any RunPeriod.
        Ignores any daylight saving time period on the weather file and uses this definition.
        These are not used with SizingPeriod:DesignDay objects.
        Use with SizingPeriod:WeatherFileDays object can be controlled in that object.
    """
    _schema = {'extensible-fields': OrderedDict(),
               'fields': OrderedDict([(u'start date',
                                       {'name': u'Start Date',
                                        'pyname': u'start_date',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'end date',
                                       {'name': u'End Date',
                                        'pyname': u'end_date',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': 'alpha'})]),
               'format': None,
               'group': u'Location and Climate',
               'min-fields': 2,
               'name': u'RunPeriodControl:DaylightSavingTime',
               'pyname': u'RunPeriodControlDaylightSavingTime',
               'required-object': False,
               'unique-object': True}

    @property
    def start_date(self):
        """field `Start Date`

        Args:
            value (str): value for IDD Field `Start Date`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `start_date` or None if not set

        """
        return self["Start Date"]

    @start_date.setter
    def start_date(self, value=None):
        """Corresponds to IDD field `Start Date`"""
        self["Start Date"] = value

    @property
    def end_date(self):
        """field `End Date`

        |  Dates can be several formats:
        |  <number>/<number>  (month/day)
        |  <number> <Month>
        |  <Month> <number>
        |  <Nth> <Weekday> in <Month)
        |  Last <WeekDay> in <Month>
        |  <Month> can be January, February, March, April, May, June, July, August, September, October, November, December
        |  Months can be the first 3 letters of the month
        |  <Weekday> can be Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday
        |  <Nth> can be 1 or 1st, 2 or 2nd, etc. up to 5(?)

        Args:
            value (str): value for IDD Field `End Date`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `end_date` or None if not set

        """
        return self["End Date"]

    @end_date.setter
    def end_date(self, value=None):
        """Corresponds to IDD field `End Date`"""
        self["End Date"] = value




class WeatherPropertySkyTemperature(DataObject):

    """ Corresponds to IDD object `WeatherProperty:SkyTemperature`
        This object is used to override internal sky temperature calculations.
    """
    _schema = {'extensible-fields': OrderedDict(),
               'fields': OrderedDict([(u'name',
                                       {'name': u'Name',
                                        'pyname': u'name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'calculation type',
                                       {'name': u'Calculation Type',
                                        'pyname': u'calculation_type',
                                        'required-field': True,
                                        'autosizable': False,
                                        'accepted-values': [u'ScheduleValue',
                                                            u'DifferenceScheduleDryBulbValue',
                                                            u'DifferenceScheduleDewPointValue'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'schedule name',
                                       {'name': u'Schedule Name',
                                        'pyname': u'schedule_name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'})]),
               'format': None,
               'group': u'Location and Climate',
               'min-fields': 0,
               'name': u'WeatherProperty:SkyTemperature',
               'pyname': u'WeatherPropertySkyTemperature',
               'required-object': False,
               'unique-object': False}

    @property
    def name(self):
        """field `Name`

        |  blank in this field will apply to all run periods (that is, all objects=
        |  SizingPeriod:WeatherFileDays, SizingPeriod:WeatherFileConditionType or RunPeriod
        |  otherwise, this name must match one of the environment object names.

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
    def calculation_type(self):
        """field `Calculation Type`

        Args:
            value (str): value for IDD Field `Calculation Type`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `calculation_type` or None if not set

        """
        return self["Calculation Type"]

    @calculation_type.setter
    def calculation_type(self, value=None):
        """Corresponds to IDD field `Calculation Type`"""
        self["Calculation Type"] = value

    @property
    def schedule_name(self):
        """field `Schedule Name`

        |  if name matches a SizingPeriod:DesignDay, put in a day schedule of this name
        |  if name is for a SizingPeriod:WeatherFileDays, SizingPeriod:WeatherFileConditionType or
        |  RunPeriod, put in a full year schedule that covers the appropriate days.

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




class SiteWeatherStation(DataObject):

    """ Corresponds to IDD object `Site:WeatherStation`
        This object should only be used for non-standard weather data.  Standard weather data
        such as TMY2, IWEC, and ASHRAE design day data are all measured at the
        default conditions and do not require this object.
    """
    _schema = {'extensible-fields': OrderedDict(),
               'fields': OrderedDict([(u'wind sensor height above ground',
                                       {'name': u'Wind Sensor Height Above Ground',
                                        'pyname': u'wind_sensor_height_above_ground',
                                        'default': 10.0,
                                        'minimum>': 0.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'm'}),
                                      (u'wind speed profile exponent',
                                       {'name': u'Wind Speed Profile Exponent',
                                        'pyname': u'wind_speed_profile_exponent',
                                        'default': 0.14,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'wind speed profile boundary layer thickness',
                                       {'name': u'Wind Speed Profile Boundary Layer Thickness',
                                        'pyname': u'wind_speed_profile_boundary_layer_thickness',
                                        'default': 270.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'm'}),
                                      (u'air temperature sensor height above ground',
                                       {'name': u'Air Temperature Sensor Height Above Ground',
                                        'pyname': u'air_temperature_sensor_height_above_ground',
                                        'default': 1.5,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'm'})]),
               'format': None,
               'group': u'Location and Climate',
               'min-fields': 0,
               'name': u'Site:WeatherStation',
               'pyname': u'SiteWeatherStation',
               'required-object': False,
               'unique-object': True}

    @property
    def wind_sensor_height_above_ground(self):
        """field `Wind Sensor Height Above Ground`

        |  Units: m
        |  Default value: 10.0

        Args:
            value (float): value for IDD Field `Wind Sensor Height Above Ground`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `wind_sensor_height_above_ground` or None if not set

        """
        return self["Wind Sensor Height Above Ground"]

    @wind_sensor_height_above_ground.setter
    def wind_sensor_height_above_ground(self, value=10.0):
        """Corresponds to IDD field `Wind Sensor Height Above Ground`"""
        self["Wind Sensor Height Above Ground"] = value

    @property
    def wind_speed_profile_exponent(self):
        """field `Wind Speed Profile Exponent`

        |  Default value: 0.14

        Args:
            value (float): value for IDD Field `Wind Speed Profile Exponent`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `wind_speed_profile_exponent` or None if not set

        """
        return self["Wind Speed Profile Exponent"]

    @wind_speed_profile_exponent.setter
    def wind_speed_profile_exponent(self, value=0.14):
        """Corresponds to IDD field `Wind Speed Profile Exponent`"""
        self["Wind Speed Profile Exponent"] = value

    @property
    def wind_speed_profile_boundary_layer_thickness(self):
        """field `Wind Speed Profile Boundary Layer Thickness`

        |  Units: m
        |  Default value: 270.0

        Args:
            value (float): value for IDD Field `Wind Speed Profile Boundary Layer Thickness`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `wind_speed_profile_boundary_layer_thickness` or None if not set

        """
        return self["Wind Speed Profile Boundary Layer Thickness"]

    @wind_speed_profile_boundary_layer_thickness.setter
    def wind_speed_profile_boundary_layer_thickness(self, value=270.0):
        """Corresponds to IDD field `Wind Speed Profile Boundary Layer
        Thickness`"""
        self["Wind Speed Profile Boundary Layer Thickness"] = value

    @property
    def air_temperature_sensor_height_above_ground(self):
        """field `Air Temperature Sensor Height Above Ground`

        |  Units: m
        |  Default value: 1.5

        Args:
            value (float): value for IDD Field `Air Temperature Sensor Height Above Ground`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `air_temperature_sensor_height_above_ground` or None if not set

        """
        return self["Air Temperature Sensor Height Above Ground"]

    @air_temperature_sensor_height_above_ground.setter
    def air_temperature_sensor_height_above_ground(self, value=1.5):
        """Corresponds to IDD field `Air Temperature Sensor Height Above
        Ground`"""
        self["Air Temperature Sensor Height Above Ground"] = value




class SiteHeightVariation(DataObject):

    """ Corresponds to IDD object `Site:HeightVariation`
        This object is used if the user requires advanced control over height-dependent
        variations in wind speed and temperature.  When this object is not present, the default model
        for temperature dependence on height is used, and the wind speed is modeled according
        to the Terrain field of the BUILDING object.
    """
    _schema = {'extensible-fields': OrderedDict(),
               'fields': OrderedDict([(u'wind speed profile exponent',
                                       {'name': u'Wind Speed Profile Exponent',
                                        'pyname': u'wind_speed_profile_exponent',
                                        'default': 0.22,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'wind speed profile boundary layer thickness',
                                       {'name': u'Wind Speed Profile Boundary Layer Thickness',
                                        'pyname': u'wind_speed_profile_boundary_layer_thickness',
                                        'default': 370.0,
                                        'minimum>': 0.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'm'}),
                                      (u'air temperature gradient coefficient',
                                       {'name': u'Air Temperature Gradient Coefficient',
                                        'pyname': u'air_temperature_gradient_coefficient',
                                        'default': 0.0065,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'K/m'})]),
               'format': None,
               'group': u'Location and Climate',
               'min-fields': 0,
               'name': u'Site:HeightVariation',
               'pyname': u'SiteHeightVariation',
               'required-object': False,
               'unique-object': True}

    @property
    def wind_speed_profile_exponent(self):
        """field `Wind Speed Profile Exponent`

        |  Set to zero for no wind speed dependence on height.
        |  Default value: 0.22

        Args:
            value (float): value for IDD Field `Wind Speed Profile Exponent`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `wind_speed_profile_exponent` or None if not set

        """
        return self["Wind Speed Profile Exponent"]

    @wind_speed_profile_exponent.setter
    def wind_speed_profile_exponent(self, value=0.22):
        """Corresponds to IDD field `Wind Speed Profile Exponent`"""
        self["Wind Speed Profile Exponent"] = value

    @property
    def wind_speed_profile_boundary_layer_thickness(self):
        """field `Wind Speed Profile Boundary Layer Thickness`

        |  Units: m
        |  Default value: 370.0

        Args:
            value (float): value for IDD Field `Wind Speed Profile Boundary Layer Thickness`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `wind_speed_profile_boundary_layer_thickness` or None if not set

        """
        return self["Wind Speed Profile Boundary Layer Thickness"]

    @wind_speed_profile_boundary_layer_thickness.setter
    def wind_speed_profile_boundary_layer_thickness(self, value=370.0):
        """Corresponds to IDD field `Wind Speed Profile Boundary Layer
        Thickness`"""
        self["Wind Speed Profile Boundary Layer Thickness"] = value

    @property
    def air_temperature_gradient_coefficient(self):
        """field `Air Temperature Gradient Coefficient`

        |  Set to zero for no air temperature dependence on height.
        |  Units: K/m
        |  Default value: 0.0065

        Args:
            value (float): value for IDD Field `Air Temperature Gradient Coefficient`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `air_temperature_gradient_coefficient` or None if not set

        """
        return self["Air Temperature Gradient Coefficient"]

    @air_temperature_gradient_coefficient.setter
    def air_temperature_gradient_coefficient(self, value=0.0065):
        """Corresponds to IDD field `Air Temperature Gradient Coefficient`"""
        self["Air Temperature Gradient Coefficient"] = value




class SiteGroundTemperatureBuildingSurface(DataObject):

    """ Corresponds to IDD object `Site:GroundTemperature:BuildingSurface`
        These temperatures are specifically for those surfaces that have the outside environment
        of "Ground".  Documentation about what values these should be is located in the
        Auxiliary programs document (Ground Heat Transfer) as well as the InputOutput Reference.
        CAUTION - Do not use the "undisturbed" ground temperatures from the weather data.
        These values are too extreme for the soil under a conditioned building.
        For best results, use the Slab or Basement program to calculate custom monthly
        average ground temperatures (see Auxiliary Programs).  For typical commercial
        buildings in the USA, a reasonable default value is 2C less than the average indoor space temperature.
    """
    _schema = {'extensible-fields': OrderedDict(),
               'fields': OrderedDict([(u'january ground temperature',
                                       {'name': u'January Ground Temperature',
                                        'pyname': u'january_ground_temperature',
                                        'default': 18.0,
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'C'}),
                                      (u'february ground temperature',
                                       {'name': u'February Ground Temperature',
                                        'pyname': u'february_ground_temperature',
                                        'default': 18.0,
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'C'}),
                                      (u'march ground temperature',
                                       {'name': u'March Ground Temperature',
                                        'pyname': u'march_ground_temperature',
                                        'default': 18.0,
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'C'}),
                                      (u'april ground temperature',
                                       {'name': u'April Ground Temperature',
                                        'pyname': u'april_ground_temperature',
                                        'default': 18.0,
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'C'}),
                                      (u'may ground temperature',
                                       {'name': u'May Ground Temperature',
                                        'pyname': u'may_ground_temperature',
                                        'default': 18.0,
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'C'}),
                                      (u'june ground temperature',
                                       {'name': u'June Ground Temperature',
                                        'pyname': u'june_ground_temperature',
                                        'default': 18.0,
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'C'}),
                                      (u'july ground temperature',
                                       {'name': u'July Ground Temperature',
                                        'pyname': u'july_ground_temperature',
                                        'default': 18.0,
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'C'}),
                                      (u'august ground temperature',
                                       {'name': u'August Ground Temperature',
                                        'pyname': u'august_ground_temperature',
                                        'default': 18.0,
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'C'}),
                                      (u'september ground temperature',
                                       {'name': u'September Ground Temperature',
                                        'pyname': u'september_ground_temperature',
                                        'default': 18.0,
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'C'}),
                                      (u'october ground temperature',
                                       {'name': u'October Ground Temperature',
                                        'pyname': u'october_ground_temperature',
                                        'default': 18.0,
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'C'}),
                                      (u'november ground temperature',
                                       {'name': u'November Ground Temperature',
                                        'pyname': u'november_ground_temperature',
                                        'default': 18.0,
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'C'}),
                                      (u'december ground temperature',
                                       {'name': u'December Ground Temperature',
                                        'pyname': u'december_ground_temperature',
                                        'default': 18.0,
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'C'})]),
               'format': u'singleline',
               'group': u'Location and Climate',
               'min-fields': 12,
               'name': u'Site:GroundTemperature:BuildingSurface',
               'pyname': u'SiteGroundTemperatureBuildingSurface',
               'required-object': False,
               'unique-object': True}

    @property
    def january_ground_temperature(self):
        """field `January Ground Temperature`

        |  Units: C
        |  Default value: 18.0

        Args:
            value (float): value for IDD Field `January Ground Temperature`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `january_ground_temperature` or None if not set

        """
        return self["January Ground Temperature"]

    @january_ground_temperature.setter
    def january_ground_temperature(self, value=18.0):
        """Corresponds to IDD field `January Ground Temperature`"""
        self["January Ground Temperature"] = value

    @property
    def february_ground_temperature(self):
        """field `February Ground Temperature`

        |  Units: C
        |  Default value: 18.0

        Args:
            value (float): value for IDD Field `February Ground Temperature`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `february_ground_temperature` or None if not set

        """
        return self["February Ground Temperature"]

    @february_ground_temperature.setter
    def february_ground_temperature(self, value=18.0):
        """Corresponds to IDD field `February Ground Temperature`"""
        self["February Ground Temperature"] = value

    @property
    def march_ground_temperature(self):
        """field `March Ground Temperature`

        |  Units: C
        |  Default value: 18.0

        Args:
            value (float): value for IDD Field `March Ground Temperature`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `march_ground_temperature` or None if not set

        """
        return self["March Ground Temperature"]

    @march_ground_temperature.setter
    def march_ground_temperature(self, value=18.0):
        """Corresponds to IDD field `March Ground Temperature`"""
        self["March Ground Temperature"] = value

    @property
    def april_ground_temperature(self):
        """field `April Ground Temperature`

        |  Units: C
        |  Default value: 18.0

        Args:
            value (float): value for IDD Field `April Ground Temperature`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `april_ground_temperature` or None if not set

        """
        return self["April Ground Temperature"]

    @april_ground_temperature.setter
    def april_ground_temperature(self, value=18.0):
        """Corresponds to IDD field `April Ground Temperature`"""
        self["April Ground Temperature"] = value

    @property
    def may_ground_temperature(self):
        """field `May Ground Temperature`

        |  Units: C
        |  Default value: 18.0

        Args:
            value (float): value for IDD Field `May Ground Temperature`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `may_ground_temperature` or None if not set

        """
        return self["May Ground Temperature"]

    @may_ground_temperature.setter
    def may_ground_temperature(self, value=18.0):
        """Corresponds to IDD field `May Ground Temperature`"""
        self["May Ground Temperature"] = value

    @property
    def june_ground_temperature(self):
        """field `June Ground Temperature`

        |  Units: C
        |  Default value: 18.0

        Args:
            value (float): value for IDD Field `June Ground Temperature`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `june_ground_temperature` or None if not set

        """
        return self["June Ground Temperature"]

    @june_ground_temperature.setter
    def june_ground_temperature(self, value=18.0):
        """Corresponds to IDD field `June Ground Temperature`"""
        self["June Ground Temperature"] = value

    @property
    def july_ground_temperature(self):
        """field `July Ground Temperature`

        |  Units: C
        |  Default value: 18.0

        Args:
            value (float): value for IDD Field `July Ground Temperature`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `july_ground_temperature` or None if not set

        """
        return self["July Ground Temperature"]

    @july_ground_temperature.setter
    def july_ground_temperature(self, value=18.0):
        """Corresponds to IDD field `July Ground Temperature`"""
        self["July Ground Temperature"] = value

    @property
    def august_ground_temperature(self):
        """field `August Ground Temperature`

        |  Units: C
        |  Default value: 18.0

        Args:
            value (float): value for IDD Field `August Ground Temperature`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `august_ground_temperature` or None if not set

        """
        return self["August Ground Temperature"]

    @august_ground_temperature.setter
    def august_ground_temperature(self, value=18.0):
        """Corresponds to IDD field `August Ground Temperature`"""
        self["August Ground Temperature"] = value

    @property
    def september_ground_temperature(self):
        """field `September Ground Temperature`

        |  Units: C
        |  Default value: 18.0

        Args:
            value (float): value for IDD Field `September Ground Temperature`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `september_ground_temperature` or None if not set

        """
        return self["September Ground Temperature"]

    @september_ground_temperature.setter
    def september_ground_temperature(self, value=18.0):
        """Corresponds to IDD field `September Ground Temperature`"""
        self["September Ground Temperature"] = value

    @property
    def october_ground_temperature(self):
        """field `October Ground Temperature`

        |  Units: C
        |  Default value: 18.0

        Args:
            value (float): value for IDD Field `October Ground Temperature`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `october_ground_temperature` or None if not set

        """
        return self["October Ground Temperature"]

    @october_ground_temperature.setter
    def october_ground_temperature(self, value=18.0):
        """Corresponds to IDD field `October Ground Temperature`"""
        self["October Ground Temperature"] = value

    @property
    def november_ground_temperature(self):
        """field `November Ground Temperature`

        |  Units: C
        |  Default value: 18.0

        Args:
            value (float): value for IDD Field `November Ground Temperature`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `november_ground_temperature` or None if not set

        """
        return self["November Ground Temperature"]

    @november_ground_temperature.setter
    def november_ground_temperature(self, value=18.0):
        """Corresponds to IDD field `November Ground Temperature`"""
        self["November Ground Temperature"] = value

    @property
    def december_ground_temperature(self):
        """field `December Ground Temperature`

        |  Units: C
        |  Default value: 18.0

        Args:
            value (float): value for IDD Field `December Ground Temperature`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `december_ground_temperature` or None if not set

        """
        return self["December Ground Temperature"]

    @december_ground_temperature.setter
    def december_ground_temperature(self, value=18.0):
        """Corresponds to IDD field `December Ground Temperature`"""
        self["December Ground Temperature"] = value




class SiteGroundTemperatureFcfactorMethod(DataObject):

    """ Corresponds to IDD object `Site:GroundTemperature:FCfactorMethod`
        These temperatures are specifically for underground walls and ground floors
        defined with the C-factor and F-factor methods, and should be close to the
        monthly average outdoor air temperature delayed by 3 months for the location.
    """
    _schema = {'extensible-fields': OrderedDict(),
               'fields': OrderedDict([(u'january ground temperature',
                                       {'name': u'January Ground Temperature',
                                        'pyname': u'january_ground_temperature',
                                        'default': 13.0,
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'C'}),
                                      (u'february ground temperature',
                                       {'name': u'February Ground Temperature',
                                        'pyname': u'february_ground_temperature',
                                        'default': 13.0,
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'C'}),
                                      (u'march ground temperature',
                                       {'name': u'March Ground Temperature',
                                        'pyname': u'march_ground_temperature',
                                        'default': 13.0,
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'C'}),
                                      (u'april ground temperature',
                                       {'name': u'April Ground Temperature',
                                        'pyname': u'april_ground_temperature',
                                        'default': 13.0,
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'C'}),
                                      (u'may ground temperature',
                                       {'name': u'May Ground Temperature',
                                        'pyname': u'may_ground_temperature',
                                        'default': 13.0,
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'C'}),
                                      (u'june ground temperature',
                                       {'name': u'June Ground Temperature',
                                        'pyname': u'june_ground_temperature',
                                        'default': 13.0,
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'C'}),
                                      (u'july ground temperature',
                                       {'name': u'July Ground Temperature',
                                        'pyname': u'july_ground_temperature',
                                        'default': 13.0,
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'C'}),
                                      (u'august ground temperature',
                                       {'name': u'August Ground Temperature',
                                        'pyname': u'august_ground_temperature',
                                        'default': 13.0,
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'C'}),
                                      (u'september ground temperature',
                                       {'name': u'September Ground Temperature',
                                        'pyname': u'september_ground_temperature',
                                        'default': 13.0,
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'C'}),
                                      (u'october ground temperature',
                                       {'name': u'October Ground Temperature',
                                        'pyname': u'october_ground_temperature',
                                        'default': 13.0,
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'C'}),
                                      (u'november ground temperature',
                                       {'name': u'November Ground Temperature',
                                        'pyname': u'november_ground_temperature',
                                        'default': 13.0,
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'C'}),
                                      (u'december ground temperature',
                                       {'name': u'December Ground Temperature',
                                        'pyname': u'december_ground_temperature',
                                        'default': 13.0,
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'C'})]),
               'format': u'singleline',
               'group': u'Location and Climate',
               'min-fields': 12,
               'name': u'Site:GroundTemperature:FCfactorMethod',
               'pyname': u'SiteGroundTemperatureFcfactorMethod',
               'required-object': False,
               'unique-object': True}

    @property
    def january_ground_temperature(self):
        """field `January Ground Temperature`

        |  Units: C
        |  Default value: 13.0

        Args:
            value (float): value for IDD Field `January Ground Temperature`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `january_ground_temperature` or None if not set

        """
        return self["January Ground Temperature"]

    @january_ground_temperature.setter
    def january_ground_temperature(self, value=13.0):
        """Corresponds to IDD field `January Ground Temperature`"""
        self["January Ground Temperature"] = value

    @property
    def february_ground_temperature(self):
        """field `February Ground Temperature`

        |  Units: C
        |  Default value: 13.0

        Args:
            value (float): value for IDD Field `February Ground Temperature`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `february_ground_temperature` or None if not set

        """
        return self["February Ground Temperature"]

    @february_ground_temperature.setter
    def february_ground_temperature(self, value=13.0):
        """Corresponds to IDD field `February Ground Temperature`"""
        self["February Ground Temperature"] = value

    @property
    def march_ground_temperature(self):
        """field `March Ground Temperature`

        |  Units: C
        |  Default value: 13.0

        Args:
            value (float): value for IDD Field `March Ground Temperature`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `march_ground_temperature` or None if not set

        """
        return self["March Ground Temperature"]

    @march_ground_temperature.setter
    def march_ground_temperature(self, value=13.0):
        """Corresponds to IDD field `March Ground Temperature`"""
        self["March Ground Temperature"] = value

    @property
    def april_ground_temperature(self):
        """field `April Ground Temperature`

        |  Units: C
        |  Default value: 13.0

        Args:
            value (float): value for IDD Field `April Ground Temperature`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `april_ground_temperature` or None if not set

        """
        return self["April Ground Temperature"]

    @april_ground_temperature.setter
    def april_ground_temperature(self, value=13.0):
        """Corresponds to IDD field `April Ground Temperature`"""
        self["April Ground Temperature"] = value

    @property
    def may_ground_temperature(self):
        """field `May Ground Temperature`

        |  Units: C
        |  Default value: 13.0

        Args:
            value (float): value for IDD Field `May Ground Temperature`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `may_ground_temperature` or None if not set

        """
        return self["May Ground Temperature"]

    @may_ground_temperature.setter
    def may_ground_temperature(self, value=13.0):
        """Corresponds to IDD field `May Ground Temperature`"""
        self["May Ground Temperature"] = value

    @property
    def june_ground_temperature(self):
        """field `June Ground Temperature`

        |  Units: C
        |  Default value: 13.0

        Args:
            value (float): value for IDD Field `June Ground Temperature`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `june_ground_temperature` or None if not set

        """
        return self["June Ground Temperature"]

    @june_ground_temperature.setter
    def june_ground_temperature(self, value=13.0):
        """Corresponds to IDD field `June Ground Temperature`"""
        self["June Ground Temperature"] = value

    @property
    def july_ground_temperature(self):
        """field `July Ground Temperature`

        |  Units: C
        |  Default value: 13.0

        Args:
            value (float): value for IDD Field `July Ground Temperature`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `july_ground_temperature` or None if not set

        """
        return self["July Ground Temperature"]

    @july_ground_temperature.setter
    def july_ground_temperature(self, value=13.0):
        """Corresponds to IDD field `July Ground Temperature`"""
        self["July Ground Temperature"] = value

    @property
    def august_ground_temperature(self):
        """field `August Ground Temperature`

        |  Units: C
        |  Default value: 13.0

        Args:
            value (float): value for IDD Field `August Ground Temperature`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `august_ground_temperature` or None if not set

        """
        return self["August Ground Temperature"]

    @august_ground_temperature.setter
    def august_ground_temperature(self, value=13.0):
        """Corresponds to IDD field `August Ground Temperature`"""
        self["August Ground Temperature"] = value

    @property
    def september_ground_temperature(self):
        """field `September Ground Temperature`

        |  Units: C
        |  Default value: 13.0

        Args:
            value (float): value for IDD Field `September Ground Temperature`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `september_ground_temperature` or None if not set

        """
        return self["September Ground Temperature"]

    @september_ground_temperature.setter
    def september_ground_temperature(self, value=13.0):
        """Corresponds to IDD field `September Ground Temperature`"""
        self["September Ground Temperature"] = value

    @property
    def october_ground_temperature(self):
        """field `October Ground Temperature`

        |  Units: C
        |  Default value: 13.0

        Args:
            value (float): value for IDD Field `October Ground Temperature`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `october_ground_temperature` or None if not set

        """
        return self["October Ground Temperature"]

    @october_ground_temperature.setter
    def october_ground_temperature(self, value=13.0):
        """Corresponds to IDD field `October Ground Temperature`"""
        self["October Ground Temperature"] = value

    @property
    def november_ground_temperature(self):
        """field `November Ground Temperature`

        |  Units: C
        |  Default value: 13.0

        Args:
            value (float): value for IDD Field `November Ground Temperature`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `november_ground_temperature` or None if not set

        """
        return self["November Ground Temperature"]

    @november_ground_temperature.setter
    def november_ground_temperature(self, value=13.0):
        """Corresponds to IDD field `November Ground Temperature`"""
        self["November Ground Temperature"] = value

    @property
    def december_ground_temperature(self):
        """field `December Ground Temperature`

        |  Units: C
        |  Default value: 13.0

        Args:
            value (float): value for IDD Field `December Ground Temperature`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `december_ground_temperature` or None if not set

        """
        return self["December Ground Temperature"]

    @december_ground_temperature.setter
    def december_ground_temperature(self, value=13.0):
        """Corresponds to IDD field `December Ground Temperature`"""
        self["December Ground Temperature"] = value




class SiteGroundTemperatureShallow(DataObject):

    """ Corresponds to IDD object `Site:GroundTemperature:Shallow`
        These temperatures are specifically for the Surface Ground Heat Exchanger and
        should probably be close to the average outdoor air temperature for the location.
        They are not used in other models.
    """
    _schema = {'extensible-fields': OrderedDict(),
               'fields': OrderedDict([(u'january surface ground temperature',
                                       {'name': u'January Surface Ground Temperature',
                                        'pyname': u'january_surface_ground_temperature',
                                        'default': 13.0,
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'C'}),
                                      (u'february surface ground temperature',
                                       {'name': u'February Surface Ground Temperature',
                                        'pyname': u'february_surface_ground_temperature',
                                        'default': 13.0,
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'C'}),
                                      (u'march surface ground temperature',
                                       {'name': u'March Surface Ground Temperature',
                                        'pyname': u'march_surface_ground_temperature',
                                        'default': 13.0,
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'C'}),
                                      (u'april surface ground temperature',
                                       {'name': u'April Surface Ground Temperature',
                                        'pyname': u'april_surface_ground_temperature',
                                        'default': 13.0,
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'C'}),
                                      (u'may surface ground temperature',
                                       {'name': u'May Surface Ground Temperature',
                                        'pyname': u'may_surface_ground_temperature',
                                        'default': 13.0,
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'C'}),
                                      (u'june surface ground temperature',
                                       {'name': u'June Surface Ground Temperature',
                                        'pyname': u'june_surface_ground_temperature',
                                        'default': 13.0,
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'C'}),
                                      (u'july surface ground temperature',
                                       {'name': u'July Surface Ground Temperature',
                                        'pyname': u'july_surface_ground_temperature',
                                        'default': 13.0,
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'C'}),
                                      (u'august surface ground temperature',
                                       {'name': u'August Surface Ground Temperature',
                                        'pyname': u'august_surface_ground_temperature',
                                        'default': 13.0,
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'C'}),
                                      (u'september surface ground temperature',
                                       {'name': u'September Surface Ground Temperature',
                                        'pyname': u'september_surface_ground_temperature',
                                        'default': 13.0,
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'C'}),
                                      (u'october surface ground temperature',
                                       {'name': u'October Surface Ground Temperature',
                                        'pyname': u'october_surface_ground_temperature',
                                        'default': 13.0,
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'C'}),
                                      (u'november surface ground temperature',
                                       {'name': u'November Surface Ground Temperature',
                                        'pyname': u'november_surface_ground_temperature',
                                        'default': 13.0,
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'C'}),
                                      (u'december surface ground temperature',
                                       {'name': u'December Surface Ground Temperature',
                                        'pyname': u'december_surface_ground_temperature',
                                        'default': 13.0,
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'C'})]),
               'format': u'singleline',
               'group': u'Location and Climate',
               'min-fields': 12,
               'name': u'Site:GroundTemperature:Shallow',
               'pyname': u'SiteGroundTemperatureShallow',
               'required-object': False,
               'unique-object': True}

    @property
    def january_surface_ground_temperature(self):
        """field `January Surface Ground Temperature`

        |  Units: C
        |  Default value: 13.0

        Args:
            value (float): value for IDD Field `January Surface Ground Temperature`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `january_surface_ground_temperature` or None if not set

        """
        return self["January Surface Ground Temperature"]

    @january_surface_ground_temperature.setter
    def january_surface_ground_temperature(self, value=13.0):
        """Corresponds to IDD field `January Surface Ground Temperature`"""
        self["January Surface Ground Temperature"] = value

    @property
    def february_surface_ground_temperature(self):
        """field `February Surface Ground Temperature`

        |  Units: C
        |  Default value: 13.0

        Args:
            value (float): value for IDD Field `February Surface Ground Temperature`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `february_surface_ground_temperature` or None if not set

        """
        return self["February Surface Ground Temperature"]

    @february_surface_ground_temperature.setter
    def february_surface_ground_temperature(self, value=13.0):
        """Corresponds to IDD field `February Surface Ground Temperature`"""
        self["February Surface Ground Temperature"] = value

    @property
    def march_surface_ground_temperature(self):
        """field `March Surface Ground Temperature`

        |  Units: C
        |  Default value: 13.0

        Args:
            value (float): value for IDD Field `March Surface Ground Temperature`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `march_surface_ground_temperature` or None if not set

        """
        return self["March Surface Ground Temperature"]

    @march_surface_ground_temperature.setter
    def march_surface_ground_temperature(self, value=13.0):
        """Corresponds to IDD field `March Surface Ground Temperature`"""
        self["March Surface Ground Temperature"] = value

    @property
    def april_surface_ground_temperature(self):
        """field `April Surface Ground Temperature`

        |  Units: C
        |  Default value: 13.0

        Args:
            value (float): value for IDD Field `April Surface Ground Temperature`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `april_surface_ground_temperature` or None if not set

        """
        return self["April Surface Ground Temperature"]

    @april_surface_ground_temperature.setter
    def april_surface_ground_temperature(self, value=13.0):
        """Corresponds to IDD field `April Surface Ground Temperature`"""
        self["April Surface Ground Temperature"] = value

    @property
    def may_surface_ground_temperature(self):
        """field `May Surface Ground Temperature`

        |  Units: C
        |  Default value: 13.0

        Args:
            value (float): value for IDD Field `May Surface Ground Temperature`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `may_surface_ground_temperature` or None if not set

        """
        return self["May Surface Ground Temperature"]

    @may_surface_ground_temperature.setter
    def may_surface_ground_temperature(self, value=13.0):
        """Corresponds to IDD field `May Surface Ground Temperature`"""
        self["May Surface Ground Temperature"] = value

    @property
    def june_surface_ground_temperature(self):
        """field `June Surface Ground Temperature`

        |  Units: C
        |  Default value: 13.0

        Args:
            value (float): value for IDD Field `June Surface Ground Temperature`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `june_surface_ground_temperature` or None if not set

        """
        return self["June Surface Ground Temperature"]

    @june_surface_ground_temperature.setter
    def june_surface_ground_temperature(self, value=13.0):
        """Corresponds to IDD field `June Surface Ground Temperature`"""
        self["June Surface Ground Temperature"] = value

    @property
    def july_surface_ground_temperature(self):
        """field `July Surface Ground Temperature`

        |  Units: C
        |  Default value: 13.0

        Args:
            value (float): value for IDD Field `July Surface Ground Temperature`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `july_surface_ground_temperature` or None if not set

        """
        return self["July Surface Ground Temperature"]

    @july_surface_ground_temperature.setter
    def july_surface_ground_temperature(self, value=13.0):
        """Corresponds to IDD field `July Surface Ground Temperature`"""
        self["July Surface Ground Temperature"] = value

    @property
    def august_surface_ground_temperature(self):
        """field `August Surface Ground Temperature`

        |  Units: C
        |  Default value: 13.0

        Args:
            value (float): value for IDD Field `August Surface Ground Temperature`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `august_surface_ground_temperature` or None if not set

        """
        return self["August Surface Ground Temperature"]

    @august_surface_ground_temperature.setter
    def august_surface_ground_temperature(self, value=13.0):
        """Corresponds to IDD field `August Surface Ground Temperature`"""
        self["August Surface Ground Temperature"] = value

    @property
    def september_surface_ground_temperature(self):
        """field `September Surface Ground Temperature`

        |  Units: C
        |  Default value: 13.0

        Args:
            value (float): value for IDD Field `September Surface Ground Temperature`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `september_surface_ground_temperature` or None if not set

        """
        return self["September Surface Ground Temperature"]

    @september_surface_ground_temperature.setter
    def september_surface_ground_temperature(self, value=13.0):
        """Corresponds to IDD field `September Surface Ground Temperature`"""
        self["September Surface Ground Temperature"] = value

    @property
    def october_surface_ground_temperature(self):
        """field `October Surface Ground Temperature`

        |  Units: C
        |  Default value: 13.0

        Args:
            value (float): value for IDD Field `October Surface Ground Temperature`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `october_surface_ground_temperature` or None if not set

        """
        return self["October Surface Ground Temperature"]

    @october_surface_ground_temperature.setter
    def october_surface_ground_temperature(self, value=13.0):
        """Corresponds to IDD field `October Surface Ground Temperature`"""
        self["October Surface Ground Temperature"] = value

    @property
    def november_surface_ground_temperature(self):
        """field `November Surface Ground Temperature`

        |  Units: C
        |  Default value: 13.0

        Args:
            value (float): value for IDD Field `November Surface Ground Temperature`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `november_surface_ground_temperature` or None if not set

        """
        return self["November Surface Ground Temperature"]

    @november_surface_ground_temperature.setter
    def november_surface_ground_temperature(self, value=13.0):
        """Corresponds to IDD field `November Surface Ground Temperature`"""
        self["November Surface Ground Temperature"] = value

    @property
    def december_surface_ground_temperature(self):
        """field `December Surface Ground Temperature`

        |  Units: C
        |  Default value: 13.0

        Args:
            value (float): value for IDD Field `December Surface Ground Temperature`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `december_surface_ground_temperature` or None if not set

        """
        return self["December Surface Ground Temperature"]

    @december_surface_ground_temperature.setter
    def december_surface_ground_temperature(self, value=13.0):
        """Corresponds to IDD field `December Surface Ground Temperature`"""
        self["December Surface Ground Temperature"] = value




class SiteGroundTemperatureDeep(DataObject):

    """ Corresponds to IDD object `Site:GroundTemperature:Deep`
        These temperatures are specifically for the ground heat exchangers that would use
        "deep" (3-4 m depth) ground temperatures for their heat source.
        They are not used in other models.
    """
    _schema = {'extensible-fields': OrderedDict(),
               'fields': OrderedDict([(u'january deep ground temperature',
                                       {'name': u'January Deep Ground Temperature',
                                        'pyname': u'january_deep_ground_temperature',
                                        'default': 16.0,
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'C'}),
                                      (u'february deep ground temperature',
                                       {'name': u'February Deep Ground Temperature',
                                        'pyname': u'february_deep_ground_temperature',
                                        'default': 16.0,
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'C'}),
                                      (u'march deep ground temperature',
                                       {'name': u'March Deep Ground Temperature',
                                        'pyname': u'march_deep_ground_temperature',
                                        'default': 16.0,
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'C'}),
                                      (u'april deep ground temperature',
                                       {'name': u'April Deep Ground Temperature',
                                        'pyname': u'april_deep_ground_temperature',
                                        'default': 16.0,
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'C'}),
                                      (u'may deep ground temperature',
                                       {'name': u'May Deep Ground Temperature',
                                        'pyname': u'may_deep_ground_temperature',
                                        'default': 16.0,
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'C'}),
                                      (u'june deep ground temperature',
                                       {'name': u'June Deep Ground Temperature',
                                        'pyname': u'june_deep_ground_temperature',
                                        'default': 16.0,
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'C'}),
                                      (u'july deep ground temperature',
                                       {'name': u'July Deep Ground Temperature',
                                        'pyname': u'july_deep_ground_temperature',
                                        'default': 16.0,
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'C'}),
                                      (u'august deep ground temperature',
                                       {'name': u'August Deep Ground Temperature',
                                        'pyname': u'august_deep_ground_temperature',
                                        'default': 16.0,
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'C'}),
                                      (u'september deep ground temperature',
                                       {'name': u'September Deep Ground Temperature',
                                        'pyname': u'september_deep_ground_temperature',
                                        'default': 16.0,
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'C'}),
                                      (u'october deep ground temperature',
                                       {'name': u'October Deep Ground Temperature',
                                        'pyname': u'october_deep_ground_temperature',
                                        'default': 16.0,
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'C'}),
                                      (u'november deep ground temperature',
                                       {'name': u'November Deep Ground Temperature',
                                        'pyname': u'november_deep_ground_temperature',
                                        'default': 16.0,
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'C'}),
                                      (u'december deep ground temperature',
                                       {'name': u'December Deep Ground Temperature',
                                        'pyname': u'december_deep_ground_temperature',
                                        'default': 16.0,
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'C'})]),
               'format': u'singleline',
               'group': u'Location and Climate',
               'min-fields': 12,
               'name': u'Site:GroundTemperature:Deep',
               'pyname': u'SiteGroundTemperatureDeep',
               'required-object': False,
               'unique-object': True}

    @property
    def january_deep_ground_temperature(self):
        """field `January Deep Ground Temperature`

        |  Units: C
        |  Default value: 16.0

        Args:
            value (float): value for IDD Field `January Deep Ground Temperature`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `january_deep_ground_temperature` or None if not set

        """
        return self["January Deep Ground Temperature"]

    @january_deep_ground_temperature.setter
    def january_deep_ground_temperature(self, value=16.0):
        """Corresponds to IDD field `January Deep Ground Temperature`"""
        self["January Deep Ground Temperature"] = value

    @property
    def february_deep_ground_temperature(self):
        """field `February Deep Ground Temperature`

        |  Units: C
        |  Default value: 16.0

        Args:
            value (float): value for IDD Field `February Deep Ground Temperature`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `february_deep_ground_temperature` or None if not set

        """
        return self["February Deep Ground Temperature"]

    @february_deep_ground_temperature.setter
    def february_deep_ground_temperature(self, value=16.0):
        """Corresponds to IDD field `February Deep Ground Temperature`"""
        self["February Deep Ground Temperature"] = value

    @property
    def march_deep_ground_temperature(self):
        """field `March Deep Ground Temperature`

        |  Units: C
        |  Default value: 16.0

        Args:
            value (float): value for IDD Field `March Deep Ground Temperature`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `march_deep_ground_temperature` or None if not set

        """
        return self["March Deep Ground Temperature"]

    @march_deep_ground_temperature.setter
    def march_deep_ground_temperature(self, value=16.0):
        """Corresponds to IDD field `March Deep Ground Temperature`"""
        self["March Deep Ground Temperature"] = value

    @property
    def april_deep_ground_temperature(self):
        """field `April Deep Ground Temperature`

        |  Units: C
        |  Default value: 16.0

        Args:
            value (float): value for IDD Field `April Deep Ground Temperature`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `april_deep_ground_temperature` or None if not set

        """
        return self["April Deep Ground Temperature"]

    @april_deep_ground_temperature.setter
    def april_deep_ground_temperature(self, value=16.0):
        """Corresponds to IDD field `April Deep Ground Temperature`"""
        self["April Deep Ground Temperature"] = value

    @property
    def may_deep_ground_temperature(self):
        """field `May Deep Ground Temperature`

        |  Units: C
        |  Default value: 16.0

        Args:
            value (float): value for IDD Field `May Deep Ground Temperature`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `may_deep_ground_temperature` or None if not set

        """
        return self["May Deep Ground Temperature"]

    @may_deep_ground_temperature.setter
    def may_deep_ground_temperature(self, value=16.0):
        """Corresponds to IDD field `May Deep Ground Temperature`"""
        self["May Deep Ground Temperature"] = value

    @property
    def june_deep_ground_temperature(self):
        """field `June Deep Ground Temperature`

        |  Units: C
        |  Default value: 16.0

        Args:
            value (float): value for IDD Field `June Deep Ground Temperature`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `june_deep_ground_temperature` or None if not set

        """
        return self["June Deep Ground Temperature"]

    @june_deep_ground_temperature.setter
    def june_deep_ground_temperature(self, value=16.0):
        """Corresponds to IDD field `June Deep Ground Temperature`"""
        self["June Deep Ground Temperature"] = value

    @property
    def july_deep_ground_temperature(self):
        """field `July Deep Ground Temperature`

        |  Units: C
        |  Default value: 16.0

        Args:
            value (float): value for IDD Field `July Deep Ground Temperature`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `july_deep_ground_temperature` or None if not set

        """
        return self["July Deep Ground Temperature"]

    @july_deep_ground_temperature.setter
    def july_deep_ground_temperature(self, value=16.0):
        """Corresponds to IDD field `July Deep Ground Temperature`"""
        self["July Deep Ground Temperature"] = value

    @property
    def august_deep_ground_temperature(self):
        """field `August Deep Ground Temperature`

        |  Units: C
        |  Default value: 16.0

        Args:
            value (float): value for IDD Field `August Deep Ground Temperature`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `august_deep_ground_temperature` or None if not set

        """
        return self["August Deep Ground Temperature"]

    @august_deep_ground_temperature.setter
    def august_deep_ground_temperature(self, value=16.0):
        """Corresponds to IDD field `August Deep Ground Temperature`"""
        self["August Deep Ground Temperature"] = value

    @property
    def september_deep_ground_temperature(self):
        """field `September Deep Ground Temperature`

        |  Units: C
        |  Default value: 16.0

        Args:
            value (float): value for IDD Field `September Deep Ground Temperature`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `september_deep_ground_temperature` or None if not set

        """
        return self["September Deep Ground Temperature"]

    @september_deep_ground_temperature.setter
    def september_deep_ground_temperature(self, value=16.0):
        """Corresponds to IDD field `September Deep Ground Temperature`"""
        self["September Deep Ground Temperature"] = value

    @property
    def october_deep_ground_temperature(self):
        """field `October Deep Ground Temperature`

        |  Units: C
        |  Default value: 16.0

        Args:
            value (float): value for IDD Field `October Deep Ground Temperature`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `october_deep_ground_temperature` or None if not set

        """
        return self["October Deep Ground Temperature"]

    @october_deep_ground_temperature.setter
    def october_deep_ground_temperature(self, value=16.0):
        """Corresponds to IDD field `October Deep Ground Temperature`"""
        self["October Deep Ground Temperature"] = value

    @property
    def november_deep_ground_temperature(self):
        """field `November Deep Ground Temperature`

        |  Units: C
        |  Default value: 16.0

        Args:
            value (float): value for IDD Field `November Deep Ground Temperature`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `november_deep_ground_temperature` or None if not set

        """
        return self["November Deep Ground Temperature"]

    @november_deep_ground_temperature.setter
    def november_deep_ground_temperature(self, value=16.0):
        """Corresponds to IDD field `November Deep Ground Temperature`"""
        self["November Deep Ground Temperature"] = value

    @property
    def december_deep_ground_temperature(self):
        """field `December Deep Ground Temperature`

        |  Units: C
        |  Default value: 16.0

        Args:
            value (float): value for IDD Field `December Deep Ground Temperature`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `december_deep_ground_temperature` or None if not set

        """
        return self["December Deep Ground Temperature"]

    @december_deep_ground_temperature.setter
    def december_deep_ground_temperature(self, value=16.0):
        """Corresponds to IDD field `December Deep Ground Temperature`"""
        self["December Deep Ground Temperature"] = value




class SiteGroundTemperatureUndisturbedFiniteDifference(DataObject):

    """ Corresponds to IDD object `Site:GroundTemperature:Undisturbed:FiniteDifference`
        Undisturbed ground temperature object using a
        detailed finite difference 1-D model
    """
    _schema = {'extensible-fields': OrderedDict(),
               'fields': OrderedDict([(u'name',
                                       {'name': u'Name',
                                        'pyname': u'name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'soil thermal conductivity',
                                       {'name': u'Soil Thermal Conductivity',
                                        'pyname': u'soil_thermal_conductivity',
                                        'minimum>': 0.0,
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'W/m-K'}),
                                      (u'soil density',
                                       {'name': u'Soil Density',
                                        'pyname': u'soil_density',
                                        'minimum>': 0.0,
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'kg/m3'}),
                                      (u'soil specific heat',
                                       {'name': u'Soil Specific Heat',
                                        'pyname': u'soil_specific_heat',
                                        'minimum>': 0.0,
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'J/kg-K'}),
                                      (u'soil moisture content volume fraction',
                                       {'name': u'Soil Moisture Content Volume Fraction',
                                        'pyname': u'soil_moisture_content_volume_fraction',
                                        'default': 30.0,
                                        'maximum': 100.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'percent'}),
                                      (u'soil moisture content volume fraction at saturation',
                                       {'name': u'Soil Moisture Content Volume Fraction at Saturation',
                                        'pyname': u'soil_moisture_content_volume_fraction_at_saturation',
                                        'default': 50.0,
                                        'maximum': 100.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'percent'}),
                                      (u'evapotranspiration ground cover parameter',
                                       {'name': u'Evapotranspiration Ground Cover Parameter',
                                        'pyname': u'evapotranspiration_ground_cover_parameter',
                                        'default': 0.4,
                                        'maximum': 1.5,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'dimensionless'})]),
               'format': None,
               'group': u'Location and Climate',
               'min-fields': 7,
               'name': u'Site:GroundTemperature:Undisturbed:FiniteDifference',
               'pyname': u'SiteGroundTemperatureUndisturbedFiniteDifference',
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
    def soil_thermal_conductivity(self):
        """field `Soil Thermal Conductivity`

        |  Units: W/m-K

        Args:
            value (float): value for IDD Field `Soil Thermal Conductivity`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `soil_thermal_conductivity` or None if not set

        """
        return self["Soil Thermal Conductivity"]

    @soil_thermal_conductivity.setter
    def soil_thermal_conductivity(self, value=None):
        """Corresponds to IDD field `Soil Thermal Conductivity`"""
        self["Soil Thermal Conductivity"] = value

    @property
    def soil_density(self):
        """field `Soil Density`

        |  Units: kg/m3

        Args:
            value (float): value for IDD Field `Soil Density`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `soil_density` or None if not set

        """
        return self["Soil Density"]

    @soil_density.setter
    def soil_density(self, value=None):
        """Corresponds to IDD field `Soil Density`"""
        self["Soil Density"] = value

    @property
    def soil_specific_heat(self):
        """field `Soil Specific Heat`

        |  Units: J/kg-K

        Args:
            value (float): value for IDD Field `Soil Specific Heat`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `soil_specific_heat` or None if not set

        """
        return self["Soil Specific Heat"]

    @soil_specific_heat.setter
    def soil_specific_heat(self, value=None):
        """Corresponds to IDD field `Soil Specific Heat`"""
        self["Soil Specific Heat"] = value

    @property
    def soil_moisture_content_volume_fraction(self):
        """field `Soil Moisture Content Volume Fraction`

        |  Units: percent
        |  Default value: 30.0
        |  value <= 100.0

        Args:
            value (float): value for IDD Field `Soil Moisture Content Volume Fraction`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `soil_moisture_content_volume_fraction` or None if not set

        """
        return self["Soil Moisture Content Volume Fraction"]

    @soil_moisture_content_volume_fraction.setter
    def soil_moisture_content_volume_fraction(self, value=30.0):
        """Corresponds to IDD field `Soil Moisture Content Volume Fraction`"""
        self["Soil Moisture Content Volume Fraction"] = value

    @property
    def soil_moisture_content_volume_fraction_at_saturation(self):
        """field `Soil Moisture Content Volume Fraction at Saturation`

        |  Units: percent
        |  Default value: 50.0
        |  value <= 100.0

        Args:
            value (float): value for IDD Field `Soil Moisture Content Volume Fraction at Saturation`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `soil_moisture_content_volume_fraction_at_saturation` or None if not set

        """
        return self["Soil Moisture Content Volume Fraction at Saturation"]

    @soil_moisture_content_volume_fraction_at_saturation.setter
    def soil_moisture_content_volume_fraction_at_saturation(self, value=50.0):
        """Corresponds to IDD field `Soil Moisture Content Volume Fraction at
        Saturation`"""
        self["Soil Moisture Content Volume Fraction at Saturation"] = value

    @property
    def evapotranspiration_ground_cover_parameter(self):
        """field `Evapotranspiration Ground Cover Parameter`

        |  This specifies the ground cover effects during evapotranspiration
        |  calculations.  The value roughly represents the following cases:
        |  = 0   : concrete or other solid, non-permeable ground surface material
        |  = 0.5 : short grass, much like a manicured lawn
        |  = 1   : standard reference state (12 cm grass)
        |  = 1.5 : wild growth
        |  Units: dimensionless
        |  Default value: 0.4
        |  value <= 1.5

        Args:
            value (float): value for IDD Field `Evapotranspiration Ground Cover Parameter`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `evapotranspiration_ground_cover_parameter` or None if not set

        """
        return self["Evapotranspiration Ground Cover Parameter"]

    @evapotranspiration_ground_cover_parameter.setter
    def evapotranspiration_ground_cover_parameter(self, value=0.4):
        """Corresponds to IDD field `Evapotranspiration Ground Cover
        Parameter`"""
        self["Evapotranspiration Ground Cover Parameter"] = value




class SiteGroundTemperatureUndisturbedKusudaAchenbach(DataObject):

    """ Corresponds to IDD object `Site:GroundTemperature:Undisturbed:KusudaAchenbach`
        Undisturbed ground temperature object using the
        Kusuda-Achenbach 1965 correlation.
    """
    _schema = {'extensible-fields': OrderedDict(),
               'fields': OrderedDict([(u'name',
                                       {'name': u'Name',
                                        'pyname': u'name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'soil thermal conductivity',
                                       {'name': u'Soil Thermal Conductivity',
                                        'pyname': u'soil_thermal_conductivity',
                                        'minimum>': 0.0,
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'W/m-K'}),
                                      (u'soil density',
                                       {'name': u'Soil Density',
                                        'pyname': u'soil_density',
                                        'minimum>': 0.0,
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'kg/m3'}),
                                      (u'soil specific heat',
                                       {'name': u'Soil Specific Heat',
                                        'pyname': u'soil_specific_heat',
                                        'minimum>': 0.0,
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'J/kg-K'}),
                                      (u'average soil surface temperature',
                                       {'name': u'Average Soil Surface Temperature',
                                        'pyname': u'average_soil_surface_temperature',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'C'}),
                                      (u'average amplitude of surface temperature',
                                       {'name': u'Average Amplitude of Surface Temperature',
                                        'pyname': u'average_amplitude_of_surface_temperature',
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'deltaC'}),
                                      (u'phase shift of minimum surface temperature',
                                       {'name': u'Phase Shift of Minimum Surface Temperature',
                                        'pyname': u'phase_shift_of_minimum_surface_temperature',
                                        'maximum<': 365.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'days'})]),
               'format': None,
               'group': u'Location and Climate',
               'min-fields': 7,
               'name': u'Site:GroundTemperature:Undisturbed:KusudaAchenbach',
               'pyname': u'SiteGroundTemperatureUndisturbedKusudaAchenbach',
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
    def soil_thermal_conductivity(self):
        """field `Soil Thermal Conductivity`

        |  Units: W/m-K

        Args:
            value (float): value for IDD Field `Soil Thermal Conductivity`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `soil_thermal_conductivity` or None if not set

        """
        return self["Soil Thermal Conductivity"]

    @soil_thermal_conductivity.setter
    def soil_thermal_conductivity(self, value=None):
        """Corresponds to IDD field `Soil Thermal Conductivity`"""
        self["Soil Thermal Conductivity"] = value

    @property
    def soil_density(self):
        """field `Soil Density`

        |  Units: kg/m3

        Args:
            value (float): value for IDD Field `Soil Density`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `soil_density` or None if not set

        """
        return self["Soil Density"]

    @soil_density.setter
    def soil_density(self, value=None):
        """Corresponds to IDD field `Soil Density`"""
        self["Soil Density"] = value

    @property
    def soil_specific_heat(self):
        """field `Soil Specific Heat`

        |  Units: J/kg-K

        Args:
            value (float): value for IDD Field `Soil Specific Heat`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `soil_specific_heat` or None if not set

        """
        return self["Soil Specific Heat"]

    @soil_specific_heat.setter
    def soil_specific_heat(self, value=None):
        """Corresponds to IDD field `Soil Specific Heat`"""
        self["Soil Specific Heat"] = value

    @property
    def average_soil_surface_temperature(self):
        """field `Average Soil Surface Temperature`

        |  Annual average surface temperature
        |  If left blank the Site:GroundTemperature:Shallow object must be included in the input
        |  The soil temperature, amplitude, and phase shift must all be included or omitted together
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
    def average_amplitude_of_surface_temperature(self):
        """field `Average Amplitude of Surface Temperature`

        |  Annual average surface temperature variation from average.
        |  If left blank the Site:GroundTemperature:Shallow object must be included in the input
        |  The soil temperature, amplitude, and phase shift must all be included or omitted together
        |  Units: deltaC

        Args:
            value (float): value for IDD Field `Average Amplitude of Surface Temperature`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `average_amplitude_of_surface_temperature` or None if not set

        """
        return self["Average Amplitude of Surface Temperature"]

    @average_amplitude_of_surface_temperature.setter
    def average_amplitude_of_surface_temperature(self, value=None):
        """Corresponds to IDD field `Average Amplitude of Surface
        Temperature`"""
        self["Average Amplitude of Surface Temperature"] = value

    @property
    def phase_shift_of_minimum_surface_temperature(self):
        """field `Phase Shift of Minimum Surface Temperature`

        |  The phase shift of minimum surface temperature, or the day
        |  of the year when the minimum surface temperature occurs.
        |  If left blank the Site:GroundTemperature:Shallow object must be included in the input
        |  The soil temperature, amplitude, and phase shift must all be included or omitted together
        |  Units: days
        |  value < 365.0

        Args:
            value (float): value for IDD Field `Phase Shift of Minimum Surface Temperature`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `phase_shift_of_minimum_surface_temperature` or None if not set

        """
        return self["Phase Shift of Minimum Surface Temperature"]

    @phase_shift_of_minimum_surface_temperature.setter
    def phase_shift_of_minimum_surface_temperature(self, value=None):
        """Corresponds to IDD field `Phase Shift of Minimum Surface
        Temperature`"""
        self["Phase Shift of Minimum Surface Temperature"] = value




class SiteGroundTemperatureUndisturbedXing(DataObject):

    """ Corresponds to IDD object `Site:GroundTemperature:Undisturbed:Xing`
        Undisturbed ground temperature object using the
        Xing 2014 2 harmonic parameter model.
    """
    _schema = {'extensible-fields': OrderedDict(),
               'fields': OrderedDict([(u'name',
                                       {'name': u'Name',
                                        'pyname': u'name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'soil thermal conductivity',
                                       {'name': u'Soil Thermal Conductivity',
                                        'pyname': u'soil_thermal_conductivity',
                                        'minimum>': 0.0,
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'W/m-K'}),
                                      (u'soil density',
                                       {'name': u'Soil Density',
                                        'pyname': u'soil_density',
                                        'minimum>': 0.0,
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'kg/m3'}),
                                      (u'soil specific heat',
                                       {'name': u'Soil Specific Heat',
                                        'pyname': u'soil_specific_heat',
                                        'minimum>': 0.0,
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'J/kg-K'}),
                                      (u'average soil surface tempeature',
                                       {'name': u'Average Soil Surface Tempeature',
                                        'pyname': u'average_soil_surface_tempeature',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'C'}),
                                      (u'soil surface temperature amplitude 1',
                                       {'name': u'Soil Surface Temperature Amplitude 1',
                                        'pyname': u'soil_surface_temperature_amplitude_1',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'deltaC'}),
                                      (u'soil surface temperature amplitude 2',
                                       {'name': u'Soil Surface Temperature Amplitude 2',
                                        'pyname': u'soil_surface_temperature_amplitude_2',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'deltaC'}),
                                      (u'phase shift of temperature amplitude 1',
                                       {'name': u'Phase Shift of Temperature Amplitude 1',
                                        'pyname': u'phase_shift_of_temperature_amplitude_1',
                                        'maximum<': 365.0,
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'days'}),
                                      (u'phase shift of temperature amplitude 2',
                                       {'name': u'Phase Shift of Temperature Amplitude 2',
                                        'pyname': u'phase_shift_of_temperature_amplitude_2',
                                        'maximum<': 365.0,
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'days'})]),
               'format': None,
               'group': u'Location and Climate',
               'min-fields': 9,
               'name': u'Site:GroundTemperature:Undisturbed:Xing',
               'pyname': u'SiteGroundTemperatureUndisturbedXing',
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
    def soil_thermal_conductivity(self):
        """field `Soil Thermal Conductivity`

        |  Units: W/m-K

        Args:
            value (float): value for IDD Field `Soil Thermal Conductivity`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `soil_thermal_conductivity` or None if not set

        """
        return self["Soil Thermal Conductivity"]

    @soil_thermal_conductivity.setter
    def soil_thermal_conductivity(self, value=None):
        """Corresponds to IDD field `Soil Thermal Conductivity`"""
        self["Soil Thermal Conductivity"] = value

    @property
    def soil_density(self):
        """field `Soil Density`

        |  Units: kg/m3

        Args:
            value (float): value for IDD Field `Soil Density`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `soil_density` or None if not set

        """
        return self["Soil Density"]

    @soil_density.setter
    def soil_density(self, value=None):
        """Corresponds to IDD field `Soil Density`"""
        self["Soil Density"] = value

    @property
    def soil_specific_heat(self):
        """field `Soil Specific Heat`

        |  Units: J/kg-K

        Args:
            value (float): value for IDD Field `Soil Specific Heat`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `soil_specific_heat` or None if not set

        """
        return self["Soil Specific Heat"]

    @soil_specific_heat.setter
    def soil_specific_heat(self, value=None):
        """Corresponds to IDD field `Soil Specific Heat`"""
        self["Soil Specific Heat"] = value

    @property
    def average_soil_surface_tempeature(self):
        """field `Average Soil Surface Tempeature`

        |  Units: C

        Args:
            value (float): value for IDD Field `Average Soil Surface Tempeature`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `average_soil_surface_tempeature` or None if not set

        """
        return self["Average Soil Surface Tempeature"]

    @average_soil_surface_tempeature.setter
    def average_soil_surface_tempeature(self, value=None):
        """Corresponds to IDD field `Average Soil Surface Tempeature`"""
        self["Average Soil Surface Tempeature"] = value

    @property
    def soil_surface_temperature_amplitude_1(self):
        """field `Soil Surface Temperature Amplitude 1`

        |  Units: deltaC

        Args:
            value (float): value for IDD Field `Soil Surface Temperature Amplitude 1`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `soil_surface_temperature_amplitude_1` or None if not set

        """
        return self["Soil Surface Temperature Amplitude 1"]

    @soil_surface_temperature_amplitude_1.setter
    def soil_surface_temperature_amplitude_1(self, value=None):
        """Corresponds to IDD field `Soil Surface Temperature Amplitude 1`"""
        self["Soil Surface Temperature Amplitude 1"] = value

    @property
    def soil_surface_temperature_amplitude_2(self):
        """field `Soil Surface Temperature Amplitude 2`

        |  Units: deltaC

        Args:
            value (float): value for IDD Field `Soil Surface Temperature Amplitude 2`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `soil_surface_temperature_amplitude_2` or None if not set

        """
        return self["Soil Surface Temperature Amplitude 2"]

    @soil_surface_temperature_amplitude_2.setter
    def soil_surface_temperature_amplitude_2(self, value=None):
        """Corresponds to IDD field `Soil Surface Temperature Amplitude 2`"""
        self["Soil Surface Temperature Amplitude 2"] = value

    @property
    def phase_shift_of_temperature_amplitude_1(self):
        """field `Phase Shift of Temperature Amplitude 1`

        |  Units: days
        |  value < 365.0

        Args:
            value (float): value for IDD Field `Phase Shift of Temperature Amplitude 1`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `phase_shift_of_temperature_amplitude_1` or None if not set

        """
        return self["Phase Shift of Temperature Amplitude 1"]

    @phase_shift_of_temperature_amplitude_1.setter
    def phase_shift_of_temperature_amplitude_1(self, value=None):
        """Corresponds to IDD field `Phase Shift of Temperature Amplitude 1`"""
        self["Phase Shift of Temperature Amplitude 1"] = value

    @property
    def phase_shift_of_temperature_amplitude_2(self):
        """field `Phase Shift of Temperature Amplitude 2`

        |  Units: days
        |  value < 365.0

        Args:
            value (float): value for IDD Field `Phase Shift of Temperature Amplitude 2`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `phase_shift_of_temperature_amplitude_2` or None if not set

        """
        return self["Phase Shift of Temperature Amplitude 2"]

    @phase_shift_of_temperature_amplitude_2.setter
    def phase_shift_of_temperature_amplitude_2(self, value=None):
        """Corresponds to IDD field `Phase Shift of Temperature Amplitude 2`"""
        self["Phase Shift of Temperature Amplitude 2"] = value




class SiteGroundDomainSlab(DataObject):

    """ Corresponds to IDD object `Site:GroundDomain:Slab`
        Ground-coupled slab model for on-grade and
        in-grade cases with or without insulation.
    """
    _schema = {'extensible-fields': OrderedDict(),
               'fields': OrderedDict([(u'name',
                                       {'name': u'Name',
                                        'pyname': u'name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'ground domain depth',
                                       {'name': u'Ground Domain Depth',
                                        'pyname': u'ground_domain_depth',
                                        'default': 10.0,
                                        'minimum>': 0.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'm'}),
                                      (u'aspect ratio',
                                       {'name': u'Aspect Ratio',
                                        'pyname': u'aspect_ratio',
                                        'default': 1.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'perimeter offset',
                                       {'name': u'Perimeter Offset',
                                        'pyname': u'perimeter_offset',
                                        'default': 5.0,
                                        'minimum>': 0.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'm'}),
                                      (u'soil thermal conductivity',
                                       {'name': u'Soil Thermal Conductivity',
                                        'pyname': u'soil_thermal_conductivity',
                                        'default': 1.5,
                                        'minimum>': 0.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'W/m-K'}),
                                      (u'soil density',
                                       {'name': u'Soil Density',
                                        'pyname': u'soil_density',
                                        'default': 2800.0,
                                        'minimum>': 0.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'kg/m3'}),
                                      (u'soil specific heat',
                                       {'name': u'Soil Specific Heat',
                                        'pyname': u'soil_specific_heat',
                                        'default': 850.0,
                                        'minimum>': 0.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'J/kg-K'}),
                                      (u'soil moisture content volume fraction',
                                       {'name': u'Soil Moisture Content Volume Fraction',
                                        'pyname': u'soil_moisture_content_volume_fraction',
                                        'default': 30.0,
                                        'maximum': 100.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'percent'}),
                                      (u'soil moisture content volume fraction at saturation',
                                       {'name': u'Soil Moisture Content Volume Fraction at Saturation',
                                        'pyname': u'soil_moisture_content_volume_fraction_at_saturation',
                                        'default': 50.0,
                                        'maximum': 100.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'percent'}),
                                      (u'undisturbed ground temperature model type',
                                       {'name': u'Undisturbed Ground Temperature Model Type',
                                        'pyname': u'undisturbed_ground_temperature_model_type',
                                        'required-field': True,
                                        'autosizable': False,
                                        'accepted-values': [u'Site:GroundTemperature:Undisturbed:FiniteDifference',
                                                            u'Site:GroundTemperature:Undisturbed:KusudaAchenbach',
                                                            u'Site:GroundTemperature:Undisturbed:Xing'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'undisturbed ground temperature model name',
                                       {'name': u'Undisturbed Ground Temperature Model Name',
                                        'pyname': u'undisturbed_ground_temperature_model_name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'evapotranspiration ground cover parameter',
                                       {'name': u'Evapotranspiration Ground Cover Parameter',
                                        'pyname': u'evapotranspiration_ground_cover_parameter',
                                        'default': 0.4,
                                        'maximum': 1.5,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'slab boundary condition model name',
                                       {'name': u'Slab Boundary Condition Model Name',
                                        'pyname': u'slab_boundary_condition_model_name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'slab location',
                                       {'name': u'Slab Location',
                                        'pyname': u'slab_location',
                                        'required-field': True,
                                        'autosizable': False,
                                        'accepted-values': [u'InGrade',
                                                            u'OnGrade'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'slab material name',
                                       {'name': u'Slab Material Name',
                                        'pyname': u'slab_material_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'horizontal insulation',
                                       {'name': u'Horizontal Insulation',
                                        'pyname': u'horizontal_insulation',
                                        'default': u'No',
                                        'required-field': False,
                                        'autosizable': False,
                                        'accepted-values': [u'Yes',
                                                            u'No'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'horizontal insulation material name',
                                       {'name': u'Horizontal Insulation Material Name',
                                        'pyname': u'horizontal_insulation_material_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'horizontal insulation extents',
                                       {'name': u'Horizontal Insulation Extents',
                                        'pyname': u'horizontal_insulation_extents',
                                        'default': u'Full',
                                        'required-field': False,
                                        'autosizable': False,
                                        'accepted-values': [u'Full',
                                                            u'Perimeter'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'perimeter insulation width',
                                       {'name': u'Perimeter Insulation Width',
                                        'pyname': u'perimeter_insulation_width',
                                        'minimum>': 0.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'm'}),
                                      (u'vertical insulation',
                                       {'name': u'Vertical Insulation',
                                        'pyname': u'vertical_insulation',
                                        'default': u'No',
                                        'required-field': False,
                                        'autosizable': False,
                                        'accepted-values': [u'Yes',
                                                            u'No'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'vertical insulation material name',
                                       {'name': u'Vertical Insulation Material Name',
                                        'pyname': u'vertical_insulation_material_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'vertical insulation depth',
                                       {'name': u'Vertical Insulation Depth',
                                        'pyname': u'vertical_insulation_depth',
                                        'minimum>': 0.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'm'}),
                                      (u'simulation timestep',
                                       {'name': u'Simulation Timestep',
                                        'pyname': u'simulation_timestep',
                                        'default': u'Hourly',
                                        'required-field': False,
                                        'autosizable': False,
                                        'accepted-values': [u'Hourly',
                                                            u'Timestep'],
                                        'autocalculatable': False,
                                        'type': 'alpha'})]),
               'format': None,
               'group': u'Location and Climate',
               'min-fields': 0,
               'name': u'Site:GroundDomain:Slab',
               'pyname': u'SiteGroundDomainSlab',
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
    def ground_domain_depth(self):
        """field `Ground Domain Depth`

        |  Units: m
        |  Default value: 10.0

        Args:
            value (float): value for IDD Field `Ground Domain Depth`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `ground_domain_depth` or None if not set

        """
        return self["Ground Domain Depth"]

    @ground_domain_depth.setter
    def ground_domain_depth(self, value=10.0):
        """Corresponds to IDD field `Ground Domain Depth`"""
        self["Ground Domain Depth"] = value

    @property
    def aspect_ratio(self):
        """field `Aspect Ratio`

        |  Default value: 1.0

        Args:
            value (float): value for IDD Field `Aspect Ratio`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `aspect_ratio` or None if not set

        """
        return self["Aspect Ratio"]

    @aspect_ratio.setter
    def aspect_ratio(self, value=1.0):
        """Corresponds to IDD field `Aspect Ratio`"""
        self["Aspect Ratio"] = value

    @property
    def perimeter_offset(self):
        """field `Perimeter Offset`

        |  Units: m
        |  Default value: 5.0

        Args:
            value (float): value for IDD Field `Perimeter Offset`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `perimeter_offset` or None if not set

        """
        return self["Perimeter Offset"]

    @perimeter_offset.setter
    def perimeter_offset(self, value=5.0):
        """Corresponds to IDD field `Perimeter Offset`"""
        self["Perimeter Offset"] = value

    @property
    def soil_thermal_conductivity(self):
        """field `Soil Thermal Conductivity`

        |  Units: W/m-K
        |  Default value: 1.5

        Args:
            value (float): value for IDD Field `Soil Thermal Conductivity`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `soil_thermal_conductivity` or None if not set

        """
        return self["Soil Thermal Conductivity"]

    @soil_thermal_conductivity.setter
    def soil_thermal_conductivity(self, value=1.5):
        """Corresponds to IDD field `Soil Thermal Conductivity`"""
        self["Soil Thermal Conductivity"] = value

    @property
    def soil_density(self):
        """field `Soil Density`

        |  Units: kg/m3
        |  Default value: 2800.0

        Args:
            value (float): value for IDD Field `Soil Density`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `soil_density` or None if not set

        """
        return self["Soil Density"]

    @soil_density.setter
    def soil_density(self, value=2800.0):
        """Corresponds to IDD field `Soil Density`"""
        self["Soil Density"] = value

    @property
    def soil_specific_heat(self):
        """field `Soil Specific Heat`

        |  Units: J/kg-K
        |  Default value: 850.0

        Args:
            value (float): value for IDD Field `Soil Specific Heat`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `soil_specific_heat` or None if not set

        """
        return self["Soil Specific Heat"]

    @soil_specific_heat.setter
    def soil_specific_heat(self, value=850.0):
        """Corresponds to IDD field `Soil Specific Heat`"""
        self["Soil Specific Heat"] = value

    @property
    def soil_moisture_content_volume_fraction(self):
        """field `Soil Moisture Content Volume Fraction`

        |  Units: percent
        |  Default value: 30.0
        |  value <= 100.0

        Args:
            value (float): value for IDD Field `Soil Moisture Content Volume Fraction`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `soil_moisture_content_volume_fraction` or None if not set

        """
        return self["Soil Moisture Content Volume Fraction"]

    @soil_moisture_content_volume_fraction.setter
    def soil_moisture_content_volume_fraction(self, value=30.0):
        """Corresponds to IDD field `Soil Moisture Content Volume Fraction`"""
        self["Soil Moisture Content Volume Fraction"] = value

    @property
    def soil_moisture_content_volume_fraction_at_saturation(self):
        """field `Soil Moisture Content Volume Fraction at Saturation`

        |  Units: percent
        |  Default value: 50.0
        |  value <= 100.0

        Args:
            value (float): value for IDD Field `Soil Moisture Content Volume Fraction at Saturation`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `soil_moisture_content_volume_fraction_at_saturation` or None if not set

        """
        return self["Soil Moisture Content Volume Fraction at Saturation"]

    @soil_moisture_content_volume_fraction_at_saturation.setter
    def soil_moisture_content_volume_fraction_at_saturation(self, value=50.0):
        """Corresponds to IDD field `Soil Moisture Content Volume Fraction at
        Saturation`"""
        self["Soil Moisture Content Volume Fraction at Saturation"] = value

    @property
    def undisturbed_ground_temperature_model_type(self):
        """field `Undisturbed Ground Temperature Model Type`

        Args:
            value (str): value for IDD Field `Undisturbed Ground Temperature Model Type`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `undisturbed_ground_temperature_model_type` or None if not set

        """
        return self["Undisturbed Ground Temperature Model Type"]

    @undisturbed_ground_temperature_model_type.setter
    def undisturbed_ground_temperature_model_type(self, value=None):
        """Corresponds to IDD field `Undisturbed Ground Temperature Model
        Type`"""
        self["Undisturbed Ground Temperature Model Type"] = value

    @property
    def undisturbed_ground_temperature_model_name(self):
        """field `Undisturbed Ground Temperature Model Name`

        Args:
            value (str): value for IDD Field `Undisturbed Ground Temperature Model Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `undisturbed_ground_temperature_model_name` or None if not set

        """
        return self["Undisturbed Ground Temperature Model Name"]

    @undisturbed_ground_temperature_model_name.setter
    def undisturbed_ground_temperature_model_name(self, value=None):
        """Corresponds to IDD field `Undisturbed Ground Temperature Model
        Name`"""
        self["Undisturbed Ground Temperature Model Name"] = value

    @property
    def evapotranspiration_ground_cover_parameter(self):
        """field `Evapotranspiration Ground Cover Parameter`

        |  This specifies the ground cover effects during evapotranspiration
        |  calculations.  The value roughly represents the following cases:
        |  = 0   : concrete or other solid, non-permeable ground surface material
        |  = 0.5 : short grass, much like a manicured lawn
        |  = 1   : standard reference state (12 cm grass)
        |  = 1.5 : wild growth
        |  Default value: 0.4
        |  value <= 1.5

        Args:
            value (float): value for IDD Field `Evapotranspiration Ground Cover Parameter`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `evapotranspiration_ground_cover_parameter` or None if not set

        """
        return self["Evapotranspiration Ground Cover Parameter"]

    @evapotranspiration_ground_cover_parameter.setter
    def evapotranspiration_ground_cover_parameter(self, value=0.4):
        """Corresponds to IDD field `Evapotranspiration Ground Cover
        Parameter`"""
        self["Evapotranspiration Ground Cover Parameter"] = value

    @property
    def slab_boundary_condition_model_name(self):
        """field `Slab Boundary Condition Model Name`

        Args:
            value (str): value for IDD Field `Slab Boundary Condition Model Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `slab_boundary_condition_model_name` or None if not set

        """
        return self["Slab Boundary Condition Model Name"]

    @slab_boundary_condition_model_name.setter
    def slab_boundary_condition_model_name(self, value=None):
        """Corresponds to IDD field `Slab Boundary Condition Model Name`"""
        self["Slab Boundary Condition Model Name"] = value

    @property
    def slab_location(self):
        """field `Slab Location`

        |  This field specifies whether the slab is located "in-grade" or "on-grade"

        Args:
            value (str): value for IDD Field `Slab Location`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `slab_location` or None if not set

        """
        return self["Slab Location"]

    @slab_location.setter
    def slab_location(self, value=None):
        """Corresponds to IDD field `Slab Location`"""
        self["Slab Location"] = value

    @property
    def slab_material_name(self):
        """field `Slab Material Name`

        |  Only applicable for the in-grade case

        Args:
            value (str): value for IDD Field `Slab Material Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `slab_material_name` or None if not set

        """
        return self["Slab Material Name"]

    @slab_material_name.setter
    def slab_material_name(self, value=None):
        """Corresponds to IDD field `Slab Material Name`"""
        self["Slab Material Name"] = value

    @property
    def horizontal_insulation(self):
        """field `Horizontal Insulation`

        |  This field specifies the presence of insulation beneath the slab.
        |  Only required for in-grade case.
        |  Default value: No

        Args:
            value (str): value for IDD Field `Horizontal Insulation`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `horizontal_insulation` or None if not set

        """
        return self["Horizontal Insulation"]

    @horizontal_insulation.setter
    def horizontal_insulation(self, value="No"):
        """Corresponds to IDD field `Horizontal Insulation`"""
        self["Horizontal Insulation"] = value

    @property
    def horizontal_insulation_material_name(self):
        """field `Horizontal Insulation Material Name`

        |  This field specifies the horizontal insulation material.

        Args:
            value (str): value for IDD Field `Horizontal Insulation Material Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `horizontal_insulation_material_name` or None if not set

        """
        return self["Horizontal Insulation Material Name"]

    @horizontal_insulation_material_name.setter
    def horizontal_insulation_material_name(self, value=None):
        """Corresponds to IDD field `Horizontal Insulation Material Name`"""
        self["Horizontal Insulation Material Name"] = value

    @property
    def horizontal_insulation_extents(self):
        """field `Horizontal Insulation Extents`

        |  This field specifies whether the horizontal insulation fully insulates
        |  the surface or is perimeter only insulation
        |  Default value: Full

        Args:
            value (str): value for IDD Field `Horizontal Insulation Extents`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `horizontal_insulation_extents` or None if not set

        """
        return self["Horizontal Insulation Extents"]

    @horizontal_insulation_extents.setter
    def horizontal_insulation_extents(self, value="Full"):
        """Corresponds to IDD field `Horizontal Insulation Extents`"""
        self["Horizontal Insulation Extents"] = value

    @property
    def perimeter_insulation_width(self):
        """field `Perimeter Insulation Width`

        |  This field specifies the width of the underfloor perimeter insulation
        |  Units: m

        Args:
            value (float): value for IDD Field `Perimeter Insulation Width`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `perimeter_insulation_width` or None if not set

        """
        return self["Perimeter Insulation Width"]

    @perimeter_insulation_width.setter
    def perimeter_insulation_width(self, value=None):
        """Corresponds to IDD field `Perimeter Insulation Width`"""
        self["Perimeter Insulation Width"] = value

    @property
    def vertical_insulation(self):
        """field `Vertical Insulation`

        |  This field specifies the presence of vertical insulation at the slab edge.
        |  Default value: No

        Args:
            value (str): value for IDD Field `Vertical Insulation`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `vertical_insulation` or None if not set

        """
        return self["Vertical Insulation"]

    @vertical_insulation.setter
    def vertical_insulation(self, value="No"):
        """Corresponds to IDD field `Vertical Insulation`"""
        self["Vertical Insulation"] = value

    @property
    def vertical_insulation_material_name(self):
        """field `Vertical Insulation Material Name`

        |  This field specifies the vertical insulation material.

        Args:
            value (str): value for IDD Field `Vertical Insulation Material Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `vertical_insulation_material_name` or None if not set

        """
        return self["Vertical Insulation Material Name"]

    @vertical_insulation_material_name.setter
    def vertical_insulation_material_name(self, value=None):
        """Corresponds to IDD field `Vertical Insulation Material Name`"""
        self["Vertical Insulation Material Name"] = value

    @property
    def vertical_insulation_depth(self):
        """field `Vertical Insulation Depth`

        |  Only used when including vertical insulation
        |  This field specifies the depth of the vertical insulation
        |  Units: m

        Args:
            value (float): value for IDD Field `Vertical Insulation Depth`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `vertical_insulation_depth` or None if not set

        """
        return self["Vertical Insulation Depth"]

    @vertical_insulation_depth.setter
    def vertical_insulation_depth(self, value=None):
        """Corresponds to IDD field `Vertical Insulation Depth`"""
        self["Vertical Insulation Depth"] = value

    @property
    def simulation_timestep(self):
        """field `Simulation Timestep`

        |  This field specifies the ground domain simulation timestep.
        |  Default value: Hourly

        Args:
            value (str): value for IDD Field `Simulation Timestep`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `simulation_timestep` or None if not set

        """
        return self["Simulation Timestep"]

    @simulation_timestep.setter
    def simulation_timestep(self, value="Hourly"):
        """Corresponds to IDD field `Simulation Timestep`"""
        self["Simulation Timestep"] = value




class SiteGroundDomainBasement(DataObject):

    """ Corresponds to IDD object `Site:GroundDomain:Basement`
        Ground-coupled basement model for simulating basements
        or other underground zones.
    """
    _schema = {'extensible-fields': OrderedDict(),
               'fields': OrderedDict([(u'name',
                                       {'name': u'Name',
                                        'pyname': u'name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'ground domain depth',
                                       {'name': u'Ground Domain Depth',
                                        'pyname': u'ground_domain_depth',
                                        'default': 10.0,
                                        'minimum>': 0.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'm'}),
                                      (u'aspect ratio',
                                       {'name': u'Aspect Ratio',
                                        'pyname': u'aspect_ratio',
                                        'default': 1.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'perimeter offset',
                                       {'name': u'Perimeter Offset',
                                        'pyname': u'perimeter_offset',
                                        'default': 5.0,
                                        'minimum>': 0.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'm'}),
                                      (u'soil thermal conductivity',
                                       {'name': u'Soil Thermal Conductivity',
                                        'pyname': u'soil_thermal_conductivity',
                                        'default': 1.5,
                                        'minimum>': 0.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'W/m-K'}),
                                      (u'soil density',
                                       {'name': u'Soil Density',
                                        'pyname': u'soil_density',
                                        'default': 2800.0,
                                        'minimum>': 0.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'kg/m3'}),
                                      (u'soil specific heat',
                                       {'name': u'Soil Specific Heat',
                                        'pyname': u'soil_specific_heat',
                                        'default': 850.0,
                                        'minimum>': 0.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'J/kg-K'}),
                                      (u'soil moisture content volume fraction',
                                       {'name': u'Soil Moisture Content Volume Fraction',
                                        'pyname': u'soil_moisture_content_volume_fraction',
                                        'default': 30.0,
                                        'maximum': 100.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'percent'}),
                                      (u'soil moisture content volume fraction at saturation',
                                       {'name': u'Soil Moisture Content Volume Fraction at Saturation',
                                        'pyname': u'soil_moisture_content_volume_fraction_at_saturation',
                                        'default': 50.0,
                                        'maximum': 100.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'percent'}),
                                      (u'undisturbed ground temperature model type',
                                       {'name': u'Undisturbed Ground Temperature Model Type',
                                        'pyname': u'undisturbed_ground_temperature_model_type',
                                        'required-field': True,
                                        'autosizable': False,
                                        'accepted-values': [u'Site:GroundTemperature:Undisturbed:FiniteDifference',
                                                            u'Site:GroundTemperature:Undisturbed:KusudaAchenbach',
                                                            u'Site:GroundTemperature:Undisturbed:Xing'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'undisturbed ground temperature model name',
                                       {'name': u'Undisturbed Ground Temperature Model Name',
                                        'pyname': u'undisturbed_ground_temperature_model_name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'evapotranspiration ground cover parameter',
                                       {'name': u'Evapotranspiration Ground Cover Parameter',
                                        'pyname': u'evapotranspiration_ground_cover_parameter',
                                        'default': 0.4,
                                        'maximum': 1.5,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'basement floor boundary condition model name',
                                       {'name': u'Basement Floor Boundary Condition Model Name',
                                        'pyname': u'basement_floor_boundary_condition_model_name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'horizontal insulation',
                                       {'name': u'Horizontal Insulation',
                                        'pyname': u'horizontal_insulation',
                                        'default': u'No',
                                        'required-field': False,
                                        'autosizable': False,
                                        'accepted-values': [u'Yes',
                                                            u'No'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'horizontal insulation material name',
                                       {'name': u'Horizontal Insulation Material Name',
                                        'pyname': u'horizontal_insulation_material_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'horizontal insulation extents',
                                       {'name': u'Horizontal Insulation Extents',
                                        'pyname': u'horizontal_insulation_extents',
                                        'default': u'Full',
                                        'required-field': False,
                                        'autosizable': False,
                                        'accepted-values': [u'Perimeter',
                                                            u'Full'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'perimeter horizontal insulation width',
                                       {'name': u'Perimeter Horizontal Insulation Width',
                                        'pyname': u'perimeter_horizontal_insulation_width',
                                        'minimum>': 0.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'm'}),
                                      (u'basement wall depth',
                                       {'name': u'Basement Wall Depth',
                                        'pyname': u'basement_wall_depth',
                                        'minimum>': 0.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'm'}),
                                      (u'basement wall boundary condition model name',
                                       {'name': u'Basement Wall Boundary Condition Model Name',
                                        'pyname': u'basement_wall_boundary_condition_model_name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'vertical insulation',
                                       {'name': u'Vertical Insulation',
                                        'pyname': u'vertical_insulation',
                                        'default': u'No',
                                        'required-field': False,
                                        'autosizable': False,
                                        'accepted-values': [u'Yes',
                                                            u'No'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'basement wall vertical insulation material name',
                                       {'name': u'Basement Wall Vertical Insulation Material Name',
                                        'pyname': u'basement_wall_vertical_insulation_material_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'vertical insulation depth',
                                       {'name': u'Vertical Insulation Depth',
                                        'pyname': u'vertical_insulation_depth',
                                        'minimum>': 0.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'm'}),
                                      (u'simulation timestep',
                                       {'name': u'Simulation Timestep',
                                        'pyname': u'simulation_timestep',
                                        'default': u'Hourly',
                                        'required-field': False,
                                        'autosizable': False,
                                        'accepted-values': [u'Timestep',
                                                            u'Hourly'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'mesh density parameter',
                                       {'name': u'Mesh Density Parameter',
                                        'pyname': u'mesh_density_parameter',
                                        'default': 4,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 2,
                                        'autocalculatable': False,
                                        'type': u'integer'})]),
               'format': None,
               'group': u'Location and Climate',
               'min-fields': 0,
               'name': u'Site:GroundDomain:Basement',
               'pyname': u'SiteGroundDomainBasement',
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
    def ground_domain_depth(self):
        """field `Ground Domain Depth`

        |  The depth from ground surface to the deep ground boundary of the domain.
        |  Units: m
        |  Default value: 10.0

        Args:
            value (float): value for IDD Field `Ground Domain Depth`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `ground_domain_depth` or None if not set

        """
        return self["Ground Domain Depth"]

    @ground_domain_depth.setter
    def ground_domain_depth(self, value=10.0):
        """Corresponds to IDD field `Ground Domain Depth`"""
        self["Ground Domain Depth"] = value

    @property
    def aspect_ratio(self):
        """field `Aspect Ratio`

        |  This defines the height to width ratio of the basement zone.
        |  Default value: 1.0

        Args:
            value (float): value for IDD Field `Aspect Ratio`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `aspect_ratio` or None if not set

        """
        return self["Aspect Ratio"]

    @aspect_ratio.setter
    def aspect_ratio(self, value=1.0):
        """Corresponds to IDD field `Aspect Ratio`"""
        self["Aspect Ratio"] = value

    @property
    def perimeter_offset(self):
        """field `Perimeter Offset`

        |  The distance from the basement wall edge to the edge of the ground domain
        |  Units: m
        |  Default value: 5.0

        Args:
            value (float): value for IDD Field `Perimeter Offset`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `perimeter_offset` or None if not set

        """
        return self["Perimeter Offset"]

    @perimeter_offset.setter
    def perimeter_offset(self, value=5.0):
        """Corresponds to IDD field `Perimeter Offset`"""
        self["Perimeter Offset"] = value

    @property
    def soil_thermal_conductivity(self):
        """field `Soil Thermal Conductivity`

        |  Units: W/m-K
        |  Default value: 1.5

        Args:
            value (float): value for IDD Field `Soil Thermal Conductivity`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `soil_thermal_conductivity` or None if not set

        """
        return self["Soil Thermal Conductivity"]

    @soil_thermal_conductivity.setter
    def soil_thermal_conductivity(self, value=1.5):
        """Corresponds to IDD field `Soil Thermal Conductivity`"""
        self["Soil Thermal Conductivity"] = value

    @property
    def soil_density(self):
        """field `Soil Density`

        |  Units: kg/m3
        |  Default value: 2800.0

        Args:
            value (float): value for IDD Field `Soil Density`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `soil_density` or None if not set

        """
        return self["Soil Density"]

    @soil_density.setter
    def soil_density(self, value=2800.0):
        """Corresponds to IDD field `Soil Density`"""
        self["Soil Density"] = value

    @property
    def soil_specific_heat(self):
        """field `Soil Specific Heat`

        |  Units: J/kg-K
        |  Default value: 850.0

        Args:
            value (float): value for IDD Field `Soil Specific Heat`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `soil_specific_heat` or None if not set

        """
        return self["Soil Specific Heat"]

    @soil_specific_heat.setter
    def soil_specific_heat(self, value=850.0):
        """Corresponds to IDD field `Soil Specific Heat`"""
        self["Soil Specific Heat"] = value

    @property
    def soil_moisture_content_volume_fraction(self):
        """field `Soil Moisture Content Volume Fraction`

        |  Units: percent
        |  Default value: 30.0
        |  value <= 100.0

        Args:
            value (float): value for IDD Field `Soil Moisture Content Volume Fraction`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `soil_moisture_content_volume_fraction` or None if not set

        """
        return self["Soil Moisture Content Volume Fraction"]

    @soil_moisture_content_volume_fraction.setter
    def soil_moisture_content_volume_fraction(self, value=30.0):
        """Corresponds to IDD field `Soil Moisture Content Volume Fraction`"""
        self["Soil Moisture Content Volume Fraction"] = value

    @property
    def soil_moisture_content_volume_fraction_at_saturation(self):
        """field `Soil Moisture Content Volume Fraction at Saturation`

        |  Units: percent
        |  Default value: 50.0
        |  value <= 100.0

        Args:
            value (float): value for IDD Field `Soil Moisture Content Volume Fraction at Saturation`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `soil_moisture_content_volume_fraction_at_saturation` or None if not set

        """
        return self["Soil Moisture Content Volume Fraction at Saturation"]

    @soil_moisture_content_volume_fraction_at_saturation.setter
    def soil_moisture_content_volume_fraction_at_saturation(self, value=50.0):
        """Corresponds to IDD field `Soil Moisture Content Volume Fraction at
        Saturation`"""
        self["Soil Moisture Content Volume Fraction at Saturation"] = value

    @property
    def undisturbed_ground_temperature_model_type(self):
        """field `Undisturbed Ground Temperature Model Type`

        Args:
            value (str): value for IDD Field `Undisturbed Ground Temperature Model Type`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `undisturbed_ground_temperature_model_type` or None if not set

        """
        return self["Undisturbed Ground Temperature Model Type"]

    @undisturbed_ground_temperature_model_type.setter
    def undisturbed_ground_temperature_model_type(self, value=None):
        """Corresponds to IDD field `Undisturbed Ground Temperature Model
        Type`"""
        self["Undisturbed Ground Temperature Model Type"] = value

    @property
    def undisturbed_ground_temperature_model_name(self):
        """field `Undisturbed Ground Temperature Model Name`

        Args:
            value (str): value for IDD Field `Undisturbed Ground Temperature Model Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `undisturbed_ground_temperature_model_name` or None if not set

        """
        return self["Undisturbed Ground Temperature Model Name"]

    @undisturbed_ground_temperature_model_name.setter
    def undisturbed_ground_temperature_model_name(self, value=None):
        """Corresponds to IDD field `Undisturbed Ground Temperature Model
        Name`"""
        self["Undisturbed Ground Temperature Model Name"] = value

    @property
    def evapotranspiration_ground_cover_parameter(self):
        """field `Evapotranspiration Ground Cover Parameter`

        |  This specifies the ground cover effects during evapotranspiration
        |  calculations.  The value roughly represents the following cases:
        |  = 0   : concrete or other solid, non-permeable ground surface material
        |  = 0.5 : short grass, much like a manicured lawn
        |  = 1   : standard reference state (12 cm grass)
        |  = 1.5 : wild growth
        |  Default value: 0.4
        |  value <= 1.5

        Args:
            value (float): value for IDD Field `Evapotranspiration Ground Cover Parameter`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `evapotranspiration_ground_cover_parameter` or None if not set

        """
        return self["Evapotranspiration Ground Cover Parameter"]

    @evapotranspiration_ground_cover_parameter.setter
    def evapotranspiration_ground_cover_parameter(self, value=0.4):
        """Corresponds to IDD field `Evapotranspiration Ground Cover
        Parameter`"""
        self["Evapotranspiration Ground Cover Parameter"] = value

    @property
    def basement_floor_boundary_condition_model_name(self):
        """field `Basement Floor Boundary Condition Model Name`

        Args:
            value (str): value for IDD Field `Basement Floor Boundary Condition Model Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `basement_floor_boundary_condition_model_name` or None if not set

        """
        return self["Basement Floor Boundary Condition Model Name"]

    @basement_floor_boundary_condition_model_name.setter
    def basement_floor_boundary_condition_model_name(self, value=None):
        """Corresponds to IDD field `Basement Floor Boundary Condition Model
        Name`"""
        self["Basement Floor Boundary Condition Model Name"] = value

    @property
    def horizontal_insulation(self):
        """field `Horizontal Insulation`

        |  This field specifies the presence of insulation beneath the basement floor.
        |  Default value: No

        Args:
            value (str): value for IDD Field `Horizontal Insulation`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `horizontal_insulation` or None if not set

        """
        return self["Horizontal Insulation"]

    @horizontal_insulation.setter
    def horizontal_insulation(self, value="No"):
        """Corresponds to IDD field `Horizontal Insulation`"""
        self["Horizontal Insulation"] = value

    @property
    def horizontal_insulation_material_name(self):
        """field `Horizontal Insulation Material Name`

        Args:
            value (str): value for IDD Field `Horizontal Insulation Material Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `horizontal_insulation_material_name` or None if not set

        """
        return self["Horizontal Insulation Material Name"]

    @horizontal_insulation_material_name.setter
    def horizontal_insulation_material_name(self, value=None):
        """Corresponds to IDD field `Horizontal Insulation Material Name`"""
        self["Horizontal Insulation Material Name"] = value

    @property
    def horizontal_insulation_extents(self):
        """field `Horizontal Insulation Extents`

        |  This field specifies whether the horizontal insulation fully insulates
        |  the surface or is perimeter only insulation
        |  Default value: Full

        Args:
            value (str): value for IDD Field `Horizontal Insulation Extents`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `horizontal_insulation_extents` or None if not set

        """
        return self["Horizontal Insulation Extents"]

    @horizontal_insulation_extents.setter
    def horizontal_insulation_extents(self, value="Full"):
        """Corresponds to IDD field `Horizontal Insulation Extents`"""
        self["Horizontal Insulation Extents"] = value

    @property
    def perimeter_horizontal_insulation_width(self):
        """field `Perimeter Horizontal Insulation Width`

        |  Width of horizontal perimeter insulation measured from
        |  foundation wall inside surface.
        |  Units: m

        Args:
            value (float): value for IDD Field `Perimeter Horizontal Insulation Width`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `perimeter_horizontal_insulation_width` or None if not set

        """
        return self["Perimeter Horizontal Insulation Width"]

    @perimeter_horizontal_insulation_width.setter
    def perimeter_horizontal_insulation_width(self, value=None):
        """Corresponds to IDD field `Perimeter Horizontal Insulation Width`"""
        self["Perimeter Horizontal Insulation Width"] = value

    @property
    def basement_wall_depth(self):
        """field `Basement Wall Depth`

        |  Depth measured from ground surface.
        |  Units: m

        Args:
            value (float): value for IDD Field `Basement Wall Depth`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `basement_wall_depth` or None if not set

        """
        return self["Basement Wall Depth"]

    @basement_wall_depth.setter
    def basement_wall_depth(self, value=None):
        """Corresponds to IDD field `Basement Wall Depth`"""
        self["Basement Wall Depth"] = value

    @property
    def basement_wall_boundary_condition_model_name(self):
        """field `Basement Wall Boundary Condition Model Name`

        Args:
            value (str): value for IDD Field `Basement Wall Boundary Condition Model Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `basement_wall_boundary_condition_model_name` or None if not set

        """
        return self["Basement Wall Boundary Condition Model Name"]

    @basement_wall_boundary_condition_model_name.setter
    def basement_wall_boundary_condition_model_name(self, value=None):
        """Corresponds to IDD field `Basement Wall Boundary Condition Model
        Name`"""
        self["Basement Wall Boundary Condition Model Name"] = value

    @property
    def vertical_insulation(self):
        """field `Vertical Insulation`

        |  Default value: No

        Args:
            value (str): value for IDD Field `Vertical Insulation`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `vertical_insulation` or None if not set

        """
        return self["Vertical Insulation"]

    @vertical_insulation.setter
    def vertical_insulation(self, value="No"):
        """Corresponds to IDD field `Vertical Insulation`"""
        self["Vertical Insulation"] = value

    @property
    def basement_wall_vertical_insulation_material_name(self):
        """field `Basement Wall Vertical Insulation Material Name`

        Args:
            value (str): value for IDD Field `Basement Wall Vertical Insulation Material Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `basement_wall_vertical_insulation_material_name` or None if not set

        """
        return self["Basement Wall Vertical Insulation Material Name"]

    @basement_wall_vertical_insulation_material_name.setter
    def basement_wall_vertical_insulation_material_name(self, value=None):
        """Corresponds to IDD field `Basement Wall Vertical Insulation Material
        Name`"""
        self["Basement Wall Vertical Insulation Material Name"] = value

    @property
    def vertical_insulation_depth(self):
        """field `Vertical Insulation Depth`

        |  Depth measured from the ground surface.
        |  Units: m

        Args:
            value (float): value for IDD Field `Vertical Insulation Depth`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `vertical_insulation_depth` or None if not set

        """
        return self["Vertical Insulation Depth"]

    @vertical_insulation_depth.setter
    def vertical_insulation_depth(self, value=None):
        """Corresponds to IDD field `Vertical Insulation Depth`"""
        self["Vertical Insulation Depth"] = value

    @property
    def simulation_timestep(self):
        """field `Simulation Timestep`

        |  This field specifies the basement domain simulation interval.
        |  Default value: Hourly

        Args:
            value (str): value for IDD Field `Simulation Timestep`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `simulation_timestep` or None if not set

        """
        return self["Simulation Timestep"]

    @simulation_timestep.setter
    def simulation_timestep(self, value="Hourly"):
        """Corresponds to IDD field `Simulation Timestep`"""
        self["Simulation Timestep"] = value

    @property
    def mesh_density_parameter(self):
        """field `Mesh Density Parameter`

        |  Default value: 4
        |  value >= 2

        Args:
            value (int): value for IDD Field `Mesh Density Parameter`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            int: the value of `mesh_density_parameter` or None if not set

        """
        return self["Mesh Density Parameter"]

    @mesh_density_parameter.setter
    def mesh_density_parameter(self, value=4):
        """Corresponds to IDD field `Mesh Density Parameter`"""
        self["Mesh Density Parameter"] = value




class SiteGroundReflectance(DataObject):

    """ Corresponds to IDD object `Site:GroundReflectance`
        Specifies the ground reflectance values used to calculate ground reflected solar.
        The ground reflectance can be further modified when snow is on the ground
        by Site:GroundReflectance:SnowModifier.
    """
    _schema = {'extensible-fields': OrderedDict(),
               'fields': OrderedDict([(u'january ground reflectance',
                                       {'name': u'January Ground Reflectance',
                                        'pyname': u'january_ground_reflectance',
                                        'default': 0.2,
                                        'maximum': 1.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'dimensionless'}),
                                      (u'february ground reflectance',
                                       {'name': u'February Ground Reflectance',
                                        'pyname': u'february_ground_reflectance',
                                        'default': 0.2,
                                        'maximum': 1.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'dimensionless'}),
                                      (u'march ground reflectance',
                                       {'name': u'March Ground Reflectance',
                                        'pyname': u'march_ground_reflectance',
                                        'default': 0.2,
                                        'maximum': 1.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'dimensionless'}),
                                      (u'april ground reflectance',
                                       {'name': u'April Ground Reflectance',
                                        'pyname': u'april_ground_reflectance',
                                        'default': 0.2,
                                        'maximum': 1.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'dimensionless'}),
                                      (u'may ground reflectance',
                                       {'name': u'May Ground Reflectance',
                                        'pyname': u'may_ground_reflectance',
                                        'default': 0.2,
                                        'maximum': 1.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'dimensionless'}),
                                      (u'june ground reflectance',
                                       {'name': u'June Ground Reflectance',
                                        'pyname': u'june_ground_reflectance',
                                        'default': 0.2,
                                        'maximum': 1.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'dimensionless'}),
                                      (u'july ground reflectance',
                                       {'name': u'July Ground Reflectance',
                                        'pyname': u'july_ground_reflectance',
                                        'default': 0.2,
                                        'maximum': 1.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'dimensionless'}),
                                      (u'august ground reflectance',
                                       {'name': u'August Ground Reflectance',
                                        'pyname': u'august_ground_reflectance',
                                        'default': 0.2,
                                        'maximum': 1.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'dimensionless'}),
                                      (u'september ground reflectance',
                                       {'name': u'September Ground Reflectance',
                                        'pyname': u'september_ground_reflectance',
                                        'default': 0.2,
                                        'maximum': 1.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'dimensionless'}),
                                      (u'october ground reflectance',
                                       {'name': u'October Ground Reflectance',
                                        'pyname': u'october_ground_reflectance',
                                        'default': 0.2,
                                        'maximum': 1.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'dimensionless'}),
                                      (u'november ground reflectance',
                                       {'name': u'November Ground Reflectance',
                                        'pyname': u'november_ground_reflectance',
                                        'default': 0.2,
                                        'maximum': 1.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'dimensionless'}),
                                      (u'december ground reflectance',
                                       {'name': u'December Ground Reflectance',
                                        'pyname': u'december_ground_reflectance',
                                        'default': 0.2,
                                        'maximum': 1.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'dimensionless'})]),
               'format': u'singleline',
               'group': u'Location and Climate',
               'min-fields': 12,
               'name': u'Site:GroundReflectance',
               'pyname': u'SiteGroundReflectance',
               'required-object': False,
               'unique-object': True}

    @property
    def january_ground_reflectance(self):
        """field `January Ground Reflectance`

        |  Units: dimensionless
        |  Default value: 0.2
        |  value <= 1.0

        Args:
            value (float): value for IDD Field `January Ground Reflectance`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `january_ground_reflectance` or None if not set

        """
        return self["January Ground Reflectance"]

    @january_ground_reflectance.setter
    def january_ground_reflectance(self, value=0.2):
        """Corresponds to IDD field `January Ground Reflectance`"""
        self["January Ground Reflectance"] = value

    @property
    def february_ground_reflectance(self):
        """field `February Ground Reflectance`

        |  Units: dimensionless
        |  Default value: 0.2
        |  value <= 1.0

        Args:
            value (float): value for IDD Field `February Ground Reflectance`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `february_ground_reflectance` or None if not set

        """
        return self["February Ground Reflectance"]

    @february_ground_reflectance.setter
    def february_ground_reflectance(self, value=0.2):
        """Corresponds to IDD field `February Ground Reflectance`"""
        self["February Ground Reflectance"] = value

    @property
    def march_ground_reflectance(self):
        """field `March Ground Reflectance`

        |  Units: dimensionless
        |  Default value: 0.2
        |  value <= 1.0

        Args:
            value (float): value for IDD Field `March Ground Reflectance`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `march_ground_reflectance` or None if not set

        """
        return self["March Ground Reflectance"]

    @march_ground_reflectance.setter
    def march_ground_reflectance(self, value=0.2):
        """Corresponds to IDD field `March Ground Reflectance`"""
        self["March Ground Reflectance"] = value

    @property
    def april_ground_reflectance(self):
        """field `April Ground Reflectance`

        |  Units: dimensionless
        |  Default value: 0.2
        |  value <= 1.0

        Args:
            value (float): value for IDD Field `April Ground Reflectance`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `april_ground_reflectance` or None if not set

        """
        return self["April Ground Reflectance"]

    @april_ground_reflectance.setter
    def april_ground_reflectance(self, value=0.2):
        """Corresponds to IDD field `April Ground Reflectance`"""
        self["April Ground Reflectance"] = value

    @property
    def may_ground_reflectance(self):
        """field `May Ground Reflectance`

        |  Units: dimensionless
        |  Default value: 0.2
        |  value <= 1.0

        Args:
            value (float): value for IDD Field `May Ground Reflectance`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `may_ground_reflectance` or None if not set

        """
        return self["May Ground Reflectance"]

    @may_ground_reflectance.setter
    def may_ground_reflectance(self, value=0.2):
        """Corresponds to IDD field `May Ground Reflectance`"""
        self["May Ground Reflectance"] = value

    @property
    def june_ground_reflectance(self):
        """field `June Ground Reflectance`

        |  Units: dimensionless
        |  Default value: 0.2
        |  value <= 1.0

        Args:
            value (float): value for IDD Field `June Ground Reflectance`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `june_ground_reflectance` or None if not set

        """
        return self["June Ground Reflectance"]

    @june_ground_reflectance.setter
    def june_ground_reflectance(self, value=0.2):
        """Corresponds to IDD field `June Ground Reflectance`"""
        self["June Ground Reflectance"] = value

    @property
    def july_ground_reflectance(self):
        """field `July Ground Reflectance`

        |  Units: dimensionless
        |  Default value: 0.2
        |  value <= 1.0

        Args:
            value (float): value for IDD Field `July Ground Reflectance`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `july_ground_reflectance` or None if not set

        """
        return self["July Ground Reflectance"]

    @july_ground_reflectance.setter
    def july_ground_reflectance(self, value=0.2):
        """Corresponds to IDD field `July Ground Reflectance`"""
        self["July Ground Reflectance"] = value

    @property
    def august_ground_reflectance(self):
        """field `August Ground Reflectance`

        |  Units: dimensionless
        |  Default value: 0.2
        |  value <= 1.0

        Args:
            value (float): value for IDD Field `August Ground Reflectance`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `august_ground_reflectance` or None if not set

        """
        return self["August Ground Reflectance"]

    @august_ground_reflectance.setter
    def august_ground_reflectance(self, value=0.2):
        """Corresponds to IDD field `August Ground Reflectance`"""
        self["August Ground Reflectance"] = value

    @property
    def september_ground_reflectance(self):
        """field `September Ground Reflectance`

        |  Units: dimensionless
        |  Default value: 0.2
        |  value <= 1.0

        Args:
            value (float): value for IDD Field `September Ground Reflectance`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `september_ground_reflectance` or None if not set

        """
        return self["September Ground Reflectance"]

    @september_ground_reflectance.setter
    def september_ground_reflectance(self, value=0.2):
        """Corresponds to IDD field `September Ground Reflectance`"""
        self["September Ground Reflectance"] = value

    @property
    def october_ground_reflectance(self):
        """field `October Ground Reflectance`

        |  Units: dimensionless
        |  Default value: 0.2
        |  value <= 1.0

        Args:
            value (float): value for IDD Field `October Ground Reflectance`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `october_ground_reflectance` or None if not set

        """
        return self["October Ground Reflectance"]

    @october_ground_reflectance.setter
    def october_ground_reflectance(self, value=0.2):
        """Corresponds to IDD field `October Ground Reflectance`"""
        self["October Ground Reflectance"] = value

    @property
    def november_ground_reflectance(self):
        """field `November Ground Reflectance`

        |  Units: dimensionless
        |  Default value: 0.2
        |  value <= 1.0

        Args:
            value (float): value for IDD Field `November Ground Reflectance`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `november_ground_reflectance` or None if not set

        """
        return self["November Ground Reflectance"]

    @november_ground_reflectance.setter
    def november_ground_reflectance(self, value=0.2):
        """Corresponds to IDD field `November Ground Reflectance`"""
        self["November Ground Reflectance"] = value

    @property
    def december_ground_reflectance(self):
        """field `December Ground Reflectance`

        |  Units: dimensionless
        |  Default value: 0.2
        |  value <= 1.0

        Args:
            value (float): value for IDD Field `December Ground Reflectance`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `december_ground_reflectance` or None if not set

        """
        return self["December Ground Reflectance"]

    @december_ground_reflectance.setter
    def december_ground_reflectance(self, value=0.2):
        """Corresponds to IDD field `December Ground Reflectance`"""
        self["December Ground Reflectance"] = value




class SiteGroundReflectanceSnowModifier(DataObject):

    """ Corresponds to IDD object `Site:GroundReflectance:SnowModifier`
        Specifies ground reflectance multipliers when snow resident on the ground.
        These multipliers are applied to the "normal" ground reflectances specified
        in Site:GroundReflectance.
    """
    _schema = {'extensible-fields': OrderedDict(),
               'fields': OrderedDict([(u'ground reflected solar modifier',
                                       {'name': u'Ground Reflected Solar Modifier',
                                        'pyname': u'ground_reflected_solar_modifier',
                                        'default': 1.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': 'real'}),
                                      (u'daylighting ground reflected solar modifier',
                                       {'name': u'Daylighting Ground Reflected Solar Modifier',
                                        'pyname': u'daylighting_ground_reflected_solar_modifier',
                                        'default': 1.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': 'real'})]),
               'format': None,
               'group': u'Location and Climate',
               'min-fields': 0,
               'name': u'Site:GroundReflectance:SnowModifier',
               'pyname': u'SiteGroundReflectanceSnowModifier',
               'required-object': False,
               'unique-object': False}

    @property
    def ground_reflected_solar_modifier(self):
        """field `Ground Reflected Solar Modifier`

        |  Value for modifying the "normal" ground reflectance when Snow is on ground
        |  when calculating the "Ground Reflected Solar Radiation Value"
        |  a value of 1.0 here uses the "normal" ground reflectance
        |  Ground Reflected Solar = (BeamSolar*CosSunZenith + DiffuseSolar)*GroundReflectance
        |  This would be further modified by the Snow Ground Reflectance Modifier when Snow was on the ground
        |  When Snow on ground, effective GroundReflectance is normal GroundReflectance*"Ground Reflectance Snow Modifier"
        |  Ground Reflectance achieved in this manner will be restricted to [0.0,1.0]
        |  Default value: 1.0

        Args:
            value (float): value for IDD Field `Ground Reflected Solar Modifier`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `ground_reflected_solar_modifier` or None if not set

        """
        return self["Ground Reflected Solar Modifier"]

    @ground_reflected_solar_modifier.setter
    def ground_reflected_solar_modifier(self, value=1.0):
        """Corresponds to IDD field `Ground Reflected Solar Modifier`"""
        self["Ground Reflected Solar Modifier"] = value

    @property
    def daylighting_ground_reflected_solar_modifier(self):
        """field `Daylighting Ground Reflected Solar Modifier`

        |  Value for modifying the "normal" daylighting ground reflectance when Snow is on ground
        |  when calculating the "Ground Reflected Solar Radiation Value"
        |  a value of 1.0 here uses the "normal" ground reflectance
        |  Ground Reflected Solar = (BeamSolar*CosSunZenith + DiffuseSolar)*GroundReflectance
        |  This would be further modified by the Snow Ground Reflectance Modifier when Snow was on the ground
        |  When Snow on ground, effective GroundReflectance is normal GroundReflectance*"Daylighting Ground Reflectance Snow Modifier"
        |  Ground Reflectance achieved in this manner will be restricted to [0.0,1.0]
        |  Default value: 1.0

        Args:
            value (float): value for IDD Field `Daylighting Ground Reflected Solar Modifier`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `daylighting_ground_reflected_solar_modifier` or None if not set

        """
        return self["Daylighting Ground Reflected Solar Modifier"]

    @daylighting_ground_reflected_solar_modifier.setter
    def daylighting_ground_reflected_solar_modifier(self, value=1.0):
        """Corresponds to IDD field `Daylighting Ground Reflected Solar
        Modifier`"""
        self["Daylighting Ground Reflected Solar Modifier"] = value




class SiteWaterMainsTemperature(DataObject):

    """ Corresponds to IDD object `Site:WaterMainsTemperature`
        Used to calculate water mains temperatures delivered by underground water main pipes.
        Water mains temperatures are a function of outdoor climate conditions
        and vary with time of year.
    """
    _schema = {'extensible-fields': OrderedDict(),
               'fields': OrderedDict([(u'calculation method',
                                       {'name': u'Calculation Method',
                                        'pyname': u'calculation_method',
                                        'required-field': True,
                                        'autosizable': False,
                                        'accepted-values': [u'Schedule',
                                                            u'Correlation'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'temperature schedule name',
                                       {'name': u'Temperature Schedule Name',
                                        'pyname': u'temperature_schedule_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'annual average outdoor air temperature',
                                       {'name': u'Annual Average Outdoor Air Temperature',
                                        'pyname': u'annual_average_outdoor_air_temperature',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'C'}),
                                      (u'maximum difference in monthly average outdoor air temperatures',
                                       {'name': u'Maximum Difference In Monthly Average Outdoor Air Temperatures',
                                        'pyname': u'maximum_difference_in_monthly_average_outdoor_air_temperatures',
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'deltaC'})]),
               'format': None,
               'group': u'Location and Climate',
               'min-fields': 0,
               'name': u'Site:WaterMainsTemperature',
               'pyname': u'SiteWaterMainsTemperature',
               'required-object': False,
               'unique-object': False}

    @property
    def calculation_method(self):
        """field `Calculation Method`

        Args:
            value (str): value for IDD Field `Calculation Method`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `calculation_method` or None if not set

        """
        return self["Calculation Method"]

    @calculation_method.setter
    def calculation_method(self, value=None):
        """Corresponds to IDD field `Calculation Method`"""
        self["Calculation Method"] = value

    @property
    def temperature_schedule_name(self):
        """field `Temperature Schedule Name`

        Args:
            value (str): value for IDD Field `Temperature Schedule Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `temperature_schedule_name` or None if not set

        """
        return self["Temperature Schedule Name"]

    @temperature_schedule_name.setter
    def temperature_schedule_name(self, value=None):
        """Corresponds to IDD field `Temperature Schedule Name`"""
        self["Temperature Schedule Name"] = value

    @property
    def annual_average_outdoor_air_temperature(self):
        """field `Annual Average Outdoor Air Temperature`

        |  Units: C

        Args:
            value (float): value for IDD Field `Annual Average Outdoor Air Temperature`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `annual_average_outdoor_air_temperature` or None if not set

        """
        return self["Annual Average Outdoor Air Temperature"]

    @annual_average_outdoor_air_temperature.setter
    def annual_average_outdoor_air_temperature(self, value=None):
        """Corresponds to IDD field `Annual Average Outdoor Air Temperature`"""
        self["Annual Average Outdoor Air Temperature"] = value

    @property
    def maximum_difference_in_monthly_average_outdoor_air_temperatures(self):
        """field `Maximum Difference In Monthly Average Outdoor Air
        Temperatures`

        |  Units: deltaC

        Args:
            value (float): value for IDD Field `Maximum Difference In Monthly Average Outdoor Air Temperatures`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `maximum_difference_in_monthly_average_outdoor_air_temperatures` or None if not set

        """
        return self[
            "Maximum Difference In Monthly Average Outdoor Air Temperatures"]

    @maximum_difference_in_monthly_average_outdoor_air_temperatures.setter
    def maximum_difference_in_monthly_average_outdoor_air_temperatures(
            self,
            value=None):
        """Corresponds to IDD field `Maximum Difference In Monthly Average
        Outdoor Air Temperatures`"""
        self[
            "Maximum Difference In Monthly Average Outdoor Air Temperatures"] = value




class SitePrecipitation(DataObject):

    """ Corresponds to IDD object `Site:Precipitation`
        Used to describe the amount of water precipitation at the building site.
        Precipitation includes both rain and the equivalent water content of snow.
    """
    _schema = {'extensible-fields': OrderedDict(),
               'fields': OrderedDict([(u'precipitation model type',
                                       {'name': u'Precipitation Model Type',
                                        'pyname': u'precipitation_model_type',
                                        'required-field': False,
                                        'autosizable': False,
                                        'accepted-values': [u'ScheduleAndDesignLevel'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'design level for total annual precipitation',
                                       {'name': u'Design Level for Total Annual Precipitation',
                                        'pyname': u'design_level_for_total_annual_precipitation',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': 'real',
                                        'unit': u'm/yr'}),
                                      (u'precipitation rates schedule name',
                                       {'name': u'Precipitation Rates Schedule Name',
                                        'pyname': u'precipitation_rates_schedule_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'average total annual precipitation',
                                       {'name': u'Average Total Annual Precipitation',
                                        'pyname': u'average_total_annual_precipitation',
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': 'real',
                                        'unit': u'm/yr'})]),
               'format': None,
               'group': u'Location and Climate',
               'min-fields': 0,
               'name': u'Site:Precipitation',
               'pyname': u'SitePrecipitation',
               'required-object': False,
               'unique-object': False}

    @property
    def precipitation_model_type(self):
        """field `Precipitation Model Type`

        Args:
            value (str): value for IDD Field `Precipitation Model Type`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `precipitation_model_type` or None if not set

        """
        return self["Precipitation Model Type"]

    @precipitation_model_type.setter
    def precipitation_model_type(self, value=None):
        """Corresponds to IDD field `Precipitation Model Type`"""
        self["Precipitation Model Type"] = value

    @property
    def design_level_for_total_annual_precipitation(self):
        """field `Design Level for Total Annual Precipitation`

        |  meters of water per year used for design level
        |  Units: m/yr

        Args:
            value (float): value for IDD Field `Design Level for Total Annual Precipitation`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `design_level_for_total_annual_precipitation` or None if not set

        """
        return self["Design Level for Total Annual Precipitation"]

    @design_level_for_total_annual_precipitation.setter
    def design_level_for_total_annual_precipitation(self, value=None):
        """Corresponds to IDD field `Design Level for Total Annual
        Precipitation`"""
        self["Design Level for Total Annual Precipitation"] = value

    @property
    def precipitation_rates_schedule_name(self):
        """field `Precipitation Rates Schedule Name`

        |  Schedule values in meters of water per hour
        |  values should be non-negative

        Args:
            value (str): value for IDD Field `Precipitation Rates Schedule Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `precipitation_rates_schedule_name` or None if not set

        """
        return self["Precipitation Rates Schedule Name"]

    @precipitation_rates_schedule_name.setter
    def precipitation_rates_schedule_name(self, value=None):
        """Corresponds to IDD field `Precipitation Rates Schedule Name`"""
        self["Precipitation Rates Schedule Name"] = value

    @property
    def average_total_annual_precipitation(self):
        """field `Average Total Annual Precipitation`

        |  meters of water per year from average weather statistics
        |  Units: m/yr

        Args:
            value (float): value for IDD Field `Average Total Annual Precipitation`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `average_total_annual_precipitation` or None if not set

        """
        return self["Average Total Annual Precipitation"]

    @average_total_annual_precipitation.setter
    def average_total_annual_precipitation(self, value=None):
        """Corresponds to IDD field `Average Total Annual Precipitation`"""
        self["Average Total Annual Precipitation"] = value




class RoofIrrigation(DataObject):

    """Corresponds to IDD object `RoofIrrigation` Used to describe the amount
    of irrigation on the ecoroof surface over the course of the simulation
    runperiod."""
    _schema = {'extensible-fields': OrderedDict(),
               'fields': OrderedDict([(u'irrigation model type',
                                       {'name': u'Irrigation Model Type',
                                        'pyname': u'irrigation_model_type',
                                        'required-field': False,
                                        'autosizable': False,
                                        'accepted-values': [u'Schedule',
                                                            u'SmartSchedule'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'irrigation rate schedule name',
                                       {'name': u'Irrigation Rate Schedule Name',
                                        'pyname': u'irrigation_rate_schedule_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'irrigation maximum saturation threshold',
                                       {'name': u'Irrigation Maximum Saturation Threshold',
                                        'pyname': u'irrigation_maximum_saturation_threshold',
                                        'default': 40.0,
                                        'maximum': 100.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': 'real',
                                        'unit': u'percent'})]),
               'format': None,
               'group': u'Location and Climate',
               'min-fields': 0,
               'name': u'RoofIrrigation',
               'pyname': u'RoofIrrigation',
               'required-object': False,
               'unique-object': False}

    @property
    def irrigation_model_type(self):
        """field `Irrigation Model Type`

        |  SmartSchedule will not allow irrigation when soil is already moist.
        |  Current threshold set at 30% of saturation.

        Args:
            value (str): value for IDD Field `Irrigation Model Type`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `irrigation_model_type` or None if not set

        """
        return self["Irrigation Model Type"]

    @irrigation_model_type.setter
    def irrigation_model_type(self, value=None):
        """Corresponds to IDD field `Irrigation Model Type`"""
        self["Irrigation Model Type"] = value

    @property
    def irrigation_rate_schedule_name(self):
        """field `Irrigation Rate Schedule Name`

        |  Schedule values in meters of water per hour
        |  values should be non-negative

        Args:
            value (str): value for IDD Field `Irrigation Rate Schedule Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `irrigation_rate_schedule_name` or None if not set

        """
        return self["Irrigation Rate Schedule Name"]

    @irrigation_rate_schedule_name.setter
    def irrigation_rate_schedule_name(self, value=None):
        """Corresponds to IDD field `Irrigation Rate Schedule Name`"""
        self["Irrigation Rate Schedule Name"] = value

    @property
    def irrigation_maximum_saturation_threshold(self):
        """field `Irrigation Maximum Saturation Threshold`

        |  Used with SmartSchedule to set the saturation level at which no
        |  irrigation is allowed.
        |  Units: percent
        |  Default value: 40.0
        |  value <= 100.0

        Args:
            value (float): value for IDD Field `Irrigation Maximum Saturation Threshold`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `irrigation_maximum_saturation_threshold` or None if not set

        """
        return self["Irrigation Maximum Saturation Threshold"]

    @irrigation_maximum_saturation_threshold.setter
    def irrigation_maximum_saturation_threshold(self, value=40.0):
        """Corresponds to IDD field `Irrigation Maximum Saturation
        Threshold`"""
        self["Irrigation Maximum Saturation Threshold"] = value




class SiteSolarAndVisibleSpectrum(DataObject):

    """ Corresponds to IDD object `Site:SolarAndVisibleSpectrum`
        If this object is omitted, the default solar and visible spectrum data will be used.
    """
    _schema = {'extensible-fields': OrderedDict(),
               'fields': OrderedDict([(u'name',
                                       {'name': u'Name',
                                        'pyname': u'name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'alpha'}),
                                      (u'spectrum data method',
                                       {'name': u'Spectrum Data Method',
                                        'pyname': u'spectrum_data_method',
                                        'default': u'Default',
                                        'required-field': False,
                                        'autosizable': False,
                                        'accepted-values': [u'Default',
                                                            u'UserDefined'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'solar spectrum data object name',
                                       {'name': u'Solar Spectrum Data Object Name',
                                        'pyname': u'solar_spectrum_data_object_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'visible spectrum data object name',
                                       {'name': u'Visible Spectrum Data Object Name',
                                        'pyname': u'visible_spectrum_data_object_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'})]),
               'format': None,
               'group': u'Location and Climate',
               'min-fields': 0,
               'name': u'Site:SolarAndVisibleSpectrum',
               'pyname': u'SiteSolarAndVisibleSpectrum',
               'required-object': False,
               'unique-object': True}

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
    def spectrum_data_method(self):
        """field `Spectrum Data Method`

        |  The method specifies which of the solar and visible spectrum data to use in the calculations.
        |  Choices: Default - existing hard-wired spectrum data in EnergyPlus.
        |  UserDefined - user specified spectrum data referenced by the next two fields
        |  Default value: Default

        Args:
            value (str): value for IDD Field `Spectrum Data Method`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `spectrum_data_method` or None if not set

        """
        return self["Spectrum Data Method"]

    @spectrum_data_method.setter
    def spectrum_data_method(self, value="Default"):
        """Corresponds to IDD field `Spectrum Data Method`"""
        self["Spectrum Data Method"] = value

    @property
    def solar_spectrum_data_object_name(self):
        """field `Solar Spectrum Data Object Name`

        Args:
            value (str): value for IDD Field `Solar Spectrum Data Object Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `solar_spectrum_data_object_name` or None if not set

        """
        return self["Solar Spectrum Data Object Name"]

    @solar_spectrum_data_object_name.setter
    def solar_spectrum_data_object_name(self, value=None):
        """Corresponds to IDD field `Solar Spectrum Data Object Name`"""
        self["Solar Spectrum Data Object Name"] = value

    @property
    def visible_spectrum_data_object_name(self):
        """field `Visible Spectrum Data Object Name`

        Args:
            value (str): value for IDD Field `Visible Spectrum Data Object Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `visible_spectrum_data_object_name` or None if not set

        """
        return self["Visible Spectrum Data Object Name"]

    @visible_spectrum_data_object_name.setter
    def visible_spectrum_data_object_name(self, value=None):
        """Corresponds to IDD field `Visible Spectrum Data Object Name`"""
        self["Visible Spectrum Data Object Name"] = value


