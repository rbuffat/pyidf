from collections import OrderedDict
import logging
import re

logger = logging.getLogger(__name__)
logger.addHandler(logging.NullHandler())

class DaylightingControls(object):
    """ Corresponds to IDD object `Daylighting:Controls`
        Dimming of overhead electric lighting is determined from
        interior daylight illuminance calculated at one or two reference points.
        reference points are given in coordinates specified in the GlobalGeometryRules object
        Daylighting Reference Point CoordinateSystem field
        Glare from daylighting is also calculated.
    """
    internal_name = "Daylighting:Controls"
    field_count = 20
    required_fields = ["Zone Name", "X-Coordinate of First Reference Point", "Y-Coordinate of First Reference Point", "Glare Calculation Azimuth Angle of View Direction Clockwise from Zone y-Axis"]
    extensible_fields = 0
    format = None
    min_fields = 19
    extensible_keys = []

    def __init__(self):
        """ Init data dictionary object for IDD  `Daylighting:Controls`
        """
        self._data = OrderedDict()
        self._data["Zone Name"] = None
        self._data["Total Daylighting Reference Points"] = None
        self._data["X-Coordinate of First Reference Point"] = None
        self._data["Y-Coordinate of First Reference Point"] = None
        self._data["Z-Coordinate of First Reference Point"] = None
        self._data["X-Coordinate of Second Reference Point"] = None
        self._data["Y-Coordinate of Second Reference Point"] = None
        self._data["Z-Coordinate of Second Reference Point"] = None
        self._data["Fraction of Zone Controlled by First Reference Point"] = None
        self._data["Fraction of Zone Controlled by Second Reference Point"] = None
        self._data["Illuminance Setpoint at First Reference Point"] = None
        self._data["Illuminance Setpoint at Second Reference Point"] = None
        self._data["Lighting Control Type"] = None
        self._data["Glare Calculation Azimuth Angle of View Direction Clockwise from Zone y-Axis"] = None
        self._data["Maximum Allowable Discomfort Glare Index"] = None
        self._data["Minimum Input Power Fraction for Continuous Dimming Control"] = None
        self._data["Minimum Light Output Fraction for Continuous Dimming Control"] = None
        self._data["Number of Stepped Control Steps"] = None
        self._data["Probability Lighting will be Reset When Needed in Manual Stepped Control"] = None
        self._data["Availability Schedule Name"] = None
        self._data["extensibles"] = []
        self.strict = True

    def read(self, vals, strict=False):
        """ Read values

        Args:
            vals (list): list of strings representing values
        """
        old_strict = self.strict
        self.strict = strict
        i = 0
        if len(vals[i]) == 0:
            self.zone_name = None
        else:
            self.zone_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.total_daylighting_reference_points = None
        else:
            self.total_daylighting_reference_points = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.xcoordinate_of_first_reference_point = None
        else:
            self.xcoordinate_of_first_reference_point = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.ycoordinate_of_first_reference_point = None
        else:
            self.ycoordinate_of_first_reference_point = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.zcoordinate_of_first_reference_point = None
        else:
            self.zcoordinate_of_first_reference_point = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.xcoordinate_of_second_reference_point = None
        else:
            self.xcoordinate_of_second_reference_point = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.ycoordinate_of_second_reference_point = None
        else:
            self.ycoordinate_of_second_reference_point = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.zcoordinate_of_second_reference_point = None
        else:
            self.zcoordinate_of_second_reference_point = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.fraction_of_zone_controlled_by_first_reference_point = None
        else:
            self.fraction_of_zone_controlled_by_first_reference_point = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.fraction_of_zone_controlled_by_second_reference_point = None
        else:
            self.fraction_of_zone_controlled_by_second_reference_point = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.illuminance_setpoint_at_first_reference_point = None
        else:
            self.illuminance_setpoint_at_first_reference_point = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.illuminance_setpoint_at_second_reference_point = None
        else:
            self.illuminance_setpoint_at_second_reference_point = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.lighting_control_type = None
        else:
            self.lighting_control_type = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.glare_calculation_azimuth_angle_of_view_direction_clockwise_from_zone_yaxis = None
        else:
            self.glare_calculation_azimuth_angle_of_view_direction_clockwise_from_zone_yaxis = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.maximum_allowable_discomfort_glare_index = None
        else:
            self.maximum_allowable_discomfort_glare_index = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.minimum_input_power_fraction_for_continuous_dimming_control = None
        else:
            self.minimum_input_power_fraction_for_continuous_dimming_control = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.minimum_light_output_fraction_for_continuous_dimming_control = None
        else:
            self.minimum_light_output_fraction_for_continuous_dimming_control = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.number_of_stepped_control_steps = None
        else:
            self.number_of_stepped_control_steps = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.probability_lighting_will_be_reset_when_needed_in_manual_stepped_control = None
        else:
            self.probability_lighting_will_be_reset_when_needed_in_manual_stepped_control = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.availability_schedule_name = None
        else:
            self.availability_schedule_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        self.strict = old_strict

    @property
    def zone_name(self):
        """Get zone_name

        Returns:
            str: the value of `zone_name` or None if not set
        """
        return self._data["Zone Name"]

    @zone_name.setter
    def zone_name(self, value=None):
        """  Corresponds to IDD Field `Zone Name`

        Args:
            value (str): value for IDD Field `Zone Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str'
                                 ' for field `DaylightingControls.zone_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `DaylightingControls.zone_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `DaylightingControls.zone_name`')
        self._data["Zone Name"] = value

    @property
    def total_daylighting_reference_points(self):
        """Get total_daylighting_reference_points

        Returns:
            int: the value of `total_daylighting_reference_points` or None if not set
        """
        return self._data["Total Daylighting Reference Points"]

    @total_daylighting_reference_points.setter
    def total_daylighting_reference_points(self, value=1):
        """  Corresponds to IDD Field `Total Daylighting Reference Points`

        Args:
            value (int): value for IDD Field `Total Daylighting Reference Points`
                Default value: 1
                value >= 1
                value <= 2
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = int(value)
            except ValueError:
                if not self.strict:
                    try:
                        conv_value = int(float(value))
                        logger.warn('Cast float {} to int {}, precision may be lost '
                                     'for field `DaylightingControls.total_daylighting_reference_points`'.format(value, conv_value))
                        value = conv_value
                    except ValueError:
                        raise ValueError('value {} need to be of type int '
                                         'for field `DaylightingControls.total_daylighting_reference_points`'.format(value))
            if value < 1:
                raise ValueError('value need to be greater or equal 1 '
                                 'for field `DaylightingControls.total_daylighting_reference_points`')
            if value > 2:
                raise ValueError('value need to be smaller 2 '
                                 'for field `DaylightingControls.total_daylighting_reference_points`')
        self._data["Total Daylighting Reference Points"] = value

    @property
    def xcoordinate_of_first_reference_point(self):
        """Get xcoordinate_of_first_reference_point

        Returns:
            float: the value of `xcoordinate_of_first_reference_point` or None if not set
        """
        return self._data["X-Coordinate of First Reference Point"]

    @xcoordinate_of_first_reference_point.setter
    def xcoordinate_of_first_reference_point(self, value=None):
        """  Corresponds to IDD Field `X-Coordinate of First Reference Point`

        Args:
            value (float): value for IDD Field `X-Coordinate of First Reference Point`
                Units: m
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float'
                                 ' for field `DaylightingControls.xcoordinate_of_first_reference_point`'.format(value))
        self._data["X-Coordinate of First Reference Point"] = value

    @property
    def ycoordinate_of_first_reference_point(self):
        """Get ycoordinate_of_first_reference_point

        Returns:
            float: the value of `ycoordinate_of_first_reference_point` or None if not set
        """
        return self._data["Y-Coordinate of First Reference Point"]

    @ycoordinate_of_first_reference_point.setter
    def ycoordinate_of_first_reference_point(self, value=None):
        """  Corresponds to IDD Field `Y-Coordinate of First Reference Point`

        Args:
            value (float): value for IDD Field `Y-Coordinate of First Reference Point`
                Units: m
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float'
                                 ' for field `DaylightingControls.ycoordinate_of_first_reference_point`'.format(value))
        self._data["Y-Coordinate of First Reference Point"] = value

    @property
    def zcoordinate_of_first_reference_point(self):
        """Get zcoordinate_of_first_reference_point

        Returns:
            float: the value of `zcoordinate_of_first_reference_point` or None if not set
        """
        return self._data["Z-Coordinate of First Reference Point"]

    @zcoordinate_of_first_reference_point.setter
    def zcoordinate_of_first_reference_point(self, value=0.8):
        """  Corresponds to IDD Field `Z-Coordinate of First Reference Point`

        Args:
            value (float): value for IDD Field `Z-Coordinate of First Reference Point`
                Units: m
                Default value: 0.8
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float'
                                 ' for field `DaylightingControls.zcoordinate_of_first_reference_point`'.format(value))
        self._data["Z-Coordinate of First Reference Point"] = value

    @property
    def xcoordinate_of_second_reference_point(self):
        """Get xcoordinate_of_second_reference_point

        Returns:
            float: the value of `xcoordinate_of_second_reference_point` or None if not set
        """
        return self._data["X-Coordinate of Second Reference Point"]

    @xcoordinate_of_second_reference_point.setter
    def xcoordinate_of_second_reference_point(self, value=None):
        """  Corresponds to IDD Field `X-Coordinate of Second Reference Point`
        Required if Total Daylighting Reference Points = 2

        Args:
            value (float): value for IDD Field `X-Coordinate of Second Reference Point`
                Units: m
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float'
                                 ' for field `DaylightingControls.xcoordinate_of_second_reference_point`'.format(value))
        self._data["X-Coordinate of Second Reference Point"] = value

    @property
    def ycoordinate_of_second_reference_point(self):
        """Get ycoordinate_of_second_reference_point

        Returns:
            float: the value of `ycoordinate_of_second_reference_point` or None if not set
        """
        return self._data["Y-Coordinate of Second Reference Point"]

    @ycoordinate_of_second_reference_point.setter
    def ycoordinate_of_second_reference_point(self, value=None):
        """  Corresponds to IDD Field `Y-Coordinate of Second Reference Point`
        Required if Total Daylighting Reference Points = 2

        Args:
            value (float): value for IDD Field `Y-Coordinate of Second Reference Point`
                Units: m
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float'
                                 ' for field `DaylightingControls.ycoordinate_of_second_reference_point`'.format(value))
        self._data["Y-Coordinate of Second Reference Point"] = value

    @property
    def zcoordinate_of_second_reference_point(self):
        """Get zcoordinate_of_second_reference_point

        Returns:
            float: the value of `zcoordinate_of_second_reference_point` or None if not set
        """
        return self._data["Z-Coordinate of Second Reference Point"]

    @zcoordinate_of_second_reference_point.setter
    def zcoordinate_of_second_reference_point(self, value=0.8):
        """  Corresponds to IDD Field `Z-Coordinate of Second Reference Point`

        Args:
            value (float): value for IDD Field `Z-Coordinate of Second Reference Point`
                Units: m
                Default value: 0.8
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float'
                                 ' for field `DaylightingControls.zcoordinate_of_second_reference_point`'.format(value))
        self._data["Z-Coordinate of Second Reference Point"] = value

    @property
    def fraction_of_zone_controlled_by_first_reference_point(self):
        """Get fraction_of_zone_controlled_by_first_reference_point

        Returns:
            float: the value of `fraction_of_zone_controlled_by_first_reference_point` or None if not set
        """
        return self._data["Fraction of Zone Controlled by First Reference Point"]

    @fraction_of_zone_controlled_by_first_reference_point.setter
    def fraction_of_zone_controlled_by_first_reference_point(self, value=1.0):
        """  Corresponds to IDD Field `Fraction of Zone Controlled by First Reference Point`

        Args:
            value (float): value for IDD Field `Fraction of Zone Controlled by First Reference Point`
                Default value: 1.0
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
                raise ValueError('value {} need to be of type float'
                                 ' for field `DaylightingControls.fraction_of_zone_controlled_by_first_reference_point`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `DaylightingControls.fraction_of_zone_controlled_by_first_reference_point`')
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `DaylightingControls.fraction_of_zone_controlled_by_first_reference_point`')
        self._data["Fraction of Zone Controlled by First Reference Point"] = value

    @property
    def fraction_of_zone_controlled_by_second_reference_point(self):
        """Get fraction_of_zone_controlled_by_second_reference_point

        Returns:
            float: the value of `fraction_of_zone_controlled_by_second_reference_point` or None if not set
        """
        return self._data["Fraction of Zone Controlled by Second Reference Point"]

    @fraction_of_zone_controlled_by_second_reference_point.setter
    def fraction_of_zone_controlled_by_second_reference_point(self, value=0.0):
        """  Corresponds to IDD Field `Fraction of Zone Controlled by Second Reference Point`

        Args:
            value (float): value for IDD Field `Fraction of Zone Controlled by Second Reference Point`
                Default value: 0.0
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
                raise ValueError('value {} need to be of type float'
                                 ' for field `DaylightingControls.fraction_of_zone_controlled_by_second_reference_point`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `DaylightingControls.fraction_of_zone_controlled_by_second_reference_point`')
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `DaylightingControls.fraction_of_zone_controlled_by_second_reference_point`')
        self._data["Fraction of Zone Controlled by Second Reference Point"] = value

    @property
    def illuminance_setpoint_at_first_reference_point(self):
        """Get illuminance_setpoint_at_first_reference_point

        Returns:
            float: the value of `illuminance_setpoint_at_first_reference_point` or None if not set
        """
        return self._data["Illuminance Setpoint at First Reference Point"]

    @illuminance_setpoint_at_first_reference_point.setter
    def illuminance_setpoint_at_first_reference_point(self, value=500.0):
        """  Corresponds to IDD Field `Illuminance Setpoint at First Reference Point`

        Args:
            value (float): value for IDD Field `Illuminance Setpoint at First Reference Point`
                Units: lux
                Default value: 500.0
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
                raise ValueError('value {} need to be of type float'
                                 ' for field `DaylightingControls.illuminance_setpoint_at_first_reference_point`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `DaylightingControls.illuminance_setpoint_at_first_reference_point`')
        self._data["Illuminance Setpoint at First Reference Point"] = value

    @property
    def illuminance_setpoint_at_second_reference_point(self):
        """Get illuminance_setpoint_at_second_reference_point

        Returns:
            float: the value of `illuminance_setpoint_at_second_reference_point` or None if not set
        """
        return self._data["Illuminance Setpoint at Second Reference Point"]

    @illuminance_setpoint_at_second_reference_point.setter
    def illuminance_setpoint_at_second_reference_point(self, value=500.0):
        """  Corresponds to IDD Field `Illuminance Setpoint at Second Reference Point`

        Args:
            value (float): value for IDD Field `Illuminance Setpoint at Second Reference Point`
                Units: lux
                Default value: 500.0
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
                raise ValueError('value {} need to be of type float'
                                 ' for field `DaylightingControls.illuminance_setpoint_at_second_reference_point`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `DaylightingControls.illuminance_setpoint_at_second_reference_point`')
        self._data["Illuminance Setpoint at Second Reference Point"] = value

    @property
    def lighting_control_type(self):
        """Get lighting_control_type

        Returns:
            int: the value of `lighting_control_type` or None if not set
        """
        return self._data["Lighting Control Type"]

    @lighting_control_type.setter
    def lighting_control_type(self, value=1):
        """  Corresponds to IDD Field `Lighting Control Type`
        1=continuous,2=stepped,3=continuous/off

        Args:
            value (int): value for IDD Field `Lighting Control Type`
                Default value: 1
                value >= 1
                value <= 3
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = int(value)
            except ValueError:
                if not self.strict:
                    try:
                        conv_value = int(float(value))
                        logger.warn('Cast float {} to int {}, precision may be lost '
                                     'for field `DaylightingControls.lighting_control_type`'.format(value, conv_value))
                        value = conv_value
                    except ValueError:
                        raise ValueError('value {} need to be of type int '
                                         'for field `DaylightingControls.lighting_control_type`'.format(value))
            if value < 1:
                raise ValueError('value need to be greater or equal 1 '
                                 'for field `DaylightingControls.lighting_control_type`')
            if value > 3:
                raise ValueError('value need to be smaller 3 '
                                 'for field `DaylightingControls.lighting_control_type`')
        self._data["Lighting Control Type"] = value

    @property
    def glare_calculation_azimuth_angle_of_view_direction_clockwise_from_zone_yaxis(self):
        """Get glare_calculation_azimuth_angle_of_view_direction_clockwise_from_zone_yaxis

        Returns:
            float: the value of `glare_calculation_azimuth_angle_of_view_direction_clockwise_from_zone_yaxis` or None if not set
        """
        return self._data["Glare Calculation Azimuth Angle of View Direction Clockwise from Zone y-Axis"]

    @glare_calculation_azimuth_angle_of_view_direction_clockwise_from_zone_yaxis.setter
    def glare_calculation_azimuth_angle_of_view_direction_clockwise_from_zone_yaxis(self, value=None):
        """  Corresponds to IDD Field `Glare Calculation Azimuth Angle of View Direction Clockwise from Zone y-Axis`

        Args:
            value (float): value for IDD Field `Glare Calculation Azimuth Angle of View Direction Clockwise from Zone y-Axis`
                Units: deg
                value >= 0.0
                value <= 360.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float'
                                 ' for field `DaylightingControls.glare_calculation_azimuth_angle_of_view_direction_clockwise_from_zone_yaxis`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `DaylightingControls.glare_calculation_azimuth_angle_of_view_direction_clockwise_from_zone_yaxis`')
            if value > 360.0:
                raise ValueError('value need to be smaller 360.0 '
                                 'for field `DaylightingControls.glare_calculation_azimuth_angle_of_view_direction_clockwise_from_zone_yaxis`')
        self._data["Glare Calculation Azimuth Angle of View Direction Clockwise from Zone y-Axis"] = value

    @property
    def maximum_allowable_discomfort_glare_index(self):
        """Get maximum_allowable_discomfort_glare_index

        Returns:
            float: the value of `maximum_allowable_discomfort_glare_index` or None if not set
        """
        return self._data["Maximum Allowable Discomfort Glare Index"]

    @maximum_allowable_discomfort_glare_index.setter
    def maximum_allowable_discomfort_glare_index(self, value=22.0):
        """  Corresponds to IDD Field `Maximum Allowable Discomfort Glare Index`
        The default is for general office work

        Args:
            value (float): value for IDD Field `Maximum Allowable Discomfort Glare Index`
                Default value: 22.0
                value >= 1.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float'
                                 ' for field `DaylightingControls.maximum_allowable_discomfort_glare_index`'.format(value))
            if value < 1.0:
                raise ValueError('value need to be greater or equal 1.0 '
                                 'for field `DaylightingControls.maximum_allowable_discomfort_glare_index`')
        self._data["Maximum Allowable Discomfort Glare Index"] = value

    @property
    def minimum_input_power_fraction_for_continuous_dimming_control(self):
        """Get minimum_input_power_fraction_for_continuous_dimming_control

        Returns:
            float: the value of `minimum_input_power_fraction_for_continuous_dimming_control` or None if not set
        """
        return self._data["Minimum Input Power Fraction for Continuous Dimming Control"]

    @minimum_input_power_fraction_for_continuous_dimming_control.setter
    def minimum_input_power_fraction_for_continuous_dimming_control(self, value=0.3):
        """  Corresponds to IDD Field `Minimum Input Power Fraction for Continuous Dimming Control`

        Args:
            value (float): value for IDD Field `Minimum Input Power Fraction for Continuous Dimming Control`
                Default value: 0.3
                value >= 0.0
                value <= 0.6
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float'
                                 ' for field `DaylightingControls.minimum_input_power_fraction_for_continuous_dimming_control`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `DaylightingControls.minimum_input_power_fraction_for_continuous_dimming_control`')
            if value > 0.6:
                raise ValueError('value need to be smaller 0.6 '
                                 'for field `DaylightingControls.minimum_input_power_fraction_for_continuous_dimming_control`')
        self._data["Minimum Input Power Fraction for Continuous Dimming Control"] = value

    @property
    def minimum_light_output_fraction_for_continuous_dimming_control(self):
        """Get minimum_light_output_fraction_for_continuous_dimming_control

        Returns:
            float: the value of `minimum_light_output_fraction_for_continuous_dimming_control` or None if not set
        """
        return self._data["Minimum Light Output Fraction for Continuous Dimming Control"]

    @minimum_light_output_fraction_for_continuous_dimming_control.setter
    def minimum_light_output_fraction_for_continuous_dimming_control(self, value=0.2):
        """  Corresponds to IDD Field `Minimum Light Output Fraction for Continuous Dimming Control`

        Args:
            value (float): value for IDD Field `Minimum Light Output Fraction for Continuous Dimming Control`
                Default value: 0.2
                value >= 0.0
                value <= 0.6
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float'
                                 ' for field `DaylightingControls.minimum_light_output_fraction_for_continuous_dimming_control`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `DaylightingControls.minimum_light_output_fraction_for_continuous_dimming_control`')
            if value > 0.6:
                raise ValueError('value need to be smaller 0.6 '
                                 'for field `DaylightingControls.minimum_light_output_fraction_for_continuous_dimming_control`')
        self._data["Minimum Light Output Fraction for Continuous Dimming Control"] = value

    @property
    def number_of_stepped_control_steps(self):
        """Get number_of_stepped_control_steps

        Returns:
            int: the value of `number_of_stepped_control_steps` or None if not set
        """
        return self._data["Number of Stepped Control Steps"]

    @number_of_stepped_control_steps.setter
    def number_of_stepped_control_steps(self, value=1):
        """  Corresponds to IDD Field `Number of Stepped Control Steps`
        for Lighting Control Type=2, this field cannot be zero.

        Args:
            value (int): value for IDD Field `Number of Stepped Control Steps`
                Default value: 1
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = int(value)
            except ValueError:
                if not self.strict:
                    try:
                        conv_value = int(float(value))
                        logger.warn('Cast float {} to int {}, precision may be lost '
                                     'for field `DaylightingControls.number_of_stepped_control_steps`'.format(value, conv_value))
                        value = conv_value
                    except ValueError:
                        raise ValueError('value {} need to be of type int '
                                         'for field `DaylightingControls.number_of_stepped_control_steps`'.format(value))
        self._data["Number of Stepped Control Steps"] = value

    @property
    def probability_lighting_will_be_reset_when_needed_in_manual_stepped_control(self):
        """Get probability_lighting_will_be_reset_when_needed_in_manual_stepped_control

        Returns:
            float: the value of `probability_lighting_will_be_reset_when_needed_in_manual_stepped_control` or None if not set
        """
        return self._data["Probability Lighting will be Reset When Needed in Manual Stepped Control"]

    @probability_lighting_will_be_reset_when_needed_in_manual_stepped_control.setter
    def probability_lighting_will_be_reset_when_needed_in_manual_stepped_control(self, value=1.0):
        """  Corresponds to IDD Field `Probability Lighting will be Reset When Needed in Manual Stepped Control`

        Args:
            value (float): value for IDD Field `Probability Lighting will be Reset When Needed in Manual Stepped Control`
                Default value: 1.0
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
                raise ValueError('value {} need to be of type float'
                                 ' for field `DaylightingControls.probability_lighting_will_be_reset_when_needed_in_manual_stepped_control`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `DaylightingControls.probability_lighting_will_be_reset_when_needed_in_manual_stepped_control`')
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `DaylightingControls.probability_lighting_will_be_reset_when_needed_in_manual_stepped_control`')
        self._data["Probability Lighting will be Reset When Needed in Manual Stepped Control"] = value

    @property
    def availability_schedule_name(self):
        """Get availability_schedule_name

        Returns:
            str: the value of `availability_schedule_name` or None if not set
        """
        return self._data["Availability Schedule Name"]

    @availability_schedule_name.setter
    def availability_schedule_name(self, value=None):
        """  Corresponds to IDD Field `Availability Schedule Name`

        Args:
            value (str): value for IDD Field `Availability Schedule Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str'
                                 ' for field `DaylightingControls.availability_schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `DaylightingControls.availability_schedule_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `DaylightingControls.availability_schedule_name`')
        self._data["Availability Schedule Name"] = value

    def check(self, strict=True):
        """ Checks if all required fields are not None

        Args:
            strict (bool):
                True: raises an Execption in case of error
                False: logs a warning in case of error

        Raises:
            ValueError
        """
        good = True
        for key in self.required_fields:
            if self._data[key] is None:
                good = False
                if strict:
                    raise ValueError("Required field DaylightingControls:{} is None".format(key))
                    break
                else:
                    logger.warn("Required field DaylightingControls:{} is None".format(key))

        out_fields = len(self.export())
        has_minfields = out_fields >= self.min_fields
        if not has_minfields and strict:
            raise ValueError("Not enough fields set for DaylightingControls: {} / {}".format(out_fields,
                                                                                            self.min_fields))
        elif not has_minfields and not strict:
            logger.warn("Not enough fields set for DaylightingControls: {} / {}".format(out_fields,
                                                                                       self.min_fields))
        good = good and has_minfields

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

        # Calculate max elements to export
        has_extensibles = False
        for vals in self._data["extensibles"]:
            for i, value in enumerate(vals):
                if value is not None:
                    has_extensibles = True
                    break
            if has_extensibles:
                break

        if has_extensibles:
            maxel = len(self._data) - 1
        else:
            for i, key in reversed(list(enumerate(self._data.keys()[:-1]))):
                maxel = i + 1
                if self._data[key] is not None:
                    break

        maxel = max(maxel, self.min_fields)

        for key in self._data.keys()[0:maxel]:
            if not key == "extensibles":
                out.append((key, self._to_str(self._data[key])))
        for vals in self._data["extensibles"]:
            for i, value in enumerate(vals):
                out.append((self.extensible_keys[i], self._to_str(value)))
        return out

    def __str__(self):
        out = [self.internal_name]
        out += self.export()
        return ",".join(out[:20])

class DaylightingDelightControls(object):
    """ Corresponds to IDD object `Daylighting:DELight:Controls`
        Dimming of overhead electric lighting is determined from
        DElight calculated interior daylight illuminance at one or more reference points.
    """
    internal_name = "Daylighting:DELight:Controls"
    field_count = 8
    required_fields = ["Name", "Zone Name"]
    extensible_fields = 0
    format = None
    min_fields = 8
    extensible_keys = []

    def __init__(self):
        """ Init data dictionary object for IDD  `Daylighting:DELight:Controls`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Zone Name"] = None
        self._data["Lighting Control Type"] = None
        self._data["Minimum Input Power Fraction for Continuous Dimming Control"] = None
        self._data["Minimum Light Output Fraction for Continuous Dimming Control"] = None
        self._data["Number of Stepped Control Steps"] = None
        self._data["Probability Lighting will be Reset When Needed in Manual Stepped Control"] = None
        self._data["Gridding Resolution"] = None
        self._data["extensibles"] = []
        self.strict = True

    def read(self, vals, strict=False):
        """ Read values

        Args:
            vals (list): list of strings representing values
        """
        old_strict = self.strict
        self.strict = strict
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
            self.lighting_control_type = None
        else:
            self.lighting_control_type = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.minimum_input_power_fraction_for_continuous_dimming_control = None
        else:
            self.minimum_input_power_fraction_for_continuous_dimming_control = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.minimum_light_output_fraction_for_continuous_dimming_control = None
        else:
            self.minimum_light_output_fraction_for_continuous_dimming_control = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.number_of_stepped_control_steps = None
        else:
            self.number_of_stepped_control_steps = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.probability_lighting_will_be_reset_when_needed_in_manual_stepped_control = None
        else:
            self.probability_lighting_will_be_reset_when_needed_in_manual_stepped_control = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.gridding_resolution = None
        else:
            self.gridding_resolution = vals[i]
        i += 1
        if i >= len(vals):
            return
        self.strict = old_strict

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
                raise ValueError('value {} need to be of type str'
                                 ' for field `DaylightingDelightControls.name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `DaylightingDelightControls.name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `DaylightingDelightControls.name`')
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
        """  Corresponds to IDD Field `Zone Name`
        Name of Thermal Zone hosting the given DElight Zone

        Args:
            value (str): value for IDD Field `Zone Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str'
                                 ' for field `DaylightingDelightControls.zone_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `DaylightingDelightControls.zone_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `DaylightingDelightControls.zone_name`')
        self._data["Zone Name"] = value

    @property
    def lighting_control_type(self):
        """Get lighting_control_type

        Returns:
            int: the value of `lighting_control_type` or None if not set
        """
        return self._data["Lighting Control Type"]

    @lighting_control_type.setter
    def lighting_control_type(self, value=1):
        """  Corresponds to IDD Field `Lighting Control Type`
        1=continuous,2=stepped,3=continuous/off

        Args:
            value (int): value for IDD Field `Lighting Control Type`
                Default value: 1
                value >= 1
                value <= 3
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = int(value)
            except ValueError:
                if not self.strict:
                    try:
                        conv_value = int(float(value))
                        logger.warn('Cast float {} to int {}, precision may be lost '
                                     'for field `DaylightingDelightControls.lighting_control_type`'.format(value, conv_value))
                        value = conv_value
                    except ValueError:
                        raise ValueError('value {} need to be of type int '
                                         'for field `DaylightingDelightControls.lighting_control_type`'.format(value))
            if value < 1:
                raise ValueError('value need to be greater or equal 1 '
                                 'for field `DaylightingDelightControls.lighting_control_type`')
            if value > 3:
                raise ValueError('value need to be smaller 3 '
                                 'for field `DaylightingDelightControls.lighting_control_type`')
        self._data["Lighting Control Type"] = value

    @property
    def minimum_input_power_fraction_for_continuous_dimming_control(self):
        """Get minimum_input_power_fraction_for_continuous_dimming_control

        Returns:
            float: the value of `minimum_input_power_fraction_for_continuous_dimming_control` or None if not set
        """
        return self._data["Minimum Input Power Fraction for Continuous Dimming Control"]

    @minimum_input_power_fraction_for_continuous_dimming_control.setter
    def minimum_input_power_fraction_for_continuous_dimming_control(self, value=0.3):
        """  Corresponds to IDD Field `Minimum Input Power Fraction for Continuous Dimming Control`

        Args:
            value (float): value for IDD Field `Minimum Input Power Fraction for Continuous Dimming Control`
                Default value: 0.3
                value >= 0.0
                value <= 0.6
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float'
                                 ' for field `DaylightingDelightControls.minimum_input_power_fraction_for_continuous_dimming_control`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `DaylightingDelightControls.minimum_input_power_fraction_for_continuous_dimming_control`')
            if value > 0.6:
                raise ValueError('value need to be smaller 0.6 '
                                 'for field `DaylightingDelightControls.minimum_input_power_fraction_for_continuous_dimming_control`')
        self._data["Minimum Input Power Fraction for Continuous Dimming Control"] = value

    @property
    def minimum_light_output_fraction_for_continuous_dimming_control(self):
        """Get minimum_light_output_fraction_for_continuous_dimming_control

        Returns:
            float: the value of `minimum_light_output_fraction_for_continuous_dimming_control` or None if not set
        """
        return self._data["Minimum Light Output Fraction for Continuous Dimming Control"]

    @minimum_light_output_fraction_for_continuous_dimming_control.setter
    def minimum_light_output_fraction_for_continuous_dimming_control(self, value=0.2):
        """  Corresponds to IDD Field `Minimum Light Output Fraction for Continuous Dimming Control`

        Args:
            value (float): value for IDD Field `Minimum Light Output Fraction for Continuous Dimming Control`
                Default value: 0.2
                value >= 0.0
                value <= 0.6
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float'
                                 ' for field `DaylightingDelightControls.minimum_light_output_fraction_for_continuous_dimming_control`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `DaylightingDelightControls.minimum_light_output_fraction_for_continuous_dimming_control`')
            if value > 0.6:
                raise ValueError('value need to be smaller 0.6 '
                                 'for field `DaylightingDelightControls.minimum_light_output_fraction_for_continuous_dimming_control`')
        self._data["Minimum Light Output Fraction for Continuous Dimming Control"] = value

    @property
    def number_of_stepped_control_steps(self):
        """Get number_of_stepped_control_steps

        Returns:
            int: the value of `number_of_stepped_control_steps` or None if not set
        """
        return self._data["Number of Stepped Control Steps"]

    @number_of_stepped_control_steps.setter
    def number_of_stepped_control_steps(self, value=1):
        """  Corresponds to IDD Field `Number of Stepped Control Steps`
        for Lighting Control Type=2, this field cannot be zero.

        Args:
            value (int): value for IDD Field `Number of Stepped Control Steps`
                Default value: 1
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = int(value)
            except ValueError:
                if not self.strict:
                    try:
                        conv_value = int(float(value))
                        logger.warn('Cast float {} to int {}, precision may be lost '
                                     'for field `DaylightingDelightControls.number_of_stepped_control_steps`'.format(value, conv_value))
                        value = conv_value
                    except ValueError:
                        raise ValueError('value {} need to be of type int '
                                         'for field `DaylightingDelightControls.number_of_stepped_control_steps`'.format(value))
        self._data["Number of Stepped Control Steps"] = value

    @property
    def probability_lighting_will_be_reset_when_needed_in_manual_stepped_control(self):
        """Get probability_lighting_will_be_reset_when_needed_in_manual_stepped_control

        Returns:
            float: the value of `probability_lighting_will_be_reset_when_needed_in_manual_stepped_control` or None if not set
        """
        return self._data["Probability Lighting will be Reset When Needed in Manual Stepped Control"]

    @probability_lighting_will_be_reset_when_needed_in_manual_stepped_control.setter
    def probability_lighting_will_be_reset_when_needed_in_manual_stepped_control(self, value=0.0):
        """  Corresponds to IDD Field `Probability Lighting will be Reset When Needed in Manual Stepped Control`

        Args:
            value (float): value for IDD Field `Probability Lighting will be Reset When Needed in Manual Stepped Control`
                Default value: 0.0
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
                raise ValueError('value {} need to be of type float'
                                 ' for field `DaylightingDelightControls.probability_lighting_will_be_reset_when_needed_in_manual_stepped_control`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `DaylightingDelightControls.probability_lighting_will_be_reset_when_needed_in_manual_stepped_control`')
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `DaylightingDelightControls.probability_lighting_will_be_reset_when_needed_in_manual_stepped_control`')
        self._data["Probability Lighting will be Reset When Needed in Manual Stepped Control"] = value

    @property
    def gridding_resolution(self):
        """Get gridding_resolution

        Returns:
            float: the value of `gridding_resolution` or None if not set
        """
        return self._data["Gridding Resolution"]

    @gridding_resolution.setter
    def gridding_resolution(self, value=None):
        """  Corresponds to IDD Field `Gridding Resolution`
        Maximum surface area for nodes in gridding all surfaces in the DElight zone.
        All reflective and transmitting surfaces will be subdivided
        into approximately square nodes that do not exceed this maximum.
        Higher resolution subdivisions require greater calculation times,
        but generally produce more accurate results.

        Args:
            value (float): value for IDD Field `Gridding Resolution`
                Units: m2
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
                raise ValueError('value {} need to be of type float'
                                 ' for field `DaylightingDelightControls.gridding_resolution`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `DaylightingDelightControls.gridding_resolution`')
        self._data["Gridding Resolution"] = value

    def check(self, strict=True):
        """ Checks if all required fields are not None

        Args:
            strict (bool):
                True: raises an Execption in case of error
                False: logs a warning in case of error

        Raises:
            ValueError
        """
        good = True
        for key in self.required_fields:
            if self._data[key] is None:
                good = False
                if strict:
                    raise ValueError("Required field DaylightingDelightControls:{} is None".format(key))
                    break
                else:
                    logger.warn("Required field DaylightingDelightControls:{} is None".format(key))

        out_fields = len(self.export())
        has_minfields = out_fields >= self.min_fields
        if not has_minfields and strict:
            raise ValueError("Not enough fields set for DaylightingDelightControls: {} / {}".format(out_fields,
                                                                                            self.min_fields))
        elif not has_minfields and not strict:
            logger.warn("Not enough fields set for DaylightingDelightControls: {} / {}".format(out_fields,
                                                                                       self.min_fields))
        good = good and has_minfields

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

        # Calculate max elements to export
        has_extensibles = False
        for vals in self._data["extensibles"]:
            for i, value in enumerate(vals):
                if value is not None:
                    has_extensibles = True
                    break
            if has_extensibles:
                break

        if has_extensibles:
            maxel = len(self._data) - 1
        else:
            for i, key in reversed(list(enumerate(self._data.keys()[:-1]))):
                maxel = i + 1
                if self._data[key] is not None:
                    break

        maxel = max(maxel, self.min_fields)

        for key in self._data.keys()[0:maxel]:
            if not key == "extensibles":
                out.append((key, self._to_str(self._data[key])))
        for vals in self._data["extensibles"]:
            for i, value in enumerate(vals):
                out.append((self.extensible_keys[i], self._to_str(value)))
        return out

    def __str__(self):
        out = [self.internal_name]
        out += self.export()
        return ",".join(out[:20])

