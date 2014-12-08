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

        + is North, - is South, degree minutes represented in decimal (i.e. 30 minutes is .5)

        Args:
            value (float): value for IDD Field `Latitude`
                Units: deg
                value >= -90.0
                value <= 90.0

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

        - is West, + is East, degree minutes represented in decimal (i.e. 30 minutes is .5)

        Args:
            value (float): value for IDD Field `Longitude`
                Units: deg
                value >= -180.0
                value <= 180.0

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
        """field `Time Zone` basic these limits on the WorldTimeZone Map (2003)
        Time relative to GMT. Decimal hours.

        Args:
            value (float): value for IDD Field `Time Zone`
                Units: hr
                value >= -12.0
                value <= 14.0

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

        Args:
            value (float): value for IDD Field `Elevation`
                Units: m
                value >= -300.0
                value < 8900.0

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
                                      (u'enthalpy at maximum dry-bulb  !will require units transition.',
                                       {'name': u'Enthalpy at Maximum Dry-Bulb  !will require units transition.',
                                        'pyname': u'enthalpy_at_maximum_drybulb_will_require_units_transition_',
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

        Args:
            value (int): value for IDD Field `Month`
                value >= 1
                value <= 12

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
        """field `Day of Month` must be valid for Month field.

        Args:
            value (int): value for IDD Field `Day of Month`
                value >= 1
                value <= 31

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
        """field `Day Type` Day Type selects the schedules appropriate for this
        design day.

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
        This field is required when field "Dry-Bulb Temperature Range Modifier Type"
        is not "TemperatureProfileSchedule".

        Args:
            value (float): value for IDD Field `Maximum Dry-Bulb Temperature`
                Units: C
                value >= -90.0
                value <= 70.0

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
        Must still produce appropriate maximum dry bulb (within range)
        This field is not needed if Dry-Bulb Temperature Range Modifier Type
        is "delta".

        Args:
            value (float): value for IDD Field `Daily Dry-Bulb Temperature Range`
                Units: deltaC

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
        Type of modifier to the dry-bulb temperature calculated for the timestep

        Args:
            value (str): value for IDD Field `Dry-Bulb Temperature Range Modifier Type`
                Default value: DefaultMultipliers

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
        Only used when previous field is "MultiplierSchedule", "DifferenceSchedule" or
        "TemperatureProfileSchedule".
        For type "MultiplierSchedule"  the hour/time interval values should specify
        the fraction (0-1) of the dry-bulb temperature range to be subtracted
        from the maximum dry-bulb temperature for each timestep in the day
        For type "DifferenceSchedule" the values should specify a number to be subtracted
        from the maximum dry-bulb temperature for each timestep in the day.
        Note that numbers in the difference schedule cannot be negative as that
        would result in a higher maximum than the maximum previously specified.
        For type "TemperatureProfileSchedule" the values should specify the actual drybulb
        temperature for each timestep in the day.

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
        """field `Humidity Condition Type` values/schedules indicated here and
        in subsequent fields create the humidity values in the 24 hour design
        day conditions profile.

        Args:
            value (str): value for IDD Field `Humidity Condition Type`
                Default value: WetBulb

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
        Wetbulb or dewpoint temperature coincident with the maximum temperature.
        Required only if field Humidity Condition Type is "Wetbulb", "Dewpoint",
        "WetBulbProfileMultiplierSchedule", "WetBulbProfileDifferenceSchedule",
        or "WetBulbProfileDefaultMultipliers"

        Args:
            value (float): value for IDD Field `Wetbulb or DewPoint at Maximum Dry-Bulb`
                Units: C

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
        Only used when Humidity Condition Type is "RelativeHumiditySchedule",
        "WetBulbProfileMultiplierSchedule", or "WetBulbProfileDifferenceSchedule"
        For type "RelativeHumiditySchedule", the hour/time interval values should specify
        relative humidity (percent) from 0.0 to 100.0.
        For type "WetBulbProfileMultiplierSchedule" the hour/time interval values should specify
        the fraction (0-1) of the wet-bulb temperature range to be subtracted from the
        maximum wet-bulb temperature for each timestep in the day (units = Fraction)
        For type "WetBulbProfileDifferenceSchedule" the values should specify a number to be subtracted
        from the maximum wet-bulb temperature for each timestep in the day. (units = deltaC)

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
        Humidity ratio coincident with the maximum temperature (constant humidity ratio throughout day).
        Required only if field Humidity Condition Type is "HumidityRatio".

        Args:
            value (float): value for IDD Field `Humidity Ratio at Maximum Dry-Bulb`
                Units: kgWater/kgDryAir

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
    def enthalpy_at_maximum_drybulb_will_require_units_transition_(self):
        """field `Enthalpy at Maximum Dry-Bulb  !will require units transition.`
        Enthalpy coincident with the maximum temperature.
        Required only if field Humidity Condition Type is "Enthalpy".

        Args:
            value (float): value for IDD Field `Enthalpy at Maximum Dry-Bulb  !will require units transition.`
                Units: J/kg

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `enthalpy_at_maximum_drybulb_will_require_units_transition_` or None if not set
        """
        return self[
            "Enthalpy at Maximum Dry-Bulb  !will require units transition."]

    @enthalpy_at_maximum_drybulb_will_require_units_transition_.setter
    def enthalpy_at_maximum_drybulb_will_require_units_transition_(
            self,
            value=None):
        """  Corresponds to IDD field `Enthalpy at Maximum Dry-Bulb  !will require units transition.`

        """
        self[
            "Enthalpy at Maximum Dry-Bulb  !will require units transition."] = value

    @property
    def daily_wetbulb_temperature_range(self):
        """field `Daily Wet-Bulb Temperature Range`
        Required only if Humidity Condition Type = "WetbulbProfileMultiplierSchedule" or
        "WetBulbProfileDefaultMultipliers"

        Args:
            value (float): value for IDD Field `Daily Wet-Bulb Temperature Range`
                Units: deltaC

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
        """field `Barometric Pressure` This field's value is also checked
        against the calculated "standard barometric pressure" for the location.
        If out of range (>10%) or blank, then is replaced by standard value.

        Args:
            value (float): value for IDD Field `Barometric Pressure`
                Units: Pa
                IP-Units: inHg
                value >= 31000.0
                value <= 120000.0

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

        Args:
            value (float): value for IDD Field `Wind Speed`
                Units: m/s
                IP-Units: miles/hr
                value <= 40.0

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
        North=0.0 East=90.0
        0 and 360 are the same direction.

        Args:
            value (float): value for IDD Field `Wind Direction`
                Units: deg
                value <= 360.0

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
        """field `Rain Indicator` Yes is raining (all day), No is not raining.

        Args:
            value (str): value for IDD Field `Rain Indicator`
                Default value: No

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
        """field `Snow Indicator` Yes is Snow on Ground, No is no Snow on
        Ground.

        Args:
            value (str): value for IDD Field `Snow Indicator`
                Default value: No

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
        Yes -- use schedules modified for Daylight Saving Time Schedules.
        No - do not use schedules modified for Daylight Saving Time Schedules

        Args:
            value (str): value for IDD Field `Daylight Saving Time Indicator`
                Default value: No

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

        Args:
            value (str): value for IDD Field `Solar Model Indicator`
                Default value: ASHRAEClearSky

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
        if Solar Model Indicator = Schedule, then beam schedule name (for day)

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
        if Solar Model Indicator = Schedule, then diffuse schedule name (for day)

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
        Required if Solar Model Indicator = ASHRAETau

        Args:
            value (float): value for IDD Field `ASHRAE Clear Sky Optical Depth for Beam Irradiance (taub)`
                Units: dimensionless
                value <= 1.2

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
        Required if Solar Model Indicator = ASHRAETau

        Args:
            value (float): value for IDD Field `ASHRAE Clear Sky Optical Depth for Diffuse Irradiance (taud)`
                Units: dimensionless
                value <= 3.0

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
        Used if Sky Model Indicator = ASHRAEClearSky or ZhangHuang
        0.0 is totally unclear, 1.0 is totally clear

        Args:
            value (float): value for IDD Field `Sky Clearness`
                value <= 1.2

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
        """field `Name` user supplied name for reporting.

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

        Args:
            value (int): value for IDD Field `Begin Month`
                value >= 1
                value <= 12

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

        Args:
            value (int): value for IDD Field `Begin Day of Month`
                value >= 1
                value <= 31

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

        Args:
            value (int): value for IDD Field `End Month`
                value >= 1
                value <= 12

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

        Args:
            value (int): value for IDD Field `End Day of Month`
                value >= 1
                value <= 31

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

        =[|Sunday|Monday|Tuesday|Wednesday|Thursday|Friday|Saturday|SummerDesignDay|WinterDesignDay|
        |CustomDay1|CustomDay2];
        if you use SummerDesignDay or WinterDesignDay or the CustomDays then this will apply
        to the whole period; other days (i.e., Monday) will signify a start day and
        normal sequence ofsubsequent days

        Args:
            value (str): value for IDD Field `Day of Week for Start Day`
                Default value: Monday

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
        """field `Use Weather File Daylight Saving Period` If yes or blank, use
        daylight saving period as specified on Weatherfile. If no, do not use
        the daylight saving period as specified on the Weatherfile.

        Args:
            value (str): value for IDD Field `Use Weather File Daylight Saving Period`
                Default value: Yes

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

        Args:
            value (str): value for IDD Field `Use Weather File Rain and Snow Indicators`
                Default value: Yes

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
        """field `Name` user supplied name for reporting.

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
        """field `Period Selection` Following is a list of all possible types
        of Extreme and Typical periods that might be identified in the Weather
        File. Not all possible types are available for all weather files.

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

        =[|Sunday|Monday|Tuesday|Wednesday|Thursday|Friday|Saturday|SummerDesignDay|WinterDesignDay|
        |CustomDay1|CustomDay2];
        if you use SummerDesignDay or WinterDesignDay or the CustomDays then this will apply
        to the whole period; other days (i.e., Monday) will signify a start day and
        normal sequence ofsubsequent days

        Args:
            value (str): value for IDD Field `Day of Week for Start Day`
                Default value: Monday

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
        """field `Use Weather File Daylight Saving Period` If yes or blank, use
        daylight saving period as specified on Weatherfile. If no, do not use
        the daylight saving period as specified on the Weatherfile.

        Args:
            value (str): value for IDD Field `Use Weather File Daylight Saving Period`
                Default value: Yes

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

        Args:
            value (str): value for IDD Field `Use Weather File Rain and Snow Indicators`
                Default value: Yes

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
        """field `Name` descriptive name (used in reporting mainly) if blank,
        weather file title is used.  if not blank, must be unique.

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

        Args:
            value (int): value for IDD Field `Begin Month`
                value >= 1
                value <= 12

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

        Args:
            value (int): value for IDD Field `Begin Day of Month`
                value >= 1
                value <= 31

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

        Args:
            value (int): value for IDD Field `End Month`
                value >= 1
                value <= 12

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

        Args:
            value (int): value for IDD Field `End Day of Month`
                value >= 1
                value <= 31

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

        =<blank - use WeatherFile>|Sunday|Monday|Tuesday|Wednesday|Thursday|Friday|Saturday];

        Args:
            value (str): value for IDD Field `Day of Week for Start Day`
                Default value: UseWeatherFile

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
        If yes or blank, use holidays as specified on Weatherfile.
        If no, do not use the holidays specified on the Weatherfile.
        Note: You can still specify holidays/special days using the RunPeriodControl:SpecialDays object(s).

        Args:
            value (str): value for IDD Field `Use Weather File Holidays and Special Days`
                Default value: Yes

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
        """field `Use Weather File Daylight Saving Period` If yes or blank, use
        daylight saving period as specified on Weatherfile. If no, do not use
        the daylight saving period as specified on the Weatherfile.

        Args:
            value (str): value for IDD Field `Use Weather File Daylight Saving Period`
                Default value: Yes

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
        """field `Apply Weekend Holiday Rule` if yes and single day holiday
        falls on weekend, "holiday" occurs on following Monday.

        Args:
            value (str): value for IDD Field `Apply Weekend Holiday Rule`
                Default value: No

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

        Args:
            value (str): value for IDD Field `Use Weather File Rain Indicators`
                Default value: Yes

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

        Args:
            value (str): value for IDD Field `Use Weather File Snow Indicators`
                Default value: Yes

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

        Args:
            value (int): value for IDD Field `Number of Times Runperiod to be Repeated`
                Default value: 1
                value >= 1

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

        Args:
            value (str): value for IDD Field `Increment Day of Week on repeat`
                Default value: Yes

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
        this is the start year for the start date.  If the leap year is "Yes" in the weather file header
        (that is HOLIDAYS/SPECIAL DAYS header first field), then any year which is a leap year will assume
        there will be a Feb 29. A repeat of this runperiod will automatically increment the year.

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
        """field `Name` descriptive name (used in reporting mainly) if blank,
        weather file title is used.  if not blank, must be unique.

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

        Args:
            value (int): value for IDD Field `Begin Month`
                value >= 1
                value <= 12

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

        Args:
            value (int): value for IDD Field `Begin Day of Month`
                value >= 1
                value <= 31

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
        """field `Begin Year` must be start year of this date on weather file.

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

        Args:
            value (int): value for IDD Field `End Month`
                value >= 1
                value <= 12

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

        Args:
            value (int): value for IDD Field `End Day of Month`
                value >= 1
                value <= 31

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
        """field `End Year` must be end year of this date on weather file.

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

        =<blank - use WeatherFile>|Sunday|Monday|Tuesday|Wednesday|Thursday|Friday|Saturday];

        Args:
            value (str): value for IDD Field `Day of Week for Start Day`
                Default value: UseWeatherFile

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
        If yes or blank, use holidays as specified on Weatherfile.
        If no, do not use the holidays specified on the Weatherfile.
        Note: You can still specify holidays/special days using the RunPeriodControl:SpecialDays object(s).

        Args:
            value (str): value for IDD Field `Use Weather File Holidays and Special Days`
                Default value: Yes

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
        """field `Use Weather File Daylight Saving Period` If yes or blank, use
        daylight saving period as specified on Weatherfile. If no, do not use
        the daylight saving period as specified on the Weatherfile.

        Args:
            value (str): value for IDD Field `Use Weather File Daylight Saving Period`
                Default value: Yes

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
        """field `Apply Weekend Holiday Rule` if yes and single day holiday
        falls on weekend, "holiday" occurs on following Monday.

        Args:
            value (str): value for IDD Field `Apply Weekend Holiday Rule`
                Default value: No

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

        Args:
            value (str): value for IDD Field `Use Weather File Rain Indicators`
                Default value: Yes

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

        Args:
            value (str): value for IDD Field `Use Weather File Snow Indicators`
                Default value: Yes

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
        Dates can be several formats:
        <number>/<number>  (month/day)
        <number> <Month>
        <Month> <number>
        <Nth> <Weekday> in <Month)
        Last <WeekDay> in <Month>
        <Month> can be January, February, March, April, May, June, July, August, September, October, November, December
        Months can be the first 3 letters of the month
        <Weekday> can be Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday
        <Nth> can be 1 or 1st, 2 or 2nd, etc. up to 5(?)

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

        Args:
            value (float): value for IDD Field `Duration`
                Units: days
                Default value: 1.0
                value >= 1.0
                value <= 366.0

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
        """field `Special Day Type` Special Day Type selects the schedules
        appropriate for each day so labeled.

        Args:
            value (str): value for IDD Field `Special Day Type`
                Default value: Holiday

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
        Dates can be several formats:
        <number>/<number>  (month/day)
        <number> <Month>
        <Month> <number>
        <Nth> <Weekday> in <Month)
        Last <WeekDay> in <Month>
        <Month> can be January, February, March, April, May, June, July, August, September, October, November, December
        Months can be the first 3 letters of the month
        <Weekday> can be Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday
        <Nth> can be 1 or 1st, 2 or 2nd, etc. up to 5(?)

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
        blank in this field will apply to all run periods (that is, all objects=
        SizingPeriod:WeatherFileDays, SizingPeriod:WeatherFileConditionType or RunPeriod
        otherwise, this name must match one of the environment object names.

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
        if name matches a SizingPeriod:DesignDay, put in a day schedule of this name
        if name is for a SizingPeriod:WeatherFileDays, SizingPeriod:WeatherFileConditionType or
        RunPeriod, put in a full year schedule that covers the appropriate days.

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

        Args:
            value (float): value for IDD Field `Wind Sensor Height Above Ground`
                Units: m
                Default value: 10.0

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

        Args:
            value (float): value for IDD Field `Wind Speed Profile Exponent`
                Default value: 0.14

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

        Args:
            value (float): value for IDD Field `Wind Speed Profile Boundary Layer Thickness`
                Units: m
                Default value: 270.0

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

        Args:
            value (float): value for IDD Field `Air Temperature Sensor Height Above Ground`
                Units: m
                Default value: 1.5

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
        """field `Wind Speed Profile Exponent` Set to zero for no wind speed
        dependence on height.

        Args:
            value (float): value for IDD Field `Wind Speed Profile Exponent`
                Default value: 0.22

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

        Args:
            value (float): value for IDD Field `Wind Speed Profile Boundary Layer Thickness`
                Units: m
                Default value: 370.0

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
        """field `Air Temperature Gradient Coefficient` Set to zero for no air
        temperature dependence on height.

        Args:
            value (float): value for IDD Field `Air Temperature Gradient Coefficient`
                Units: K/m
                Default value: 0.0065

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

        Args:
            value (float): value for IDD Field `January Ground Temperature`
                Units: C
                Default value: 18.0

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

        Args:
            value (float): value for IDD Field `February Ground Temperature`
                Units: C
                Default value: 18.0

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

        Args:
            value (float): value for IDD Field `March Ground Temperature`
                Units: C
                Default value: 18.0

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

        Args:
            value (float): value for IDD Field `April Ground Temperature`
                Units: C
                Default value: 18.0

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

        Args:
            value (float): value for IDD Field `May Ground Temperature`
                Units: C
                Default value: 18.0

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

        Args:
            value (float): value for IDD Field `June Ground Temperature`
                Units: C
                Default value: 18.0

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

        Args:
            value (float): value for IDD Field `July Ground Temperature`
                Units: C
                Default value: 18.0

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

        Args:
            value (float): value for IDD Field `August Ground Temperature`
                Units: C
                Default value: 18.0

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

        Args:
            value (float): value for IDD Field `September Ground Temperature`
                Units: C
                Default value: 18.0

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

        Args:
            value (float): value for IDD Field `October Ground Temperature`
                Units: C
                Default value: 18.0

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

        Args:
            value (float): value for IDD Field `November Ground Temperature`
                Units: C
                Default value: 18.0

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

        Args:
            value (float): value for IDD Field `December Ground Temperature`
                Units: C
                Default value: 18.0

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

        Args:
            value (float): value for IDD Field `January Ground Temperature`
                Units: C
                Default value: 13.0

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

        Args:
            value (float): value for IDD Field `February Ground Temperature`
                Units: C
                Default value: 13.0

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

        Args:
            value (float): value for IDD Field `March Ground Temperature`
                Units: C
                Default value: 13.0

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

        Args:
            value (float): value for IDD Field `April Ground Temperature`
                Units: C
                Default value: 13.0

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

        Args:
            value (float): value for IDD Field `May Ground Temperature`
                Units: C
                Default value: 13.0

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

        Args:
            value (float): value for IDD Field `June Ground Temperature`
                Units: C
                Default value: 13.0

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

        Args:
            value (float): value for IDD Field `July Ground Temperature`
                Units: C
                Default value: 13.0

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

        Args:
            value (float): value for IDD Field `August Ground Temperature`
                Units: C
                Default value: 13.0

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

        Args:
            value (float): value for IDD Field `September Ground Temperature`
                Units: C
                Default value: 13.0

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

        Args:
            value (float): value for IDD Field `October Ground Temperature`
                Units: C
                Default value: 13.0

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

        Args:
            value (float): value for IDD Field `November Ground Temperature`
                Units: C
                Default value: 13.0

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

        Args:
            value (float): value for IDD Field `December Ground Temperature`
                Units: C
                Default value: 13.0

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

        Args:
            value (float): value for IDD Field `January Surface Ground Temperature`
                Units: C
                Default value: 13.0

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

        Args:
            value (float): value for IDD Field `February Surface Ground Temperature`
                Units: C
                Default value: 13.0

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

        Args:
            value (float): value for IDD Field `March Surface Ground Temperature`
                Units: C
                Default value: 13.0

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

        Args:
            value (float): value for IDD Field `April Surface Ground Temperature`
                Units: C
                Default value: 13.0

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

        Args:
            value (float): value for IDD Field `May Surface Ground Temperature`
                Units: C
                Default value: 13.0

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

        Args:
            value (float): value for IDD Field `June Surface Ground Temperature`
                Units: C
                Default value: 13.0

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

        Args:
            value (float): value for IDD Field `July Surface Ground Temperature`
                Units: C
                Default value: 13.0

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

        Args:
            value (float): value for IDD Field `August Surface Ground Temperature`
                Units: C
                Default value: 13.0

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

        Args:
            value (float): value for IDD Field `September Surface Ground Temperature`
                Units: C
                Default value: 13.0

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

        Args:
            value (float): value for IDD Field `October Surface Ground Temperature`
                Units: C
                Default value: 13.0

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

        Args:
            value (float): value for IDD Field `November Surface Ground Temperature`
                Units: C
                Default value: 13.0

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

        Args:
            value (float): value for IDD Field `December Surface Ground Temperature`
                Units: C
                Default value: 13.0

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

        Args:
            value (float): value for IDD Field `January Deep Ground Temperature`
                Units: C
                Default value: 16.0

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

        Args:
            value (float): value for IDD Field `February Deep Ground Temperature`
                Units: C
                Default value: 16.0

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

        Args:
            value (float): value for IDD Field `March Deep Ground Temperature`
                Units: C
                Default value: 16.0

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

        Args:
            value (float): value for IDD Field `April Deep Ground Temperature`
                Units: C
                Default value: 16.0

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

        Args:
            value (float): value for IDD Field `May Deep Ground Temperature`
                Units: C
                Default value: 16.0

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

        Args:
            value (float): value for IDD Field `June Deep Ground Temperature`
                Units: C
                Default value: 16.0

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

        Args:
            value (float): value for IDD Field `July Deep Ground Temperature`
                Units: C
                Default value: 16.0

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

        Args:
            value (float): value for IDD Field `August Deep Ground Temperature`
                Units: C
                Default value: 16.0

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

        Args:
            value (float): value for IDD Field `September Deep Ground Temperature`
                Units: C
                Default value: 16.0

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

        Args:
            value (float): value for IDD Field `October Deep Ground Temperature`
                Units: C
                Default value: 16.0

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

        Args:
            value (float): value for IDD Field `November Deep Ground Temperature`
                Units: C
                Default value: 16.0

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

        Args:
            value (float): value for IDD Field `December Deep Ground Temperature`
                Units: C
                Default value: 16.0

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




class SiteGroundDomain(DataObject):

    """ Corresponds to IDD object `Site:GroundDomain`
        Ground coupled slab model for on-grade and
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
                                        'minimum>': 0.0,
                                        'required-field': True,
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
                                        'minimum>': 0.0,
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'm'}),
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
                                      (u'kusuda-achenbach average surface temperature',
                                       {'name': u'Kusuda-Achenbach Average Surface Temperature',
                                        'pyname': u'kusudaachenbach_average_surface_temperature',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'C'}),
                                      (u'kusuda-achenbach average amplitude of surface temperature',
                                       {'name': u'Kusuda-Achenbach Average Amplitude of Surface Temperature',
                                        'pyname': u'kusudaachenbach_average_amplitude_of_surface_temperature',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'deltaC'}),
                                      (u'kusuda-achenbach phase shift of minimum surface temperature',
                                       {'name': u'Kusuda-Achenbach Phase Shift of Minimum Surface Temperature',
                                        'pyname': u'kusudaachenbach_phase_shift_of_minimum_surface_temperature',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'days'}),
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
                                        'required-field': True,
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
                                        'required-field': True,
                                        'autosizable': False,
                                        'accepted-values': [u'Hourly',
                                                            u'Timestep'],
                                        'autocalculatable': False,
                                        'type': 'alpha'})]),
               'format': None,
               'group': u'Location and Climate',
               'min-fields': 0,
               'name': u'Site:GroundDomain',
               'pyname': u'SiteGroundDomain',
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

        Args:
            value (float): value for IDD Field `Ground Domain Depth`
                Units: m

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `ground_domain_depth` or None if not set

        """
        return self["Ground Domain Depth"]

    @ground_domain_depth.setter
    def ground_domain_depth(self, value=None):
        """Corresponds to IDD field `Ground Domain Depth`"""
        self["Ground Domain Depth"] = value

    @property
    def aspect_ratio(self):
        """field `Aspect Ratio`

        Args:
            value (float): value for IDD Field `Aspect Ratio`
                Default value: 1.0

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

        Args:
            value (float): value for IDD Field `Perimeter Offset`
                Units: m

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `perimeter_offset` or None if not set

        """
        return self["Perimeter Offset"]

    @perimeter_offset.setter
    def perimeter_offset(self, value=None):
        """Corresponds to IDD field `Perimeter Offset`"""
        self["Perimeter Offset"] = value

    @property
    def soil_thermal_conductivity(self):
        """field `Soil Thermal Conductivity`

        Args:
            value (float): value for IDD Field `Soil Thermal Conductivity`
                Units: W/m-K

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

        Args:
            value (float): value for IDD Field `Soil Density`
                Units: kg/m3

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

        Args:
            value (float): value for IDD Field `Soil Specific Heat`
                Units: J/kg-K

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

        Args:
            value (float): value for IDD Field `Soil Moisture Content Volume Fraction`
                Units: percent
                Default value: 30.0
                value <= 100.0

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

        Args:
            value (float): value for IDD Field `Soil Moisture Content Volume Fraction at Saturation`
                Units: percent
                Default value: 50.0
                value <= 100.0

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
    def kusudaachenbach_average_surface_temperature(self):
        """field `Kusuda-Achenbach Average Surface Temperature`
        Annual average surface temperature.

        Args:
            value (float): value for IDD Field `Kusuda-Achenbach Average Surface Temperature`
                Units: C

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `kusudaachenbach_average_surface_temperature` or None if not set
        """
        return self["Kusuda-Achenbach Average Surface Temperature"]

    @kusudaachenbach_average_surface_temperature.setter
    def kusudaachenbach_average_surface_temperature(self, value=None):
        """  Corresponds to IDD field `Kusuda-Achenbach Average Surface Temperature`

        """
        self["Kusuda-Achenbach Average Surface Temperature"] = value

    @property
    def kusudaachenbach_average_amplitude_of_surface_temperature(self):
        """field `Kusuda-Achenbach Average Amplitude of Surface Temperature`
        Annual average surface temperature variation from average.

        Args:
            value (float): value for IDD Field `Kusuda-Achenbach Average Amplitude of Surface Temperature`
                Units: deltaC

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `kusudaachenbach_average_amplitude_of_surface_temperature` or None if not set
        """
        return self[
            "Kusuda-Achenbach Average Amplitude of Surface Temperature"]

    @kusudaachenbach_average_amplitude_of_surface_temperature.setter
    def kusudaachenbach_average_amplitude_of_surface_temperature(
            self,
            value=None):
        """  Corresponds to IDD field `Kusuda-Achenbach Average Amplitude of Surface Temperature`

        """
        self[
            "Kusuda-Achenbach Average Amplitude of Surface Temperature"] = value

    @property
    def kusudaachenbach_phase_shift_of_minimum_surface_temperature(self):
        """field `Kusuda-Achenbach Phase Shift of Minimum Surface Temperature`
        The phase shift of minimum surface temperature, or the day
        of the year when the minimum surface temperature occurs.

        Args:
            value (float): value for IDD Field `Kusuda-Achenbach Phase Shift of Minimum Surface Temperature`
                Units: days

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `kusudaachenbach_phase_shift_of_minimum_surface_temperature` or None if not set
        """
        return self[
            "Kusuda-Achenbach Phase Shift of Minimum Surface Temperature"]

    @kusudaachenbach_phase_shift_of_minimum_surface_temperature.setter
    def kusudaachenbach_phase_shift_of_minimum_surface_temperature(
            self,
            value=None):
        """  Corresponds to IDD field `Kusuda-Achenbach Phase Shift of Minimum Surface Temperature`

        """
        self[
            "Kusuda-Achenbach Phase Shift of Minimum Surface Temperature"] = value

    @property
    def evapotranspiration_ground_cover_parameter(self):
        """field `Evapotranspiration Ground Cover Parameter`
        This specifies the ground cover effects during evapotranspiration
        calculations.  The value roughly represents the following cases:
        = 0   : concrete or other solid, non-permeable ground surface material
        = 0.5 : short grass, much like a manicured lawn
        = 1   : standard reference state (12 cm grass)
        = 1.5 : wild growth

        Args:
            value (float): value for IDD Field `Evapotranspiration Ground Cover Parameter`
                Default value: 0.4
                value <= 1.5

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
        This field specifies whether the slab is located "in-grade" or "on-grade"

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
        Only applicable for the in-grade case

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
        This field specifies the presence of insulation beneath the slab.
        Only required for in-grade case.

        Args:
            value (str): value for IDD Field `Horizontal Insulation`
                Default value: No

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
        """field `Horizontal Insulation Material Name` This field specifies the
        horizontal insulation material.

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
        """field `Horizontal Insulation Extents` This field specifies whether
        the horizontal insulation fully insulates the surface or is perimeter
        only insulation.

        Args:
            value (str): value for IDD Field `Horizontal Insulation Extents`
                Default value: Full

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
        """field `Perimeter Insulation Width` This field specifies the width of
        the underfloor perimeter insulation.

        Args:
            value (float): value for IDD Field `Perimeter Insulation Width`
                Units: m

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
        """field `Vertical Insulation` This field specifies the presence of
        vertical insulation at the slab edge.

        Args:
            value (str): value for IDD Field `Vertical Insulation`
                Default value: No

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
        """field `Vertical Insulation Material Name` This field specifies the
        vertical insulation material.

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
        """field `Vertical Insulation Depth` Only used when including vertical
        insulation This field specifies the depth of the vertical insulation.

        Args:
            value (float): value for IDD Field `Vertical Insulation Depth`
                Units: m

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
        """field `Simulation Timestep` This field specifies the domain
        simulation timestep.

        Args:
            value (str): value for IDD Field `Simulation Timestep`
                Default value: Hourly

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

        Args:
            value (float): value for IDD Field `January Ground Reflectance`
                Units: dimensionless
                Default value: 0.2
                value <= 1.0

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

        Args:
            value (float): value for IDD Field `February Ground Reflectance`
                Units: dimensionless
                Default value: 0.2
                value <= 1.0

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

        Args:
            value (float): value for IDD Field `March Ground Reflectance`
                Units: dimensionless
                Default value: 0.2
                value <= 1.0

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

        Args:
            value (float): value for IDD Field `April Ground Reflectance`
                Units: dimensionless
                Default value: 0.2
                value <= 1.0

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

        Args:
            value (float): value for IDD Field `May Ground Reflectance`
                Units: dimensionless
                Default value: 0.2
                value <= 1.0

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

        Args:
            value (float): value for IDD Field `June Ground Reflectance`
                Units: dimensionless
                Default value: 0.2
                value <= 1.0

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

        Args:
            value (float): value for IDD Field `July Ground Reflectance`
                Units: dimensionless
                Default value: 0.2
                value <= 1.0

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

        Args:
            value (float): value for IDD Field `August Ground Reflectance`
                Units: dimensionless
                Default value: 0.2
                value <= 1.0

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

        Args:
            value (float): value for IDD Field `September Ground Reflectance`
                Units: dimensionless
                Default value: 0.2
                value <= 1.0

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

        Args:
            value (float): value for IDD Field `October Ground Reflectance`
                Units: dimensionless
                Default value: 0.2
                value <= 1.0

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

        Args:
            value (float): value for IDD Field `November Ground Reflectance`
                Units: dimensionless
                Default value: 0.2
                value <= 1.0

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

        Args:
            value (float): value for IDD Field `December Ground Reflectance`
                Units: dimensionless
                Default value: 0.2
                value <= 1.0

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
        Value for modifying the "normal" ground reflectance when Snow is on ground
        when calculating the "Ground Reflected Solar Radiation Value"
        a value of 1.0 here uses the "normal" ground reflectance
        Ground Reflected Solar = (BeamSolar*CosSunZenith + DiffuseSolar)*GroundReflectance
        This would be further modified by the Snow Ground Reflectance Modifier when Snow was on the ground
        When Snow on ground, effective GroundReflectance is normal GroundReflectance*"Ground Reflectance Snow Modifier"
        Ground Reflectance achieved in this manner will be restricted to [0.0,1.0]

        Args:
            value (float): value for IDD Field `Ground Reflected Solar Modifier`
                Default value: 1.0

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
        Value for modifying the "normal" daylighting ground reflectance when Snow is on ground
        when calculating the "Ground Reflected Solar Radiation Value"
        a value of 1.0 here uses the "normal" ground reflectance
        Ground Reflected Solar = (BeamSolar*CosSunZenith + DiffuseSolar)*GroundReflectance
        This would be further modified by the Snow Ground Reflectance Modifier when Snow was on the ground
        When Snow on ground, effective GroundReflectance is normal GroundReflectance*"Daylighting Ground Reflectance Snow Modifier"
        Ground Reflectance achieved in this manner will be restricted to [0.0,1.0]

        Args:
            value (float): value for IDD Field `Daylighting Ground Reflected Solar Modifier`
                Default value: 1.0

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

        Args:
            value (float): value for IDD Field `Annual Average Outdoor Air Temperature`
                Units: C

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

        Args:
            value (float): value for IDD Field `Maximum Difference In Monthly Average Outdoor Air Temperatures`
                Units: deltaC

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
        """field `Design Level for Total Annual Precipitation` meters of water
        per year used for design level.

        Args:
            value (float): value for IDD Field `Design Level for Total Annual Precipitation`
                Units: m/yr

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
        Schedule values in meters of water per hour
        values should be non-negative

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
        """field `Average Total Annual Precipitation` meters of water per year
        from average weather statistics.

        Args:
            value (float): value for IDD Field `Average Total Annual Precipitation`
                Units: m/yr

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
        """field `Irrigation Model Type` SmartSchedule will not allow
        irrigation when soil is already moist. Current threshold set at 30% of
        saturation.

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
        Schedule values in meters of water per hour
        values should be non-negative

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
        """field `Irrigation Maximum Saturation Threshold` Used with
        SmartSchedule to set the saturation level at which no irrigation is
        allowed.

        Args:
            value (float): value for IDD Field `Irrigation Maximum Saturation Threshold`
                Units: percent
                Default value: 40.0
                value <= 100.0

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
                                        'type': u'alpha'}),
                                      (u'visible spectrum data object name',
                                       {'name': u'Visible Spectrum Data Object Name',
                                        'pyname': u'visible_spectrum_data_object_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'alpha'})]),
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
        """field `Spectrum Data Method` The method specifies which of the solar
        and visible spectrum data to use in the calculations.

        Choices: Default - existing hard-wired spectrum data in EnergyPlus.
        UserDefined - user specified spectrum data referenced by the next two fields

        Args:
            value (str): value for IDD Field `Spectrum Data Method`
                Default value: Default

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




class SiteSpectrumData(DataObject):

    """ Corresponds to IDD object `Site:SpectrumData`
        Spectrum Data Type is followed by up to 107 sets of normal-incidence measured values of
        [wavelength, spectrum] for wavelengths covering the solar (0.25 to 2.5 microns) or visible
        spectrum (0.38 to 0.78 microns)
    """
    _schema = {'extensible-fields': OrderedDict(),
               'fields': OrderedDict([(u'name',
                                       {'name': u'Name',
                                        'pyname': u'name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'alpha'}),
                                      (u'spectrum data type',
                                       {'name': u'Spectrum Data Type',
                                        'pyname': u'spectrum_data_type',
                                        'required-field': True,
                                        'autosizable': False,
                                        'accepted-values': [u'Solar',
                                                            u'Visible'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'wavelength 1',
                                       {'name': u'Wavelength 1',
                                        'pyname': u'wavelength_1',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'micron'}),
                                      (u'spectrum 1',
                                       {'name': u'Spectrum 1',
                                        'pyname': u'spectrum_1',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'wavelength 2',
                                       {'name': u'Wavelength 2',
                                        'pyname': u'wavelength_2',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'micron'}),
                                      (u'spectrum 2',
                                       {'name': u'Spectrum 2',
                                        'pyname': u'spectrum_2',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'wavelength 3',
                                       {'name': u'Wavelength 3',
                                        'pyname': u'wavelength_3',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'micron'}),
                                      (u'spectrum 3',
                                       {'name': u'Spectrum 3',
                                        'pyname': u'spectrum_3',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'wavelength 4',
                                       {'name': u'Wavelength 4',
                                        'pyname': u'wavelength_4',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'micron'}),
                                      (u'spectrum 4',
                                       {'name': u'Spectrum 4',
                                        'pyname': u'spectrum_4',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'wavelength 5',
                                       {'name': u'Wavelength 5',
                                        'pyname': u'wavelength_5',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'micron'}),
                                      (u'spectrum 5',
                                       {'name': u'Spectrum 5',
                                        'pyname': u'spectrum_5',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'wavelength 6',
                                       {'name': u'Wavelength 6',
                                        'pyname': u'wavelength_6',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'micron'}),
                                      (u'spectrum 6',
                                       {'name': u'Spectrum 6',
                                        'pyname': u'spectrum_6',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'wavelength 7',
                                       {'name': u'Wavelength 7',
                                        'pyname': u'wavelength_7',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'micron'}),
                                      (u'spectrum 7',
                                       {'name': u'Spectrum 7',
                                        'pyname': u'spectrum_7',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'wavelength 8',
                                       {'name': u'Wavelength 8',
                                        'pyname': u'wavelength_8',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'micron'}),
                                      (u'spectrum 8',
                                       {'name': u'Spectrum 8',
                                        'pyname': u'spectrum_8',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'wavelength 9',
                                       {'name': u'Wavelength 9',
                                        'pyname': u'wavelength_9',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'micron'}),
                                      (u'spectrum 9',
                                       {'name': u'Spectrum 9',
                                        'pyname': u'spectrum_9',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'wavelength 10',
                                       {'name': u'Wavelength 10',
                                        'pyname': u'wavelength_10',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'micron'}),
                                      (u'spectrum 10',
                                       {'name': u'Spectrum 10',
                                        'pyname': u'spectrum_10',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'wavelength 11',
                                       {'name': u'Wavelength 11',
                                        'pyname': u'wavelength_11',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'micron'}),
                                      (u'spectrum 11',
                                       {'name': u'Spectrum 11',
                                        'pyname': u'spectrum_11',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'wavelength 12',
                                       {'name': u'Wavelength 12',
                                        'pyname': u'wavelength_12',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'micron'}),
                                      (u'spectrum 12',
                                       {'name': u'Spectrum 12',
                                        'pyname': u'spectrum_12',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'wavelength 13',
                                       {'name': u'Wavelength 13',
                                        'pyname': u'wavelength_13',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'micron'}),
                                      (u'spectrum 13',
                                       {'name': u'Spectrum 13',
                                        'pyname': u'spectrum_13',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'wavelength 14',
                                       {'name': u'Wavelength 14',
                                        'pyname': u'wavelength_14',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'micron'}),
                                      (u'spectrum 14',
                                       {'name': u'Spectrum 14',
                                        'pyname': u'spectrum_14',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'wavelength 15',
                                       {'name': u'Wavelength 15',
                                        'pyname': u'wavelength_15',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'micron'}),
                                      (u'spectrum 15',
                                       {'name': u'Spectrum 15',
                                        'pyname': u'spectrum_15',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'wavelength 16',
                                       {'name': u'Wavelength 16',
                                        'pyname': u'wavelength_16',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'micron'}),
                                      (u'spectrum 16',
                                       {'name': u'Spectrum 16',
                                        'pyname': u'spectrum_16',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'wavelength 17',
                                       {'name': u'Wavelength 17',
                                        'pyname': u'wavelength_17',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'micron'}),
                                      (u'spectrum 17',
                                       {'name': u'Spectrum 17',
                                        'pyname': u'spectrum_17',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'wavelength 18',
                                       {'name': u'Wavelength 18',
                                        'pyname': u'wavelength_18',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'micron'}),
                                      (u'spectrum 18',
                                       {'name': u'Spectrum 18',
                                        'pyname': u'spectrum_18',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'wavelength 19',
                                       {'name': u'Wavelength 19',
                                        'pyname': u'wavelength_19',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'micron'}),
                                      (u'spectrum 19',
                                       {'name': u'Spectrum 19',
                                        'pyname': u'spectrum_19',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'wavelength 20',
                                       {'name': u'Wavelength 20',
                                        'pyname': u'wavelength_20',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'micron'}),
                                      (u'spectrum 20',
                                       {'name': u'Spectrum 20',
                                        'pyname': u'spectrum_20',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'wavelength 21',
                                       {'name': u'Wavelength 21',
                                        'pyname': u'wavelength_21',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'micron'}),
                                      (u'spectrum 21',
                                       {'name': u'Spectrum 21',
                                        'pyname': u'spectrum_21',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'wavelength 22',
                                       {'name': u'Wavelength 22',
                                        'pyname': u'wavelength_22',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'micron'}),
                                      (u'spectrum 22',
                                       {'name': u'Spectrum 22',
                                        'pyname': u'spectrum_22',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'wavelength 23',
                                       {'name': u'Wavelength 23',
                                        'pyname': u'wavelength_23',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'micron'}),
                                      (u'spectrum 23',
                                       {'name': u'Spectrum 23',
                                        'pyname': u'spectrum_23',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'wavelength 24',
                                       {'name': u'Wavelength 24',
                                        'pyname': u'wavelength_24',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'micron'}),
                                      (u'spectrum 24',
                                       {'name': u'Spectrum 24',
                                        'pyname': u'spectrum_24',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'wavelength 25',
                                       {'name': u'Wavelength 25',
                                        'pyname': u'wavelength_25',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'micron'}),
                                      (u'spectrum 25',
                                       {'name': u'Spectrum 25',
                                        'pyname': u'spectrum_25',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'wavelength 26',
                                       {'name': u'Wavelength 26',
                                        'pyname': u'wavelength_26',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'micron'}),
                                      (u'spectrum 26',
                                       {'name': u'Spectrum 26',
                                        'pyname': u'spectrum_26',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'wavelength 27',
                                       {'name': u'Wavelength 27',
                                        'pyname': u'wavelength_27',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'micron'}),
                                      (u'spectrum 27',
                                       {'name': u'Spectrum 27',
                                        'pyname': u'spectrum_27',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'wavelength 28',
                                       {'name': u'Wavelength 28',
                                        'pyname': u'wavelength_28',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'micron'}),
                                      (u'spectrum 28',
                                       {'name': u'Spectrum 28',
                                        'pyname': u'spectrum_28',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'wavelength 29',
                                       {'name': u'Wavelength 29',
                                        'pyname': u'wavelength_29',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'micron'}),
                                      (u'spectrum 29',
                                       {'name': u'Spectrum 29',
                                        'pyname': u'spectrum_29',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'wavelength 30',
                                       {'name': u'Wavelength 30',
                                        'pyname': u'wavelength_30',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'micron'}),
                                      (u'spectrum 30',
                                       {'name': u'Spectrum 30',
                                        'pyname': u'spectrum_30',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'wavelength 31',
                                       {'name': u'Wavelength 31',
                                        'pyname': u'wavelength_31',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'micron'}),
                                      (u'spectrum 31',
                                       {'name': u'Spectrum 31',
                                        'pyname': u'spectrum_31',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'wavelength 32',
                                       {'name': u'Wavelength 32',
                                        'pyname': u'wavelength_32',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'micron'}),
                                      (u'spectrum 32',
                                       {'name': u'Spectrum 32',
                                        'pyname': u'spectrum_32',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'wavelength 33',
                                       {'name': u'Wavelength 33',
                                        'pyname': u'wavelength_33',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'micron'}),
                                      (u'spectrum 33',
                                       {'name': u'Spectrum 33',
                                        'pyname': u'spectrum_33',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'wavelength 34',
                                       {'name': u'Wavelength 34',
                                        'pyname': u'wavelength_34',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'micron'}),
                                      (u'spectrum 34',
                                       {'name': u'Spectrum 34',
                                        'pyname': u'spectrum_34',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'wavelength 35',
                                       {'name': u'Wavelength 35',
                                        'pyname': u'wavelength_35',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'micron'}),
                                      (u'spectrum 35',
                                       {'name': u'Spectrum 35',
                                        'pyname': u'spectrum_35',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'wavelength 36',
                                       {'name': u'Wavelength 36',
                                        'pyname': u'wavelength_36',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'micron'}),
                                      (u'spectrum 36',
                                       {'name': u'Spectrum 36',
                                        'pyname': u'spectrum_36',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'wavelength 37',
                                       {'name': u'Wavelength 37',
                                        'pyname': u'wavelength_37',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'micron'}),
                                      (u'spectrum 37',
                                       {'name': u'Spectrum 37',
                                        'pyname': u'spectrum_37',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'wavelength 38',
                                       {'name': u'Wavelength 38',
                                        'pyname': u'wavelength_38',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'micron'}),
                                      (u'spectrum 38',
                                       {'name': u'Spectrum 38',
                                        'pyname': u'spectrum_38',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'wavelength 39',
                                       {'name': u'Wavelength 39',
                                        'pyname': u'wavelength_39',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'micron'}),
                                      (u'spectrum 39',
                                       {'name': u'Spectrum 39',
                                        'pyname': u'spectrum_39',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'wavelength 40',
                                       {'name': u'Wavelength 40',
                                        'pyname': u'wavelength_40',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'micron'}),
                                      (u'spectrum 40',
                                       {'name': u'Spectrum 40',
                                        'pyname': u'spectrum_40',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'wavelength 41',
                                       {'name': u'Wavelength 41',
                                        'pyname': u'wavelength_41',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'micron'}),
                                      (u'spectrum 41',
                                       {'name': u'Spectrum 41',
                                        'pyname': u'spectrum_41',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'wavelength 42',
                                       {'name': u'Wavelength 42',
                                        'pyname': u'wavelength_42',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'micron'}),
                                      (u'spectrum 42',
                                       {'name': u'Spectrum 42',
                                        'pyname': u'spectrum_42',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'wavelength 43',
                                       {'name': u'Wavelength 43',
                                        'pyname': u'wavelength_43',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'micron'}),
                                      (u'spectrum 43',
                                       {'name': u'Spectrum 43',
                                        'pyname': u'spectrum_43',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'wavelength 44',
                                       {'name': u'Wavelength 44',
                                        'pyname': u'wavelength_44',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'micron'}),
                                      (u'spectrum 44',
                                       {'name': u'Spectrum 44',
                                        'pyname': u'spectrum_44',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'wavelength 45',
                                       {'name': u'Wavelength 45',
                                        'pyname': u'wavelength_45',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'micron'}),
                                      (u'spectrum 45',
                                       {'name': u'Spectrum 45',
                                        'pyname': u'spectrum_45',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'wavelength 46',
                                       {'name': u'Wavelength 46',
                                        'pyname': u'wavelength_46',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'micron'}),
                                      (u'spectrum 46',
                                       {'name': u'Spectrum 46',
                                        'pyname': u'spectrum_46',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'wavelength 47',
                                       {'name': u'Wavelength 47',
                                        'pyname': u'wavelength_47',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'micron'}),
                                      (u'spectrum 47',
                                       {'name': u'Spectrum 47',
                                        'pyname': u'spectrum_47',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'wavelength 48',
                                       {'name': u'Wavelength 48',
                                        'pyname': u'wavelength_48',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'micron'}),
                                      (u'spectrum 48',
                                       {'name': u'Spectrum 48',
                                        'pyname': u'spectrum_48',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'wavelength 49',
                                       {'name': u'Wavelength 49',
                                        'pyname': u'wavelength_49',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'micron'}),
                                      (u'spectrum 49',
                                       {'name': u'Spectrum 49',
                                        'pyname': u'spectrum_49',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'wavelength 50',
                                       {'name': u'Wavelength 50',
                                        'pyname': u'wavelength_50',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'micron'}),
                                      (u'spectrum 50',
                                       {'name': u'Spectrum 50',
                                        'pyname': u'spectrum_50',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'wavelength 51',
                                       {'name': u'Wavelength 51',
                                        'pyname': u'wavelength_51',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'micron'}),
                                      (u'spectrum 51',
                                       {'name': u'Spectrum 51',
                                        'pyname': u'spectrum_51',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'wavelength 52',
                                       {'name': u'Wavelength 52',
                                        'pyname': u'wavelength_52',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'micron'}),
                                      (u'spectrum 52',
                                       {'name': u'Spectrum 52',
                                        'pyname': u'spectrum_52',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'wavelength 53',
                                       {'name': u'Wavelength 53',
                                        'pyname': u'wavelength_53',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'micron'}),
                                      (u'spectrum 53',
                                       {'name': u'Spectrum 53',
                                        'pyname': u'spectrum_53',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'wavelength 54',
                                       {'name': u'Wavelength 54',
                                        'pyname': u'wavelength_54',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'micron'}),
                                      (u'spectrum 54',
                                       {'name': u'Spectrum 54',
                                        'pyname': u'spectrum_54',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'wavelength 55',
                                       {'name': u'Wavelength 55',
                                        'pyname': u'wavelength_55',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'micron'}),
                                      (u'spectrum 55',
                                       {'name': u'Spectrum 55',
                                        'pyname': u'spectrum_55',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'wavelength 56',
                                       {'name': u'Wavelength 56',
                                        'pyname': u'wavelength_56',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'micron'}),
                                      (u'spectrum 56',
                                       {'name': u'Spectrum 56',
                                        'pyname': u'spectrum_56',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'wavelength 57',
                                       {'name': u'Wavelength 57',
                                        'pyname': u'wavelength_57',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'micron'}),
                                      (u'spectrum 57',
                                       {'name': u'Spectrum 57',
                                        'pyname': u'spectrum_57',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'wavelength 58',
                                       {'name': u'Wavelength 58',
                                        'pyname': u'wavelength_58',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'micron'}),
                                      (u'spectrum 58',
                                       {'name': u'Spectrum 58',
                                        'pyname': u'spectrum_58',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'wavelength 59',
                                       {'name': u'Wavelength 59',
                                        'pyname': u'wavelength_59',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'micron'}),
                                      (u'spectrum 59',
                                       {'name': u'Spectrum 59',
                                        'pyname': u'spectrum_59',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'wavelength 60',
                                       {'name': u'Wavelength 60',
                                        'pyname': u'wavelength_60',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'micron'}),
                                      (u'spectrum 60',
                                       {'name': u'Spectrum 60',
                                        'pyname': u'spectrum_60',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'wavelength 61',
                                       {'name': u'Wavelength 61',
                                        'pyname': u'wavelength_61',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'micron'}),
                                      (u'spectrum 61',
                                       {'name': u'Spectrum 61',
                                        'pyname': u'spectrum_61',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'wavelength 62',
                                       {'name': u'Wavelength 62',
                                        'pyname': u'wavelength_62',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'micron'}),
                                      (u'spectrum 62',
                                       {'name': u'Spectrum 62',
                                        'pyname': u'spectrum_62',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'wavelength 63',
                                       {'name': u'Wavelength 63',
                                        'pyname': u'wavelength_63',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'micron'}),
                                      (u'spectrum 63',
                                       {'name': u'Spectrum 63',
                                        'pyname': u'spectrum_63',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'wavelength 64',
                                       {'name': u'Wavelength 64',
                                        'pyname': u'wavelength_64',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'micron'}),
                                      (u'spectrum 64',
                                       {'name': u'Spectrum 64',
                                        'pyname': u'spectrum_64',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'wavelength 65',
                                       {'name': u'Wavelength 65',
                                        'pyname': u'wavelength_65',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'micron'}),
                                      (u'spectrum 65',
                                       {'name': u'Spectrum 65',
                                        'pyname': u'spectrum_65',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'wavelength 66',
                                       {'name': u'Wavelength 66',
                                        'pyname': u'wavelength_66',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'micron'}),
                                      (u'spectrum 66',
                                       {'name': u'Spectrum 66',
                                        'pyname': u'spectrum_66',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'wavelength 67',
                                       {'name': u'Wavelength 67',
                                        'pyname': u'wavelength_67',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'micron'}),
                                      (u'spectrum 67',
                                       {'name': u'Spectrum 67',
                                        'pyname': u'spectrum_67',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'wavelength 68',
                                       {'name': u'Wavelength 68',
                                        'pyname': u'wavelength_68',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'micron'}),
                                      (u'spectrum 68',
                                       {'name': u'Spectrum 68',
                                        'pyname': u'spectrum_68',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'wavelength 69',
                                       {'name': u'Wavelength 69',
                                        'pyname': u'wavelength_69',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'micron'}),
                                      (u'spectrum 69',
                                       {'name': u'Spectrum 69',
                                        'pyname': u'spectrum_69',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'wavelength 70',
                                       {'name': u'Wavelength 70',
                                        'pyname': u'wavelength_70',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'micron'}),
                                      (u'spectrum 70',
                                       {'name': u'Spectrum 70',
                                        'pyname': u'spectrum_70',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'wavelength 71',
                                       {'name': u'Wavelength 71',
                                        'pyname': u'wavelength_71',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'micron'}),
                                      (u'spectrum 71',
                                       {'name': u'Spectrum 71',
                                        'pyname': u'spectrum_71',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'wavelength 72',
                                       {'name': u'Wavelength 72',
                                        'pyname': u'wavelength_72',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'micron'}),
                                      (u'spectrum 72',
                                       {'name': u'Spectrum 72',
                                        'pyname': u'spectrum_72',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'wavelength 73',
                                       {'name': u'Wavelength 73',
                                        'pyname': u'wavelength_73',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'micron'}),
                                      (u'spectrum 73',
                                       {'name': u'Spectrum 73',
                                        'pyname': u'spectrum_73',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'wavelength 74',
                                       {'name': u'Wavelength 74',
                                        'pyname': u'wavelength_74',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'micron'}),
                                      (u'spectrum 74',
                                       {'name': u'Spectrum 74',
                                        'pyname': u'spectrum_74',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'wavelength 75',
                                       {'name': u'Wavelength 75',
                                        'pyname': u'wavelength_75',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'micron'}),
                                      (u'spectrum 75',
                                       {'name': u'Spectrum 75',
                                        'pyname': u'spectrum_75',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'wavelength 76',
                                       {'name': u'Wavelength 76',
                                        'pyname': u'wavelength_76',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'micron'}),
                                      (u'spectrum 76',
                                       {'name': u'Spectrum 76',
                                        'pyname': u'spectrum_76',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'wavelength 77',
                                       {'name': u'Wavelength 77',
                                        'pyname': u'wavelength_77',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'micron'}),
                                      (u'spectrum 77',
                                       {'name': u'Spectrum 77',
                                        'pyname': u'spectrum_77',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'wavelength 78',
                                       {'name': u'Wavelength 78',
                                        'pyname': u'wavelength_78',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'micron'}),
                                      (u'spectrum 78',
                                       {'name': u'Spectrum 78',
                                        'pyname': u'spectrum_78',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'wavelength 79',
                                       {'name': u'Wavelength 79',
                                        'pyname': u'wavelength_79',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'micron'}),
                                      (u'spectrum 79',
                                       {'name': u'Spectrum 79',
                                        'pyname': u'spectrum_79',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'wavelength 80',
                                       {'name': u'Wavelength 80',
                                        'pyname': u'wavelength_80',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'micron'}),
                                      (u'spectrum 80',
                                       {'name': u'Spectrum 80',
                                        'pyname': u'spectrum_80',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'wavelength 81',
                                       {'name': u'Wavelength 81',
                                        'pyname': u'wavelength_81',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'micron'}),
                                      (u'spectrum 81',
                                       {'name': u'Spectrum 81',
                                        'pyname': u'spectrum_81',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'wavelength 82',
                                       {'name': u'Wavelength 82',
                                        'pyname': u'wavelength_82',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'micron'}),
                                      (u'spectrum 82',
                                       {'name': u'Spectrum 82',
                                        'pyname': u'spectrum_82',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'wavelength 83',
                                       {'name': u'Wavelength 83',
                                        'pyname': u'wavelength_83',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'micron'}),
                                      (u'spectrum 83',
                                       {'name': u'Spectrum 83',
                                        'pyname': u'spectrum_83',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'wavelength 84',
                                       {'name': u'Wavelength 84',
                                        'pyname': u'wavelength_84',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'micron'}),
                                      (u'spectrum 84',
                                       {'name': u'Spectrum 84',
                                        'pyname': u'spectrum_84',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'wavelength 85',
                                       {'name': u'Wavelength 85',
                                        'pyname': u'wavelength_85',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'micron'}),
                                      (u'spectrum 85',
                                       {'name': u'Spectrum 85',
                                        'pyname': u'spectrum_85',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'wavelength 86',
                                       {'name': u'Wavelength 86',
                                        'pyname': u'wavelength_86',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'micron'}),
                                      (u'spectrum 86',
                                       {'name': u'Spectrum 86',
                                        'pyname': u'spectrum_86',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'wavelength 87',
                                       {'name': u'Wavelength 87',
                                        'pyname': u'wavelength_87',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'micron'}),
                                      (u'spectrum 87',
                                       {'name': u'Spectrum 87',
                                        'pyname': u'spectrum_87',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'wavelength 88',
                                       {'name': u'Wavelength 88',
                                        'pyname': u'wavelength_88',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'micron'}),
                                      (u'spectrum 88',
                                       {'name': u'Spectrum 88',
                                        'pyname': u'spectrum_88',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'wavelength 89',
                                       {'name': u'Wavelength 89',
                                        'pyname': u'wavelength_89',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'micron'}),
                                      (u'spectrum 89',
                                       {'name': u'Spectrum 89',
                                        'pyname': u'spectrum_89',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'wavelength 90',
                                       {'name': u'Wavelength 90',
                                        'pyname': u'wavelength_90',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'micron'}),
                                      (u'spectrum 90',
                                       {'name': u'Spectrum 90',
                                        'pyname': u'spectrum_90',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'wavelength 91',
                                       {'name': u'Wavelength 91',
                                        'pyname': u'wavelength_91',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'micron'}),
                                      (u'spectrum 91',
                                       {'name': u'Spectrum 91',
                                        'pyname': u'spectrum_91',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'wavelength 92',
                                       {'name': u'Wavelength 92',
                                        'pyname': u'wavelength_92',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'micron'}),
                                      (u'spectrum 92',
                                       {'name': u'Spectrum 92',
                                        'pyname': u'spectrum_92',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'wavelength 93',
                                       {'name': u'Wavelength 93',
                                        'pyname': u'wavelength_93',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'micron'}),
                                      (u'spectrum 93',
                                       {'name': u'Spectrum 93',
                                        'pyname': u'spectrum_93',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'wavelength 94',
                                       {'name': u'Wavelength 94',
                                        'pyname': u'wavelength_94',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'micron'}),
                                      (u'spectrum 94',
                                       {'name': u'Spectrum 94',
                                        'pyname': u'spectrum_94',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'wavelength 95',
                                       {'name': u'Wavelength 95',
                                        'pyname': u'wavelength_95',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'micron'}),
                                      (u'spectrum 95',
                                       {'name': u'Spectrum 95',
                                        'pyname': u'spectrum_95',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'wavelength 96',
                                       {'name': u'Wavelength 96',
                                        'pyname': u'wavelength_96',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'micron'}),
                                      (u'spectrum 96',
                                       {'name': u'Spectrum 96',
                                        'pyname': u'spectrum_96',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'wavelength 97',
                                       {'name': u'Wavelength 97',
                                        'pyname': u'wavelength_97',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'micron'}),
                                      (u'spectrum 97',
                                       {'name': u'Spectrum 97',
                                        'pyname': u'spectrum_97',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'wavelength 98',
                                       {'name': u'Wavelength 98',
                                        'pyname': u'wavelength_98',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'micron'}),
                                      (u'spectrum 98',
                                       {'name': u'Spectrum 98',
                                        'pyname': u'spectrum_98',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'wavelength 99',
                                       {'name': u'Wavelength 99',
                                        'pyname': u'wavelength_99',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'micron'}),
                                      (u'spectrum 99',
                                       {'name': u'Spectrum 99',
                                        'pyname': u'spectrum_99',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'wavelength 100',
                                       {'name': u'Wavelength 100',
                                        'pyname': u'wavelength_100',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'micron'}),
                                      (u'spectrum 100',
                                       {'name': u'Spectrum 100',
                                        'pyname': u'spectrum_100',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'wavelength 101',
                                       {'name': u'Wavelength 101',
                                        'pyname': u'wavelength_101',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'micron'}),
                                      (u'spectrum 101',
                                       {'name': u'Spectrum 101',
                                        'pyname': u'spectrum_101',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'wavelength 102',
                                       {'name': u'Wavelength 102',
                                        'pyname': u'wavelength_102',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'micron'}),
                                      (u'spectrum 102',
                                       {'name': u'Spectrum 102',
                                        'pyname': u'spectrum_102',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'wavelength 103',
                                       {'name': u'Wavelength 103',
                                        'pyname': u'wavelength_103',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'micron'}),
                                      (u'spectrum 103',
                                       {'name': u'Spectrum 103',
                                        'pyname': u'spectrum_103',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'wavelength 104',
                                       {'name': u'Wavelength 104',
                                        'pyname': u'wavelength_104',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'micron'}),
                                      (u'spectrum 104',
                                       {'name': u'Spectrum 104',
                                        'pyname': u'spectrum_104',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'wavelength 105',
                                       {'name': u'Wavelength 105',
                                        'pyname': u'wavelength_105',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'micron'}),
                                      (u'spectrum 105',
                                       {'name': u'Spectrum 105',
                                        'pyname': u'spectrum_105',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'wavelength 106',
                                       {'name': u'Wavelength 106',
                                        'pyname': u'wavelength_106',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'micron'}),
                                      (u'spectrum 106',
                                       {'name': u'Spectrum 106',
                                        'pyname': u'spectrum_106',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'wavelength 107',
                                       {'name': u'Wavelength 107',
                                        'pyname': u'wavelength_107',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'micron'}),
                                      (u'spectrum 107',
                                       {'name': u'Spectrum 107',
                                        'pyname': u'spectrum_107',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real'})]),
               'format': None,
               'group': u'Location and Climate',
               'min-fields': 8,
               'name': u'Site:SpectrumData',
               'pyname': u'SiteSpectrumData',
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
    def spectrum_data_type(self):
        """field `Spectrum Data Type`

        Args:
            value (str): value for IDD Field `Spectrum Data Type`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `spectrum_data_type` or None if not set

        """
        return self["Spectrum Data Type"]

    @spectrum_data_type.setter
    def spectrum_data_type(self, value=None):
        """Corresponds to IDD field `Spectrum Data Type`"""
        self["Spectrum Data Type"] = value

    @property
    def wavelength_1(self):
        """field `Wavelength 1`

        Args:
            value (float): value for IDD Field `Wavelength 1`
                Units: micron

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `wavelength_1` or None if not set

        """
        return self["Wavelength 1"]

    @wavelength_1.setter
    def wavelength_1(self, value=None):
        """Corresponds to IDD field `Wavelength 1`"""
        self["Wavelength 1"] = value

    @property
    def spectrum_1(self):
        """field `Spectrum 1`

        Args:
            value (float): value for IDD Field `Spectrum 1`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `spectrum_1` or None if not set

        """
        return self["Spectrum 1"]

    @spectrum_1.setter
    def spectrum_1(self, value=None):
        """Corresponds to IDD field `Spectrum 1`"""
        self["Spectrum 1"] = value

    @property
    def wavelength_2(self):
        """field `Wavelength 2`

        Args:
            value (float): value for IDD Field `Wavelength 2`
                Units: micron

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `wavelength_2` or None if not set

        """
        return self["Wavelength 2"]

    @wavelength_2.setter
    def wavelength_2(self, value=None):
        """Corresponds to IDD field `Wavelength 2`"""
        self["Wavelength 2"] = value

    @property
    def spectrum_2(self):
        """field `Spectrum 2`

        Args:
            value (float): value for IDD Field `Spectrum 2`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `spectrum_2` or None if not set

        """
        return self["Spectrum 2"]

    @spectrum_2.setter
    def spectrum_2(self, value=None):
        """Corresponds to IDD field `Spectrum 2`"""
        self["Spectrum 2"] = value

    @property
    def wavelength_3(self):
        """field `Wavelength 3`

        Args:
            value (float): value for IDD Field `Wavelength 3`
                Units: micron

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `wavelength_3` or None if not set

        """
        return self["Wavelength 3"]

    @wavelength_3.setter
    def wavelength_3(self, value=None):
        """Corresponds to IDD field `Wavelength 3`"""
        self["Wavelength 3"] = value

    @property
    def spectrum_3(self):
        """field `Spectrum 3`

        Args:
            value (float): value for IDD Field `Spectrum 3`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `spectrum_3` or None if not set

        """
        return self["Spectrum 3"]

    @spectrum_3.setter
    def spectrum_3(self, value=None):
        """Corresponds to IDD field `Spectrum 3`"""
        self["Spectrum 3"] = value

    @property
    def wavelength_4(self):
        """field `Wavelength 4`

        Args:
            value (float): value for IDD Field `Wavelength 4`
                Units: micron

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `wavelength_4` or None if not set

        """
        return self["Wavelength 4"]

    @wavelength_4.setter
    def wavelength_4(self, value=None):
        """Corresponds to IDD field `Wavelength 4`"""
        self["Wavelength 4"] = value

    @property
    def spectrum_4(self):
        """field `Spectrum 4`

        Args:
            value (float): value for IDD Field `Spectrum 4`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `spectrum_4` or None if not set

        """
        return self["Spectrum 4"]

    @spectrum_4.setter
    def spectrum_4(self, value=None):
        """Corresponds to IDD field `Spectrum 4`"""
        self["Spectrum 4"] = value

    @property
    def wavelength_5(self):
        """field `Wavelength 5`

        Args:
            value (float): value for IDD Field `Wavelength 5`
                Units: micron

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `wavelength_5` or None if not set

        """
        return self["Wavelength 5"]

    @wavelength_5.setter
    def wavelength_5(self, value=None):
        """Corresponds to IDD field `Wavelength 5`"""
        self["Wavelength 5"] = value

    @property
    def spectrum_5(self):
        """field `Spectrum 5`

        Args:
            value (float): value for IDD Field `Spectrum 5`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `spectrum_5` or None if not set

        """
        return self["Spectrum 5"]

    @spectrum_5.setter
    def spectrum_5(self, value=None):
        """Corresponds to IDD field `Spectrum 5`"""
        self["Spectrum 5"] = value

    @property
    def wavelength_6(self):
        """field `Wavelength 6`

        Args:
            value (float): value for IDD Field `Wavelength 6`
                Units: micron

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `wavelength_6` or None if not set

        """
        return self["Wavelength 6"]

    @wavelength_6.setter
    def wavelength_6(self, value=None):
        """Corresponds to IDD field `Wavelength 6`"""
        self["Wavelength 6"] = value

    @property
    def spectrum_6(self):
        """field `Spectrum 6`

        Args:
            value (float): value for IDD Field `Spectrum 6`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `spectrum_6` or None if not set

        """
        return self["Spectrum 6"]

    @spectrum_6.setter
    def spectrum_6(self, value=None):
        """Corresponds to IDD field `Spectrum 6`"""
        self["Spectrum 6"] = value

    @property
    def wavelength_7(self):
        """field `Wavelength 7`

        Args:
            value (float): value for IDD Field `Wavelength 7`
                Units: micron

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `wavelength_7` or None if not set

        """
        return self["Wavelength 7"]

    @wavelength_7.setter
    def wavelength_7(self, value=None):
        """Corresponds to IDD field `Wavelength 7`"""
        self["Wavelength 7"] = value

    @property
    def spectrum_7(self):
        """field `Spectrum 7`

        Args:
            value (float): value for IDD Field `Spectrum 7`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `spectrum_7` or None if not set

        """
        return self["Spectrum 7"]

    @spectrum_7.setter
    def spectrum_7(self, value=None):
        """Corresponds to IDD field `Spectrum 7`"""
        self["Spectrum 7"] = value

    @property
    def wavelength_8(self):
        """field `Wavelength 8`

        Args:
            value (float): value for IDD Field `Wavelength 8`
                Units: micron

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `wavelength_8` or None if not set

        """
        return self["Wavelength 8"]

    @wavelength_8.setter
    def wavelength_8(self, value=None):
        """Corresponds to IDD field `Wavelength 8`"""
        self["Wavelength 8"] = value

    @property
    def spectrum_8(self):
        """field `Spectrum 8`

        Args:
            value (float): value for IDD Field `Spectrum 8`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `spectrum_8` or None if not set

        """
        return self["Spectrum 8"]

    @spectrum_8.setter
    def spectrum_8(self, value=None):
        """Corresponds to IDD field `Spectrum 8`"""
        self["Spectrum 8"] = value

    @property
    def wavelength_9(self):
        """field `Wavelength 9`

        Args:
            value (float): value for IDD Field `Wavelength 9`
                Units: micron

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `wavelength_9` or None if not set

        """
        return self["Wavelength 9"]

    @wavelength_9.setter
    def wavelength_9(self, value=None):
        """Corresponds to IDD field `Wavelength 9`"""
        self["Wavelength 9"] = value

    @property
    def spectrum_9(self):
        """field `Spectrum 9`

        Args:
            value (float): value for IDD Field `Spectrum 9`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `spectrum_9` or None if not set

        """
        return self["Spectrum 9"]

    @spectrum_9.setter
    def spectrum_9(self, value=None):
        """Corresponds to IDD field `Spectrum 9`"""
        self["Spectrum 9"] = value

    @property
    def wavelength_10(self):
        """field `Wavelength 10`

        Args:
            value (float): value for IDD Field `Wavelength 10`
                Units: micron

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `wavelength_10` or None if not set

        """
        return self["Wavelength 10"]

    @wavelength_10.setter
    def wavelength_10(self, value=None):
        """Corresponds to IDD field `Wavelength 10`"""
        self["Wavelength 10"] = value

    @property
    def spectrum_10(self):
        """field `Spectrum 10`

        Args:
            value (float): value for IDD Field `Spectrum 10`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `spectrum_10` or None if not set

        """
        return self["Spectrum 10"]

    @spectrum_10.setter
    def spectrum_10(self, value=None):
        """Corresponds to IDD field `Spectrum 10`"""
        self["Spectrum 10"] = value

    @property
    def wavelength_11(self):
        """field `Wavelength 11`

        Args:
            value (float): value for IDD Field `Wavelength 11`
                Units: micron

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `wavelength_11` or None if not set

        """
        return self["Wavelength 11"]

    @wavelength_11.setter
    def wavelength_11(self, value=None):
        """Corresponds to IDD field `Wavelength 11`"""
        self["Wavelength 11"] = value

    @property
    def spectrum_11(self):
        """field `Spectrum 11`

        Args:
            value (float): value for IDD Field `Spectrum 11`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `spectrum_11` or None if not set

        """
        return self["Spectrum 11"]

    @spectrum_11.setter
    def spectrum_11(self, value=None):
        """Corresponds to IDD field `Spectrum 11`"""
        self["Spectrum 11"] = value

    @property
    def wavelength_12(self):
        """field `Wavelength 12`

        Args:
            value (float): value for IDD Field `Wavelength 12`
                Units: micron

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `wavelength_12` or None if not set

        """
        return self["Wavelength 12"]

    @wavelength_12.setter
    def wavelength_12(self, value=None):
        """Corresponds to IDD field `Wavelength 12`"""
        self["Wavelength 12"] = value

    @property
    def spectrum_12(self):
        """field `Spectrum 12`

        Args:
            value (float): value for IDD Field `Spectrum 12`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `spectrum_12` or None if not set

        """
        return self["Spectrum 12"]

    @spectrum_12.setter
    def spectrum_12(self, value=None):
        """Corresponds to IDD field `Spectrum 12`"""
        self["Spectrum 12"] = value

    @property
    def wavelength_13(self):
        """field `Wavelength 13`

        Args:
            value (float): value for IDD Field `Wavelength 13`
                Units: micron

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `wavelength_13` or None if not set

        """
        return self["Wavelength 13"]

    @wavelength_13.setter
    def wavelength_13(self, value=None):
        """Corresponds to IDD field `Wavelength 13`"""
        self["Wavelength 13"] = value

    @property
    def spectrum_13(self):
        """field `Spectrum 13`

        Args:
            value (float): value for IDD Field `Spectrum 13`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `spectrum_13` or None if not set

        """
        return self["Spectrum 13"]

    @spectrum_13.setter
    def spectrum_13(self, value=None):
        """Corresponds to IDD field `Spectrum 13`"""
        self["Spectrum 13"] = value

    @property
    def wavelength_14(self):
        """field `Wavelength 14`

        Args:
            value (float): value for IDD Field `Wavelength 14`
                Units: micron

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `wavelength_14` or None if not set

        """
        return self["Wavelength 14"]

    @wavelength_14.setter
    def wavelength_14(self, value=None):
        """Corresponds to IDD field `Wavelength 14`"""
        self["Wavelength 14"] = value

    @property
    def spectrum_14(self):
        """field `Spectrum 14`

        Args:
            value (float): value for IDD Field `Spectrum 14`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `spectrum_14` or None if not set

        """
        return self["Spectrum 14"]

    @spectrum_14.setter
    def spectrum_14(self, value=None):
        """Corresponds to IDD field `Spectrum 14`"""
        self["Spectrum 14"] = value

    @property
    def wavelength_15(self):
        """field `Wavelength 15`

        Args:
            value (float): value for IDD Field `Wavelength 15`
                Units: micron

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `wavelength_15` or None if not set

        """
        return self["Wavelength 15"]

    @wavelength_15.setter
    def wavelength_15(self, value=None):
        """Corresponds to IDD field `Wavelength 15`"""
        self["Wavelength 15"] = value

    @property
    def spectrum_15(self):
        """field `Spectrum 15`

        Args:
            value (float): value for IDD Field `Spectrum 15`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `spectrum_15` or None if not set

        """
        return self["Spectrum 15"]

    @spectrum_15.setter
    def spectrum_15(self, value=None):
        """Corresponds to IDD field `Spectrum 15`"""
        self["Spectrum 15"] = value

    @property
    def wavelength_16(self):
        """field `Wavelength 16`

        Args:
            value (float): value for IDD Field `Wavelength 16`
                Units: micron

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `wavelength_16` or None if not set

        """
        return self["Wavelength 16"]

    @wavelength_16.setter
    def wavelength_16(self, value=None):
        """Corresponds to IDD field `Wavelength 16`"""
        self["Wavelength 16"] = value

    @property
    def spectrum_16(self):
        """field `Spectrum 16`

        Args:
            value (float): value for IDD Field `Spectrum 16`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `spectrum_16` or None if not set

        """
        return self["Spectrum 16"]

    @spectrum_16.setter
    def spectrum_16(self, value=None):
        """Corresponds to IDD field `Spectrum 16`"""
        self["Spectrum 16"] = value

    @property
    def wavelength_17(self):
        """field `Wavelength 17`

        Args:
            value (float): value for IDD Field `Wavelength 17`
                Units: micron

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `wavelength_17` or None if not set

        """
        return self["Wavelength 17"]

    @wavelength_17.setter
    def wavelength_17(self, value=None):
        """Corresponds to IDD field `Wavelength 17`"""
        self["Wavelength 17"] = value

    @property
    def spectrum_17(self):
        """field `Spectrum 17`

        Args:
            value (float): value for IDD Field `Spectrum 17`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `spectrum_17` or None if not set

        """
        return self["Spectrum 17"]

    @spectrum_17.setter
    def spectrum_17(self, value=None):
        """Corresponds to IDD field `Spectrum 17`"""
        self["Spectrum 17"] = value

    @property
    def wavelength_18(self):
        """field `Wavelength 18`

        Args:
            value (float): value for IDD Field `Wavelength 18`
                Units: micron

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `wavelength_18` or None if not set

        """
        return self["Wavelength 18"]

    @wavelength_18.setter
    def wavelength_18(self, value=None):
        """Corresponds to IDD field `Wavelength 18`"""
        self["Wavelength 18"] = value

    @property
    def spectrum_18(self):
        """field `Spectrum 18`

        Args:
            value (float): value for IDD Field `Spectrum 18`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `spectrum_18` or None if not set

        """
        return self["Spectrum 18"]

    @spectrum_18.setter
    def spectrum_18(self, value=None):
        """Corresponds to IDD field `Spectrum 18`"""
        self["Spectrum 18"] = value

    @property
    def wavelength_19(self):
        """field `Wavelength 19`

        Args:
            value (float): value for IDD Field `Wavelength 19`
                Units: micron

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `wavelength_19` or None if not set

        """
        return self["Wavelength 19"]

    @wavelength_19.setter
    def wavelength_19(self, value=None):
        """Corresponds to IDD field `Wavelength 19`"""
        self["Wavelength 19"] = value

    @property
    def spectrum_19(self):
        """field `Spectrum 19`

        Args:
            value (float): value for IDD Field `Spectrum 19`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `spectrum_19` or None if not set

        """
        return self["Spectrum 19"]

    @spectrum_19.setter
    def spectrum_19(self, value=None):
        """Corresponds to IDD field `Spectrum 19`"""
        self["Spectrum 19"] = value

    @property
    def wavelength_20(self):
        """field `Wavelength 20`

        Args:
            value (float): value for IDD Field `Wavelength 20`
                Units: micron

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `wavelength_20` or None if not set

        """
        return self["Wavelength 20"]

    @wavelength_20.setter
    def wavelength_20(self, value=None):
        """Corresponds to IDD field `Wavelength 20`"""
        self["Wavelength 20"] = value

    @property
    def spectrum_20(self):
        """field `Spectrum 20`

        Args:
            value (float): value for IDD Field `Spectrum 20`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `spectrum_20` or None if not set

        """
        return self["Spectrum 20"]

    @spectrum_20.setter
    def spectrum_20(self, value=None):
        """Corresponds to IDD field `Spectrum 20`"""
        self["Spectrum 20"] = value

    @property
    def wavelength_21(self):
        """field `Wavelength 21`

        Args:
            value (float): value for IDD Field `Wavelength 21`
                Units: micron

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `wavelength_21` or None if not set

        """
        return self["Wavelength 21"]

    @wavelength_21.setter
    def wavelength_21(self, value=None):
        """Corresponds to IDD field `Wavelength 21`"""
        self["Wavelength 21"] = value

    @property
    def spectrum_21(self):
        """field `Spectrum 21`

        Args:
            value (float): value for IDD Field `Spectrum 21`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `spectrum_21` or None if not set

        """
        return self["Spectrum 21"]

    @spectrum_21.setter
    def spectrum_21(self, value=None):
        """Corresponds to IDD field `Spectrum 21`"""
        self["Spectrum 21"] = value

    @property
    def wavelength_22(self):
        """field `Wavelength 22`

        Args:
            value (float): value for IDD Field `Wavelength 22`
                Units: micron

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `wavelength_22` or None if not set

        """
        return self["Wavelength 22"]

    @wavelength_22.setter
    def wavelength_22(self, value=None):
        """Corresponds to IDD field `Wavelength 22`"""
        self["Wavelength 22"] = value

    @property
    def spectrum_22(self):
        """field `Spectrum 22`

        Args:
            value (float): value for IDD Field `Spectrum 22`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `spectrum_22` or None if not set

        """
        return self["Spectrum 22"]

    @spectrum_22.setter
    def spectrum_22(self, value=None):
        """Corresponds to IDD field `Spectrum 22`"""
        self["Spectrum 22"] = value

    @property
    def wavelength_23(self):
        """field `Wavelength 23`

        Args:
            value (float): value for IDD Field `Wavelength 23`
                Units: micron

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `wavelength_23` or None if not set

        """
        return self["Wavelength 23"]

    @wavelength_23.setter
    def wavelength_23(self, value=None):
        """Corresponds to IDD field `Wavelength 23`"""
        self["Wavelength 23"] = value

    @property
    def spectrum_23(self):
        """field `Spectrum 23`

        Args:
            value (float): value for IDD Field `Spectrum 23`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `spectrum_23` or None if not set

        """
        return self["Spectrum 23"]

    @spectrum_23.setter
    def spectrum_23(self, value=None):
        """Corresponds to IDD field `Spectrum 23`"""
        self["Spectrum 23"] = value

    @property
    def wavelength_24(self):
        """field `Wavelength 24`

        Args:
            value (float): value for IDD Field `Wavelength 24`
                Units: micron

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `wavelength_24` or None if not set

        """
        return self["Wavelength 24"]

    @wavelength_24.setter
    def wavelength_24(self, value=None):
        """Corresponds to IDD field `Wavelength 24`"""
        self["Wavelength 24"] = value

    @property
    def spectrum_24(self):
        """field `Spectrum 24`

        Args:
            value (float): value for IDD Field `Spectrum 24`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `spectrum_24` or None if not set

        """
        return self["Spectrum 24"]

    @spectrum_24.setter
    def spectrum_24(self, value=None):
        """Corresponds to IDD field `Spectrum 24`"""
        self["Spectrum 24"] = value

    @property
    def wavelength_25(self):
        """field `Wavelength 25`

        Args:
            value (float): value for IDD Field `Wavelength 25`
                Units: micron

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `wavelength_25` or None if not set

        """
        return self["Wavelength 25"]

    @wavelength_25.setter
    def wavelength_25(self, value=None):
        """Corresponds to IDD field `Wavelength 25`"""
        self["Wavelength 25"] = value

    @property
    def spectrum_25(self):
        """field `Spectrum 25`

        Args:
            value (float): value for IDD Field `Spectrum 25`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `spectrum_25` or None if not set

        """
        return self["Spectrum 25"]

    @spectrum_25.setter
    def spectrum_25(self, value=None):
        """Corresponds to IDD field `Spectrum 25`"""
        self["Spectrum 25"] = value

    @property
    def wavelength_26(self):
        """field `Wavelength 26`

        Args:
            value (float): value for IDD Field `Wavelength 26`
                Units: micron

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `wavelength_26` or None if not set

        """
        return self["Wavelength 26"]

    @wavelength_26.setter
    def wavelength_26(self, value=None):
        """Corresponds to IDD field `Wavelength 26`"""
        self["Wavelength 26"] = value

    @property
    def spectrum_26(self):
        """field `Spectrum 26`

        Args:
            value (float): value for IDD Field `Spectrum 26`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `spectrum_26` or None if not set

        """
        return self["Spectrum 26"]

    @spectrum_26.setter
    def spectrum_26(self, value=None):
        """Corresponds to IDD field `Spectrum 26`"""
        self["Spectrum 26"] = value

    @property
    def wavelength_27(self):
        """field `Wavelength 27`

        Args:
            value (float): value for IDD Field `Wavelength 27`
                Units: micron

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `wavelength_27` or None if not set

        """
        return self["Wavelength 27"]

    @wavelength_27.setter
    def wavelength_27(self, value=None):
        """Corresponds to IDD field `Wavelength 27`"""
        self["Wavelength 27"] = value

    @property
    def spectrum_27(self):
        """field `Spectrum 27`

        Args:
            value (float): value for IDD Field `Spectrum 27`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `spectrum_27` or None if not set

        """
        return self["Spectrum 27"]

    @spectrum_27.setter
    def spectrum_27(self, value=None):
        """Corresponds to IDD field `Spectrum 27`"""
        self["Spectrum 27"] = value

    @property
    def wavelength_28(self):
        """field `Wavelength 28`

        Args:
            value (float): value for IDD Field `Wavelength 28`
                Units: micron

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `wavelength_28` or None if not set

        """
        return self["Wavelength 28"]

    @wavelength_28.setter
    def wavelength_28(self, value=None):
        """Corresponds to IDD field `Wavelength 28`"""
        self["Wavelength 28"] = value

    @property
    def spectrum_28(self):
        """field `Spectrum 28`

        Args:
            value (float): value for IDD Field `Spectrum 28`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `spectrum_28` or None if not set

        """
        return self["Spectrum 28"]

    @spectrum_28.setter
    def spectrum_28(self, value=None):
        """Corresponds to IDD field `Spectrum 28`"""
        self["Spectrum 28"] = value

    @property
    def wavelength_29(self):
        """field `Wavelength 29`

        Args:
            value (float): value for IDD Field `Wavelength 29`
                Units: micron

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `wavelength_29` or None if not set

        """
        return self["Wavelength 29"]

    @wavelength_29.setter
    def wavelength_29(self, value=None):
        """Corresponds to IDD field `Wavelength 29`"""
        self["Wavelength 29"] = value

    @property
    def spectrum_29(self):
        """field `Spectrum 29`

        Args:
            value (float): value for IDD Field `Spectrum 29`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `spectrum_29` or None if not set

        """
        return self["Spectrum 29"]

    @spectrum_29.setter
    def spectrum_29(self, value=None):
        """Corresponds to IDD field `Spectrum 29`"""
        self["Spectrum 29"] = value

    @property
    def wavelength_30(self):
        """field `Wavelength 30`

        Args:
            value (float): value for IDD Field `Wavelength 30`
                Units: micron

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `wavelength_30` or None if not set

        """
        return self["Wavelength 30"]

    @wavelength_30.setter
    def wavelength_30(self, value=None):
        """Corresponds to IDD field `Wavelength 30`"""
        self["Wavelength 30"] = value

    @property
    def spectrum_30(self):
        """field `Spectrum 30`

        Args:
            value (float): value for IDD Field `Spectrum 30`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `spectrum_30` or None if not set

        """
        return self["Spectrum 30"]

    @spectrum_30.setter
    def spectrum_30(self, value=None):
        """Corresponds to IDD field `Spectrum 30`"""
        self["Spectrum 30"] = value

    @property
    def wavelength_31(self):
        """field `Wavelength 31`

        Args:
            value (float): value for IDD Field `Wavelength 31`
                Units: micron

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `wavelength_31` or None if not set

        """
        return self["Wavelength 31"]

    @wavelength_31.setter
    def wavelength_31(self, value=None):
        """Corresponds to IDD field `Wavelength 31`"""
        self["Wavelength 31"] = value

    @property
    def spectrum_31(self):
        """field `Spectrum 31`

        Args:
            value (float): value for IDD Field `Spectrum 31`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `spectrum_31` or None if not set

        """
        return self["Spectrum 31"]

    @spectrum_31.setter
    def spectrum_31(self, value=None):
        """Corresponds to IDD field `Spectrum 31`"""
        self["Spectrum 31"] = value

    @property
    def wavelength_32(self):
        """field `Wavelength 32`

        Args:
            value (float): value for IDD Field `Wavelength 32`
                Units: micron

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `wavelength_32` or None if not set

        """
        return self["Wavelength 32"]

    @wavelength_32.setter
    def wavelength_32(self, value=None):
        """Corresponds to IDD field `Wavelength 32`"""
        self["Wavelength 32"] = value

    @property
    def spectrum_32(self):
        """field `Spectrum 32`

        Args:
            value (float): value for IDD Field `Spectrum 32`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `spectrum_32` or None if not set

        """
        return self["Spectrum 32"]

    @spectrum_32.setter
    def spectrum_32(self, value=None):
        """Corresponds to IDD field `Spectrum 32`"""
        self["Spectrum 32"] = value

    @property
    def wavelength_33(self):
        """field `Wavelength 33`

        Args:
            value (float): value for IDD Field `Wavelength 33`
                Units: micron

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `wavelength_33` or None if not set

        """
        return self["Wavelength 33"]

    @wavelength_33.setter
    def wavelength_33(self, value=None):
        """Corresponds to IDD field `Wavelength 33`"""
        self["Wavelength 33"] = value

    @property
    def spectrum_33(self):
        """field `Spectrum 33`

        Args:
            value (float): value for IDD Field `Spectrum 33`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `spectrum_33` or None if not set

        """
        return self["Spectrum 33"]

    @spectrum_33.setter
    def spectrum_33(self, value=None):
        """Corresponds to IDD field `Spectrum 33`"""
        self["Spectrum 33"] = value

    @property
    def wavelength_34(self):
        """field `Wavelength 34`

        Args:
            value (float): value for IDD Field `Wavelength 34`
                Units: micron

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `wavelength_34` or None if not set

        """
        return self["Wavelength 34"]

    @wavelength_34.setter
    def wavelength_34(self, value=None):
        """Corresponds to IDD field `Wavelength 34`"""
        self["Wavelength 34"] = value

    @property
    def spectrum_34(self):
        """field `Spectrum 34`

        Args:
            value (float): value for IDD Field `Spectrum 34`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `spectrum_34` or None if not set

        """
        return self["Spectrum 34"]

    @spectrum_34.setter
    def spectrum_34(self, value=None):
        """Corresponds to IDD field `Spectrum 34`"""
        self["Spectrum 34"] = value

    @property
    def wavelength_35(self):
        """field `Wavelength 35`

        Args:
            value (float): value for IDD Field `Wavelength 35`
                Units: micron

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `wavelength_35` or None if not set

        """
        return self["Wavelength 35"]

    @wavelength_35.setter
    def wavelength_35(self, value=None):
        """Corresponds to IDD field `Wavelength 35`"""
        self["Wavelength 35"] = value

    @property
    def spectrum_35(self):
        """field `Spectrum 35`

        Args:
            value (float): value for IDD Field `Spectrum 35`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `spectrum_35` or None if not set

        """
        return self["Spectrum 35"]

    @spectrum_35.setter
    def spectrum_35(self, value=None):
        """Corresponds to IDD field `Spectrum 35`"""
        self["Spectrum 35"] = value

    @property
    def wavelength_36(self):
        """field `Wavelength 36`

        Args:
            value (float): value for IDD Field `Wavelength 36`
                Units: micron

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `wavelength_36` or None if not set

        """
        return self["Wavelength 36"]

    @wavelength_36.setter
    def wavelength_36(self, value=None):
        """Corresponds to IDD field `Wavelength 36`"""
        self["Wavelength 36"] = value

    @property
    def spectrum_36(self):
        """field `Spectrum 36`

        Args:
            value (float): value for IDD Field `Spectrum 36`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `spectrum_36` or None if not set

        """
        return self["Spectrum 36"]

    @spectrum_36.setter
    def spectrum_36(self, value=None):
        """Corresponds to IDD field `Spectrum 36`"""
        self["Spectrum 36"] = value

    @property
    def wavelength_37(self):
        """field `Wavelength 37`

        Args:
            value (float): value for IDD Field `Wavelength 37`
                Units: micron

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `wavelength_37` or None if not set

        """
        return self["Wavelength 37"]

    @wavelength_37.setter
    def wavelength_37(self, value=None):
        """Corresponds to IDD field `Wavelength 37`"""
        self["Wavelength 37"] = value

    @property
    def spectrum_37(self):
        """field `Spectrum 37`

        Args:
            value (float): value for IDD Field `Spectrum 37`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `spectrum_37` or None if not set

        """
        return self["Spectrum 37"]

    @spectrum_37.setter
    def spectrum_37(self, value=None):
        """Corresponds to IDD field `Spectrum 37`"""
        self["Spectrum 37"] = value

    @property
    def wavelength_38(self):
        """field `Wavelength 38`

        Args:
            value (float): value for IDD Field `Wavelength 38`
                Units: micron

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `wavelength_38` or None if not set

        """
        return self["Wavelength 38"]

    @wavelength_38.setter
    def wavelength_38(self, value=None):
        """Corresponds to IDD field `Wavelength 38`"""
        self["Wavelength 38"] = value

    @property
    def spectrum_38(self):
        """field `Spectrum 38`

        Args:
            value (float): value for IDD Field `Spectrum 38`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `spectrum_38` or None if not set

        """
        return self["Spectrum 38"]

    @spectrum_38.setter
    def spectrum_38(self, value=None):
        """Corresponds to IDD field `Spectrum 38`"""
        self["Spectrum 38"] = value

    @property
    def wavelength_39(self):
        """field `Wavelength 39`

        Args:
            value (float): value for IDD Field `Wavelength 39`
                Units: micron

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `wavelength_39` or None if not set

        """
        return self["Wavelength 39"]

    @wavelength_39.setter
    def wavelength_39(self, value=None):
        """Corresponds to IDD field `Wavelength 39`"""
        self["Wavelength 39"] = value

    @property
    def spectrum_39(self):
        """field `Spectrum 39`

        Args:
            value (float): value for IDD Field `Spectrum 39`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `spectrum_39` or None if not set

        """
        return self["Spectrum 39"]

    @spectrum_39.setter
    def spectrum_39(self, value=None):
        """Corresponds to IDD field `Spectrum 39`"""
        self["Spectrum 39"] = value

    @property
    def wavelength_40(self):
        """field `Wavelength 40`

        Args:
            value (float): value for IDD Field `Wavelength 40`
                Units: micron

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `wavelength_40` or None if not set

        """
        return self["Wavelength 40"]

    @wavelength_40.setter
    def wavelength_40(self, value=None):
        """Corresponds to IDD field `Wavelength 40`"""
        self["Wavelength 40"] = value

    @property
    def spectrum_40(self):
        """field `Spectrum 40`

        Args:
            value (float): value for IDD Field `Spectrum 40`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `spectrum_40` or None if not set

        """
        return self["Spectrum 40"]

    @spectrum_40.setter
    def spectrum_40(self, value=None):
        """Corresponds to IDD field `Spectrum 40`"""
        self["Spectrum 40"] = value

    @property
    def wavelength_41(self):
        """field `Wavelength 41`

        Args:
            value (float): value for IDD Field `Wavelength 41`
                Units: micron

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `wavelength_41` or None if not set

        """
        return self["Wavelength 41"]

    @wavelength_41.setter
    def wavelength_41(self, value=None):
        """Corresponds to IDD field `Wavelength 41`"""
        self["Wavelength 41"] = value

    @property
    def spectrum_41(self):
        """field `Spectrum 41`

        Args:
            value (float): value for IDD Field `Spectrum 41`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `spectrum_41` or None if not set

        """
        return self["Spectrum 41"]

    @spectrum_41.setter
    def spectrum_41(self, value=None):
        """Corresponds to IDD field `Spectrum 41`"""
        self["Spectrum 41"] = value

    @property
    def wavelength_42(self):
        """field `Wavelength 42`

        Args:
            value (float): value for IDD Field `Wavelength 42`
                Units: micron

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `wavelength_42` or None if not set

        """
        return self["Wavelength 42"]

    @wavelength_42.setter
    def wavelength_42(self, value=None):
        """Corresponds to IDD field `Wavelength 42`"""
        self["Wavelength 42"] = value

    @property
    def spectrum_42(self):
        """field `Spectrum 42`

        Args:
            value (float): value for IDD Field `Spectrum 42`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `spectrum_42` or None if not set

        """
        return self["Spectrum 42"]

    @spectrum_42.setter
    def spectrum_42(self, value=None):
        """Corresponds to IDD field `Spectrum 42`"""
        self["Spectrum 42"] = value

    @property
    def wavelength_43(self):
        """field `Wavelength 43`

        Args:
            value (float): value for IDD Field `Wavelength 43`
                Units: micron

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `wavelength_43` or None if not set

        """
        return self["Wavelength 43"]

    @wavelength_43.setter
    def wavelength_43(self, value=None):
        """Corresponds to IDD field `Wavelength 43`"""
        self["Wavelength 43"] = value

    @property
    def spectrum_43(self):
        """field `Spectrum 43`

        Args:
            value (float): value for IDD Field `Spectrum 43`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `spectrum_43` or None if not set

        """
        return self["Spectrum 43"]

    @spectrum_43.setter
    def spectrum_43(self, value=None):
        """Corresponds to IDD field `Spectrum 43`"""
        self["Spectrum 43"] = value

    @property
    def wavelength_44(self):
        """field `Wavelength 44`

        Args:
            value (float): value for IDD Field `Wavelength 44`
                Units: micron

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `wavelength_44` or None if not set

        """
        return self["Wavelength 44"]

    @wavelength_44.setter
    def wavelength_44(self, value=None):
        """Corresponds to IDD field `Wavelength 44`"""
        self["Wavelength 44"] = value

    @property
    def spectrum_44(self):
        """field `Spectrum 44`

        Args:
            value (float): value for IDD Field `Spectrum 44`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `spectrum_44` or None if not set

        """
        return self["Spectrum 44"]

    @spectrum_44.setter
    def spectrum_44(self, value=None):
        """Corresponds to IDD field `Spectrum 44`"""
        self["Spectrum 44"] = value

    @property
    def wavelength_45(self):
        """field `Wavelength 45`

        Args:
            value (float): value for IDD Field `Wavelength 45`
                Units: micron

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `wavelength_45` or None if not set

        """
        return self["Wavelength 45"]

    @wavelength_45.setter
    def wavelength_45(self, value=None):
        """Corresponds to IDD field `Wavelength 45`"""
        self["Wavelength 45"] = value

    @property
    def spectrum_45(self):
        """field `Spectrum 45`

        Args:
            value (float): value for IDD Field `Spectrum 45`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `spectrum_45` or None if not set

        """
        return self["Spectrum 45"]

    @spectrum_45.setter
    def spectrum_45(self, value=None):
        """Corresponds to IDD field `Spectrum 45`"""
        self["Spectrum 45"] = value

    @property
    def wavelength_46(self):
        """field `Wavelength 46`

        Args:
            value (float): value for IDD Field `Wavelength 46`
                Units: micron

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `wavelength_46` or None if not set

        """
        return self["Wavelength 46"]

    @wavelength_46.setter
    def wavelength_46(self, value=None):
        """Corresponds to IDD field `Wavelength 46`"""
        self["Wavelength 46"] = value

    @property
    def spectrum_46(self):
        """field `Spectrum 46`

        Args:
            value (float): value for IDD Field `Spectrum 46`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `spectrum_46` or None if not set

        """
        return self["Spectrum 46"]

    @spectrum_46.setter
    def spectrum_46(self, value=None):
        """Corresponds to IDD field `Spectrum 46`"""
        self["Spectrum 46"] = value

    @property
    def wavelength_47(self):
        """field `Wavelength 47`

        Args:
            value (float): value for IDD Field `Wavelength 47`
                Units: micron

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `wavelength_47` or None if not set

        """
        return self["Wavelength 47"]

    @wavelength_47.setter
    def wavelength_47(self, value=None):
        """Corresponds to IDD field `Wavelength 47`"""
        self["Wavelength 47"] = value

    @property
    def spectrum_47(self):
        """field `Spectrum 47`

        Args:
            value (float): value for IDD Field `Spectrum 47`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `spectrum_47` or None if not set

        """
        return self["Spectrum 47"]

    @spectrum_47.setter
    def spectrum_47(self, value=None):
        """Corresponds to IDD field `Spectrum 47`"""
        self["Spectrum 47"] = value

    @property
    def wavelength_48(self):
        """field `Wavelength 48`

        Args:
            value (float): value for IDD Field `Wavelength 48`
                Units: micron

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `wavelength_48` or None if not set

        """
        return self["Wavelength 48"]

    @wavelength_48.setter
    def wavelength_48(self, value=None):
        """Corresponds to IDD field `Wavelength 48`"""
        self["Wavelength 48"] = value

    @property
    def spectrum_48(self):
        """field `Spectrum 48`

        Args:
            value (float): value for IDD Field `Spectrum 48`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `spectrum_48` or None if not set

        """
        return self["Spectrum 48"]

    @spectrum_48.setter
    def spectrum_48(self, value=None):
        """Corresponds to IDD field `Spectrum 48`"""
        self["Spectrum 48"] = value

    @property
    def wavelength_49(self):
        """field `Wavelength 49`

        Args:
            value (float): value for IDD Field `Wavelength 49`
                Units: micron

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `wavelength_49` or None if not set

        """
        return self["Wavelength 49"]

    @wavelength_49.setter
    def wavelength_49(self, value=None):
        """Corresponds to IDD field `Wavelength 49`"""
        self["Wavelength 49"] = value

    @property
    def spectrum_49(self):
        """field `Spectrum 49`

        Args:
            value (float): value for IDD Field `Spectrum 49`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `spectrum_49` or None if not set

        """
        return self["Spectrum 49"]

    @spectrum_49.setter
    def spectrum_49(self, value=None):
        """Corresponds to IDD field `Spectrum 49`"""
        self["Spectrum 49"] = value

    @property
    def wavelength_50(self):
        """field `Wavelength 50`

        Args:
            value (float): value for IDD Field `Wavelength 50`
                Units: micron

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `wavelength_50` or None if not set

        """
        return self["Wavelength 50"]

    @wavelength_50.setter
    def wavelength_50(self, value=None):
        """Corresponds to IDD field `Wavelength 50`"""
        self["Wavelength 50"] = value

    @property
    def spectrum_50(self):
        """field `Spectrum 50`

        Args:
            value (float): value for IDD Field `Spectrum 50`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `spectrum_50` or None if not set

        """
        return self["Spectrum 50"]

    @spectrum_50.setter
    def spectrum_50(self, value=None):
        """Corresponds to IDD field `Spectrum 50`"""
        self["Spectrum 50"] = value

    @property
    def wavelength_51(self):
        """field `Wavelength 51`

        Args:
            value (float): value for IDD Field `Wavelength 51`
                Units: micron

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `wavelength_51` or None if not set

        """
        return self["Wavelength 51"]

    @wavelength_51.setter
    def wavelength_51(self, value=None):
        """Corresponds to IDD field `Wavelength 51`"""
        self["Wavelength 51"] = value

    @property
    def spectrum_51(self):
        """field `Spectrum 51`

        Args:
            value (float): value for IDD Field `Spectrum 51`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `spectrum_51` or None if not set

        """
        return self["Spectrum 51"]

    @spectrum_51.setter
    def spectrum_51(self, value=None):
        """Corresponds to IDD field `Spectrum 51`"""
        self["Spectrum 51"] = value

    @property
    def wavelength_52(self):
        """field `Wavelength 52`

        Args:
            value (float): value for IDD Field `Wavelength 52`
                Units: micron

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `wavelength_52` or None if not set

        """
        return self["Wavelength 52"]

    @wavelength_52.setter
    def wavelength_52(self, value=None):
        """Corresponds to IDD field `Wavelength 52`"""
        self["Wavelength 52"] = value

    @property
    def spectrum_52(self):
        """field `Spectrum 52`

        Args:
            value (float): value for IDD Field `Spectrum 52`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `spectrum_52` or None if not set

        """
        return self["Spectrum 52"]

    @spectrum_52.setter
    def spectrum_52(self, value=None):
        """Corresponds to IDD field `Spectrum 52`"""
        self["Spectrum 52"] = value

    @property
    def wavelength_53(self):
        """field `Wavelength 53`

        Args:
            value (float): value for IDD Field `Wavelength 53`
                Units: micron

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `wavelength_53` or None if not set

        """
        return self["Wavelength 53"]

    @wavelength_53.setter
    def wavelength_53(self, value=None):
        """Corresponds to IDD field `Wavelength 53`"""
        self["Wavelength 53"] = value

    @property
    def spectrum_53(self):
        """field `Spectrum 53`

        Args:
            value (float): value for IDD Field `Spectrum 53`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `spectrum_53` or None if not set

        """
        return self["Spectrum 53"]

    @spectrum_53.setter
    def spectrum_53(self, value=None):
        """Corresponds to IDD field `Spectrum 53`"""
        self["Spectrum 53"] = value

    @property
    def wavelength_54(self):
        """field `Wavelength 54`

        Args:
            value (float): value for IDD Field `Wavelength 54`
                Units: micron

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `wavelength_54` or None if not set

        """
        return self["Wavelength 54"]

    @wavelength_54.setter
    def wavelength_54(self, value=None):
        """Corresponds to IDD field `Wavelength 54`"""
        self["Wavelength 54"] = value

    @property
    def spectrum_54(self):
        """field `Spectrum 54`

        Args:
            value (float): value for IDD Field `Spectrum 54`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `spectrum_54` or None if not set

        """
        return self["Spectrum 54"]

    @spectrum_54.setter
    def spectrum_54(self, value=None):
        """Corresponds to IDD field `Spectrum 54`"""
        self["Spectrum 54"] = value

    @property
    def wavelength_55(self):
        """field `Wavelength 55`

        Args:
            value (float): value for IDD Field `Wavelength 55`
                Units: micron

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `wavelength_55` or None if not set

        """
        return self["Wavelength 55"]

    @wavelength_55.setter
    def wavelength_55(self, value=None):
        """Corresponds to IDD field `Wavelength 55`"""
        self["Wavelength 55"] = value

    @property
    def spectrum_55(self):
        """field `Spectrum 55`

        Args:
            value (float): value for IDD Field `Spectrum 55`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `spectrum_55` or None if not set

        """
        return self["Spectrum 55"]

    @spectrum_55.setter
    def spectrum_55(self, value=None):
        """Corresponds to IDD field `Spectrum 55`"""
        self["Spectrum 55"] = value

    @property
    def wavelength_56(self):
        """field `Wavelength 56`

        Args:
            value (float): value for IDD Field `Wavelength 56`
                Units: micron

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `wavelength_56` or None if not set

        """
        return self["Wavelength 56"]

    @wavelength_56.setter
    def wavelength_56(self, value=None):
        """Corresponds to IDD field `Wavelength 56`"""
        self["Wavelength 56"] = value

    @property
    def spectrum_56(self):
        """field `Spectrum 56`

        Args:
            value (float): value for IDD Field `Spectrum 56`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `spectrum_56` or None if not set

        """
        return self["Spectrum 56"]

    @spectrum_56.setter
    def spectrum_56(self, value=None):
        """Corresponds to IDD field `Spectrum 56`"""
        self["Spectrum 56"] = value

    @property
    def wavelength_57(self):
        """field `Wavelength 57`

        Args:
            value (float): value for IDD Field `Wavelength 57`
                Units: micron

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `wavelength_57` or None if not set

        """
        return self["Wavelength 57"]

    @wavelength_57.setter
    def wavelength_57(self, value=None):
        """Corresponds to IDD field `Wavelength 57`"""
        self["Wavelength 57"] = value

    @property
    def spectrum_57(self):
        """field `Spectrum 57`

        Args:
            value (float): value for IDD Field `Spectrum 57`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `spectrum_57` or None if not set

        """
        return self["Spectrum 57"]

    @spectrum_57.setter
    def spectrum_57(self, value=None):
        """Corresponds to IDD field `Spectrum 57`"""
        self["Spectrum 57"] = value

    @property
    def wavelength_58(self):
        """field `Wavelength 58`

        Args:
            value (float): value for IDD Field `Wavelength 58`
                Units: micron

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `wavelength_58` or None if not set

        """
        return self["Wavelength 58"]

    @wavelength_58.setter
    def wavelength_58(self, value=None):
        """Corresponds to IDD field `Wavelength 58`"""
        self["Wavelength 58"] = value

    @property
    def spectrum_58(self):
        """field `Spectrum 58`

        Args:
            value (float): value for IDD Field `Spectrum 58`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `spectrum_58` or None if not set

        """
        return self["Spectrum 58"]

    @spectrum_58.setter
    def spectrum_58(self, value=None):
        """Corresponds to IDD field `Spectrum 58`"""
        self["Spectrum 58"] = value

    @property
    def wavelength_59(self):
        """field `Wavelength 59`

        Args:
            value (float): value for IDD Field `Wavelength 59`
                Units: micron

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `wavelength_59` or None if not set

        """
        return self["Wavelength 59"]

    @wavelength_59.setter
    def wavelength_59(self, value=None):
        """Corresponds to IDD field `Wavelength 59`"""
        self["Wavelength 59"] = value

    @property
    def spectrum_59(self):
        """field `Spectrum 59`

        Args:
            value (float): value for IDD Field `Spectrum 59`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `spectrum_59` or None if not set

        """
        return self["Spectrum 59"]

    @spectrum_59.setter
    def spectrum_59(self, value=None):
        """Corresponds to IDD field `Spectrum 59`"""
        self["Spectrum 59"] = value

    @property
    def wavelength_60(self):
        """field `Wavelength 60`

        Args:
            value (float): value for IDD Field `Wavelength 60`
                Units: micron

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `wavelength_60` or None if not set

        """
        return self["Wavelength 60"]

    @wavelength_60.setter
    def wavelength_60(self, value=None):
        """Corresponds to IDD field `Wavelength 60`"""
        self["Wavelength 60"] = value

    @property
    def spectrum_60(self):
        """field `Spectrum 60`

        Args:
            value (float): value for IDD Field `Spectrum 60`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `spectrum_60` or None if not set

        """
        return self["Spectrum 60"]

    @spectrum_60.setter
    def spectrum_60(self, value=None):
        """Corresponds to IDD field `Spectrum 60`"""
        self["Spectrum 60"] = value

    @property
    def wavelength_61(self):
        """field `Wavelength 61`

        Args:
            value (float): value for IDD Field `Wavelength 61`
                Units: micron

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `wavelength_61` or None if not set

        """
        return self["Wavelength 61"]

    @wavelength_61.setter
    def wavelength_61(self, value=None):
        """Corresponds to IDD field `Wavelength 61`"""
        self["Wavelength 61"] = value

    @property
    def spectrum_61(self):
        """field `Spectrum 61`

        Args:
            value (float): value for IDD Field `Spectrum 61`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `spectrum_61` or None if not set

        """
        return self["Spectrum 61"]

    @spectrum_61.setter
    def spectrum_61(self, value=None):
        """Corresponds to IDD field `Spectrum 61`"""
        self["Spectrum 61"] = value

    @property
    def wavelength_62(self):
        """field `Wavelength 62`

        Args:
            value (float): value for IDD Field `Wavelength 62`
                Units: micron

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `wavelength_62` or None if not set

        """
        return self["Wavelength 62"]

    @wavelength_62.setter
    def wavelength_62(self, value=None):
        """Corresponds to IDD field `Wavelength 62`"""
        self["Wavelength 62"] = value

    @property
    def spectrum_62(self):
        """field `Spectrum 62`

        Args:
            value (float): value for IDD Field `Spectrum 62`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `spectrum_62` or None if not set

        """
        return self["Spectrum 62"]

    @spectrum_62.setter
    def spectrum_62(self, value=None):
        """Corresponds to IDD field `Spectrum 62`"""
        self["Spectrum 62"] = value

    @property
    def wavelength_63(self):
        """field `Wavelength 63`

        Args:
            value (float): value for IDD Field `Wavelength 63`
                Units: micron

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `wavelength_63` or None if not set

        """
        return self["Wavelength 63"]

    @wavelength_63.setter
    def wavelength_63(self, value=None):
        """Corresponds to IDD field `Wavelength 63`"""
        self["Wavelength 63"] = value

    @property
    def spectrum_63(self):
        """field `Spectrum 63`

        Args:
            value (float): value for IDD Field `Spectrum 63`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `spectrum_63` or None if not set

        """
        return self["Spectrum 63"]

    @spectrum_63.setter
    def spectrum_63(self, value=None):
        """Corresponds to IDD field `Spectrum 63`"""
        self["Spectrum 63"] = value

    @property
    def wavelength_64(self):
        """field `Wavelength 64`

        Args:
            value (float): value for IDD Field `Wavelength 64`
                Units: micron

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `wavelength_64` or None if not set

        """
        return self["Wavelength 64"]

    @wavelength_64.setter
    def wavelength_64(self, value=None):
        """Corresponds to IDD field `Wavelength 64`"""
        self["Wavelength 64"] = value

    @property
    def spectrum_64(self):
        """field `Spectrum 64`

        Args:
            value (float): value for IDD Field `Spectrum 64`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `spectrum_64` or None if not set

        """
        return self["Spectrum 64"]

    @spectrum_64.setter
    def spectrum_64(self, value=None):
        """Corresponds to IDD field `Spectrum 64`"""
        self["Spectrum 64"] = value

    @property
    def wavelength_65(self):
        """field `Wavelength 65`

        Args:
            value (float): value for IDD Field `Wavelength 65`
                Units: micron

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `wavelength_65` or None if not set

        """
        return self["Wavelength 65"]

    @wavelength_65.setter
    def wavelength_65(self, value=None):
        """Corresponds to IDD field `Wavelength 65`"""
        self["Wavelength 65"] = value

    @property
    def spectrum_65(self):
        """field `Spectrum 65`

        Args:
            value (float): value for IDD Field `Spectrum 65`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `spectrum_65` or None if not set

        """
        return self["Spectrum 65"]

    @spectrum_65.setter
    def spectrum_65(self, value=None):
        """Corresponds to IDD field `Spectrum 65`"""
        self["Spectrum 65"] = value

    @property
    def wavelength_66(self):
        """field `Wavelength 66`

        Args:
            value (float): value for IDD Field `Wavelength 66`
                Units: micron

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `wavelength_66` or None if not set

        """
        return self["Wavelength 66"]

    @wavelength_66.setter
    def wavelength_66(self, value=None):
        """Corresponds to IDD field `Wavelength 66`"""
        self["Wavelength 66"] = value

    @property
    def spectrum_66(self):
        """field `Spectrum 66`

        Args:
            value (float): value for IDD Field `Spectrum 66`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `spectrum_66` or None if not set

        """
        return self["Spectrum 66"]

    @spectrum_66.setter
    def spectrum_66(self, value=None):
        """Corresponds to IDD field `Spectrum 66`"""
        self["Spectrum 66"] = value

    @property
    def wavelength_67(self):
        """field `Wavelength 67`

        Args:
            value (float): value for IDD Field `Wavelength 67`
                Units: micron

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `wavelength_67` or None if not set

        """
        return self["Wavelength 67"]

    @wavelength_67.setter
    def wavelength_67(self, value=None):
        """Corresponds to IDD field `Wavelength 67`"""
        self["Wavelength 67"] = value

    @property
    def spectrum_67(self):
        """field `Spectrum 67`

        Args:
            value (float): value for IDD Field `Spectrum 67`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `spectrum_67` or None if not set

        """
        return self["Spectrum 67"]

    @spectrum_67.setter
    def spectrum_67(self, value=None):
        """Corresponds to IDD field `Spectrum 67`"""
        self["Spectrum 67"] = value

    @property
    def wavelength_68(self):
        """field `Wavelength 68`

        Args:
            value (float): value for IDD Field `Wavelength 68`
                Units: micron

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `wavelength_68` or None if not set

        """
        return self["Wavelength 68"]

    @wavelength_68.setter
    def wavelength_68(self, value=None):
        """Corresponds to IDD field `Wavelength 68`"""
        self["Wavelength 68"] = value

    @property
    def spectrum_68(self):
        """field `Spectrum 68`

        Args:
            value (float): value for IDD Field `Spectrum 68`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `spectrum_68` or None if not set

        """
        return self["Spectrum 68"]

    @spectrum_68.setter
    def spectrum_68(self, value=None):
        """Corresponds to IDD field `Spectrum 68`"""
        self["Spectrum 68"] = value

    @property
    def wavelength_69(self):
        """field `Wavelength 69`

        Args:
            value (float): value for IDD Field `Wavelength 69`
                Units: micron

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `wavelength_69` or None if not set

        """
        return self["Wavelength 69"]

    @wavelength_69.setter
    def wavelength_69(self, value=None):
        """Corresponds to IDD field `Wavelength 69`"""
        self["Wavelength 69"] = value

    @property
    def spectrum_69(self):
        """field `Spectrum 69`

        Args:
            value (float): value for IDD Field `Spectrum 69`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `spectrum_69` or None if not set

        """
        return self["Spectrum 69"]

    @spectrum_69.setter
    def spectrum_69(self, value=None):
        """Corresponds to IDD field `Spectrum 69`"""
        self["Spectrum 69"] = value

    @property
    def wavelength_70(self):
        """field `Wavelength 70`

        Args:
            value (float): value for IDD Field `Wavelength 70`
                Units: micron

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `wavelength_70` or None if not set

        """
        return self["Wavelength 70"]

    @wavelength_70.setter
    def wavelength_70(self, value=None):
        """Corresponds to IDD field `Wavelength 70`"""
        self["Wavelength 70"] = value

    @property
    def spectrum_70(self):
        """field `Spectrum 70`

        Args:
            value (float): value for IDD Field `Spectrum 70`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `spectrum_70` or None if not set

        """
        return self["Spectrum 70"]

    @spectrum_70.setter
    def spectrum_70(self, value=None):
        """Corresponds to IDD field `Spectrum 70`"""
        self["Spectrum 70"] = value

    @property
    def wavelength_71(self):
        """field `Wavelength 71`

        Args:
            value (float): value for IDD Field `Wavelength 71`
                Units: micron

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `wavelength_71` or None if not set

        """
        return self["Wavelength 71"]

    @wavelength_71.setter
    def wavelength_71(self, value=None):
        """Corresponds to IDD field `Wavelength 71`"""
        self["Wavelength 71"] = value

    @property
    def spectrum_71(self):
        """field `Spectrum 71`

        Args:
            value (float): value for IDD Field `Spectrum 71`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `spectrum_71` or None if not set

        """
        return self["Spectrum 71"]

    @spectrum_71.setter
    def spectrum_71(self, value=None):
        """Corresponds to IDD field `Spectrum 71`"""
        self["Spectrum 71"] = value

    @property
    def wavelength_72(self):
        """field `Wavelength 72`

        Args:
            value (float): value for IDD Field `Wavelength 72`
                Units: micron

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `wavelength_72` or None if not set

        """
        return self["Wavelength 72"]

    @wavelength_72.setter
    def wavelength_72(self, value=None):
        """Corresponds to IDD field `Wavelength 72`"""
        self["Wavelength 72"] = value

    @property
    def spectrum_72(self):
        """field `Spectrum 72`

        Args:
            value (float): value for IDD Field `Spectrum 72`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `spectrum_72` or None if not set

        """
        return self["Spectrum 72"]

    @spectrum_72.setter
    def spectrum_72(self, value=None):
        """Corresponds to IDD field `Spectrum 72`"""
        self["Spectrum 72"] = value

    @property
    def wavelength_73(self):
        """field `Wavelength 73`

        Args:
            value (float): value for IDD Field `Wavelength 73`
                Units: micron

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `wavelength_73` or None if not set

        """
        return self["Wavelength 73"]

    @wavelength_73.setter
    def wavelength_73(self, value=None):
        """Corresponds to IDD field `Wavelength 73`"""
        self["Wavelength 73"] = value

    @property
    def spectrum_73(self):
        """field `Spectrum 73`

        Args:
            value (float): value for IDD Field `Spectrum 73`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `spectrum_73` or None if not set

        """
        return self["Spectrum 73"]

    @spectrum_73.setter
    def spectrum_73(self, value=None):
        """Corresponds to IDD field `Spectrum 73`"""
        self["Spectrum 73"] = value

    @property
    def wavelength_74(self):
        """field `Wavelength 74`

        Args:
            value (float): value for IDD Field `Wavelength 74`
                Units: micron

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `wavelength_74` or None if not set

        """
        return self["Wavelength 74"]

    @wavelength_74.setter
    def wavelength_74(self, value=None):
        """Corresponds to IDD field `Wavelength 74`"""
        self["Wavelength 74"] = value

    @property
    def spectrum_74(self):
        """field `Spectrum 74`

        Args:
            value (float): value for IDD Field `Spectrum 74`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `spectrum_74` or None if not set

        """
        return self["Spectrum 74"]

    @spectrum_74.setter
    def spectrum_74(self, value=None):
        """Corresponds to IDD field `Spectrum 74`"""
        self["Spectrum 74"] = value

    @property
    def wavelength_75(self):
        """field `Wavelength 75`

        Args:
            value (float): value for IDD Field `Wavelength 75`
                Units: micron

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `wavelength_75` or None if not set

        """
        return self["Wavelength 75"]

    @wavelength_75.setter
    def wavelength_75(self, value=None):
        """Corresponds to IDD field `Wavelength 75`"""
        self["Wavelength 75"] = value

    @property
    def spectrum_75(self):
        """field `Spectrum 75`

        Args:
            value (float): value for IDD Field `Spectrum 75`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `spectrum_75` or None if not set

        """
        return self["Spectrum 75"]

    @spectrum_75.setter
    def spectrum_75(self, value=None):
        """Corresponds to IDD field `Spectrum 75`"""
        self["Spectrum 75"] = value

    @property
    def wavelength_76(self):
        """field `Wavelength 76`

        Args:
            value (float): value for IDD Field `Wavelength 76`
                Units: micron

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `wavelength_76` or None if not set

        """
        return self["Wavelength 76"]

    @wavelength_76.setter
    def wavelength_76(self, value=None):
        """Corresponds to IDD field `Wavelength 76`"""
        self["Wavelength 76"] = value

    @property
    def spectrum_76(self):
        """field `Spectrum 76`

        Args:
            value (float): value for IDD Field `Spectrum 76`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `spectrum_76` or None if not set

        """
        return self["Spectrum 76"]

    @spectrum_76.setter
    def spectrum_76(self, value=None):
        """Corresponds to IDD field `Spectrum 76`"""
        self["Spectrum 76"] = value

    @property
    def wavelength_77(self):
        """field `Wavelength 77`

        Args:
            value (float): value for IDD Field `Wavelength 77`
                Units: micron

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `wavelength_77` or None if not set

        """
        return self["Wavelength 77"]

    @wavelength_77.setter
    def wavelength_77(self, value=None):
        """Corresponds to IDD field `Wavelength 77`"""
        self["Wavelength 77"] = value

    @property
    def spectrum_77(self):
        """field `Spectrum 77`

        Args:
            value (float): value for IDD Field `Spectrum 77`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `spectrum_77` or None if not set

        """
        return self["Spectrum 77"]

    @spectrum_77.setter
    def spectrum_77(self, value=None):
        """Corresponds to IDD field `Spectrum 77`"""
        self["Spectrum 77"] = value

    @property
    def wavelength_78(self):
        """field `Wavelength 78`

        Args:
            value (float): value for IDD Field `Wavelength 78`
                Units: micron

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `wavelength_78` or None if not set

        """
        return self["Wavelength 78"]

    @wavelength_78.setter
    def wavelength_78(self, value=None):
        """Corresponds to IDD field `Wavelength 78`"""
        self["Wavelength 78"] = value

    @property
    def spectrum_78(self):
        """field `Spectrum 78`

        Args:
            value (float): value for IDD Field `Spectrum 78`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `spectrum_78` or None if not set

        """
        return self["Spectrum 78"]

    @spectrum_78.setter
    def spectrum_78(self, value=None):
        """Corresponds to IDD field `Spectrum 78`"""
        self["Spectrum 78"] = value

    @property
    def wavelength_79(self):
        """field `Wavelength 79`

        Args:
            value (float): value for IDD Field `Wavelength 79`
                Units: micron

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `wavelength_79` or None if not set

        """
        return self["Wavelength 79"]

    @wavelength_79.setter
    def wavelength_79(self, value=None):
        """Corresponds to IDD field `Wavelength 79`"""
        self["Wavelength 79"] = value

    @property
    def spectrum_79(self):
        """field `Spectrum 79`

        Args:
            value (float): value for IDD Field `Spectrum 79`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `spectrum_79` or None if not set

        """
        return self["Spectrum 79"]

    @spectrum_79.setter
    def spectrum_79(self, value=None):
        """Corresponds to IDD field `Spectrum 79`"""
        self["Spectrum 79"] = value

    @property
    def wavelength_80(self):
        """field `Wavelength 80`

        Args:
            value (float): value for IDD Field `Wavelength 80`
                Units: micron

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `wavelength_80` or None if not set

        """
        return self["Wavelength 80"]

    @wavelength_80.setter
    def wavelength_80(self, value=None):
        """Corresponds to IDD field `Wavelength 80`"""
        self["Wavelength 80"] = value

    @property
    def spectrum_80(self):
        """field `Spectrum 80`

        Args:
            value (float): value for IDD Field `Spectrum 80`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `spectrum_80` or None if not set

        """
        return self["Spectrum 80"]

    @spectrum_80.setter
    def spectrum_80(self, value=None):
        """Corresponds to IDD field `Spectrum 80`"""
        self["Spectrum 80"] = value

    @property
    def wavelength_81(self):
        """field `Wavelength 81`

        Args:
            value (float): value for IDD Field `Wavelength 81`
                Units: micron

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `wavelength_81` or None if not set

        """
        return self["Wavelength 81"]

    @wavelength_81.setter
    def wavelength_81(self, value=None):
        """Corresponds to IDD field `Wavelength 81`"""
        self["Wavelength 81"] = value

    @property
    def spectrum_81(self):
        """field `Spectrum 81`

        Args:
            value (float): value for IDD Field `Spectrum 81`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `spectrum_81` or None if not set

        """
        return self["Spectrum 81"]

    @spectrum_81.setter
    def spectrum_81(self, value=None):
        """Corresponds to IDD field `Spectrum 81`"""
        self["Spectrum 81"] = value

    @property
    def wavelength_82(self):
        """field `Wavelength 82`

        Args:
            value (float): value for IDD Field `Wavelength 82`
                Units: micron

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `wavelength_82` or None if not set

        """
        return self["Wavelength 82"]

    @wavelength_82.setter
    def wavelength_82(self, value=None):
        """Corresponds to IDD field `Wavelength 82`"""
        self["Wavelength 82"] = value

    @property
    def spectrum_82(self):
        """field `Spectrum 82`

        Args:
            value (float): value for IDD Field `Spectrum 82`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `spectrum_82` or None if not set

        """
        return self["Spectrum 82"]

    @spectrum_82.setter
    def spectrum_82(self, value=None):
        """Corresponds to IDD field `Spectrum 82`"""
        self["Spectrum 82"] = value

    @property
    def wavelength_83(self):
        """field `Wavelength 83`

        Args:
            value (float): value for IDD Field `Wavelength 83`
                Units: micron

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `wavelength_83` or None if not set

        """
        return self["Wavelength 83"]

    @wavelength_83.setter
    def wavelength_83(self, value=None):
        """Corresponds to IDD field `Wavelength 83`"""
        self["Wavelength 83"] = value

    @property
    def spectrum_83(self):
        """field `Spectrum 83`

        Args:
            value (float): value for IDD Field `Spectrum 83`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `spectrum_83` or None if not set

        """
        return self["Spectrum 83"]

    @spectrum_83.setter
    def spectrum_83(self, value=None):
        """Corresponds to IDD field `Spectrum 83`"""
        self["Spectrum 83"] = value

    @property
    def wavelength_84(self):
        """field `Wavelength 84`

        Args:
            value (float): value for IDD Field `Wavelength 84`
                Units: micron

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `wavelength_84` or None if not set

        """
        return self["Wavelength 84"]

    @wavelength_84.setter
    def wavelength_84(self, value=None):
        """Corresponds to IDD field `Wavelength 84`"""
        self["Wavelength 84"] = value

    @property
    def spectrum_84(self):
        """field `Spectrum 84`

        Args:
            value (float): value for IDD Field `Spectrum 84`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `spectrum_84` or None if not set

        """
        return self["Spectrum 84"]

    @spectrum_84.setter
    def spectrum_84(self, value=None):
        """Corresponds to IDD field `Spectrum 84`"""
        self["Spectrum 84"] = value

    @property
    def wavelength_85(self):
        """field `Wavelength 85`

        Args:
            value (float): value for IDD Field `Wavelength 85`
                Units: micron

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `wavelength_85` or None if not set

        """
        return self["Wavelength 85"]

    @wavelength_85.setter
    def wavelength_85(self, value=None):
        """Corresponds to IDD field `Wavelength 85`"""
        self["Wavelength 85"] = value

    @property
    def spectrum_85(self):
        """field `Spectrum 85`

        Args:
            value (float): value for IDD Field `Spectrum 85`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `spectrum_85` or None if not set

        """
        return self["Spectrum 85"]

    @spectrum_85.setter
    def spectrum_85(self, value=None):
        """Corresponds to IDD field `Spectrum 85`"""
        self["Spectrum 85"] = value

    @property
    def wavelength_86(self):
        """field `Wavelength 86`

        Args:
            value (float): value for IDD Field `Wavelength 86`
                Units: micron

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `wavelength_86` or None if not set

        """
        return self["Wavelength 86"]

    @wavelength_86.setter
    def wavelength_86(self, value=None):
        """Corresponds to IDD field `Wavelength 86`"""
        self["Wavelength 86"] = value

    @property
    def spectrum_86(self):
        """field `Spectrum 86`

        Args:
            value (float): value for IDD Field `Spectrum 86`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `spectrum_86` or None if not set

        """
        return self["Spectrum 86"]

    @spectrum_86.setter
    def spectrum_86(self, value=None):
        """Corresponds to IDD field `Spectrum 86`"""
        self["Spectrum 86"] = value

    @property
    def wavelength_87(self):
        """field `Wavelength 87`

        Args:
            value (float): value for IDD Field `Wavelength 87`
                Units: micron

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `wavelength_87` or None if not set

        """
        return self["Wavelength 87"]

    @wavelength_87.setter
    def wavelength_87(self, value=None):
        """Corresponds to IDD field `Wavelength 87`"""
        self["Wavelength 87"] = value

    @property
    def spectrum_87(self):
        """field `Spectrum 87`

        Args:
            value (float): value for IDD Field `Spectrum 87`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `spectrum_87` or None if not set

        """
        return self["Spectrum 87"]

    @spectrum_87.setter
    def spectrum_87(self, value=None):
        """Corresponds to IDD field `Spectrum 87`"""
        self["Spectrum 87"] = value

    @property
    def wavelength_88(self):
        """field `Wavelength 88`

        Args:
            value (float): value for IDD Field `Wavelength 88`
                Units: micron

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `wavelength_88` or None if not set

        """
        return self["Wavelength 88"]

    @wavelength_88.setter
    def wavelength_88(self, value=None):
        """Corresponds to IDD field `Wavelength 88`"""
        self["Wavelength 88"] = value

    @property
    def spectrum_88(self):
        """field `Spectrum 88`

        Args:
            value (float): value for IDD Field `Spectrum 88`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `spectrum_88` or None if not set

        """
        return self["Spectrum 88"]

    @spectrum_88.setter
    def spectrum_88(self, value=None):
        """Corresponds to IDD field `Spectrum 88`"""
        self["Spectrum 88"] = value

    @property
    def wavelength_89(self):
        """field `Wavelength 89`

        Args:
            value (float): value for IDD Field `Wavelength 89`
                Units: micron

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `wavelength_89` or None if not set

        """
        return self["Wavelength 89"]

    @wavelength_89.setter
    def wavelength_89(self, value=None):
        """Corresponds to IDD field `Wavelength 89`"""
        self["Wavelength 89"] = value

    @property
    def spectrum_89(self):
        """field `Spectrum 89`

        Args:
            value (float): value for IDD Field `Spectrum 89`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `spectrum_89` or None if not set

        """
        return self["Spectrum 89"]

    @spectrum_89.setter
    def spectrum_89(self, value=None):
        """Corresponds to IDD field `Spectrum 89`"""
        self["Spectrum 89"] = value

    @property
    def wavelength_90(self):
        """field `Wavelength 90`

        Args:
            value (float): value for IDD Field `Wavelength 90`
                Units: micron

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `wavelength_90` or None if not set

        """
        return self["Wavelength 90"]

    @wavelength_90.setter
    def wavelength_90(self, value=None):
        """Corresponds to IDD field `Wavelength 90`"""
        self["Wavelength 90"] = value

    @property
    def spectrum_90(self):
        """field `Spectrum 90`

        Args:
            value (float): value for IDD Field `Spectrum 90`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `spectrum_90` or None if not set

        """
        return self["Spectrum 90"]

    @spectrum_90.setter
    def spectrum_90(self, value=None):
        """Corresponds to IDD field `Spectrum 90`"""
        self["Spectrum 90"] = value

    @property
    def wavelength_91(self):
        """field `Wavelength 91`

        Args:
            value (float): value for IDD Field `Wavelength 91`
                Units: micron

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `wavelength_91` or None if not set

        """
        return self["Wavelength 91"]

    @wavelength_91.setter
    def wavelength_91(self, value=None):
        """Corresponds to IDD field `Wavelength 91`"""
        self["Wavelength 91"] = value

    @property
    def spectrum_91(self):
        """field `Spectrum 91`

        Args:
            value (float): value for IDD Field `Spectrum 91`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `spectrum_91` or None if not set

        """
        return self["Spectrum 91"]

    @spectrum_91.setter
    def spectrum_91(self, value=None):
        """Corresponds to IDD field `Spectrum 91`"""
        self["Spectrum 91"] = value

    @property
    def wavelength_92(self):
        """field `Wavelength 92`

        Args:
            value (float): value for IDD Field `Wavelength 92`
                Units: micron

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `wavelength_92` or None if not set

        """
        return self["Wavelength 92"]

    @wavelength_92.setter
    def wavelength_92(self, value=None):
        """Corresponds to IDD field `Wavelength 92`"""
        self["Wavelength 92"] = value

    @property
    def spectrum_92(self):
        """field `Spectrum 92`

        Args:
            value (float): value for IDD Field `Spectrum 92`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `spectrum_92` or None if not set

        """
        return self["Spectrum 92"]

    @spectrum_92.setter
    def spectrum_92(self, value=None):
        """Corresponds to IDD field `Spectrum 92`"""
        self["Spectrum 92"] = value

    @property
    def wavelength_93(self):
        """field `Wavelength 93`

        Args:
            value (float): value for IDD Field `Wavelength 93`
                Units: micron

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `wavelength_93` or None if not set

        """
        return self["Wavelength 93"]

    @wavelength_93.setter
    def wavelength_93(self, value=None):
        """Corresponds to IDD field `Wavelength 93`"""
        self["Wavelength 93"] = value

    @property
    def spectrum_93(self):
        """field `Spectrum 93`

        Args:
            value (float): value for IDD Field `Spectrum 93`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `spectrum_93` or None if not set

        """
        return self["Spectrum 93"]

    @spectrum_93.setter
    def spectrum_93(self, value=None):
        """Corresponds to IDD field `Spectrum 93`"""
        self["Spectrum 93"] = value

    @property
    def wavelength_94(self):
        """field `Wavelength 94`

        Args:
            value (float): value for IDD Field `Wavelength 94`
                Units: micron

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `wavelength_94` or None if not set

        """
        return self["Wavelength 94"]

    @wavelength_94.setter
    def wavelength_94(self, value=None):
        """Corresponds to IDD field `Wavelength 94`"""
        self["Wavelength 94"] = value

    @property
    def spectrum_94(self):
        """field `Spectrum 94`

        Args:
            value (float): value for IDD Field `Spectrum 94`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `spectrum_94` or None if not set

        """
        return self["Spectrum 94"]

    @spectrum_94.setter
    def spectrum_94(self, value=None):
        """Corresponds to IDD field `Spectrum 94`"""
        self["Spectrum 94"] = value

    @property
    def wavelength_95(self):
        """field `Wavelength 95`

        Args:
            value (float): value for IDD Field `Wavelength 95`
                Units: micron

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `wavelength_95` or None if not set

        """
        return self["Wavelength 95"]

    @wavelength_95.setter
    def wavelength_95(self, value=None):
        """Corresponds to IDD field `Wavelength 95`"""
        self["Wavelength 95"] = value

    @property
    def spectrum_95(self):
        """field `Spectrum 95`

        Args:
            value (float): value for IDD Field `Spectrum 95`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `spectrum_95` or None if not set

        """
        return self["Spectrum 95"]

    @spectrum_95.setter
    def spectrum_95(self, value=None):
        """Corresponds to IDD field `Spectrum 95`"""
        self["Spectrum 95"] = value

    @property
    def wavelength_96(self):
        """field `Wavelength 96`

        Args:
            value (float): value for IDD Field `Wavelength 96`
                Units: micron

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `wavelength_96` or None if not set

        """
        return self["Wavelength 96"]

    @wavelength_96.setter
    def wavelength_96(self, value=None):
        """Corresponds to IDD field `Wavelength 96`"""
        self["Wavelength 96"] = value

    @property
    def spectrum_96(self):
        """field `Spectrum 96`

        Args:
            value (float): value for IDD Field `Spectrum 96`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `spectrum_96` or None if not set

        """
        return self["Spectrum 96"]

    @spectrum_96.setter
    def spectrum_96(self, value=None):
        """Corresponds to IDD field `Spectrum 96`"""
        self["Spectrum 96"] = value

    @property
    def wavelength_97(self):
        """field `Wavelength 97`

        Args:
            value (float): value for IDD Field `Wavelength 97`
                Units: micron

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `wavelength_97` or None if not set

        """
        return self["Wavelength 97"]

    @wavelength_97.setter
    def wavelength_97(self, value=None):
        """Corresponds to IDD field `Wavelength 97`"""
        self["Wavelength 97"] = value

    @property
    def spectrum_97(self):
        """field `Spectrum 97`

        Args:
            value (float): value for IDD Field `Spectrum 97`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `spectrum_97` or None if not set

        """
        return self["Spectrum 97"]

    @spectrum_97.setter
    def spectrum_97(self, value=None):
        """Corresponds to IDD field `Spectrum 97`"""
        self["Spectrum 97"] = value

    @property
    def wavelength_98(self):
        """field `Wavelength 98`

        Args:
            value (float): value for IDD Field `Wavelength 98`
                Units: micron

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `wavelength_98` or None if not set

        """
        return self["Wavelength 98"]

    @wavelength_98.setter
    def wavelength_98(self, value=None):
        """Corresponds to IDD field `Wavelength 98`"""
        self["Wavelength 98"] = value

    @property
    def spectrum_98(self):
        """field `Spectrum 98`

        Args:
            value (float): value for IDD Field `Spectrum 98`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `spectrum_98` or None if not set

        """
        return self["Spectrum 98"]

    @spectrum_98.setter
    def spectrum_98(self, value=None):
        """Corresponds to IDD field `Spectrum 98`"""
        self["Spectrum 98"] = value

    @property
    def wavelength_99(self):
        """field `Wavelength 99`

        Args:
            value (float): value for IDD Field `Wavelength 99`
                Units: micron

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `wavelength_99` or None if not set

        """
        return self["Wavelength 99"]

    @wavelength_99.setter
    def wavelength_99(self, value=None):
        """Corresponds to IDD field `Wavelength 99`"""
        self["Wavelength 99"] = value

    @property
    def spectrum_99(self):
        """field `Spectrum 99`

        Args:
            value (float): value for IDD Field `Spectrum 99`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `spectrum_99` or None if not set

        """
        return self["Spectrum 99"]

    @spectrum_99.setter
    def spectrum_99(self, value=None):
        """Corresponds to IDD field `Spectrum 99`"""
        self["Spectrum 99"] = value

    @property
    def wavelength_100(self):
        """field `Wavelength 100`

        Args:
            value (float): value for IDD Field `Wavelength 100`
                Units: micron

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `wavelength_100` or None if not set

        """
        return self["Wavelength 100"]

    @wavelength_100.setter
    def wavelength_100(self, value=None):
        """Corresponds to IDD field `Wavelength 100`"""
        self["Wavelength 100"] = value

    @property
    def spectrum_100(self):
        """field `Spectrum 100`

        Args:
            value (float): value for IDD Field `Spectrum 100`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `spectrum_100` or None if not set

        """
        return self["Spectrum 100"]

    @spectrum_100.setter
    def spectrum_100(self, value=None):
        """Corresponds to IDD field `Spectrum 100`"""
        self["Spectrum 100"] = value

    @property
    def wavelength_101(self):
        """field `Wavelength 101`

        Args:
            value (float): value for IDD Field `Wavelength 101`
                Units: micron

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `wavelength_101` or None if not set

        """
        return self["Wavelength 101"]

    @wavelength_101.setter
    def wavelength_101(self, value=None):
        """Corresponds to IDD field `Wavelength 101`"""
        self["Wavelength 101"] = value

    @property
    def spectrum_101(self):
        """field `Spectrum 101`

        Args:
            value (float): value for IDD Field `Spectrum 101`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `spectrum_101` or None if not set

        """
        return self["Spectrum 101"]

    @spectrum_101.setter
    def spectrum_101(self, value=None):
        """Corresponds to IDD field `Spectrum 101`"""
        self["Spectrum 101"] = value

    @property
    def wavelength_102(self):
        """field `Wavelength 102`

        Args:
            value (float): value for IDD Field `Wavelength 102`
                Units: micron

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `wavelength_102` or None if not set

        """
        return self["Wavelength 102"]

    @wavelength_102.setter
    def wavelength_102(self, value=None):
        """Corresponds to IDD field `Wavelength 102`"""
        self["Wavelength 102"] = value

    @property
    def spectrum_102(self):
        """field `Spectrum 102`

        Args:
            value (float): value for IDD Field `Spectrum 102`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `spectrum_102` or None if not set

        """
        return self["Spectrum 102"]

    @spectrum_102.setter
    def spectrum_102(self, value=None):
        """Corresponds to IDD field `Spectrum 102`"""
        self["Spectrum 102"] = value

    @property
    def wavelength_103(self):
        """field `Wavelength 103`

        Args:
            value (float): value for IDD Field `Wavelength 103`
                Units: micron

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `wavelength_103` or None if not set

        """
        return self["Wavelength 103"]

    @wavelength_103.setter
    def wavelength_103(self, value=None):
        """Corresponds to IDD field `Wavelength 103`"""
        self["Wavelength 103"] = value

    @property
    def spectrum_103(self):
        """field `Spectrum 103`

        Args:
            value (float): value for IDD Field `Spectrum 103`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `spectrum_103` or None if not set

        """
        return self["Spectrum 103"]

    @spectrum_103.setter
    def spectrum_103(self, value=None):
        """Corresponds to IDD field `Spectrum 103`"""
        self["Spectrum 103"] = value

    @property
    def wavelength_104(self):
        """field `Wavelength 104`

        Args:
            value (float): value for IDD Field `Wavelength 104`
                Units: micron

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `wavelength_104` or None if not set

        """
        return self["Wavelength 104"]

    @wavelength_104.setter
    def wavelength_104(self, value=None):
        """Corresponds to IDD field `Wavelength 104`"""
        self["Wavelength 104"] = value

    @property
    def spectrum_104(self):
        """field `Spectrum 104`

        Args:
            value (float): value for IDD Field `Spectrum 104`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `spectrum_104` or None if not set

        """
        return self["Spectrum 104"]

    @spectrum_104.setter
    def spectrum_104(self, value=None):
        """Corresponds to IDD field `Spectrum 104`"""
        self["Spectrum 104"] = value

    @property
    def wavelength_105(self):
        """field `Wavelength 105`

        Args:
            value (float): value for IDD Field `Wavelength 105`
                Units: micron

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `wavelength_105` or None if not set

        """
        return self["Wavelength 105"]

    @wavelength_105.setter
    def wavelength_105(self, value=None):
        """Corresponds to IDD field `Wavelength 105`"""
        self["Wavelength 105"] = value

    @property
    def spectrum_105(self):
        """field `Spectrum 105`

        Args:
            value (float): value for IDD Field `Spectrum 105`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `spectrum_105` or None if not set

        """
        return self["Spectrum 105"]

    @spectrum_105.setter
    def spectrum_105(self, value=None):
        """Corresponds to IDD field `Spectrum 105`"""
        self["Spectrum 105"] = value

    @property
    def wavelength_106(self):
        """field `Wavelength 106`

        Args:
            value (float): value for IDD Field `Wavelength 106`
                Units: micron

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `wavelength_106` or None if not set

        """
        return self["Wavelength 106"]

    @wavelength_106.setter
    def wavelength_106(self, value=None):
        """Corresponds to IDD field `Wavelength 106`"""
        self["Wavelength 106"] = value

    @property
    def spectrum_106(self):
        """field `Spectrum 106`

        Args:
            value (float): value for IDD Field `Spectrum 106`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `spectrum_106` or None if not set

        """
        return self["Spectrum 106"]

    @spectrum_106.setter
    def spectrum_106(self, value=None):
        """Corresponds to IDD field `Spectrum 106`"""
        self["Spectrum 106"] = value

    @property
    def wavelength_107(self):
        """field `Wavelength 107`

        Args:
            value (float): value for IDD Field `Wavelength 107`
                Units: micron

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `wavelength_107` or None if not set

        """
        return self["Wavelength 107"]

    @wavelength_107.setter
    def wavelength_107(self, value=None):
        """Corresponds to IDD field `Wavelength 107`"""
        self["Wavelength 107"] = value

    @property
    def spectrum_107(self):
        """field `Spectrum 107`

        Args:
            value (float): value for IDD Field `Spectrum 107`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `spectrum_107` or None if not set

        """
        return self["Spectrum 107"]

    @spectrum_107.setter
    def spectrum_107(self, value=None):
        """Corresponds to IDD field `Spectrum 107`"""
        self["Spectrum 107"] = value


