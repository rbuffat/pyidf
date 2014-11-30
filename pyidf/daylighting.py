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
    required_fields = ["Zone Name", "X-Coordinate of First Reference Point", "Y-Coordinate of First Reference Point", "Glare Calculation Azimuth Angle of View Direction Clockwise from Zone y-Axis"]

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
        self.accept_substring = False

    def read(self, vals, accept_substring=True):
        """ Read values

        Args:
            vals (list): list of strings representing values
        """
        self.accept_substring = accept_substring
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
            if '!' in value:
                raise ValueError('value should not contain a ! '
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
                Units: m
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
                Units: m
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
                Units: m
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
                Units: m
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
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `availability_schedule_name`')

        self._data["Availability Schedule Name"] = value

    def check(self):
        """ Checks if all required fields are not None
        """
        good = True
        for key in self.required_fields:
            if self._data[key] is None:
                good = False
                break
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
        for key, value in self._data.iteritems():
            out.append(self._to_str(value))
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
        self.accept_substring = False

    def read(self, vals, accept_substring=True):
        """ Read values

        Args:
            vals (list): list of strings representing values
        """
        self.accept_substring = accept_substring
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
            if '!' in value:
                raise ValueError('value should not contain a ! '
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
            if '!' in value:
                raise ValueError('value should not contain a ! '
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
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `gridding_resolution`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `gridding_resolution`')

        self._data["Gridding Resolution"] = value

    def check(self):
        """ Checks if all required fields are not None
        """
        good = True
        for key in self.required_fields:
            if self._data[key] is None:
                good = False
                break
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
        for key, value in self._data.iteritems():
            out.append(self._to_str(value))
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
        self.accept_substring = False

    def read(self, vals, accept_substring=True):
        """ Read values

        Args:
            vals (list): list of strings representing values
        """
        self.accept_substring = accept_substring
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
            if '!' in value:
                raise ValueError('value should not contain a ! '
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
            if '!' in value:
                raise ValueError('value should not contain a ! '
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
                Units: m
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
                Units: m
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
                Units: m
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
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `illuminance_setpoint_at_reference_point`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `illuminance_setpoint_at_reference_point`')

        self._data["Illuminance Setpoint at Reference Point"] = value

    def check(self):
        """ Checks if all required fields are not None
        """
        good = True
        for key in self.required_fields:
            if self._data[key] is None:
                good = False
                break
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
        for key, value in self._data.iteritems():
            out.append(self._to_str(value))
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

    def __init__(self):
        """ Init data dictionary object for IDD  `Daylighting:DELight:ComplexFenestration`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Complex Fenestration Type"] = None
        self._data["Building Surface Name"] = None
        self._data["Window Name"] = None
        self._data["Fenestration Rotation"] = None
        self.accept_substring = False

    def read(self, vals, accept_substring=True):
        """ Read values

        Args:
            vals (list): list of strings representing values
        """
        self.accept_substring = accept_substring
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
            if '!' in value:
                raise ValueError('value should not contain a ! '
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
            if '!' in value:
                raise ValueError('value should not contain a ! '
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
            if '!' in value:
                raise ValueError('value should not contain a ! '
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
            if '!' in value:
                raise ValueError('value should not contain a ! '
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
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `fenestration_rotation`'.format(value))

        self._data["Fenestration Rotation"] = value

    def check(self):
        """ Checks if all required fields are not None
        """
        good = True
        for key in self.required_fields:
            if self._data[key] is None:
                good = False
                break
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
        for key, value in self._data.iteritems():
            out.append(self._to_str(value))
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
    field_count = 15
    required_fields = ["Name", "Dome Name", "Diffuser Name", "Construction Name", "Diameter", "Total Length", "Effective Thermal Resistance"]

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
        self._data["Transition Zone 1 Name"] = None
        self._data["Transition Zone 1 Length"] = None
        self._data["Transition Zone 2 Name"] = None
        self._data["Transition Zone 2 Length"] = None
        self._data["Transition Zone 3 Name"] = None
        self._data["Transition Zone 3 Length"] = None
        self._data["Transition Zone 4 Name"] = None
        self._data["Transition Zone 4 Length"] = None
        self.accept_substring = False

    def read(self, vals, accept_substring=True):
        """ Read values

        Args:
            vals (list): list of strings representing values
        """
        self.accept_substring = accept_substring
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
        if len(vals[i]) == 0:
            self.transition_zone_1_name = None
        else:
            self.transition_zone_1_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.transition_zone_1_length = None
        else:
            self.transition_zone_1_length = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.transition_zone_2_name = None
        else:
            self.transition_zone_2_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.transition_zone_2_length = None
        else:
            self.transition_zone_2_length = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.transition_zone_3_name = None
        else:
            self.transition_zone_3_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.transition_zone_3_length = None
        else:
            self.transition_zone_3_length = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.transition_zone_4_name = None
        else:
            self.transition_zone_4_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.transition_zone_4_length = None
        else:
            self.transition_zone_4_length = vals[i]
        i += 1
        if i >= len(vals):
            return

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
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `name`')

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
        """  Corresponds to IDD Field `dome_name`
        This must refer to a subsurface object of type TubularDaylightDome

        Args:
            value (str): value for IDD Field `dome_name`
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
                                 'for field `dome_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `dome_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `dome_name`')

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
        """  Corresponds to IDD Field `diffuser_name`
        This must refer to a subsurface object of type TubularDaylightDiffuser
        Delivery zone is specified in the diffuser object

        Args:
            value (str): value for IDD Field `diffuser_name`
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
                                 'for field `diffuser_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `diffuser_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `diffuser_name`')

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
        """  Corresponds to IDD Field `construction_name`

        Args:
            value (str): value for IDD Field `construction_name`
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
                                 'for field `construction_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `construction_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `construction_name`')

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
        """  Corresponds to IDD Field `diameter`

        Args:
            value (float): value for IDD Field `diameter`
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
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `diameter`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `diameter`')

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
        """  Corresponds to IDD Field `total_length`
        The exterior exposed length is the difference between total and sum of zone lengths

        Args:
            value (float): value for IDD Field `total_length`
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
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `total_length`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `total_length`')

        self._data["Total Length"] = value

    @property
    def effective_thermal_resistance(self):
        """Get effective_thermal_resistance

        Returns:
            float: the value of `effective_thermal_resistance` or None if not set
        """
        return self._data["Effective Thermal Resistance"]

    @effective_thermal_resistance.setter
    def effective_thermal_resistance(self, value=0.28 ):
        """  Corresponds to IDD Field `effective_thermal_resistance`
        R value between TubularDaylightDome and TubularDaylightDiffuser

        Args:
            value (float): value for IDD Field `effective_thermal_resistance`
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
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `effective_thermal_resistance`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `effective_thermal_resistance`')

        self._data["Effective Thermal Resistance"] = value

    @property
    def transition_zone_1_name(self):
        """Get transition_zone_1_name

        Returns:
            str: the value of `transition_zone_1_name` or None if not set
        """
        return self._data["Transition Zone 1 Name"]

    @transition_zone_1_name.setter
    def transition_zone_1_name(self, value=None):
        """  Corresponds to IDD Field `transition_zone_1_name`

        Args:
            value (str): value for IDD Field `transition_zone_1_name`
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
                                 'for field `transition_zone_1_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `transition_zone_1_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `transition_zone_1_name`')

        self._data["Transition Zone 1 Name"] = value

    @property
    def transition_zone_1_length(self):
        """Get transition_zone_1_length

        Returns:
            float: the value of `transition_zone_1_length` or None if not set
        """
        return self._data["Transition Zone 1 Length"]

    @transition_zone_1_length.setter
    def transition_zone_1_length(self, value=None):
        """  Corresponds to IDD Field `transition_zone_1_length`

        Args:
            value (float): value for IDD Field `transition_zone_1_length`
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
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `transition_zone_1_length`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `transition_zone_1_length`')

        self._data["Transition Zone 1 Length"] = value

    @property
    def transition_zone_2_name(self):
        """Get transition_zone_2_name

        Returns:
            str: the value of `transition_zone_2_name` or None if not set
        """
        return self._data["Transition Zone 2 Name"]

    @transition_zone_2_name.setter
    def transition_zone_2_name(self, value=None):
        """  Corresponds to IDD Field `transition_zone_2_name`

        Args:
            value (str): value for IDD Field `transition_zone_2_name`
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
                                 'for field `transition_zone_2_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `transition_zone_2_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `transition_zone_2_name`')

        self._data["Transition Zone 2 Name"] = value

    @property
    def transition_zone_2_length(self):
        """Get transition_zone_2_length

        Returns:
            float: the value of `transition_zone_2_length` or None if not set
        """
        return self._data["Transition Zone 2 Length"]

    @transition_zone_2_length.setter
    def transition_zone_2_length(self, value=None):
        """  Corresponds to IDD Field `transition_zone_2_length`

        Args:
            value (float): value for IDD Field `transition_zone_2_length`
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
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `transition_zone_2_length`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `transition_zone_2_length`')

        self._data["Transition Zone 2 Length"] = value

    @property
    def transition_zone_3_name(self):
        """Get transition_zone_3_name

        Returns:
            str: the value of `transition_zone_3_name` or None if not set
        """
        return self._data["Transition Zone 3 Name"]

    @transition_zone_3_name.setter
    def transition_zone_3_name(self, value=None):
        """  Corresponds to IDD Field `transition_zone_3_name`

        Args:
            value (str): value for IDD Field `transition_zone_3_name`
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
                                 'for field `transition_zone_3_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `transition_zone_3_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `transition_zone_3_name`')

        self._data["Transition Zone 3 Name"] = value

    @property
    def transition_zone_3_length(self):
        """Get transition_zone_3_length

        Returns:
            float: the value of `transition_zone_3_length` or None if not set
        """
        return self._data["Transition Zone 3 Length"]

    @transition_zone_3_length.setter
    def transition_zone_3_length(self, value=None):
        """  Corresponds to IDD Field `transition_zone_3_length`

        Args:
            value (float): value for IDD Field `transition_zone_3_length`
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
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `transition_zone_3_length`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `transition_zone_3_length`')

        self._data["Transition Zone 3 Length"] = value

    @property
    def transition_zone_4_name(self):
        """Get transition_zone_4_name

        Returns:
            str: the value of `transition_zone_4_name` or None if not set
        """
        return self._data["Transition Zone 4 Name"]

    @transition_zone_4_name.setter
    def transition_zone_4_name(self, value=None):
        """  Corresponds to IDD Field `transition_zone_4_name`

        Args:
            value (str): value for IDD Field `transition_zone_4_name`
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
                                 'for field `transition_zone_4_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `transition_zone_4_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `transition_zone_4_name`')

        self._data["Transition Zone 4 Name"] = value

    @property
    def transition_zone_4_length(self):
        """Get transition_zone_4_length

        Returns:
            float: the value of `transition_zone_4_length` or None if not set
        """
        return self._data["Transition Zone 4 Length"]

    @transition_zone_4_length.setter
    def transition_zone_4_length(self, value=None):
        """  Corresponds to IDD Field `transition_zone_4_length`

        Args:
            value (float): value for IDD Field `transition_zone_4_length`
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
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `transition_zone_4_length`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `transition_zone_4_length`')

        self._data["Transition Zone 4 Length"] = value

    def check(self):
        """ Checks if all required fields are not None
        """
        good = True
        for key in self.required_fields:
            if self._data[key] is None:
                good = False
                break
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
        for key, value in self._data.iteritems():
            out.append(self._to_str(value))
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
        self.accept_substring = False

    def read(self, vals, accept_substring=True):
        """ Read values

        Args:
            vals (list): list of strings representing values
        """
        self.accept_substring = accept_substring
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
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `name`')

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
        """  Corresponds to IDD Field `window_name`

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
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `window_name`')

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
        """  Corresponds to IDD Field `inside_shelf_name`
        This must refer to a BuildingSurface:Detailed or equivalent object
        This surface must be its own Surface for other side boundary conditions.

        Args:
            value (str): value for IDD Field `inside_shelf_name`
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
                                 'for field `inside_shelf_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `inside_shelf_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `inside_shelf_name`')

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
        """  Corresponds to IDD Field `outside_shelf_name`
        This must refer to a Shading:Zone:Detailed object

        Args:
            value (str): value for IDD Field `outside_shelf_name`
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
                                 'for field `outside_shelf_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `outside_shelf_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `outside_shelf_name`')

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
        """  Corresponds to IDD Field `outside_shelf_construction_name`
        Required if outside shelf is specified

        Args:
            value (str): value for IDD Field `outside_shelf_construction_name`
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
                                 'for field `outside_shelf_construction_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `outside_shelf_construction_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `outside_shelf_construction_name`')

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
        """  Corresponds to IDD Field `view_factor_to_outside_shelf`

        Args:
            value (float): value for IDD Field `view_factor_to_outside_shelf`
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
                                 'for field `view_factor_to_outside_shelf`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `view_factor_to_outside_shelf`')
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `view_factor_to_outside_shelf`')

        self._data["View Factor to Outside Shelf"] = value

    def check(self):
        """ Checks if all required fields are not None
        """
        good = True
        for key in self.required_fields:
            if self._data[key] is None:
                good = False
                break
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
        for key, value in self._data.iteritems():
            out.append(self._to_str(value))
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

    def __init__(self):
        """ Init data dictionary object for IDD  `DaylightingDevice:LightWell`
        """
        self._data = OrderedDict()
        self._data["Exterior Window Name"] = None
        self._data["Height of Well"] = None
        self._data["Perimeter of Bottom of Well"] = None
        self._data["Area of Bottom of Well"] = None
        self._data["Visible Reflectance of Well Walls"] = None
        self.accept_substring = False

    def read(self, vals, accept_substring=True):
        """ Read values

        Args:
            vals (list): list of strings representing values
        """
        self.accept_substring = accept_substring
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

    @property
    def exterior_window_name(self):
        """Get exterior_window_name

        Returns:
            str: the value of `exterior_window_name` or None if not set
        """
        return self._data["Exterior Window Name"]

    @exterior_window_name.setter
    def exterior_window_name(self, value=None):
        """  Corresponds to IDD Field `exterior_window_name`

        Args:
            value (str): value for IDD Field `exterior_window_name`
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
                                 'for field `exterior_window_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `exterior_window_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `exterior_window_name`')

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
        """  Corresponds to IDD Field `height_of_well`
        Distance from Bottom of Window to Bottom of Well

        Args:
            value (float): value for IDD Field `height_of_well`
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
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `height_of_well`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `height_of_well`')

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
        """  Corresponds to IDD Field `perimeter_of_bottom_of_well`

        Args:
            value (float): value for IDD Field `perimeter_of_bottom_of_well`
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
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `perimeter_of_bottom_of_well`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `perimeter_of_bottom_of_well`')

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
        """  Corresponds to IDD Field `area_of_bottom_of_well`

        Args:
            value (float): value for IDD Field `area_of_bottom_of_well`
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
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `area_of_bottom_of_well`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `area_of_bottom_of_well`')

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
        """  Corresponds to IDD Field `visible_reflectance_of_well_walls`

        Args:
            value (float): value for IDD Field `visible_reflectance_of_well_walls`
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
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `visible_reflectance_of_well_walls`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `visible_reflectance_of_well_walls`')
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `visible_reflectance_of_well_walls`')

        self._data["Visible Reflectance of Well Walls"] = value

    def check(self):
        """ Checks if all required fields are not None
        """
        good = True
        for key in self.required_fields:
            if self._data[key] is None:
                good = False
                break
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
        for key, value in self._data.iteritems():
            out.append(self._to_str(value))
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

    def __init__(self):
        """ Init data dictionary object for IDD  `Output:DaylightFactors`
        """
        self._data = OrderedDict()
        self._data["Reporting Days"] = None
        self.accept_substring = False

    def read(self, vals, accept_substring=True):
        """ Read values

        Args:
            vals (list): list of strings representing values
        """
        self.accept_substring = accept_substring
        i = 0
        if len(vals[i]) == 0:
            self.reporting_days = None
        else:
            self.reporting_days = vals[i]
        i += 1
        if i >= len(vals):
            return

    @property
    def reporting_days(self):
        """Get reporting_days

        Returns:
            str: the value of `reporting_days` or None if not set
        """
        return self._data["Reporting Days"]

    @reporting_days.setter
    def reporting_days(self, value=None):
        """  Corresponds to IDD Field `reporting_days`

        Args:
            value (str): value for IDD Field `reporting_days`
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
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `reporting_days`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `reporting_days`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `reporting_days`')
            vals = {}
            vals["sizingdays"] = "SizingDays"
            vals["allshadowcalculationdays"] = "AllShadowCalculationDays"
            value_lower = value.lower()
            if value_lower not in vals:
                found = False
                if self.accept_substring:
                    for key in vals:
                        if key in value_lower:
                            value_lower = key
                            found = True
                            break

                if not found:
                    raise ValueError('value {} is not an accepted value for '
                                     'field `reporting_days`'.format(value))
            value = vals[value_lower]

        self._data["Reporting Days"] = value

    def check(self):
        """ Checks if all required fields are not None
        """
        good = True
        for key in self.required_fields:
            if self._data[key] is None:
                good = False
                break
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
        for key, value in self._data.iteritems():
            out.append(self._to_str(value))
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
        self.accept_substring = False

    def read(self, vals, accept_substring=True):
        """ Read values

        Args:
            vals (list): list of strings representing values
        """
        self.accept_substring = accept_substring
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
            if '!' in value:
                raise ValueError('value should not contain a ! '
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
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `zone_name`')

        self._data["Zone Name"] = value

    @property
    def z_height(self):
        """Get z_height

        Returns:
            float: the value of `z_height` or None if not set
        """
        return self._data["Z height"]

    @z_height.setter
    def z_height(self, value=0.0 ):
        """  Corresponds to IDD Field `z_height`

        Args:
            value (float): value for IDD Field `z_height`
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
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `z_height`'.format(value))

        self._data["Z height"] = value

    @property
    def x_minimum_coordinate(self):
        """Get x_minimum_coordinate

        Returns:
            float: the value of `x_minimum_coordinate` or None if not set
        """
        return self._data["X Minimum Coordinate"]

    @x_minimum_coordinate.setter
    def x_minimum_coordinate(self, value=0.0 ):
        """  Corresponds to IDD Field `x_minimum_coordinate`

        Args:
            value (float): value for IDD Field `x_minimum_coordinate`
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
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `x_minimum_coordinate`'.format(value))

        self._data["X Minimum Coordinate"] = value

    @property
    def x_maximum_coordinate(self):
        """Get x_maximum_coordinate

        Returns:
            float: the value of `x_maximum_coordinate` or None if not set
        """
        return self._data["X Maximum Coordinate"]

    @x_maximum_coordinate.setter
    def x_maximum_coordinate(self, value=1.0 ):
        """  Corresponds to IDD Field `x_maximum_coordinate`

        Args:
            value (float): value for IDD Field `x_maximum_coordinate`
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
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `x_maximum_coordinate`'.format(value))

        self._data["X Maximum Coordinate"] = value

    @property
    def number_of_x_grid_points(self):
        """Get number_of_x_grid_points

        Returns:
            int: the value of `number_of_x_grid_points` or None if not set
        """
        return self._data["Number of X Grid Points"]

    @number_of_x_grid_points.setter
    def number_of_x_grid_points(self, value=2 ):
        """  Corresponds to IDD Field `number_of_x_grid_points`
        Maximum number of total grid points must be <= 2500 (X*Y)

        Args:
            value (int): value for IDD Field `number_of_x_grid_points`
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
            except:
                raise ValueError('value {} need to be of type int '
                                 'for field `number_of_x_grid_points`'.format(value))
            if value <= 0:
                raise ValueError('value need to be greater 0 '
                                 'for field `number_of_x_grid_points`')

        self._data["Number of X Grid Points"] = value

    @property
    def y_minimum_coordinate(self):
        """Get y_minimum_coordinate

        Returns:
            float: the value of `y_minimum_coordinate` or None if not set
        """
        return self._data["Y Minimum Coordinate"]

    @y_minimum_coordinate.setter
    def y_minimum_coordinate(self, value=0.0 ):
        """  Corresponds to IDD Field `y_minimum_coordinate`

        Args:
            value (float): value for IDD Field `y_minimum_coordinate`
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
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `y_minimum_coordinate`'.format(value))

        self._data["Y Minimum Coordinate"] = value

    @property
    def y_maximum_coordinate(self):
        """Get y_maximum_coordinate

        Returns:
            float: the value of `y_maximum_coordinate` or None if not set
        """
        return self._data["Y Maximum Coordinate"]

    @y_maximum_coordinate.setter
    def y_maximum_coordinate(self, value=1.0 ):
        """  Corresponds to IDD Field `y_maximum_coordinate`

        Args:
            value (float): value for IDD Field `y_maximum_coordinate`
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
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `y_maximum_coordinate`'.format(value))

        self._data["Y Maximum Coordinate"] = value

    @property
    def number_of_y_grid_points(self):
        """Get number_of_y_grid_points

        Returns:
            int: the value of `number_of_y_grid_points` or None if not set
        """
        return self._data["Number of Y Grid Points"]

    @number_of_y_grid_points.setter
    def number_of_y_grid_points(self, value=2 ):
        """  Corresponds to IDD Field `number_of_y_grid_points`
        Maximum number of total grid points must be <= 2500 (X*Y)

        Args:
            value (int): value for IDD Field `number_of_y_grid_points`
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
            except:
                raise ValueError('value {} need to be of type int '
                                 'for field `number_of_y_grid_points`'.format(value))
            if value <= 0:
                raise ValueError('value need to be greater 0 '
                                 'for field `number_of_y_grid_points`')

        self._data["Number of Y Grid Points"] = value

    def check(self):
        """ Checks if all required fields are not None
        """
        good = True
        for key in self.required_fields:
            if self._data[key] is None:
                good = False
                break
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
        for key, value in self._data.iteritems():
            out.append(self._to_str(value))
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

    def __init__(self):
        """ Init data dictionary object for IDD  `OutputControl:IlluminanceMap:Style`
        """
        self._data = OrderedDict()
        self._data["Column Separator"] = None
        self.accept_substring = False

    def read(self, vals, accept_substring=True):
        """ Read values

        Args:
            vals (list): list of strings representing values
        """
        self.accept_substring = accept_substring
        i = 0
        if len(vals[i]) == 0:
            self.column_separator = None
        else:
            self.column_separator = vals[i]
        i += 1
        if i >= len(vals):
            return

    @property
    def column_separator(self):
        """Get column_separator

        Returns:
            str: the value of `column_separator` or None if not set
        """
        return self._data["Column Separator"]

    @column_separator.setter
    def column_separator(self, value="Comma"):
        """  Corresponds to IDD Field `column_separator`

        Args:
            value (str): value for IDD Field `column_separator`
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
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `column_separator`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `column_separator`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `column_separator`')
            vals = {}
            vals["comma"] = "Comma"
            vals["tab"] = "Tab"
            vals["fixed"] = "Fixed"
            value_lower = value.lower()
            if value_lower not in vals:
                found = False
                if self.accept_substring:
                    for key in vals:
                        if key in value_lower:
                            value_lower = key
                            found = True
                            break

                if not found:
                    raise ValueError('value {} is not an accepted value for '
                                     'field `column_separator`'.format(value))
            value = vals[value_lower]

        self._data["Column Separator"] = value

    def check(self):
        """ Checks if all required fields are not None
        """
        good = True
        for key in self.required_fields:
            if self._data[key] is None:
                good = False
                break
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
        for key, value in self._data.iteritems():
            out.append(self._to_str(value))
        return out

    def __str__(self):
        out = [self.internal_name]
        out += self.export()
        return ",".join(out[:20])