class DaylightingDelightReferencePoint(object):
    """ Corresponds to IDD object `Daylighting:DELight:ReferencePoint`
        DElight reference point for illuminance calculation and electric lighting dimming.
        reference points are given in coordinates specified in the GlobalGeometryRules object
        Daylighting Reference Point CoordinateSystem field
        There is a maximum number of 100 reference points per DElight daylighting zone.
    """
    internal_name = "Daylighting:DELight:ReferencePoint"
    field_count = 7
    required_fields = ["DElight Name", "X-coordinate of Reference Point", "Y-coordinate of Reference Point", "Z-coordinate of Reference Point", "Fraction of Zone Controlled by Reference Point", "Illuminance Setpoint at Reference Point"]
    extensible_fields = 0
    format = None
    min_fields = 7
    extensible_keys = []

    def __init__(self):
        """ Init data dictionary object for IDD  `Daylighting:DELight:ReferencePoint`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["DElight Name"] = None
        self._data["X-coordinate of Reference Point"] = None
        self._data["Y-coordinate of Reference Point"] = None
        self._data["Z-coordinate of Reference Point"] = None
        self._data["Fraction of Zone Controlled by Reference Point"] = None
        self._data["Illuminance Setpoint at Reference Point"] = None
        self._data["extensibles"] = []
        self.strict = True

    def read(self, vals, strict=False):
        """ Read values

        Args:
            vals (list): list of strings representing values
        """
        old_strict = self.strict
        self.strict = strict
        i = 0
        if len(vals[i]) == 0:
            self.name = None
        else:
            self.name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.delight_name = None
        else:
            self.delight_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.xcoordinate_of_reference_point = None
        else:
            self.xcoordinate_of_reference_point = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.ycoordinate_of_reference_point = None
        else:
            self.ycoordinate_of_reference_point = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.zcoordinate_of_reference_point = None
        else:
            self.zcoordinate_of_reference_point = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.fraction_of_zone_controlled_by_reference_point = None
        else:
            self.fraction_of_zone_controlled_by_reference_point = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.illuminance_setpoint_at_reference_point = None
        else:
            self.illuminance_setpoint_at_reference_point = vals[i]
        i += 1
        if i >= len(vals):
            return
        self.strict = old_strict

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
                raise ValueError('value {} need to be of type str'
                                 ' for field `DaylightingDelightReferencePoint.name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `DaylightingDelightReferencePoint.name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `DaylightingDelightReferencePoint.name`')
        self._data["Name"] = value

    @property
    def delight_name(self):
        """Get delight_name

        Returns:
            str: the value of `delight_name` or None if not set
        """
        return self._data["DElight Name"]

    @delight_name.setter
    def delight_name(self, value=None):
        """  Corresponds to IDD Field `DElight Name`

        Args:
            value (str): value for IDD Field `DElight Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str'
                                 ' for field `DaylightingDelightReferencePoint.delight_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `DaylightingDelightReferencePoint.delight_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `DaylightingDelightReferencePoint.delight_name`')
        self._data["DElight Name"] = value

    @property
    def xcoordinate_of_reference_point(self):
        """Get xcoordinate_of_reference_point

        Returns:
            float: the value of `xcoordinate_of_reference_point` or None if not set
        """
        return self._data["X-coordinate of Reference Point"]

    @xcoordinate_of_reference_point.setter
    def xcoordinate_of_reference_point(self, value=None):
        """  Corresponds to IDD Field `X-coordinate of Reference Point`

        Args:
            value (float): value for IDD Field `X-coordinate of Reference Point`
                Units: m
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float'
                                 ' for field `DaylightingDelightReferencePoint.xcoordinate_of_reference_point`'.format(value))
        self._data["X-coordinate of Reference Point"] = value

    @property
    def ycoordinate_of_reference_point(self):
        """Get ycoordinate_of_reference_point

        Returns:
            float: the value of `ycoordinate_of_reference_point` or None if not set
        """
        return self._data["Y-coordinate of Reference Point"]

    @ycoordinate_of_reference_point.setter
    def ycoordinate_of_reference_point(self, value=None):
        """  Corresponds to IDD Field `Y-coordinate of Reference Point`

        Args:
            value (float): value for IDD Field `Y-coordinate of Reference Point`
                Units: m
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float'
                                 ' for field `DaylightingDelightReferencePoint.ycoordinate_of_reference_point`'.format(value))
        self._data["Y-coordinate of Reference Point"] = value

    @property
    def zcoordinate_of_reference_point(self):
        """Get zcoordinate_of_reference_point

        Returns:
            float: the value of `zcoordinate_of_reference_point` or None if not set
        """
        return self._data["Z-coordinate of Reference Point"]

    @zcoordinate_of_reference_point.setter
    def zcoordinate_of_reference_point(self, value=None):
        """  Corresponds to IDD Field `Z-coordinate of Reference Point`

        Args:
            value (float): value for IDD Field `Z-coordinate of Reference Point`
                Units: m
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float'
                                 ' for field `DaylightingDelightReferencePoint.zcoordinate_of_reference_point`'.format(value))
        self._data["Z-coordinate of Reference Point"] = value

    @property
    def fraction_of_zone_controlled_by_reference_point(self):
        """Get fraction_of_zone_controlled_by_reference_point

        Returns:
            float: the value of `fraction_of_zone_controlled_by_reference_point` or None if not set
        """
        return self._data["Fraction of Zone Controlled by Reference Point"]

    @fraction_of_zone_controlled_by_reference_point.setter
    def fraction_of_zone_controlled_by_reference_point(self, value=1.0):
        """  Corresponds to IDD Field `Fraction of Zone Controlled by Reference Point`

        Args:
            value (float): value for IDD Field `Fraction of Zone Controlled by Reference Point`
                Default value: 1.0
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
                raise ValueError('value {} need to be of type float'
                                 ' for field `DaylightingDelightReferencePoint.fraction_of_zone_controlled_by_reference_point`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `DaylightingDelightReferencePoint.fraction_of_zone_controlled_by_reference_point`')
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `DaylightingDelightReferencePoint.fraction_of_zone_controlled_by_reference_point`')
        self._data["Fraction of Zone Controlled by Reference Point"] = value

    @property
    def illuminance_setpoint_at_reference_point(self):
        """Get illuminance_setpoint_at_reference_point

        Returns:
            float: the value of `illuminance_setpoint_at_reference_point` or None if not set
        """
        return self._data["Illuminance Setpoint at Reference Point"]

    @illuminance_setpoint_at_reference_point.setter
    def illuminance_setpoint_at_reference_point(self, value=500.0):
        """  Corresponds to IDD Field `Illuminance Setpoint at Reference Point`

        Args:
            value (float): value for IDD Field `Illuminance Setpoint at Reference Point`
                Units: lux
                Default value: 500.0
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
                raise ValueError('value {} need to be of type float'
                                 ' for field `DaylightingDelightReferencePoint.illuminance_setpoint_at_reference_point`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `DaylightingDelightReferencePoint.illuminance_setpoint_at_reference_point`')
        self._data["Illuminance Setpoint at Reference Point"] = value

    def check(self, strict=True):
        """ Checks if all required fields are not None

        Args:
            strict (bool):
                True: raises an Execption in case of error
                False: logs a warning in case of error

        Raises:
            ValueError
        """
        good = True
        for key in self.required_fields:
            if self._data[key] is None:
                good = False
                if strict:
                    raise ValueError("Required field DaylightingDelightReferencePoint:{} is None".format(key))
                    break
                else:
                    logger.warn("Required field DaylightingDelightReferencePoint:{} is None".format(key))

        out_fields = len(self.export())
        has_minfields = out_fields >= self.min_fields
        if not has_minfields and strict:
            raise ValueError("Not enough fields set for DaylightingDelightReferencePoint: {} / {}".format(out_fields,
                                                                                            self.min_fields))
        elif not has_minfields and not strict:
            logger.warn("Not enough fields set for DaylightingDelightReferencePoint: {} / {}".format(out_fields,
                                                                                       self.min_fields))
        good = good and has_minfields

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

        # Calculate max elements to export
        has_extensibles = False
        for vals in self._data["extensibles"]:
            for i, value in enumerate(vals):
                if value is not None:
                    has_extensibles = True
                    break
            if has_extensibles:
                break

        if has_extensibles:
            maxel = len(self._data) - 1
        else:
            for i, key in reversed(list(enumerate(self._data.keys()[:-1]))):
                maxel = i + 1
                if self._data[key] is not None:
                    break

        maxel = max(maxel, self.min_fields)

        for key in self._data.keys()[0:maxel]:
            if not key == "extensibles":
                out.append((key, self._to_str(self._data[key])))
        for vals in self._data["extensibles"]:
            for i, value in enumerate(vals):
                out.append((self.extensible_keys[i], self._to_str(value)))
        return out

    def __str__(self):
        out = [self.internal_name]
        out += self.export()
        return ",".join(out[:20])

class DaylightingDelightComplexFenestration(object):
    """ Corresponds to IDD object `Daylighting:DELight:ComplexFenestration`
        Used for DElight Complex Fenestration of all types
    """
    internal_name = "Daylighting:DELight:ComplexFenestration"
    field_count = 5
    required_fields = ["Name", "Complex Fenestration Type", "Building Surface Name", "Window Name"]
    extensible_fields = 0
    format = None
    min_fields = 5
    extensible_keys = []

    def __init__(self):
        """ Init data dictionary object for IDD  `Daylighting:DELight:ComplexFenestration`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Complex Fenestration Type"] = None
        self._data["Building Surface Name"] = None
        self._data["Window Name"] = None
        self._data["Fenestration Rotation"] = None
        self._data["extensibles"] = []
        self.strict = True

    def read(self, vals, strict=False):
        """ Read values

        Args:
            vals (list): list of strings representing values
        """
        old_strict = self.strict
        self.strict = strict
        i = 0
        if len(vals[i]) == 0:
            self.name = None
        else:
            self.name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.complex_fenestration_type = None
        else:
            self.complex_fenestration_type = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.building_surface_name = None
        else:
            self.building_surface_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.window_name = None
        else:
            self.window_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.fenestration_rotation = None
        else:
            self.fenestration_rotation = vals[i]
        i += 1
        if i >= len(vals):
            return
        self.strict = old_strict

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
        Only used for user reference

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
                raise ValueError('value {} need to be of type str'
                                 ' for field `DaylightingDelightComplexFenestration.name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `DaylightingDelightComplexFenestration.name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `DaylightingDelightComplexFenestration.name`')
        self._data["Name"] = value

    @property
    def complex_fenestration_type(self):
        """Get complex_fenestration_type

        Returns:
            str: the value of `complex_fenestration_type` or None if not set
        """
        return self._data["Complex Fenestration Type"]

    @complex_fenestration_type.setter
    def complex_fenestration_type(self, value=None):
        """  Corresponds to IDD Field `Complex Fenestration Type`
        Used to select the appropriate Complex Fenestration BTDF data

        Args:
            value (str): value for IDD Field `Complex Fenestration Type`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str'
                                 ' for field `DaylightingDelightComplexFenestration.complex_fenestration_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `DaylightingDelightComplexFenestration.complex_fenestration_type`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `DaylightingDelightComplexFenestration.complex_fenestration_type`')
        self._data["Complex Fenestration Type"] = value

    @property
    def building_surface_name(self):
        """Get building_surface_name

        Returns:
            str: the value of `building_surface_name` or None if not set
        """
        return self._data["Building Surface Name"]

    @building_surface_name.setter
    def building_surface_name(self, value=None):
        """  Corresponds to IDD Field `Building Surface Name`
        This is a reference to a valid surface object (such as BuildingSurface:Detailed) hosting
        this complex fenestration, analogous to the base surface Name
        field for subsurfaces such as Windows.

        Args:
            value (str): value for IDD Field `Building Surface Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str'
                                 ' for field `DaylightingDelightComplexFenestration.building_surface_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `DaylightingDelightComplexFenestration.building_surface_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `DaylightingDelightComplexFenestration.building_surface_name`')
        self._data["Building Surface Name"] = value

    @property
    def window_name(self):
        """Get window_name

        Returns:
            str: the value of `window_name` or None if not set
        """
        return self._data["Window Name"]

    @window_name.setter
    def window_name(self, value=None):
        """  Corresponds to IDD Field `Window Name`
        This is a reference to a valid FenestrationSurface:Detailed window object
        used to account for the geometry, and the solar and thermal gains/losses,
        of the Complex Fenestration

        Args:
            value (str): value for IDD Field `Window Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str'
                                 ' for field `DaylightingDelightComplexFenestration.window_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `DaylightingDelightComplexFenestration.window_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `DaylightingDelightComplexFenestration.window_name`')
        self._data["Window Name"] = value

    @property
    def fenestration_rotation(self):
        """Get fenestration_rotation

        Returns:
            float: the value of `fenestration_rotation` or None if not set
        """
        return self._data["Fenestration Rotation"]

    @fenestration_rotation.setter
    def fenestration_rotation(self, value=0.0):
        """  Corresponds to IDD Field `Fenestration Rotation`
        In-plane counter-clockwise rotation angle of the Complex Fenestration
        optical reference direction and the base edge of the Complex Fenestration.
        The Rotation will typically be zero when the host and CFS surfaces
        are rectangular and height and width edges are aligned.

        Args:
            value (float): value for IDD Field `Fenestration Rotation`
                Units: deg
                Default value: 0.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float'
                                 ' for field `DaylightingDelightComplexFenestration.fenestration_rotation`'.format(value))
        self._data["Fenestration Rotation"] = value

    def check(self, strict=True):
        """ Checks if all required fields are not None

        Args:
            strict (bool):
                True: raises an Execption in case of error
                False: logs a warning in case of error

        Raises:
            ValueError
        """
        good = True
        for key in self.required_fields:
            if self._data[key] is None:
                good = False
                if strict:
                    raise ValueError("Required field DaylightingDelightComplexFenestration:{} is None".format(key))
                    break
                else:
                    logger.warn("Required field DaylightingDelightComplexFenestration:{} is None".format(key))

        out_fields = len(self.export())
        has_minfields = out_fields >= self.min_fields
        if not has_minfields and strict:
            raise ValueError("Not enough fields set for DaylightingDelightComplexFenestration: {} / {}".format(out_fields,
                                                                                            self.min_fields))
        elif not has_minfields and not strict:
            logger.warn("Not enough fields set for DaylightingDelightComplexFenestration: {} / {}".format(out_fields,
                                                                                       self.min_fields))
        good = good and has_minfields

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

        # Calculate max elements to export
        has_extensibles = False
        for vals in self._data["extensibles"]:
            for i, value in enumerate(vals):
                if value is not None:
                    has_extensibles = True
                    break
            if has_extensibles:
                break

        if has_extensibles:
            maxel = len(self._data) - 1
        else:
            for i, key in reversed(list(enumerate(self._data.keys()[:-1]))):
                maxel = i + 1
                if self._data[key] is not None:
                    break

        maxel = max(maxel, self.min_fields)

        for key in self._data.keys()[0:maxel]:
            if not key == "extensibles":
                out.append((key, self._to_str(self._data[key])))
        for vals in self._data["extensibles"]:
            for i, value in enumerate(vals):
                out.append((self.extensible_keys[i], self._to_str(value)))
        return out

    def __str__(self):
        out = [self.internal_name]
        out += self.export()
        return ",".join(out[:20])

class DaylightingDeviceTubular(object):
    """ Corresponds to IDD object `DaylightingDevice:Tubular`
        Defines a tubular daylighting device (TDD) consisting of three components:
        a dome, a pipe, and a diffuser. The dome and diffuser are defined separately using the
        FenestrationSurface:Detailed object.
    """
    internal_name = "DaylightingDevice:Tubular"
    field_count = 7
    required_fields = ["Name", "Dome Name", "Diffuser Name", "Construction Name", "Diameter", "Total Length", "Effective Thermal Resistance"]
    extensible_fields = 2
    format = None
    min_fields = 0
    extensible_keys = ["Transition Zone 1 Name", "Transition Zone 1 Length"]

    def __init__(self):
        """ Init data dictionary object for IDD  `DaylightingDevice:Tubular`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Dome Name"] = None
        self._data["Diffuser Name"] = None
        self._data["Construction Name"] = None
        self._data["Diameter"] = None
        self._data["Total Length"] = None
        self._data["Effective Thermal Resistance"] = None
        self._data["extensibles"] = []
        self.strict = True

    def read(self, vals, strict=False):
        """ Read values

        Args:
            vals (list): list of strings representing values
        """
        old_strict = self.strict
        self.strict = strict
        i = 0
        if len(vals[i]) == 0:
            self.name = None
        else:
            self.name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.dome_name = None
        else:
            self.dome_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.diffuser_name = None
        else:
            self.diffuser_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.construction_name = None
        else:
            self.construction_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.diameter = None
        else:
            self.diameter = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.total_length = None
        else:
            self.total_length = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.effective_thermal_resistance = None
        else:
            self.effective_thermal_resistance = vals[i]
        i += 1
        if i >= len(vals):
            return
        while i < len(vals):
            ext_vals = [None] * self.extensible_fields
            for j, val in enumerate(vals[i:i + self.extensible_fields]):
                if len(val) == 0:
                    val = None
                ext_vals[j] = val
            self.add_extensible(*ext_vals)
            i += self.extensible_fields
        self.strict = old_strict

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
                raise ValueError('value {} need to be of type str'
                                 ' for field `DaylightingDeviceTubular.name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `DaylightingDeviceTubular.name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `DaylightingDeviceTubular.name`')
        self._data["Name"] = value

    @property
    def dome_name(self):
        """Get dome_name

        Returns:
            str: the value of `dome_name` or None if not set
        """
        return self._data["Dome Name"]

    @dome_name.setter
    def dome_name(self, value=None):
        """  Corresponds to IDD Field `Dome Name`
        This must refer to a subsurface object of type TubularDaylightDome

        Args:
            value (str): value for IDD Field `Dome Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str'
                                 ' for field `DaylightingDeviceTubular.dome_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `DaylightingDeviceTubular.dome_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `DaylightingDeviceTubular.dome_name`')
        self._data["Dome Name"] = value

    @property
    def diffuser_name(self):
        """Get diffuser_name

        Returns:
            str: the value of `diffuser_name` or None if not set
        """
        return self._data["Diffuser Name"]

    @diffuser_name.setter
    def diffuser_name(self, value=None):
        """  Corresponds to IDD Field `Diffuser Name`
        This must refer to a subsurface object of type TubularDaylightDiffuser
        Delivery zone is specified in the diffuser object

        Args:
            value (str): value for IDD Field `Diffuser Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str'
                                 ' for field `DaylightingDeviceTubular.diffuser_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `DaylightingDeviceTubular.diffuser_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `DaylightingDeviceTubular.diffuser_name`')
        self._data["Diffuser Name"] = value

    @property
    def construction_name(self):
        """Get construction_name

        Returns:
            str: the value of `construction_name` or None if not set
        """
        return self._data["Construction Name"]

    @construction_name.setter
    def construction_name(self, value=None):
        """  Corresponds to IDD Field `Construction Name`

        Args:
            value (str): value for IDD Field `Construction Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str'
                                 ' for field `DaylightingDeviceTubular.construction_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `DaylightingDeviceTubular.construction_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `DaylightingDeviceTubular.construction_name`')
        self._data["Construction Name"] = value

    @property
    def diameter(self):
        """Get diameter

        Returns:
            float: the value of `diameter` or None if not set
        """
        return self._data["Diameter"]

    @diameter.setter
    def diameter(self, value=None):
        """  Corresponds to IDD Field `Diameter`

        Args:
            value (float): value for IDD Field `Diameter`
                Units: m
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
                raise ValueError('value {} need to be of type float'
                                 ' for field `DaylightingDeviceTubular.diameter`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `DaylightingDeviceTubular.diameter`')
        self._data["Diameter"] = value

    @property
    def total_length(self):
        """Get total_length

        Returns:
            float: the value of `total_length` or None if not set
        """
        return self._data["Total Length"]

    @total_length.setter
    def total_length(self, value=None):
        """  Corresponds to IDD Field `Total Length`
        The exterior exposed length is the difference between total and sum of zone lengths

        Args:
            value (float): value for IDD Field `Total Length`
                Units: m
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
                raise ValueError('value {} need to be of type float'
                                 ' for field `DaylightingDeviceTubular.total_length`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `DaylightingDeviceTubular.total_length`')
        self._data["Total Length"] = value

    @property
    def effective_thermal_resistance(self):
        """Get effective_thermal_resistance

        Returns:
            float: the value of `effective_thermal_resistance` or None if not set
        """
        return self._data["Effective Thermal Resistance"]

    @effective_thermal_resistance.setter
    def effective_thermal_resistance(self, value=0.28):
        """  Corresponds to IDD Field `Effective Thermal Resistance`
        R value between TubularDaylightDome and TubularDaylightDiffuser

        Args:
            value (float): value for IDD Field `Effective Thermal Resistance`
                Units: m2-K/W
                Default value: 0.28
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
                raise ValueError('value {} need to be of type float'
                                 ' for field `DaylightingDeviceTubular.effective_thermal_resistance`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `DaylightingDeviceTubular.effective_thermal_resistance`')
        self._data["Effective Thermal Resistance"] = value

    def add_extensible(self,
                       transition_zone_1_name=None,
                       transition_zone_1_length=None,
                       ):
        """ Add values for extensible fields

        Args:

            transition_zone_1_name (str): value for IDD Field `Transition Zone 1 Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

            transition_zone_1_length (float): value for IDD Field `Transition Zone 1 Length`
                Units: m
                value >= 0.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value
        """
        vals = []
        vals.append(self._check_transition_zone_1_name(transition_zone_1_name))
        vals.append(self._check_transition_zone_1_length(transition_zone_1_length))
        self._data["extensibles"].append(vals)

    @property
    def extensibles(self):
        """ Get list of all extensibles
        """
        return self._data["extensibles"]

    def _check_transition_zone_1_name(self, value):
        """ Validates falue of field `Transition Zone 1 Name`
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str'
                                 ' for field `DaylightingDeviceTubular.transition_zone_1_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `DaylightingDeviceTubular.transition_zone_1_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `DaylightingDeviceTubular.transition_zone_1_name`')
        return value

    def _check_transition_zone_1_length(self, value):
        """ Validates falue of field `Transition Zone 1 Length`
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float'
                                 ' for field `DaylightingDeviceTubular.transition_zone_1_length`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `DaylightingDeviceTubular.transition_zone_1_length`')
        return value

    def check(self, strict=True):
        """ Checks if all required fields are not None

        Args:
            strict (bool):
                True: raises an Execption in case of error
                False: logs a warning in case of error

        Raises:
            ValueError
        """
        good = True
        for key in self.required_fields:
            if self._data[key] is None:
                good = False
                if strict:
                    raise ValueError("Required field DaylightingDeviceTubular:{} is None".format(key))
                    break
                else:
                    logger.warn("Required field DaylightingDeviceTubular:{} is None".format(key))

        out_fields = len(self.export())
        has_minfields = out_fields >= self.min_fields
        if not has_minfields and strict:
            raise ValueError("Not enough fields set for DaylightingDeviceTubular: {} / {}".format(out_fields,
                                                                                            self.min_fields))
        elif not has_minfields and not strict:
            logger.warn("Not enough fields set for DaylightingDeviceTubular: {} / {}".format(out_fields,
                                                                                       self.min_fields))
        good = good and has_minfields

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

        # Calculate max elements to export
        has_extensibles = False
        for vals in self._data["extensibles"]:
            for i, value in enumerate(vals):
                if value is not None:
                    has_extensibles = True
                    break
            if has_extensibles:
                break

        if has_extensibles:
            maxel = len(self._data) - 1
        else:
            for i, key in reversed(list(enumerate(self._data.keys()[:-1]))):
                maxel = i + 1
                if self._data[key] is not None:
                    break

        maxel = max(maxel, self.min_fields)

        for key in self._data.keys()[0:maxel]:
            if not key == "extensibles":
                out.append((key, self._to_str(self._data[key])))
        for vals in self._data["extensibles"]:
            for i, value in enumerate(vals):
                out.append((self.extensible_keys[i], self._to_str(value)))
        return out

    def __str__(self):
        out = [self.internal_name]
        out += self.export()
        return ",".join(out[:20])

class DaylightingDeviceShelf(object):
    """ Corresponds to IDD object `DaylightingDevice:Shelf`
        Defines a daylighting which can have an inside shelf, an outside shelf, or both.
        The inside shelf is defined as a building surface and the outside shelf is defined
        as a shading surface.
    """
    internal_name = "DaylightingDevice:Shelf"
    field_count = 6
    required_fields = ["Name", "Window Name"]
    extensible_fields = 0
    format = None
    min_fields = 0
    extensible_keys = []

    def __init__(self):
        """ Init data dictionary object for IDD  `DaylightingDevice:Shelf`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Window Name"] = None
        self._data["Inside Shelf Name"] = None
        self._data["Outside Shelf Name"] = None
        self._data["Outside Shelf Construction Name"] = None
        self._data["View Factor to Outside Shelf"] = None
        self._data["extensibles"] = []
        self.strict = True

    def read(self, vals, strict=False):
        """ Read values

        Args:
            vals (list): list of strings representing values
        """
        old_strict = self.strict
        self.strict = strict
        i = 0
        if len(vals[i]) == 0:
            self.name = None
        else:
            self.name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.window_name = None
        else:
            self.window_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.inside_shelf_name = None
        else:
            self.inside_shelf_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.outside_shelf_name = None
        else:
            self.outside_shelf_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.outside_shelf_construction_name = None
        else:
            self.outside_shelf_construction_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.view_factor_to_outside_shelf = None
        else:
            self.view_factor_to_outside_shelf = vals[i]
        i += 1
        if i >= len(vals):
            return
        self.strict = old_strict

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
                raise ValueError('value {} need to be of type str'
                                 ' for field `DaylightingDeviceShelf.name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `DaylightingDeviceShelf.name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `DaylightingDeviceShelf.name`')
        self._data["Name"] = value

    @property
    def window_name(self):
        """Get window_name

        Returns:
            str: the value of `window_name` or None if not set
        """
        return self._data["Window Name"]

    @window_name.setter
    def window_name(self, value=None):
        """  Corresponds to IDD Field `Window Name`

        Args:
            value (str): value for IDD Field `Window Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str'
                                 ' for field `DaylightingDeviceShelf.window_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `DaylightingDeviceShelf.window_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `DaylightingDeviceShelf.window_name`')
        self._data["Window Name"] = value

    @property
    def inside_shelf_name(self):
        """Get inside_shelf_name

        Returns:
            str: the value of `inside_shelf_name` or None if not set
        """
        return self._data["Inside Shelf Name"]

    @inside_shelf_name.setter
    def inside_shelf_name(self, value=None):
        """  Corresponds to IDD Field `Inside Shelf Name`
        This must refer to a BuildingSurface:Detailed or equivalent object
        This surface must be its own Surface for other side boundary conditions.

        Args:
            value (str): value for IDD Field `Inside Shelf Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str'
                                 ' for field `DaylightingDeviceShelf.inside_shelf_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `DaylightingDeviceShelf.inside_shelf_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `DaylightingDeviceShelf.inside_shelf_name`')
        self._data["Inside Shelf Name"] = value

    @property
    def outside_shelf_name(self):
        """Get outside_shelf_name

        Returns:
            str: the value of `outside_shelf_name` or None if not set
        """
        return self._data["Outside Shelf Name"]

    @outside_shelf_name.setter
    def outside_shelf_name(self, value=None):
        """  Corresponds to IDD Field `Outside Shelf Name`
        This must refer to a Shading:Zone:Detailed object

        Args:
            value (str): value for IDD Field `Outside Shelf Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str'
                                 ' for field `DaylightingDeviceShelf.outside_shelf_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `DaylightingDeviceShelf.outside_shelf_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `DaylightingDeviceShelf.outside_shelf_name`')
        self._data["Outside Shelf Name"] = value

    @property
    def outside_shelf_construction_name(self):
        """Get outside_shelf_construction_name

        Returns:
            str: the value of `outside_shelf_construction_name` or None if not set
        """
        return self._data["Outside Shelf Construction Name"]

    @outside_shelf_construction_name.setter
    def outside_shelf_construction_name(self, value=None):
        """  Corresponds to IDD Field `Outside Shelf Construction Name`
        Required if outside shelf is specified

        Args:
            value (str): value for IDD Field `Outside Shelf Construction Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str'
                                 ' for field `DaylightingDeviceShelf.outside_shelf_construction_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `DaylightingDeviceShelf.outside_shelf_construction_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `DaylightingDeviceShelf.outside_shelf_construction_name`')
        self._data["Outside Shelf Construction Name"] = value

    @property
    def view_factor_to_outside_shelf(self):
        """Get view_factor_to_outside_shelf

        Returns:
            float: the value of `view_factor_to_outside_shelf` or None if not set
        """
        return self._data["View Factor to Outside Shelf"]

    @view_factor_to_outside_shelf.setter
    def view_factor_to_outside_shelf(self, value=None):
        """  Corresponds to IDD Field `View Factor to Outside Shelf`

        Args:
            value (float): value for IDD Field `View Factor to Outside Shelf`
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
                raise ValueError('value {} need to be of type float'
                                 ' for field `DaylightingDeviceShelf.view_factor_to_outside_shelf`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `DaylightingDeviceShelf.view_factor_to_outside_shelf`')
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `DaylightingDeviceShelf.view_factor_to_outside_shelf`')
        self._data["View Factor to Outside Shelf"] = value

    def check(self, strict=True):
        """ Checks if all required fields are not None

        Args:
            strict (bool):
                True: raises an Execption in case of error
                False: logs a warning in case of error

        Raises:
            ValueError
        """
        good = True
        for key in self.required_fields:
            if self._data[key] is None:
                good = False
                if strict:
                    raise ValueError("Required field DaylightingDeviceShelf:{} is None".format(key))
                    break
                else:
                    logger.warn("Required field DaylightingDeviceShelf:{} is None".format(key))

        out_fields = len(self.export())
        has_minfields = out_fields >= self.min_fields
        if not has_minfields and strict:
            raise ValueError("Not enough fields set for DaylightingDeviceShelf: {} / {}".format(out_fields,
                                                                                            self.min_fields))
        elif not has_minfields and not strict:
            logger.warn("Not enough fields set for DaylightingDeviceShelf: {} / {}".format(out_fields,
                                                                                       self.min_fields))
        good = good and has_minfields

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

        # Calculate max elements to export
        has_extensibles = False
        for vals in self._data["extensibles"]:
            for i, value in enumerate(vals):
                if value is not None:
                    has_extensibles = True
                    break
            if has_extensibles:
                break

        if has_extensibles:
            maxel = len(self._data) - 1
        else:
            for i, key in reversed(list(enumerate(self._data.keys()[:-1]))):
                maxel = i + 1
                if self._data[key] is not None:
                    break

        maxel = max(maxel, self.min_fields)

        for key in self._data.keys()[0:maxel]:
            if not key == "extensibles":
                out.append((key, self._to_str(self._data[key])))
        for vals in self._data["extensibles"]:
            for i, value in enumerate(vals):
                out.append((self.extensible_keys[i], self._to_str(value)))
        return out

    def __str__(self):
        out = [self.internal_name]
        out += self.export()
        return ",".join(out[:20])

