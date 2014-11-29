from collections import OrderedDict

class ZoneCrossMixing(object):
    """ Corresponds to IDD object `ZoneCrossMixing`
        ZoneCrossMixing exchanges an equal amount of air between two zones. Note that this
        statement affects the energy balance of both zones.
    """
    internal_name = "ZoneCrossMixing"
    field_count = 17

    def __init__(self):
        """ Init data dictionary object for EPW IDD  `ZoneCrossMixing`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Zone Name"] = None
        self._data["Schedule Name"] = None
        self._data["Design Flow Rate Calculation Method"] = None
        self._data["Design Flow Rate"] = None
        self._data["Flow Rate per Zone Floor Area"] = None
        self._data["Flow Rate per Person"] = None
        self._data["Air Changes per Hour"] = None
        self._data["Source Zone Name"] = None
        self._data["Delta Temperature"] = None
        self._data["Delta Temperature Schedule Name"] = None
        self._data["Minimum Zone Temperature Schedule Name"] = None
        self._data["Maximum Zone Temperature Schedule Name"] = None
        self._data["Minimum Source Zone Temperature Schedule Name"] = None
        self._data["Maximum Source Zone Temperature Schedule Name"] = None
        self._data["Minimum Outdoor Temperature Schedule Name"] = None
        self._data["Maximum Outdoor Temperature Schedule Name"] = None

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
            self.schedule_name = None
        else:
            self.schedule_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.design_flow_rate_calculation_method = None
        else:
            self.design_flow_rate_calculation_method = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.design_flow_rate = None
        else:
            self.design_flow_rate = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.flow_rate_per_zone_floor_area = None
        else:
            self.flow_rate_per_zone_floor_area = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.flow_rate_per_person = None
        else:
            self.flow_rate_per_person = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.air_changes_per_hour = None
        else:
            self.air_changes_per_hour = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.source_zone_name = None
        else:
            self.source_zone_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.delta_temperature = None
        else:
            self.delta_temperature = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.delta_temperature_schedule_name = None
        else:
            self.delta_temperature_schedule_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.minimum_zone_temperature_schedule_name = None
        else:
            self.minimum_zone_temperature_schedule_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.maximum_zone_temperature_schedule_name = None
        else:
            self.maximum_zone_temperature_schedule_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.minimum_source_zone_temperature_schedule_name = None
        else:
            self.minimum_source_zone_temperature_schedule_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.maximum_source_zone_temperature_schedule_name = None
        else:
            self.maximum_source_zone_temperature_schedule_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.minimum_outdoor_temperature_schedule_name = None
        else:
            self.minimum_outdoor_temperature_schedule_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.maximum_outdoor_temperature_schedule_name = None
        else:
            self.maximum_outdoor_temperature_schedule_name = vals[i]
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
    def schedule_name(self):
        """Get schedule_name

        Returns:
            str: the value of `schedule_name` or None if not set
        """
        return self._data["Schedule Name"]

    @schedule_name.setter
    def schedule_name(self, value=None):
        """  Corresponds to IDD Field `schedule_name`

        Args:
            value (str): value for IDD Field `schedule_name`
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
                                 'for field `schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `schedule_name`')

        self._data["Schedule Name"] = value

    @property
    def design_flow_rate_calculation_method(self):
        """Get design_flow_rate_calculation_method

        Returns:
            str: the value of `design_flow_rate_calculation_method` or None if not set
        """
        return self._data["Design Flow Rate Calculation Method"]

    @design_flow_rate_calculation_method.setter
    def design_flow_rate_calculation_method(self, value="Flow/Zone"):
        """  Corresponds to IDD Field `design_flow_rate_calculation_method`
        The entered calculation method is used to create the maximum amount of ventilation
        for this set of attributes
        Choices: Flow/Zone => Design Flow Rate -- simply enter Design Flow Rate
        Flow/Area => Flow Rate per Zone Floor Area - Value * Floor Area (zone) = Design Flow Rate
        Flow/Person => Flow Rate per Person - Value * #people = Design Flow Rate
        AirChanges/Hour => Air Changes per Hour - Value * Floor Volume (zone) adjusted for m3/s = Design Volume Flow Rate
        "Vdesign" in Equation is the result.

        Args:
            value (str): value for IDD Field `design_flow_rate_calculation_method`
                Accepted values are:
                      - Flow/Zone
                      - Flow/Person
                      - Flow/Area
                      - AirChanges/Hour
                Default value: Flow/Zone
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
                                 'for field `design_flow_rate_calculation_method`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `design_flow_rate_calculation_method`')
            vals = set()
            vals.add("Flow/Zone")
            vals.add("Flow/Person")
            vals.add("Flow/Area")
            vals.add("AirChanges/Hour")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `design_flow_rate_calculation_method`'.format(value))

        self._data["Design Flow Rate Calculation Method"] = value

    @property
    def design_flow_rate(self):
        """Get design_flow_rate

        Returns:
            float: the value of `design_flow_rate` or None if not set
        """
        return self._data["Design Flow Rate"]

    @design_flow_rate.setter
    def design_flow_rate(self, value=None):
        """  Corresponds to IDD Field `design_flow_rate`

        Args:
            value (float): value for IDD Field `design_flow_rate`
                Unit: m3/s
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
                                 'for field `design_flow_rate`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `design_flow_rate`')

        self._data["Design Flow Rate"] = value

    @property
    def flow_rate_per_zone_floor_area(self):
        """Get flow_rate_per_zone_floor_area

        Returns:
            float: the value of `flow_rate_per_zone_floor_area` or None if not set
        """
        return self._data["Flow Rate per Zone Floor Area"]

    @flow_rate_per_zone_floor_area.setter
    def flow_rate_per_zone_floor_area(self, value=None):
        """  Corresponds to IDD Field `flow_rate_per_zone_floor_area`

        Args:
            value (float): value for IDD Field `flow_rate_per_zone_floor_area`
                Unit: m3/s-m2
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
                                 'for field `flow_rate_per_zone_floor_area`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `flow_rate_per_zone_floor_area`')

        self._data["Flow Rate per Zone Floor Area"] = value

    @property
    def flow_rate_per_person(self):
        """Get flow_rate_per_person

        Returns:
            float: the value of `flow_rate_per_person` or None if not set
        """
        return self._data["Flow Rate per Person"]

    @flow_rate_per_person.setter
    def flow_rate_per_person(self, value=None):
        """  Corresponds to IDD Field `flow_rate_per_person`

        Args:
            value (float): value for IDD Field `flow_rate_per_person`
                Unit: m3/s-person
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
                                 'for field `flow_rate_per_person`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `flow_rate_per_person`')

        self._data["Flow Rate per Person"] = value

    @property
    def air_changes_per_hour(self):
        """Get air_changes_per_hour

        Returns:
            float: the value of `air_changes_per_hour` or None if not set
        """
        return self._data["Air Changes per Hour"]

    @air_changes_per_hour.setter
    def air_changes_per_hour(self, value=None):
        """  Corresponds to IDD Field `air_changes_per_hour`

        Args:
            value (float): value for IDD Field `air_changes_per_hour`
                Unit: 1/hr
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
                                 'for field `air_changes_per_hour`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `air_changes_per_hour`')

        self._data["Air Changes per Hour"] = value

    @property
    def source_zone_name(self):
        """Get source_zone_name

        Returns:
            str: the value of `source_zone_name` or None if not set
        """
        return self._data["Source Zone Name"]

    @source_zone_name.setter
    def source_zone_name(self, value=None):
        """  Corresponds to IDD Field `source_zone_name`

        Args:
            value (str): value for IDD Field `source_zone_name`
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
                                 'for field `source_zone_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `source_zone_name`')

        self._data["Source Zone Name"] = value

    @property
    def delta_temperature(self):
        """Get delta_temperature

        Returns:
            float: the value of `delta_temperature` or None if not set
        """
        return self._data["Delta Temperature"]

    @delta_temperature.setter
    def delta_temperature(self, value=0.0 ):
        """  Corresponds to IDD Field `delta_temperature`
        This field contains the constant temperature differential between source and
        receiving zones below which cross mixing is shutoff. This value must be greater
        than or equal to zero.

        Args:
            value (float): value for IDD Field `delta_temperature`
                Unit: deltaC
                Default value: 0.0
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
                                 'for field `delta_temperature`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `delta_temperature`')

        self._data["Delta Temperature"] = value

    @property
    def delta_temperature_schedule_name(self):
        """Get delta_temperature_schedule_name

        Returns:
            str: the value of `delta_temperature_schedule_name` or None if not set
        """
        return self._data["Delta Temperature Schedule Name"]

    @delta_temperature_schedule_name.setter
    def delta_temperature_schedule_name(self, value=None):
        """  Corresponds to IDD Field `delta_temperature_schedule_name`
        This schedule contains the temperature differential between source and receiving
        zones versus time below which cross mixing is shutoff.

        Args:
            value (str): value for IDD Field `delta_temperature_schedule_name`
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
                                 'for field `delta_temperature_schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `delta_temperature_schedule_name`')

        self._data["Delta Temperature Schedule Name"] = value

    @property
    def minimum_zone_temperature_schedule_name(self):
        """Get minimum_zone_temperature_schedule_name

        Returns:
            str: the value of `minimum_zone_temperature_schedule_name` or None if not set
        """
        return self._data["Minimum Zone Temperature Schedule Name"]

    @minimum_zone_temperature_schedule_name.setter
    def minimum_zone_temperature_schedule_name(self, value=None):
        """  Corresponds to IDD Field `minimum_zone_temperature_schedule_name`
        This schedule contains the indoor temperature versus time below which
        cross mixing is shutoff.

        Args:
            value (str): value for IDD Field `minimum_zone_temperature_schedule_name`
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
                                 'for field `minimum_zone_temperature_schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `minimum_zone_temperature_schedule_name`')

        self._data["Minimum Zone Temperature Schedule Name"] = value

    @property
    def maximum_zone_temperature_schedule_name(self):
        """Get maximum_zone_temperature_schedule_name

        Returns:
            str: the value of `maximum_zone_temperature_schedule_name` or None if not set
        """
        return self._data["Maximum Zone Temperature Schedule Name"]

    @maximum_zone_temperature_schedule_name.setter
    def maximum_zone_temperature_schedule_name(self, value=None):
        """  Corresponds to IDD Field `maximum_zone_temperature_schedule_name`
        This schedule contains the indoor temperature versus time above which
        cross mixing is shutoff.

        Args:
            value (str): value for IDD Field `maximum_zone_temperature_schedule_name`
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
                                 'for field `maximum_zone_temperature_schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `maximum_zone_temperature_schedule_name`')

        self._data["Maximum Zone Temperature Schedule Name"] = value

    @property
    def minimum_source_zone_temperature_schedule_name(self):
        """Get minimum_source_zone_temperature_schedule_name

        Returns:
            str: the value of `minimum_source_zone_temperature_schedule_name` or None if not set
        """
        return self._data["Minimum Source Zone Temperature Schedule Name"]

    @minimum_source_zone_temperature_schedule_name.setter
    def minimum_source_zone_temperature_schedule_name(self, value=None):
        """  Corresponds to IDD Field `minimum_source_zone_temperature_schedule_name`
        This schedule contains the source zone dry-bulb temperature versus time below
        which cross mixing is shutoff.

        Args:
            value (str): value for IDD Field `minimum_source_zone_temperature_schedule_name`
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
                                 'for field `minimum_source_zone_temperature_schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `minimum_source_zone_temperature_schedule_name`')

        self._data["Minimum Source Zone Temperature Schedule Name"] = value

    @property
    def maximum_source_zone_temperature_schedule_name(self):
        """Get maximum_source_zone_temperature_schedule_name

        Returns:
            str: the value of `maximum_source_zone_temperature_schedule_name` or None if not set
        """
        return self._data["Maximum Source Zone Temperature Schedule Name"]

    @maximum_source_zone_temperature_schedule_name.setter
    def maximum_source_zone_temperature_schedule_name(self, value=None):
        """  Corresponds to IDD Field `maximum_source_zone_temperature_schedule_name`
        This schedule contains the source zone dry-bulb temperature versus time above
        which cross mixing is shutoff.

        Args:
            value (str): value for IDD Field `maximum_source_zone_temperature_schedule_name`
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
                                 'for field `maximum_source_zone_temperature_schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `maximum_source_zone_temperature_schedule_name`')

        self._data["Maximum Source Zone Temperature Schedule Name"] = value

    @property
    def minimum_outdoor_temperature_schedule_name(self):
        """Get minimum_outdoor_temperature_schedule_name

        Returns:
            str: the value of `minimum_outdoor_temperature_schedule_name` or None if not set
        """
        return self._data["Minimum Outdoor Temperature Schedule Name"]

    @minimum_outdoor_temperature_schedule_name.setter
    def minimum_outdoor_temperature_schedule_name(self, value=None):
        """  Corresponds to IDD Field `minimum_outdoor_temperature_schedule_name`
        This schedule contains the outdoor temperature versus time below which
        cross mixing is shutoff.

        Args:
            value (str): value for IDD Field `minimum_outdoor_temperature_schedule_name`
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
                                 'for field `minimum_outdoor_temperature_schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `minimum_outdoor_temperature_schedule_name`')

        self._data["Minimum Outdoor Temperature Schedule Name"] = value

    @property
    def maximum_outdoor_temperature_schedule_name(self):
        """Get maximum_outdoor_temperature_schedule_name

        Returns:
            str: the value of `maximum_outdoor_temperature_schedule_name` or None if not set
        """
        return self._data["Maximum Outdoor Temperature Schedule Name"]

    @maximum_outdoor_temperature_schedule_name.setter
    def maximum_outdoor_temperature_schedule_name(self, value=None):
        """  Corresponds to IDD Field `maximum_outdoor_temperature_schedule_name`
        This schedule contains the outdoor temperature versus time above which
        cross mixing is shutoff.

        Args:
            value (str): value for IDD Field `maximum_outdoor_temperature_schedule_name`
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
                                 'for field `maximum_outdoor_temperature_schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `maximum_outdoor_temperature_schedule_name`')

        self._data["Maximum Outdoor Temperature Schedule Name"] = value

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
        out.append(self._to_str(self.schedule_name))
        out.append(self._to_str(self.design_flow_rate_calculation_method))
        out.append(self._to_str(self.design_flow_rate))
        out.append(self._to_str(self.flow_rate_per_zone_floor_area))
        out.append(self._to_str(self.flow_rate_per_person))
        out.append(self._to_str(self.air_changes_per_hour))
        out.append(self._to_str(self.source_zone_name))
        out.append(self._to_str(self.delta_temperature))
        out.append(self._to_str(self.delta_temperature_schedule_name))
        out.append(self._to_str(self.minimum_zone_temperature_schedule_name))
        out.append(self._to_str(self.maximum_zone_temperature_schedule_name))
        out.append(self._to_str(self.minimum_source_zone_temperature_schedule_name))
        out.append(self._to_str(self.maximum_source_zone_temperature_schedule_name))
        out.append(self._to_str(self.minimum_outdoor_temperature_schedule_name))
        out.append(self._to_str(self.maximum_outdoor_temperature_schedule_name))
        return ",".join(out)