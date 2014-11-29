from collections import OrderedDict

class RoofIrrigation(object):
    """ Corresponds to IDD object `RoofIrrigation`
        Used to describe the amount of irrigation on the ecoroof surface over the course
        of the simulation runperiod.
    """
    internal_name = "RoofIrrigation"
    field_count = 3

    def __init__(self):
        """ Init data dictionary object for EPW IDD  `RoofIrrigation`
        """
        self._data = OrderedDict()
        self._data["Irrigation Model Type"] = None
        self._data["Irrigation Rate Schedule Name"] = None
        self._data["Irrigation Maximum Saturation Threshold"] = None

    def read(self, vals):
        """ Read values

        Args:
            vals (list): list of strings representing values
        """
        i = 0
        if len(vals[i]) == 0:
            self.irrigation_model_type = None
        else:
            self.irrigation_model_type = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.irrigation_rate_schedule_name = None
        else:
            self.irrigation_rate_schedule_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.irrigation_maximum_saturation_threshold = None
        else:
            self.irrigation_maximum_saturation_threshold = vals[i]
        i += 1

    @property
    def irrigation_model_type(self):
        """Get irrigation_model_type

        Returns:
            str: the value of `irrigation_model_type` or None if not set
        """
        return self._data["Irrigation Model Type"]

    @irrigation_model_type.setter
    def irrigation_model_type(self, value=None):
        """  Corresponds to IDD Field `irrigation_model_type`
        SmartSchedule will not allow irrigation when soil is already moist.
        Current threshold set at 30% of saturation.

        Args:
            value (str): value for IDD Field `irrigation_model_type`
                Accepted values are:
                      - Schedule
                      - SmartSchedule
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
                                 'for field `irrigation_model_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `irrigation_model_type`')
            vals = set()
            vals.add("Schedule")
            vals.add("SmartSchedule")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `irrigation_model_type`'.format(value))

        self._data["Irrigation Model Type"] = value

    @property
    def irrigation_rate_schedule_name(self):
        """Get irrigation_rate_schedule_name

        Returns:
            str: the value of `irrigation_rate_schedule_name` or None if not set
        """
        return self._data["Irrigation Rate Schedule Name"]

    @irrigation_rate_schedule_name.setter
    def irrigation_rate_schedule_name(self, value=None):
        """  Corresponds to IDD Field `irrigation_rate_schedule_name`
        Schedule values in meters of water per hour
        values should be non-negative

        Args:
            value (str): value for IDD Field `irrigation_rate_schedule_name`
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
                                 'for field `irrigation_rate_schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `irrigation_rate_schedule_name`')

        self._data["Irrigation Rate Schedule Name"] = value

    @property
    def irrigation_maximum_saturation_threshold(self):
        """Get irrigation_maximum_saturation_threshold

        Returns:
            float: the value of `irrigation_maximum_saturation_threshold` or None if not set
        """
        return self._data["Irrigation Maximum Saturation Threshold"]

    @irrigation_maximum_saturation_threshold.setter
    def irrigation_maximum_saturation_threshold(self, value=40.0 ):
        """  Corresponds to IDD Field `irrigation_maximum_saturation_threshold`
        Used with SmartSchedule to set the saturation level at which no
        irrigation is allowed.

        Args:
            value (float): value for IDD Field `irrigation_maximum_saturation_threshold`
                Unit: percent
                Default value: 40.0
                value >= 0.0
                value <= 100.0
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
                                 'for field `irrigation_maximum_saturation_threshold`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `irrigation_maximum_saturation_threshold`')
            if value > 100.0:
                raise ValueError('value need to be smaller 100.0 '
                                 'for field `irrigation_maximum_saturation_threshold`')

        self._data["Irrigation Maximum Saturation Threshold"] = value

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
        out.append(self._to_str(self.irrigation_model_type))
        out.append(self._to_str(self.irrigation_rate_schedule_name))
        out.append(self._to_str(self.irrigation_maximum_saturation_threshold))
        return ",".join(out)