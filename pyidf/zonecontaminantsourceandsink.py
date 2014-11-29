from collections import OrderedDict

class ZoneContaminantSourceAndSinkCarbonDioxide(object):
    """ Corresponds to IDD object `ZoneContaminantSourceAndSink:CarbonDioxide`
        Represents internal CO2 gains and sinks in the zone.
    """
    internal_name = "ZoneContaminantSourceAndSink:CarbonDioxide"
    field_count = 4

    def __init__(self):
        """ Init data dictionary object for EPW IDD  `ZoneContaminantSourceAndSink:CarbonDioxide`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Zone Name"] = None
        self._data["Design Generation Rate"] = None
        self._data["Schedule Name"] = None

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
            self.design_generation_rate = None
        else:
            self.design_generation_rate = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.schedule_name = None
        else:
            self.schedule_name = vals[i]
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
    def design_generation_rate(self):
        """Get design_generation_rate

        Returns:
            float: the value of `design_generation_rate` or None if not set
        """
        return self._data["Design Generation Rate"]

    @design_generation_rate.setter
    def design_generation_rate(self, value=None):
        """  Corresponds to IDD Field `design_generation_rate`

        Args:
            value (float): value for IDD Field `design_generation_rate`
                Unit: m3/s
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
                                 'for field `design_generation_rate`'.format(value))

        self._data["Design Generation Rate"] = value

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
        Value in this schedule should be a fraction (generally 0.0 - 1.0) applied to the Design Generation Rate

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
        out.append(self._to_str(self.design_generation_rate))
        out.append(self._to_str(self.schedule_name))
        return ",".join(out)

