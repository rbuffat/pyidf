from collections import OrderedDict

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

    def __init__(self):
        """ Init data dictionary object for EPW IDD  `Daylighting:Controls`
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

    def read(self, vals):
        """ Read values

        Args:
            vals (list): list of strings representing values
        """
        i = 0
        if len(vals[i]) == 0:
            self.zone_name = None
        else:
            self.zone_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.total_daylighting_reference_points = None
        else:
            self.total_daylighting_reference_points = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.xcoordinate_of_first_reference_point = None
        else:
            self.xcoordinate_of_first_reference_point = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.ycoordinate_of_first_reference_point = None
        else:
            self.ycoordinate_of_first_reference_point = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.zcoordinate_of_first_reference_point = None
        else:
            self.zcoordinate_of_first_reference_point = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.xcoordinate_of_second_reference_point = None
        else:
            self.xcoordinate_of_second_reference_point = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.ycoordinate_of_second_reference_point = None
        else:
            self.ycoordinate_of_second_reference_point = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.zcoordinate_of_second_reference_point = None
        else:
            self.zcoordinate_of_second_reference_point = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.fraction_of_zone_controlled_by_first_reference_point = None
        else:
            self.fraction_of_zone_controlled_by_first_reference_point = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.fraction_of_zone_controlled_by_second_reference_point = None
        else:
            self.fraction_of_zone_controlled_by_second_reference_point = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.illuminance_setpoint_at_first_reference_point = None
        else:
            self.illuminance_setpoint_at_first_reference_point = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.illuminance_setpoint_at_second_reference_point = None
        else:
            self.illuminance_setpoint_at_second_reference_point = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.lighting_control_type = None
        else:
            self.lighting_control_type = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.glare_calculation_azimuth_angle_of_view_direction_clockwise_from_zone_yaxis = None
        else:
            self.glare_calculation_azimuth_angle_of_view_direction_clockwise_from_zone_yaxis = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.maximum_allowable_discomfort_glare_index = None
        else:
            self.maximum_allowable_discomfort_glare_index = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.minimum_input_power_fraction_for_continuous_dimming_control = None
        else:
            self.minimum_input_power_fraction_for_continuous_dimming_control = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.minimum_light_output_fraction_for_continuous_dimming_control = None
        else:
            self.minimum_light_output_fraction_for_continuous_dimming_control = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.number_of_stepped_control_steps = None
        else:
            self.number_of_stepped_control_steps = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.probability_lighting_will_be_reset_when_needed_in_manual_stepped_control = None
        else:
            self.probability_lighting_will_be_reset_when_needed_in_manual_stepped_control = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.availability_schedule_name = None
        else:
            self.availability_schedule_name = vals[i]
        i += 1

    @property
    def zone_name(self):
        """Get zone_name

        Returns:
            str: the value of `zone_name` or None if not set
        """
        return self._data["Zone Name"]

    @zone_name.setter
    def zone_name(self, value=None):
        """  Corresponds to IDD Field `zone_name`

        Args:
            value (str): value for IDD Field `zone_name`
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
                                 'for field `zone_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `zone_name`')

        self._data["Zone Name"] = value

    @property
    def total_daylighting_reference_points(self):
        """Get total_daylighting_reference_points

        Returns:
            int: the value of `total_daylighting_reference_points` or None if not set
        """
        return self._data["Total Daylighting Reference Points"]

    @total_daylighting_reference_points.setter
    def total_daylighting_reference_points(self, value=1 ):
        """  Corresponds to IDD Field `total_daylighting_reference_points`

        Args:
            value (int): value for IDD Field `total_daylighting_reference_points`
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
            except:
                raise ValueError('value {} need to be of type int '
                                 'for field `total_daylighting_reference_points`'.format(value))
            if value < 1:
                raise ValueError('value need to be greater or equal 1 '
                                 'for field `total_daylighting_reference_points`')
            if value > 2:
                raise ValueError('value need to be smaller 2 '
                                 'for field `total_daylighting_reference_points`')

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
        """  Corresponds to IDD Field `xcoordinate_of_first_reference_point`

        Args:
            value (float): value for IDD Field `xcoordinate_of_first_reference_point`
                Unit: m
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
                                 'for field `xcoordinate_of_first_reference_point`'.format(value))

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
        """  Corresponds to IDD Field `ycoordinate_of_first_reference_point`

        Args:
            value (float): value for IDD Field `ycoordinate_of_first_reference_point`
                Unit: m
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
                                 'for field `ycoordinate_of_first_reference_point`'.format(value))

        self._data["Y-Coordinate of First Reference Point"] = value

    @property
    def zcoordinate_of_first_reference_point(self):
        """Get zcoordinate_of_first_reference_point

        Returns:
            float: the value of `zcoordinate_of_first_reference_point` or None if not set
        """
        return self._data["Z-Coordinate of First Reference Point"]

    @zcoordinate_of_first_reference_point.setter
    def zcoordinate_of_first_reference_point(self, value=0.8 ):
        """  Corresponds to IDD Field `zcoordinate_of_first_reference_point`

        Args:
            value (float): value for IDD Field `zcoordinate_of_first_reference_point`
                Unit: m
                Default value: 0.8
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
                                 'for field `zcoordinate_of_first_reference_point`'.format(value))

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
        """  Corresponds to IDD Field `xcoordinate_of_second_reference_point`
        Required if Total Daylighting Reference Points = 2

        Args:
            value (float): value for IDD Field `xcoordinate_of_second_reference_point`
                Unit: m
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
                                 'for field `xcoordinate_of_second_reference_point`'.format(value))

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
        """  Corresponds to IDD Field `ycoordinate_of_second_reference_point`
        Required if Total Daylighting Reference Points = 2

        Args:
            value (float): value for IDD Field `ycoordinate_of_second_reference_point`
                Unit: m
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
                                 'for field `ycoordinate_of_second_reference_point`'.format(value))

        self._data["Y-Coordinate of Second Reference Point"] = value

    @property
    def zcoordinate_of_second_reference_point(self):
        """Get zcoordinate_of_second_reference_point

        Returns:
            float: the value of `zcoordinate_of_second_reference_point` or None if not set
        """
        return self._data["Z-Coordinate of Second Reference Point"]

    @zcoordinate_of_second_reference_point.setter
    def zcoordinate_of_second_reference_point(self, value=0.8 ):
        """  Corresponds to IDD Field `zcoordinate_of_second_reference_point`

        Args:
            value (float): value for IDD Field `zcoordinate_of_second_reference_point`
                Unit: m
                Default value: 0.8
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
                                 'for field `zcoordinate_of_second_reference_point`'.format(value))

        self._data["Z-Coordinate of Second Reference Point"] = value

    @property
    def fraction_of_zone_controlled_by_first_reference_point(self):
        """Get fraction_of_zone_controlled_by_first_reference_point

        Returns:
            float: the value of `fraction_of_zone_controlled_by_first_reference_point` or None if not set
        """
        return self._data["Fraction of Zone Controlled by First Reference Point"]

    @fraction_of_zone_controlled_by_first_reference_point.setter
    def fraction_of_zone_controlled_by_first_reference_point(self, value=1.0 ):
        """  Corresponds to IDD Field `fraction_of_zone_controlled_by_first_reference_point`

        Args:
            value (float): value for IDD Field `fraction_of_zone_controlled_by_first_reference_point`
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
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `fraction_of_zone_controlled_by_first_reference_point`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `fraction_of_zone_controlled_by_first_reference_point`')
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `fraction_of_zone_controlled_by_first_reference_point`')

        self._data["Fraction of Zone Controlled by First Reference Point"] = value

    @property
    def fraction_of_zone_controlled_by_second_reference_point(self):
        """Get fraction_of_zone_controlled_by_second_reference_point

        Returns:
            float: the value of `fraction_of_zone_controlled_by_second_reference_point` or None if not set
        """
        return self._data["Fraction of Zone Controlled by Second Reference Point"]

    @fraction_of_zone_controlled_by_second_reference_point.setter
    def fraction_of_zone_controlled_by_second_reference_point(self, value=0.0 ):
        """  Corresponds to IDD Field `fraction_of_zone_controlled_by_second_reference_point`

        Args:
            value (float): value for IDD Field `fraction_of_zone_controlled_by_second_reference_point`
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
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `fraction_of_zone_controlled_by_second_reference_point`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `fraction_of_zone_controlled_by_second_reference_point`')
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `fraction_of_zone_controlled_by_second_reference_point`')

        self._data["Fraction of Zone Controlled by Second Reference Point"] = value

    @property
    def illuminance_setpoint_at_first_reference_point(self):
        """Get illuminance_setpoint_at_first_reference_point

        Returns:
            float: the value of `illuminance_setpoint_at_first_reference_point` or None if not set
        """
        return self._data["Illuminance Setpoint at First Reference Point"]

    @illuminance_setpoint_at_first_reference_point.setter
    def illuminance_setpoint_at_first_reference_point(self, value=500.0 ):
        """  Corresponds to IDD Field `illuminance_setpoint_at_first_reference_point`

        Args:
            value (float): value for IDD Field `illuminance_setpoint_at_first_reference_point`
                Unit: lux
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
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `illuminance_setpoint_at_first_reference_point`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `illuminance_setpoint_at_first_reference_point`')

        self._data["Illuminance Setpoint at First Reference Point"] = value

    @property
    def illuminance_setpoint_at_second_reference_point(self):
        """Get illuminance_setpoint_at_second_reference_point

        Returns:
            float: the value of `illuminance_setpoint_at_second_reference_point` or None if not set
        """
        return self._data["Illuminance Setpoint at Second Reference Point"]

    @illuminance_setpoint_at_second_reference_point.setter
    def illuminance_setpoint_at_second_reference_point(self, value=500.0 ):
        """  Corresponds to IDD Field `illuminance_setpoint_at_second_reference_point`

        Args:
            value (float): value for IDD Field `illuminance_setpoint_at_second_reference_point`
                Unit: lux
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
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `illuminance_setpoint_at_second_reference_point`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `illuminance_setpoint_at_second_reference_point`')

        self._data["Illuminance Setpoint at Second Reference Point"] = value

    @property
    def lighting_control_type(self):
        """Get lighting_control_type

        Returns:
            int: the value of `lighting_control_type` or None if not set
        """
        return self._data["Lighting Control Type"]

    @lighting_control_type.setter
    def lighting_control_type(self, value=1 ):
        """  Corresponds to IDD Field `lighting_control_type`
        1=continuous,2=stepped,3=continuous/off

        Args:
            value (int): value for IDD Field `lighting_control_type`
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
            except:
                raise ValueError('value {} need to be of type int '
                                 'for field `lighting_control_type`'.format(value))
            if value < 1:
                raise ValueError('value need to be greater or equal 1 '
                                 'for field `lighting_control_type`')
            if value > 3:
                raise ValueError('value need to be smaller 3 '
                                 'for field `lighting_control_type`')

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
        """  Corresponds to IDD Field `glare_calculation_azimuth_angle_of_view_direction_clockwise_from_zone_yaxis`

        Args:
            value (float): value for IDD Field `glare_calculation_azimuth_angle_of_view_direction_clockwise_from_zone_yaxis`
                Unit: deg
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
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `glare_calculation_azimuth_angle_of_view_direction_clockwise_from_zone_yaxis`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `glare_calculation_azimuth_angle_of_view_direction_clockwise_from_zone_yaxis`')
            if value > 360.0:
                raise ValueError('value need to be smaller 360.0 '
                                 'for field `glare_calculation_azimuth_angle_of_view_direction_clockwise_from_zone_yaxis`')

        self._data["Glare Calculation Azimuth Angle of View Direction Clockwise from Zone y-Axis"] = value

    @property
    def maximum_allowable_discomfort_glare_index(self):
        """Get maximum_allowable_discomfort_glare_index

        Returns:
            float: the value of `maximum_allowable_discomfort_glare_index` or None if not set
        """
        return self._data["Maximum Allowable Discomfort Glare Index"]

    @maximum_allowable_discomfort_glare_index.setter
    def maximum_allowable_discomfort_glare_index(self, value=22.0 ):
        """  Corresponds to IDD Field `maximum_allowable_discomfort_glare_index`
        The default is for general office work

        Args:
            value (float): value for IDD Field `maximum_allowable_discomfort_glare_index`
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
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `maximum_allowable_discomfort_glare_index`'.format(value))
            if value < 1.0:
                raise ValueError('value need to be greater or equal 1.0 '
                                 'for field `maximum_allowable_discomfort_glare_index`')

        self._data["Maximum Allowable Discomfort Glare Index"] = value

    @property
    def minimum_input_power_fraction_for_continuous_dimming_control(self):
        """Get minimum_input_power_fraction_for_continuous_dimming_control

        Returns:
            float: the value of `minimum_input_power_fraction_for_continuous_dimming_control` or None if not set
        """
        return self._data["Minimum Input Power Fraction for Continuous Dimming Control"]

    @minimum_input_power_fraction_for_continuous_dimming_control.setter
    def minimum_input_power_fraction_for_continuous_dimming_control(self, value=0.3 ):
        """  Corresponds to IDD Field `minimum_input_power_fraction_for_continuous_dimming_control`

        Args:
            value (float): value for IDD Field `minimum_input_power_fraction_for_continuous_dimming_control`
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
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `minimum_input_power_fraction_for_continuous_dimming_control`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `minimum_input_power_fraction_for_continuous_dimming_control`')
            if value > 0.6:
                raise ValueError('value need to be smaller 0.6 '
                                 'for field `minimum_input_power_fraction_for_continuous_dimming_control`')

        self._data["Minimum Input Power Fraction for Continuous Dimming Control"] = value

    @property
    def minimum_light_output_fraction_for_continuous_dimming_control(self):
        """Get minimum_light_output_fraction_for_continuous_dimming_control

        Returns:
            float: the value of `minimum_light_output_fraction_for_continuous_dimming_control` or None if not set
        """
        return self._data["Minimum Light Output Fraction for Continuous Dimming Control"]

    @minimum_light_output_fraction_for_continuous_dimming_control.setter
    def minimum_light_output_fraction_for_continuous_dimming_control(self, value=0.2 ):
        """  Corresponds to IDD Field `minimum_light_output_fraction_for_continuous_dimming_control`

        Args:
            value (float): value for IDD Field `minimum_light_output_fraction_for_continuous_dimming_control`
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
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `minimum_light_output_fraction_for_continuous_dimming_control`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `minimum_light_output_fraction_for_continuous_dimming_control`')
            if value > 0.6:
                raise ValueError('value need to be smaller 0.6 '
                                 'for field `minimum_light_output_fraction_for_continuous_dimming_control`')

        self._data["Minimum Light Output Fraction for Continuous Dimming Control"] = value

    @property
    def number_of_stepped_control_steps(self):
        """Get number_of_stepped_control_steps

        Returns:
            int: the value of `number_of_stepped_control_steps` or None if not set
        """
        return self._data["Number of Stepped Control Steps"]

    @number_of_stepped_control_steps.setter
    def number_of_stepped_control_steps(self, value=1 ):
        """  Corresponds to IDD Field `number_of_stepped_control_steps`
        for Lighting Control Type=2, this field cannot be zero.

        Args:
            value (int): value for IDD Field `number_of_stepped_control_steps`
                Default value: 1
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = int(value)
            except:
                raise ValueError('value {} need to be of type int '
                                 'for field `number_of_stepped_control_steps`'.format(value))

        self._data["Number of Stepped Control Steps"] = value

    @property
    def probability_lighting_will_be_reset_when_needed_in_manual_stepped_control(self):
        """Get probability_lighting_will_be_reset_when_needed_in_manual_stepped_control

        Returns:
            float: the value of `probability_lighting_will_be_reset_when_needed_in_manual_stepped_control` or None if not set
        """
        return self._data["Probability Lighting will be Reset When Needed in Manual Stepped Control"]

    @probability_lighting_will_be_reset_when_needed_in_manual_stepped_control.setter
    def probability_lighting_will_be_reset_when_needed_in_manual_stepped_control(self, value=1.0 ):
        """  Corresponds to IDD Field `probability_lighting_will_be_reset_when_needed_in_manual_stepped_control`

        Args:
            value (float): value for IDD Field `probability_lighting_will_be_reset_when_needed_in_manual_stepped_control`
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
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `probability_lighting_will_be_reset_when_needed_in_manual_stepped_control`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `probability_lighting_will_be_reset_when_needed_in_manual_stepped_control`')
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `probability_lighting_will_be_reset_when_needed_in_manual_stepped_control`')

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
        """  Corresponds to IDD Field `availability_schedule_name`

        Args:
            value (str): value for IDD Field `availability_schedule_name`
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
                                 'for field `availability_schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `availability_schedule_name`')

        self._data["Availability Schedule Name"] = value

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
        out.append(self._to_str(self.zone_name))
        out.append(self._to_str(self.total_daylighting_reference_points))
        out.append(self._to_str(self.xcoordinate_of_first_reference_point))
        out.append(self._to_str(self.ycoordinate_of_first_reference_point))
        out.append(self._to_str(self.zcoordinate_of_first_reference_point))
        out.append(self._to_str(self.xcoordinate_of_second_reference_point))
        out.append(self._to_str(self.ycoordinate_of_second_reference_point))
        out.append(self._to_str(self.zcoordinate_of_second_reference_point))
        out.append(self._to_str(self.fraction_of_zone_controlled_by_first_reference_point))
        out.append(self._to_str(self.fraction_of_zone_controlled_by_second_reference_point))
        out.append(self._to_str(self.illuminance_setpoint_at_first_reference_point))
        out.append(self._to_str(self.illuminance_setpoint_at_second_reference_point))
        out.append(self._to_str(self.lighting_control_type))
        out.append(self._to_str(self.glare_calculation_azimuth_angle_of_view_direction_clockwise_from_zone_yaxis))
        out.append(self._to_str(self.maximum_allowable_discomfort_glare_index))
        out.append(self._to_str(self.minimum_input_power_fraction_for_continuous_dimming_control))
        out.append(self._to_str(self.minimum_light_output_fraction_for_continuous_dimming_control))
        out.append(self._to_str(self.number_of_stepped_control_steps))
        out.append(self._to_str(self.probability_lighting_will_be_reset_when_needed_in_manual_stepped_control))
        out.append(self._to_str(self.availability_schedule_name))
        return ",".join(out)

class DaylightingDelightControls(object):
    """ Corresponds to IDD object `Daylighting:DELight:Controls`
        Dimming of overhead electric lighting is determined from
        DElight calculated interior daylight illuminance at one or more reference points.
    """
    internal_name = "Daylighting:DELight:Controls"
    field_count = 8

    def __init__(self):
        """ Init data dictionary object for EPW IDD  `Daylighting:DELight:Controls`
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
            self.zone_name = None
        else:
            self.zone_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.lighting_control_type = None
        else:
            self.lighting_control_type = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.minimum_input_power_fraction_for_continuous_dimming_control = None
        else:
            self.minimum_input_power_fraction_for_continuous_dimming_control = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.minimum_light_output_fraction_for_continuous_dimming_control = None
        else:
            self.minimum_light_output_fraction_for_continuous_dimming_control = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.number_of_stepped_control_steps = None
        else:
            self.number_of_stepped_control_steps = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.probability_lighting_will_be_reset_when_needed_in_manual_stepped_control = None
        else:
            self.probability_lighting_will_be_reset_when_needed_in_manual_stepped_control = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.gridding_resolution = None
        else:
            self.gridding_resolution = vals[i]
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
    def zone_name(self):
        """Get zone_name

        Returns:
            str: the value of `zone_name` or None if not set
        """
        return self._data["Zone Name"]

    @zone_name.setter
    def zone_name(self, value=None):
        """  Corresponds to IDD Field `zone_name`
        Name of Thermal Zone hosting the given DElight Zone

        Args:
            value (str): value for IDD Field `zone_name`
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
                                 'for field `zone_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `zone_name`')

        self._data["Zone Name"] = value

    @property
    def lighting_control_type(self):
        """Get lighting_control_type

        Returns:
            int: the value of `lighting_control_type` or None if not set
        """
        return self._data["Lighting Control Type"]

    @lighting_control_type.setter
    def lighting_control_type(self, value=1 ):
        """  Corresponds to IDD Field `lighting_control_type`
        1=continuous,2=stepped,3=continuous/off

        Args:
            value (int): value for IDD Field `lighting_control_type`
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
            except:
                raise ValueError('value {} need to be of type int '
                                 'for field `lighting_control_type`'.format(value))
            if value < 1:
                raise ValueError('value need to be greater or equal 1 '
                                 'for field `lighting_control_type`')
            if value > 3:
                raise ValueError('value need to be smaller 3 '
                                 'for field `lighting_control_type`')

        self._data["Lighting Control Type"] = value

    @property
    def minimum_input_power_fraction_for_continuous_dimming_control(self):
        """Get minimum_input_power_fraction_for_continuous_dimming_control

        Returns:
            float: the value of `minimum_input_power_fraction_for_continuous_dimming_control` or None if not set
        """
        return self._data["Minimum Input Power Fraction for Continuous Dimming Control"]

    @minimum_input_power_fraction_for_continuous_dimming_control.setter
    def minimum_input_power_fraction_for_continuous_dimming_control(self, value=0.3 ):
        """  Corresponds to IDD Field `minimum_input_power_fraction_for_continuous_dimming_control`

        Args:
            value (float): value for IDD Field `minimum_input_power_fraction_for_continuous_dimming_control`
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
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `minimum_input_power_fraction_for_continuous_dimming_control`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `minimum_input_power_fraction_for_continuous_dimming_control`')
            if value > 0.6:
                raise ValueError('value need to be smaller 0.6 '
                                 'for field `minimum_input_power_fraction_for_continuous_dimming_control`')

        self._data["Minimum Input Power Fraction for Continuous Dimming Control"] = value

    @property
    def minimum_light_output_fraction_for_continuous_dimming_control(self):
        """Get minimum_light_output_fraction_for_continuous_dimming_control

        Returns:
            float: the value of `minimum_light_output_fraction_for_continuous_dimming_control` or None if not set
        """
        return self._data["Minimum Light Output Fraction for Continuous Dimming Control"]

    @minimum_light_output_fraction_for_continuous_dimming_control.setter
    def minimum_light_output_fraction_for_continuous_dimming_control(self, value=0.2 ):
        """  Corresponds to IDD Field `minimum_light_output_fraction_for_continuous_dimming_control`

        Args:
            value (float): value for IDD Field `minimum_light_output_fraction_for_continuous_dimming_control`
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
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `minimum_light_output_fraction_for_continuous_dimming_control`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `minimum_light_output_fraction_for_continuous_dimming_control`')
            if value > 0.6:
                raise ValueError('value need to be smaller 0.6 '
                                 'for field `minimum_light_output_fraction_for_continuous_dimming_control`')

        self._data["Minimum Light Output Fraction for Continuous Dimming Control"] = value

    @property
    def number_of_stepped_control_steps(self):
        """Get number_of_stepped_control_steps

        Returns:
            int: the value of `number_of_stepped_control_steps` or None if not set
        """
        return self._data["Number of Stepped Control Steps"]

    @number_of_stepped_control_steps.setter
    def number_of_stepped_control_steps(self, value=1 ):
        """  Corresponds to IDD Field `number_of_stepped_control_steps`
        for Lighting Control Type=2, this field cannot be zero.

        Args:
            value (int): value for IDD Field `number_of_stepped_control_steps`
                Default value: 1
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = int(value)
            except:
                raise ValueError('value {} need to be of type int '
                                 'for field `number_of_stepped_control_steps`'.format(value))

        self._data["Number of Stepped Control Steps"] = value

    @property
    def probability_lighting_will_be_reset_when_needed_in_manual_stepped_control(self):
        """Get probability_lighting_will_be_reset_when_needed_in_manual_stepped_control

        Returns:
            float: the value of `probability_lighting_will_be_reset_when_needed_in_manual_stepped_control` or None if not set
        """
        return self._data["Probability Lighting will be Reset When Needed in Manual Stepped Control"]

    @probability_lighting_will_be_reset_when_needed_in_manual_stepped_control.setter
    def probability_lighting_will_be_reset_when_needed_in_manual_stepped_control(self, value=0.0 ):
        """  Corresponds to IDD Field `probability_lighting_will_be_reset_when_needed_in_manual_stepped_control`

        Args:
            value (float): value for IDD Field `probability_lighting_will_be_reset_when_needed_in_manual_stepped_control`
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
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `probability_lighting_will_be_reset_when_needed_in_manual_stepped_control`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `probability_lighting_will_be_reset_when_needed_in_manual_stepped_control`')
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `probability_lighting_will_be_reset_when_needed_in_manual_stepped_control`')

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
        """  Corresponds to IDD Field `gridding_resolution`
        Maximum surface area for nodes in gridding all surfaces in the DElight zone.
        All reflective and transmitting surfaces will be subdivided
        into approximately square nodes that do not exceed this maximum.
        Higher resolution subdivisions require greater calculation times,
        but generally produce more accurate results.

        Args:
            value (float): value for IDD Field `gridding_resolution`
                Unit: m2
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
                                 'for field `gridding_resolution`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `gridding_resolution`')

        self._data["Gridding Resolution"] = value

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
        out.append(self._to_str(self.zone_name))
        out.append(self._to_str(self.lighting_control_type))
        out.append(self._to_str(self.minimum_input_power_fraction_for_continuous_dimming_control))
        out.append(self._to_str(self.minimum_light_output_fraction_for_continuous_dimming_control))
        out.append(self._to_str(self.number_of_stepped_control_steps))
        out.append(self._to_str(self.probability_lighting_will_be_reset_when_needed_in_manual_stepped_control))
        out.append(self._to_str(self.gridding_resolution))
        return ",".join(out)

class DaylightingDelightReferencePoint(object):
    """ Corresponds to IDD object `Daylighting:DELight:ReferencePoint`
        DElight reference point for illuminance calculation and electric lighting dimming.
        reference points are given in coordinates specified in the GlobalGeometryRules object
        Daylighting Reference Point CoordinateSystem field
        There is a maximum number of 100 reference points per DElight daylighting zone.
    """
    internal_name = "Daylighting:DELight:ReferencePoint"
    field_count = 7

    def __init__(self):
        """ Init data dictionary object for EPW IDD  `Daylighting:DELight:ReferencePoint`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["DElight Name"] = None
        self._data["X-coordinate of Reference Point"] = None
        self._data["Y-coordinate of Reference Point"] = None
        self._data["Z-coordinate of Reference Point"] = None
        self._data["Fraction of Zone Controlled by Reference Point"] = None
        self._data["Illuminance Setpoint at Reference Point"] = None

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
            self.delight_name = None
        else:
            self.delight_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.xcoordinate_of_reference_point = None
        else:
            self.xcoordinate_of_reference_point = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.ycoordinate_of_reference_point = None
        else:
            self.ycoordinate_of_reference_point = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.zcoordinate_of_reference_point = None
        else:
            self.zcoordinate_of_reference_point = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.fraction_of_zone_controlled_by_reference_point = None
        else:
            self.fraction_of_zone_controlled_by_reference_point = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.illuminance_setpoint_at_reference_point = None
        else:
            self.illuminance_setpoint_at_reference_point = vals[i]
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
    def delight_name(self):
        """Get delight_name

        Returns:
            str: the value of `delight_name` or None if not set
        """
        return self._data["DElight Name"]

    @delight_name.setter
    def delight_name(self, value=None):
        """  Corresponds to IDD Field `delight_name`

        Args:
            value (str): value for IDD Field `delight_name`
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
                                 'for field `delight_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `delight_name`')

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
        """  Corresponds to IDD Field `xcoordinate_of_reference_point`

        Args:
            value (float): value for IDD Field `xcoordinate_of_reference_point`
                Unit: m
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
                                 'for field `xcoordinate_of_reference_point`'.format(value))

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
        """  Corresponds to IDD Field `ycoordinate_of_reference_point`

        Args:
            value (float): value for IDD Field `ycoordinate_of_reference_point`
                Unit: m
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
                                 'for field `ycoordinate_of_reference_point`'.format(value))

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
        """  Corresponds to IDD Field `zcoordinate_of_reference_point`

        Args:
            value (float): value for IDD Field `zcoordinate_of_reference_point`
                Unit: m
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
                                 'for field `zcoordinate_of_reference_point`'.format(value))

        self._data["Z-coordinate of Reference Point"] = value

    @property
    def fraction_of_zone_controlled_by_reference_point(self):
        """Get fraction_of_zone_controlled_by_reference_point

        Returns:
            float: the value of `fraction_of_zone_controlled_by_reference_point` or None if not set
        """
        return self._data["Fraction of Zone Controlled by Reference Point"]

    @fraction_of_zone_controlled_by_reference_point.setter
    def fraction_of_zone_controlled_by_reference_point(self, value=1.0 ):
        """  Corresponds to IDD Field `fraction_of_zone_controlled_by_reference_point`

        Args:
            value (float): value for IDD Field `fraction_of_zone_controlled_by_reference_point`
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
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `fraction_of_zone_controlled_by_reference_point`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `fraction_of_zone_controlled_by_reference_point`')
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `fraction_of_zone_controlled_by_reference_point`')

        self._data["Fraction of Zone Controlled by Reference Point"] = value

    @property
    def illuminance_setpoint_at_reference_point(self):
        """Get illuminance_setpoint_at_reference_point

        Returns:
            float: the value of `illuminance_setpoint_at_reference_point` or None if not set
        """
        return self._data["Illuminance Setpoint at Reference Point"]

    @illuminance_setpoint_at_reference_point.setter
    def illuminance_setpoint_at_reference_point(self, value=500.0 ):
        """  Corresponds to IDD Field `illuminance_setpoint_at_reference_point`

        Args:
            value (float): value for IDD Field `illuminance_setpoint_at_reference_point`
                Unit: lux
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
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `illuminance_setpoint_at_reference_point`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `illuminance_setpoint_at_reference_point`')

        self._data["Illuminance Setpoint at Reference Point"] = value

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
        out.append(self._to_str(self.delight_name))
        out.append(self._to_str(self.xcoordinate_of_reference_point))
        out.append(self._to_str(self.ycoordinate_of_reference_point))
        out.append(self._to_str(self.zcoordinate_of_reference_point))
        out.append(self._to_str(self.fraction_of_zone_controlled_by_reference_point))
        out.append(self._to_str(self.illuminance_setpoint_at_reference_point))
        return ",".join(out)