class DaylightingDeviceLightWell(object):
    """ Corresponds to IDD object `DaylightingDevice:LightWell`
        Applies only to exterior windows in daylighting-controlled zones or
        in zones that share an interior window with a daylighting-controlled  zone.
        Generally used with skylights.
    """
    internal_name = "DaylightingDevice:LightWell"
    field_count = 5
    required_fields = ["Exterior Window Name", "Height of Well", "Perimeter of Bottom of Well", "Area of Bottom of Well", "Visible Reflectance of Well Walls"]
    extensible_fields = 0
    format = None
    min_fields = 5
    extensible_keys = []

    def __init__(self):
        """ Init data dictionary object for IDD  `DaylightingDevice:LightWell`
        """
        self._data = OrderedDict()
        self._data["Exterior Window Name"] = None
        self._data["Height of Well"] = None
        self._data["Perimeter of Bottom of Well"] = None
        self._data["Area of Bottom of Well"] = None
        self._data["Visible Reflectance of Well Walls"] = None
        self._data["extensibles"] = []
        self.strict = True

    def read(self, vals, strict=False):
        """ Read values

        Args:
            vals (list): list of strings representing values
        """
        old_strict = self.strict
        self.strict = strict
        i = 0
        if len(vals[i]) == 0:
            self.exterior_window_name = None
        else:
            self.exterior_window_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.height_of_well = None
        else:
            self.height_of_well = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.perimeter_of_bottom_of_well = None
        else:
            self.perimeter_of_bottom_of_well = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.area_of_bottom_of_well = None
        else:
            self.area_of_bottom_of_well = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.visible_reflectance_of_well_walls = None
        else:
            self.visible_reflectance_of_well_walls = vals[i]
        i += 1
        if i >= len(vals):
            return
        self.strict = old_strict

    @property
    def exterior_window_name(self):
        """Get exterior_window_name

        Returns:
            str: the value of `exterior_window_name` or None if not set
        """
        return self._data["Exterior Window Name"]

    @exterior_window_name.setter
    def exterior_window_name(self, value=None):
        """  Corresponds to IDD Field `Exterior Window Name`

        Args:
            value (str): value for IDD Field `Exterior Window Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str'
                                 ' for field `DaylightingDeviceLightWell.exterior_window_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `DaylightingDeviceLightWell.exterior_window_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `DaylightingDeviceLightWell.exterior_window_name`')
        self._data["Exterior Window Name"] = value

    @property
    def height_of_well(self):
        """Get height_of_well

        Returns:
            float: the value of `height_of_well` or None if not set
        """
        return self._data["Height of Well"]

    @height_of_well.setter
    def height_of_well(self, value=None):
        """  Corresponds to IDD Field `Height of Well`
        Distance from Bottom of Window to Bottom of Well

        Args:
            value (float): value for IDD Field `Height of Well`
                Units: m
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
                raise ValueError('value {} need to be of type float'
                                 ' for field `DaylightingDeviceLightWell.height_of_well`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `DaylightingDeviceLightWell.height_of_well`')
        self._data["Height of Well"] = value

    @property
    def perimeter_of_bottom_of_well(self):
        """Get perimeter_of_bottom_of_well

        Returns:
            float: the value of `perimeter_of_bottom_of_well` or None if not set
        """
        return self._data["Perimeter of Bottom of Well"]

    @perimeter_of_bottom_of_well.setter
    def perimeter_of_bottom_of_well(self, value=None):
        """  Corresponds to IDD Field `Perimeter of Bottom of Well`

        Args:
            value (float): value for IDD Field `Perimeter of Bottom of Well`
                Units: m
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
                raise ValueError('value {} need to be of type float'
                                 ' for field `DaylightingDeviceLightWell.perimeter_of_bottom_of_well`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `DaylightingDeviceLightWell.perimeter_of_bottom_of_well`')
        self._data["Perimeter of Bottom of Well"] = value

    @property
    def area_of_bottom_of_well(self):
        """Get area_of_bottom_of_well

        Returns:
            float: the value of `area_of_bottom_of_well` or None if not set
        """
        return self._data["Area of Bottom of Well"]

    @area_of_bottom_of_well.setter
    def area_of_bottom_of_well(self, value=None):
        """  Corresponds to IDD Field `Area of Bottom of Well`

        Args:
            value (float): value for IDD Field `Area of Bottom of Well`
                Units: m2
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
                raise ValueError('value {} need to be of type float'
                                 ' for field `DaylightingDeviceLightWell.area_of_bottom_of_well`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `DaylightingDeviceLightWell.area_of_bottom_of_well`')
        self._data["Area of Bottom of Well"] = value

    @property
    def visible_reflectance_of_well_walls(self):
        """Get visible_reflectance_of_well_walls

        Returns:
            float: the value of `visible_reflectance_of_well_walls` or None if not set
        """
        return self._data["Visible Reflectance of Well Walls"]

    @visible_reflectance_of_well_walls.setter
    def visible_reflectance_of_well_walls(self, value=None):
        """  Corresponds to IDD Field `Visible Reflectance of Well Walls`

        Args:
            value (float): value for IDD Field `Visible Reflectance of Well Walls`
                Units: dimensionless
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
                raise ValueError('value {} need to be of type float'
                                 ' for field `DaylightingDeviceLightWell.visible_reflectance_of_well_walls`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `DaylightingDeviceLightWell.visible_reflectance_of_well_walls`')
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `DaylightingDeviceLightWell.visible_reflectance_of_well_walls`')
        self._data["Visible Reflectance of Well Walls"] = value

    def check(self, strict=True):
        """ Checks if all required fields are not None

        Args:
            strict (bool):
                True: raises an Execption in case of error
                False: logs a warning in case of error

        Raises:
            ValueError
        """
        good = True
        for key in self.required_fields:
            if self._data[key] is None:
                good = False
                if strict:
                    raise ValueError("Required field DaylightingDeviceLightWell:{} is None".format(key))
                    break
                else:
                    logger.warn("Required field DaylightingDeviceLightWell:{} is None".format(key))

        out_fields = len(self.export())
        has_minfields = out_fields >= self.min_fields
        if not has_minfields and strict:
            raise ValueError("Not enough fields set for DaylightingDeviceLightWell: {} / {}".format(out_fields,
                                                                                            self.min_fields))
        elif not has_minfields and not strict:
            logger.warn("Not enough fields set for DaylightingDeviceLightWell: {} / {}".format(out_fields,
                                                                                       self.min_fields))
        good = good and has_minfields

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

        # Calculate max elements to export
        has_extensibles = False
        for vals in self._data["extensibles"]:
            for i, value in enumerate(vals):
                if value is not None:
                    has_extensibles = True
                    break
            if has_extensibles:
                break

        if has_extensibles:
            maxel = len(self._data) - 1
        else:
            for i, key in reversed(list(enumerate(self._data.keys()[:-1]))):
                maxel = i + 1
                if self._data[key] is not None:
                    break

        maxel = max(maxel, self.min_fields)

        for key in self._data.keys()[0:maxel]:
            if not key == "extensibles":
                out.append((key, self._to_str(self._data[key])))
        for vals in self._data["extensibles"]:
            for i, value in enumerate(vals):
                out.append((self.extensible_keys[i], self._to_str(value)))
        return out

    def __str__(self):
        out = [self.internal_name]
        out += self.export()
        return ",".join(out[:20])

class OutputDaylightFactors(object):
    """ Corresponds to IDD object `Output:DaylightFactors`
        Reports hourly daylight factors for each exterior window for four sky types
        (clear, turbid clear, intermediate, and overcast).
    """
    internal_name = "Output:DaylightFactors"
    field_count = 1
    required_fields = ["Reporting Days"]
    extensible_fields = 0
    format = "singleline"
    min_fields = 0
    extensible_keys = []

    def __init__(self):
        """ Init data dictionary object for IDD  `Output:DaylightFactors`
        """
        self._data = OrderedDict()
        self._data["Reporting Days"] = None
        self._data["extensibles"] = []
        self.strict = True

    def read(self, vals, strict=False):
        """ Read values

        Args:
            vals (list): list of strings representing values
        """
        old_strict = self.strict
        self.strict = strict
        i = 0
        if len(vals[i]) == 0:
            self.reporting_days = None
        else:
            self.reporting_days = vals[i]
        i += 1
        if i >= len(vals):
            return
        self.strict = old_strict

    @property
    def reporting_days(self):
        """Get reporting_days

        Returns:
            str: the value of `reporting_days` or None if not set
        """
        return self._data["Reporting Days"]

    @reporting_days.setter
    def reporting_days(self, value=None):
        """  Corresponds to IDD Field `Reporting Days`

        Args:
            value (str): value for IDD Field `Reporting Days`
                Accepted values are:
                      - SizingDays
                      - AllShadowCalculationDays
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str'
                                 ' for field `OutputDaylightFactors.reporting_days`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `OutputDaylightFactors.reporting_days`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `OutputDaylightFactors.reporting_days`')
            vals = {}
            vals["sizingdays"] = "SizingDays"
            vals["allshadowcalculationdays"] = "AllShadowCalculationDays"
            value_lower = value.lower()
            if value_lower not in vals:
                found = False
                if not self.strict:
                    for key in vals:
                        if key in value_lower or value_lower in key:
                            value_lower = key
                            found = True
                            break
                    if not found:
                        value_stripped = re.sub(r'[^a-zA-Z0-9]', '', value_lower)
                        for key in vals:
                            key_stripped = re.sub(r'[^a-zA-Z0-9]', '', key)
                            if key_stripped == value_stripped:
                                value_lower = key
                                found = True
                                break
                if not found:
                    raise ValueError('value {} is not an accepted value for '
                                     'field `OutputDaylightFactors.reporting_days`'.format(value))
                else:
                    logger.warn('change value {} to accepted value {} for '
                                 'field `OutputDaylightFactors.reporting_days`'.format(value, vals[value_lower]))
            value = vals[value_lower]
        self._data["Reporting Days"] = value

    def check(self, strict=True):
        """ Checks if all required fields are not None

        Args:
            strict (bool):
                True: raises an Execption in case of error
                False: logs a warning in case of error

        Raises:
            ValueError
        """
        good = True
        for key in self.required_fields:
            if self._data[key] is None:
                good = False
                if strict:
                    raise ValueError("Required field OutputDaylightFactors:{} is None".format(key))
                    break
                else:
                    logger.warn("Required field OutputDaylightFactors:{} is None".format(key))

        out_fields = len(self.export())
        has_minfields = out_fields >= self.min_fields
        if not has_minfields and strict:
            raise ValueError("Not enough fields set for OutputDaylightFactors: {} / {}".format(out_fields,
                                                                                            self.min_fields))
        elif not has_minfields and not strict:
            logger.warn("Not enough fields set for OutputDaylightFactors: {} / {}".format(out_fields,
                                                                                       self.min_fields))
        good = good and has_minfields

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

        # Calculate max elements to export
        has_extensibles = False
        for vals in self._data["extensibles"]:
            for i, value in enumerate(vals):
                if value is not None:
                    has_extensibles = True
                    break
            if has_extensibles:
                break

        if has_extensibles:
            maxel = len(self._data) - 1
        else:
            for i, key in reversed(list(enumerate(self._data.keys()[:-1]))):
                maxel = i + 1
                if self._data[key] is not None:
                    break

        maxel = max(maxel, self.min_fields)

        for key in self._data.keys()[0:maxel]:
            if not key == "extensibles":
                out.append((key, self._to_str(self._data[key])))
        for vals in self._data["extensibles"]:
            for i, value in enumerate(vals):
                out.append((self.extensible_keys[i], self._to_str(value)))
        return out

    def __str__(self):
        out = [self.internal_name]
        out += self.export()
        return ",".join(out[:20])