class ZoneContaminantSourceAndSinkGenericConstant(object):
    """ Corresponds to IDD object `ZoneContaminantSourceAndSink:Generic:Constant`
        Sets internal generic contaminant gains and sinks in a zone with constant values.
    """
    internal_name = "ZoneContaminantSourceAndSink:Generic:Constant"
    field_count = 6

    def __init__(self):
        """ Init data dictionary object for EPW IDD  `ZoneContaminantSourceAndSink:Generic:Constant`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Zone Name"] = None
        self._data["Design Generation Rate"] = None
        self._data["Generation Schedule Name"] = None
        self._data["Design Removal Coefficient"] = None
        self._data["Removal Schedule Name"] = None

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
            self.design_generation_rate = None
        else:
            self.design_generation_rate = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.generation_schedule_name = None
        else:
            self.generation_schedule_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.design_removal_coefficient = None
        else:
            self.design_removal_coefficient = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.removal_schedule_name = None
        else:
            self.removal_schedule_name = vals[i]
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
    def design_generation_rate(self):
        """Get design_generation_rate

        Returns:
            float: the value of `design_generation_rate` or None if not set
        """
        return self._data["Design Generation Rate"]

    @design_generation_rate.setter
    def design_generation_rate(self, value=None):
        """  Corresponds to IDD Field `design_generation_rate`

        Args:
            value (float): value for IDD Field `design_generation_rate`
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
                                 'for field `design_generation_rate`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `design_generation_rate`')

        self._data["Design Generation Rate"] = value

    @property
    def generation_schedule_name(self):
        """Get generation_schedule_name

        Returns:
            str: the value of `generation_schedule_name` or None if not set
        """
        return self._data["Generation Schedule Name"]

    @generation_schedule_name.setter
    def generation_schedule_name(self, value=None):
        """  Corresponds to IDD Field `generation_schedule_name`
        Value in this schedule should be a fraction (generally 0.0 - 1.0) applied to the Design Generation Rate

        Args:
            value (str): value for IDD Field `generation_schedule_name`
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
                                 'for field `generation_schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `generation_schedule_name`')

        self._data["Generation Schedule Name"] = value

    @property
    def design_removal_coefficient(self):
        """Get design_removal_coefficient

        Returns:
            float: the value of `design_removal_coefficient` or None if not set
        """
        return self._data["Design Removal Coefficient"]

    @design_removal_coefficient.setter
    def design_removal_coefficient(self, value=None):
        """  Corresponds to IDD Field `design_removal_coefficient`

        Args:
            value (float): value for IDD Field `design_removal_coefficient`
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
                                 'for field `design_removal_coefficient`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `design_removal_coefficient`')

        self._data["Design Removal Coefficient"] = value

    @property
    def removal_schedule_name(self):
        """Get removal_schedule_name

        Returns:
            str: the value of `removal_schedule_name` or None if not set
        """
        return self._data["Removal Schedule Name"]

    @removal_schedule_name.setter
    def removal_schedule_name(self, value=None):
        """  Corresponds to IDD Field `removal_schedule_name`
        Value in this schedule should be a fraction (generally 0.0 - 1.0) applied to the
        Design removal Coefficient

        Args:
            value (str): value for IDD Field `removal_schedule_name`
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
                                 'for field `removal_schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `removal_schedule_name`')

        self._data["Removal Schedule Name"] = value

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
        out.append(self._to_str(self.design_generation_rate))
        out.append(self._to_str(self.generation_schedule_name))
        out.append(self._to_str(self.design_removal_coefficient))
        out.append(self._to_str(self.removal_schedule_name))
        return ",".join(out)

class ZoneContaminantSourceAndSinkGenericCutoffModel(object):
    """ Corresponds to IDD object `ZoneContaminantSourceAndSink:Generic:CutoffModel`
        Simulate generic contaminant source driven by the cutoff concentration model.
    """
    internal_name = "ZoneContaminantSourceAndSink:Generic:CutoffModel"
    field_count = 5

    def __init__(self):
        """ Init data dictionary object for EPW IDD  `ZoneContaminantSourceAndSink:Generic:CutoffModel`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Zone Name"] = None
        self._data["Design Generation Rate Coefficient"] = None
        self._data["Schedule Name"] = None
        self._data["Cutoff Generic Contaminant at which Emission Ceases"] = None

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
            self.design_generation_rate_coefficient = None
        else:
            self.design_generation_rate_coefficient = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.schedule_name = None
        else:
            self.schedule_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.cutoff_generic_contaminant_at_which_emission_ceases = None
        else:
            self.cutoff_generic_contaminant_at_which_emission_ceases = vals[i]
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
    def design_generation_rate_coefficient(self):
        """Get design_generation_rate_coefficient

        Returns:
            float: the value of `design_generation_rate_coefficient` or None if not set
        """
        return self._data["Design Generation Rate Coefficient"]

    @design_generation_rate_coefficient.setter
    def design_generation_rate_coefficient(self, value=None):
        """  Corresponds to IDD Field `design_generation_rate_coefficient`

        Args:
            value (float): value for IDD Field `design_generation_rate_coefficient`
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
                                 'for field `design_generation_rate_coefficient`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `design_generation_rate_coefficient`')

        self._data["Design Generation Rate Coefficient"] = value

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
        Value in this schedule should be a fraction (generally 0.0 - 1.0) applied to the
        Design Generation Rate Coefficient

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
    def cutoff_generic_contaminant_at_which_emission_ceases(self):
        """Get cutoff_generic_contaminant_at_which_emission_ceases

        Returns:
            float: the value of `cutoff_generic_contaminant_at_which_emission_ceases` or None if not set
        """
        return self._data["Cutoff Generic Contaminant at which Emission Ceases"]

    @cutoff_generic_contaminant_at_which_emission_ceases.setter
    def cutoff_generic_contaminant_at_which_emission_ceases(self, value=None):
        """  Corresponds to IDD Field `cutoff_generic_contaminant_at_which_emission_ceases`
        When the zone concentration level is greater than the cutoff level, emission stops,
        and the source level is zero.

        Args:
            value (float): value for IDD Field `cutoff_generic_contaminant_at_which_emission_ceases`
                Unit: ppm
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
                                 'for field `cutoff_generic_contaminant_at_which_emission_ceases`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `cutoff_generic_contaminant_at_which_emission_ceases`')

        self._data["Cutoff Generic Contaminant at which Emission Ceases"] = value

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
        out.append(self._to_str(self.design_generation_rate_coefficient))
        out.append(self._to_str(self.schedule_name))
        out.append(self._to_str(self.cutoff_generic_contaminant_at_which_emission_ceases))
        return ",".join(out)