class DaylightingDelightComplexFenestration(object):
    """ Corresponds to IDD object `Daylighting:DELight:ComplexFenestration`
        Used for DElight Complex Fenestration of all types
    """
    internal_name = "Daylighting:DELight:ComplexFenestration"
    field_count = 5

    def __init__(self):
        """ Init data dictionary object for EPW IDD  `Daylighting:DELight:ComplexFenestration`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Complex Fenestration Type"] = None
        self._data["Building Surface Name"] = None
        self._data["Window Name"] = None
        self._data["Fenestration Rotation"] = None

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
            self.complex_fenestration_type = None
        else:
            self.complex_fenestration_type = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.building_surface_name = None
        else:
            self.building_surface_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.window_name = None
        else:
            self.window_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.fenestration_rotation = None
        else:
            self.fenestration_rotation = vals[i]
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
        Only used for user reference

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
    def complex_fenestration_type(self):
        """Get complex_fenestration_type

        Returns:
            str: the value of `complex_fenestration_type` or None if not set
        """
        return self._data["Complex Fenestration Type"]

    @complex_fenestration_type.setter
    def complex_fenestration_type(self, value=None):
        """  Corresponds to IDD Field `complex_fenestration_type`
        Used to select the appropriate Complex Fenestration BTDF data

        Args:
            value (str): value for IDD Field `complex_fenestration_type`
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
                                 'for field `complex_fenestration_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `complex_fenestration_type`')

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
        """  Corresponds to IDD Field `building_surface_name`
        This is a reference to a valid surface object (such as BuildingSurface:Detailed) hosting
        this complex fenestration, analogous to the base surface Name
        field for subsurfaces such as Windows.

        Args:
            value (str): value for IDD Field `building_surface_name`
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
                                 'for field `building_surface_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `building_surface_name`')

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
        """  Corresponds to IDD Field `window_name`
        This is a reference to a valid FenestrationSurface:Detailed window object
        used to account for the geometry, and the solar and thermal gains/losses,
        of the Complex Fenestration

        Args:
            value (str): value for IDD Field `window_name`
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
                                 'for field `window_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `window_name`')

        self._data["Window Name"] = value

    @property
    def fenestration_rotation(self):
        """Get fenestration_rotation

        Returns:
            float: the value of `fenestration_rotation` or None if not set
        """
        return self._data["Fenestration Rotation"]

    @fenestration_rotation.setter
    def fenestration_rotation(self, value=0.0 ):
        """  Corresponds to IDD Field `fenestration_rotation`
        In-plane counter-clockwise rotation angle of the Complex Fenestration
        optical reference direction and the base edge of the Complex Fenestration.
        The Rotation will typically be zero when the host and CFS surfaces
        are rectangular and height and width edges are aligned.

        Args:
            value (float): value for IDD Field `fenestration_rotation`
                Unit: deg
                Default value: 0.0
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
                                 'for field `fenestration_rotation`'.format(value))

        self._data["Fenestration Rotation"] = value

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
        out.append(self._to_str(self.complex_fenestration_type))
        out.append(self._to_str(self.building_surface_name))
        out.append(self._to_str(self.window_name))
        out.append(self._to_str(self.fenestration_rotation))
        return ",".join(out)