class OutputIlluminanceMap(object):
    """ Corresponds to IDD object `Output:IlluminanceMap`
        reference points are given in coordinates specified in the GlobalGeometryRules object
        Daylighting Reference Point CoordinateSystem field
    """
    internal_name = "Output:IlluminanceMap"
    field_count = 9
    required_fields = ["Name", "Zone Name"]
    extensible_fields = 0
    format = None
    min_fields = 9
    extensible_keys = []

    def __init__(self):
        """ Init data dictionary object for IDD  `Output:IlluminanceMap`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Zone Name"] = None
        self._data["Z height"] = None
        self._data["X Minimum Coordinate"] = None
        self._data["X Maximum Coordinate"] = None
        self._data["Number of X Grid Points"] = None
        self._data["Y Minimum Coordinate"] = None
        self._data["Y Maximum Coordinate"] = None
        self._data["Number of Y Grid Points"] = None
        self._data["extensibles"] = []
        self.strict = True

    def read(self, vals, strict=False):
        """ Read values

        Args:
            vals (list): list of strings representing values
        """
        old_strict = self.strict
        self.strict = strict
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
            self.z_height = None
        else:
            self.z_height = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.x_minimum_coordinate = None
        else:
            self.x_minimum_coordinate = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.x_maximum_coordinate = None
        else:
            self.x_maximum_coordinate = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.number_of_x_grid_points = None
        else:
            self.number_of_x_grid_points = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.y_minimum_coordinate = None
        else:
            self.y_minimum_coordinate = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.y_maximum_coordinate = None
        else:
            self.y_maximum_coordinate = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.number_of_y_grid_points = None
        else:
            self.number_of_y_grid_points = vals[i]
        i += 1
        if i >= len(vals):
            return
        self.strict = old_strict

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
                raise ValueError('value {} need to be of type str'
                                 ' for field `OutputIlluminanceMap.name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `OutputIlluminanceMap.name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `OutputIlluminanceMap.name`')
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
        """  Corresponds to IDD Field `Zone Name`

        Args:
            value (str): value for IDD Field `Zone Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str'
                                 ' for field `OutputIlluminanceMap.zone_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `OutputIlluminanceMap.zone_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `OutputIlluminanceMap.zone_name`')
        self._data["Zone Name"] = value

    @property
    def z_height(self):
        """Get z_height

        Returns:
            float: the value of `z_height` or None if not set
        """
        return self._data["Z height"]

    @z_height.setter
    def z_height(self, value=0.0):
        """  Corresponds to IDD Field `Z height`

        Args:
            value (float): value for IDD Field `Z height`
                Units: m
                Default value: 0.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float'
                                 ' for field `OutputIlluminanceMap.z_height`'.format(value))
        self._data["Z height"] = value

    @property
    def x_minimum_coordinate(self):
        """Get x_minimum_coordinate

        Returns:
            float: the value of `x_minimum_coordinate` or None if not set
        """
        return self._data["X Minimum Coordinate"]

    @x_minimum_coordinate.setter
    def x_minimum_coordinate(self, value=0.0):
        """  Corresponds to IDD Field `X Minimum Coordinate`

        Args:
            value (float): value for IDD Field `X Minimum Coordinate`
                Units: m
                Default value: 0.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float'
                                 ' for field `OutputIlluminanceMap.x_minimum_coordinate`'.format(value))
        self._data["X Minimum Coordinate"] = value

    @property
    def x_maximum_coordinate(self):
        """Get x_maximum_coordinate

        Returns:
            float: the value of `x_maximum_coordinate` or None if not set
        """
        return self._data["X Maximum Coordinate"]

    @x_maximum_coordinate.setter
    def x_maximum_coordinate(self, value=1.0):
        """  Corresponds to IDD Field `X Maximum Coordinate`

        Args:
            value (float): value for IDD Field `X Maximum Coordinate`
                Units: m
                Default value: 1.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float'
                                 ' for field `OutputIlluminanceMap.x_maximum_coordinate`'.format(value))
        self._data["X Maximum Coordinate"] = value

    @property
    def number_of_x_grid_points(self):
        """Get number_of_x_grid_points

        Returns:
            int: the value of `number_of_x_grid_points` or None if not set
        """
        return self._data["Number of X Grid Points"]

    @number_of_x_grid_points.setter
    def number_of_x_grid_points(self, value=2):
        """  Corresponds to IDD Field `Number of X Grid Points`
        Maximum number of total grid points must be <= 2500 (X*Y)

        Args:
            value (int): value for IDD Field `Number of X Grid Points`
                Default value: 2
                value > 0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = int(value)
            except ValueError:
                if not self.strict:
                    try:
                        conv_value = int(float(value))
                        logger.warn('Cast float {} to int {}, precision may be lost '
                                     'for field `OutputIlluminanceMap.number_of_x_grid_points`'.format(value, conv_value))
                        value = conv_value
                    except ValueError:
                        raise ValueError('value {} need to be of type int '
                                         'for field `OutputIlluminanceMap.number_of_x_grid_points`'.format(value))
            if value <= 0:
                raise ValueError('value need to be greater 0 '
                                 'for field `OutputIlluminanceMap.number_of_x_grid_points`')
        self._data["Number of X Grid Points"] = value

    @property
    def y_minimum_coordinate(self):
        """Get y_minimum_coordinate

        Returns:
            float: the value of `y_minimum_coordinate` or None if not set
        """
        return self._data["Y Minimum Coordinate"]

    @y_minimum_coordinate.setter
    def y_minimum_coordinate(self, value=0.0):
        """  Corresponds to IDD Field `Y Minimum Coordinate`

        Args:
            value (float): value for IDD Field `Y Minimum Coordinate`
                Units: m
                Default value: 0.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float'
                                 ' for field `OutputIlluminanceMap.y_minimum_coordinate`'.format(value))
        self._data["Y Minimum Coordinate"] = value

    @property
    def y_maximum_coordinate(self):
        """Get y_maximum_coordinate

        Returns:
            float: the value of `y_maximum_coordinate` or None if not set
        """
        return self._data["Y Maximum Coordinate"]

    @y_maximum_coordinate.setter
    def y_maximum_coordinate(self, value=1.0):
        """  Corresponds to IDD Field `Y Maximum Coordinate`

        Args:
            value (float): value for IDD Field `Y Maximum Coordinate`
                Units: m
                Default value: 1.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float'
                                 ' for field `OutputIlluminanceMap.y_maximum_coordinate`'.format(value))
        self._data["Y Maximum Coordinate"] = value

    @property
    def number_of_y_grid_points(self):
        """Get number_of_y_grid_points

        Returns:
            int: the value of `number_of_y_grid_points` or None if not set
        """
        return self._data["Number of Y Grid Points"]

    @number_of_y_grid_points.setter
    def number_of_y_grid_points(self, value=2):
        """  Corresponds to IDD Field `Number of Y Grid Points`
        Maximum number of total grid points must be <= 2500 (X*Y)

        Args:
            value (int): value for IDD Field `Number of Y Grid Points`
                Default value: 2
                value > 0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = int(value)
            except ValueError:
                if not self.strict:
                    try:
                        conv_value = int(float(value))
                        logger.warn('Cast float {} to int {}, precision may be lost '
                                     'for field `OutputIlluminanceMap.number_of_y_grid_points`'.format(value, conv_value))
                        value = conv_value
                    except ValueError:
                        raise ValueError('value {} need to be of type int '
                                         'for field `OutputIlluminanceMap.number_of_y_grid_points`'.format(value))
            if value <= 0:
                raise ValueError('value need to be greater 0 '
                                 'for field `OutputIlluminanceMap.number_of_y_grid_points`')
        self._data["Number of Y Grid Points"] = value

    def check(self, strict=True):
        """ Checks if all required fields are not None

        Args:
            strict (bool):
                True: raises an Execption in case of error
                False: logs a warning in case of error

        Raises:
            ValueError
        """
        good = True
        for key in self.required_fields:
            if self._data[key] is None:
                good = False
                if strict:
                    raise ValueError("Required field OutputIlluminanceMap:{} is None".format(key))
                    break
                else:
                    logger.warn("Required field OutputIlluminanceMap:{} is None".format(key))

        out_fields = len(self.export())
        has_minfields = out_fields >= self.min_fields
        if not has_minfields and strict:
            raise ValueError("Not enough fields set for OutputIlluminanceMap: {} / {}".format(out_fields,
                                                                                            self.min_fields))
        elif not has_minfields and not strict:
            logger.warn("Not enough fields set for OutputIlluminanceMap: {} / {}".format(out_fields,
                                                                                       self.min_fields))
        good = good and has_minfields

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

        # Calculate max elements to export
        has_extensibles = False
        for vals in self._data["extensibles"]:
            for i, value in enumerate(vals):
                if value is not None:
                    has_extensibles = True
                    break
            if has_extensibles:
                break

        if has_extensibles:
            maxel = len(self._data) - 1
        else:
            for i, key in reversed(list(enumerate(self._data.keys()[:-1]))):
                maxel = i + 1
                if self._data[key] is not None:
                    break

        maxel = max(maxel, self.min_fields)

        for key in self._data.keys()[0:maxel]:
            if not key == "extensibles":
                out.append((key, self._to_str(self._data[key])))
        for vals in self._data["extensibles"]:
            for i, value in enumerate(vals):
                out.append((self.extensible_keys[i], self._to_str(value)))
        return out

    def __str__(self):
        out = [self.internal_name]
        out += self.export()
        return ",".join(out[:20])

class OutputControlIlluminanceMapStyle(object):
    """ Corresponds to IDD object `OutputControl:IlluminanceMap:Style`
        default style for the Daylighting Illuminance Map is comma -- this works well for
        importing into spreadsheet programs such as Excel(tm) but not so well for word
        processing progams -- there tab may be a better choice.  fixed puts spaces between
        the "columns"
    """
    internal_name = "OutputControl:IlluminanceMap:Style"
    field_count = 1
    required_fields = []
    extensible_fields = 0
    format = None
    min_fields = 0
    extensible_keys = []

    def __init__(self):
        """ Init data dictionary object for IDD  `OutputControl:IlluminanceMap:Style`
        """
        self._data = OrderedDict()
        self._data["Column Separator"] = None
        self._data["extensibles"] = []
        self.strict = True

    def read(self, vals, strict=False):
        """ Read values

        Args:
            vals (list): list of strings representing values
        """
        old_strict = self.strict
        self.strict = strict
        i = 0
        if len(vals[i]) == 0:
            self.column_separator = None
        else:
            self.column_separator = vals[i]
        i += 1
        if i >= len(vals):
            return
        self.strict = old_strict

    @property
    def column_separator(self):
        """Get column_separator

        Returns:
            str: the value of `column_separator` or None if not set
        """
        return self._data["Column Separator"]

    @column_separator.setter
    def column_separator(self, value="Comma"):
        """  Corresponds to IDD Field `Column Separator`

        Args:
            value (str): value for IDD Field `Column Separator`
                Accepted values are:
                      - Comma
                      - Tab
                      - Fixed
                Default value: Comma
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str'
                                 ' for field `OutputControlIlluminanceMapStyle.column_separator`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `OutputControlIlluminanceMapStyle.column_separator`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `OutputControlIlluminanceMapStyle.column_separator`')
            vals = {}
            vals["comma"] = "Comma"
            vals["tab"] = "Tab"
            vals["fixed"] = "Fixed"
            value_lower = value.lower()
            if value_lower not in vals:
                found = False
                if not self.strict:
                    for key in vals:
                        if key in value_lower or value_lower in key:
                            value_lower = key
                            found = True
                            break
                    if not found:
                        value_stripped = re.sub(r'[^a-zA-Z0-9]', '', value_lower)
                        for key in vals:
                            key_stripped = re.sub(r'[^a-zA-Z0-9]', '', key)
                            if key_stripped == value_stripped:
                                value_lower = key
                                found = True
                                break
                if not found:
                    raise ValueError('value {} is not an accepted value for '
                                     'field `OutputControlIlluminanceMapStyle.column_separator`'.format(value))
                else:
                    logger.warn('change value {} to accepted value {} for '
                                 'field `OutputControlIlluminanceMapStyle.column_separator`'.format(value, vals[value_lower]))
            value = vals[value_lower]
        self._data["Column Separator"] = value

    def check(self, strict=True):
        """ Checks if all required fields are not None

        Args:
            strict (bool):
                True: raises an Execption in case of error
                False: logs a warning in case of error

        Raises:
            ValueError
        """
        good = True
        for key in self.required_fields:
            if self._data[key] is None:
                good = False
                if strict:
                    raise ValueError("Required field OutputControlIlluminanceMapStyle:{} is None".format(key))
                    break
                else:
                    logger.warn("Required field OutputControlIlluminanceMapStyle:{} is None".format(key))

        out_fields = len(self.export())
        has_minfields = out_fields >= self.min_fields
        if not has_minfields and strict:
            raise ValueError("Not enough fields set for OutputControlIlluminanceMapStyle: {} / {}".format(out_fields,
                                                                                            self.min_fields))
        elif not has_minfields and not strict:
            logger.warn("Not enough fields set for OutputControlIlluminanceMapStyle: {} / {}".format(out_fields,
                                                                                       self.min_fields))
        good = good and has_minfields

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

        # Calculate max elements to export
        has_extensibles = False
        for vals in self._data["extensibles"]:
            for i, value in enumerate(vals):
                if value is not None:
                    has_extensibles = True
                    break
            if has_extensibles:
                break

        if has_extensibles:
            maxel = len(self._data) - 1
        else:
            for i, key in reversed(list(enumerate(self._data.keys()[:-1]))):
                maxel = i + 1
                if self._data[key] is not None:
                    break

        maxel = max(maxel, self.min_fields)

        for key in self._data.keys()[0:maxel]:
            if not key == "extensibles":
                out.append((key, self._to_str(self._data[key])))
        for vals in self._data["extensibles"]:
            for i, value in enumerate(vals):
                out.append((self.extensible_keys[i], self._to_str(value)))
        return out

    def __str__(self):
        out = [self.internal_name]
        out += self.export()
        return ",".join(out[:20])