class ZoneContaminantSourceAndSinkGenericDecaySource(object):
    """ Corresponds to IDD object `ZoneContaminantSourceAndSink:Generic:DecaySource`
        Simulate generic contaminant source driven by the cutoff concentration model.
    """
    internal_name = "ZoneContaminantSourceAndSink:Generic:DecaySource"
    field_count = 5

    def __init__(self):
        """ Init data dictionary object for EPW IDD  `ZoneContaminantSourceAndSink:Generic:DecaySource`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Zone Name"] = None
        self._data["Initial Emission Rate"] = None
        self._data["Schedule Name"] = None
        self._data["Delay Time Constant"] = None

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
            self.initial_emission_rate = None
        else:
            self.initial_emission_rate = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.schedule_name = None
        else:
            self.schedule_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.delay_time_constant = None
        else:
            self.delay_time_constant = vals[i]
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
    def initial_emission_rate(self):
        """Get initial_emission_rate

        Returns:
            float: the value of `initial_emission_rate` or None if not set
        """
        return self._data["Initial Emission Rate"]

    @initial_emission_rate.setter
    def initial_emission_rate(self, value=None):
        """  Corresponds to IDD Field `initial_emission_rate`

        Args:
            value (float): value for IDD Field `initial_emission_rate`
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
                                 'for field `initial_emission_rate`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `initial_emission_rate`')

        self._data["Initial Emission Rate"] = value

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
        Value in this schedule should be a fraction (generally 0.0 - 1.0) applied to the
        Initial Emission Rate. When the value is equal to 1.0, the time will be reset to
        zero.

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
    def delay_time_constant(self):
        """Get delay_time_constant

        Returns:
            float: the value of `delay_time_constant` or None if not set
        """
        return self._data["Delay Time Constant"]

    @delay_time_constant.setter
    def delay_time_constant(self, value=None):
        """  Corresponds to IDD Field `delay_time_constant`

        Args:
            value (float): value for IDD Field `delay_time_constant`
                Unit: s
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
                                 'for field `delay_time_constant`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `delay_time_constant`')

        self._data["Delay Time Constant"] = value

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
        out.append(self._to_str(self.initial_emission_rate))
        out.append(self._to_str(self.schedule_name))
        out.append(self._to_str(self.delay_time_constant))
        return ",".join(out)

class ZoneContaminantSourceAndSinkGenericDepositionRateSink(object):
    """ Corresponds to IDD object `ZoneContaminantSourceAndSink:Generic:DepositionRateSink`
        Simulate generic contaminant source driven by the boundary layer diffusion controlled model.
    """
    internal_name = "ZoneContaminantSourceAndSink:Generic:DepositionRateSink"
    field_count = 4

    def __init__(self):
        """ Init data dictionary object for EPW IDD  `ZoneContaminantSourceAndSink:Generic:DepositionRateSink`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Zone Name"] = None
        self._data["Deposition Rate"] = None
        self._data["Schedule Name"] = None

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
            self.deposition_rate = None
        else:
            self.deposition_rate = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.schedule_name = None
        else:
            self.schedule_name = vals[i]
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
    def deposition_rate(self):
        """Get deposition_rate

        Returns:
            float: the value of `deposition_rate` or None if not set
        """
        return self._data["Deposition Rate"]

    @deposition_rate.setter
    def deposition_rate(self, value=None):
        """  Corresponds to IDD Field `deposition_rate`

        Args:
            value (float): value for IDD Field `deposition_rate`
                Unit: m/s
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
                                 'for field `deposition_rate`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `deposition_rate`')

        self._data["Deposition Rate"] = value

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
        Value in this schedule should be a fraction (generally 0.0 - 1.0) applied to the
        Initial Emission Rate. When the value is equal to 1.0, the time will be reset to
        zero.

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
        out.append(self._to_str(self.deposition_rate))
        out.append(self._to_str(self.schedule_name))
        return ",".join(out)