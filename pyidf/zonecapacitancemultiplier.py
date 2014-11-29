from collections import OrderedDict

class ZoneCapacitanceMultiplierResearchSpecial(object):
    """ Corresponds to IDD object `ZoneCapacitanceMultiplier:ResearchSpecial`
        Multiplier altering the relative capacitance of the air compared to an empty zone
    """
    internal_name = "ZoneCapacitanceMultiplier:ResearchSpecial"
    field_count = 4

    def __init__(self):
        """ Init data dictionary object for EPW IDD  `ZoneCapacitanceMultiplier:ResearchSpecial`
        """
        self._data = OrderedDict()
        self._data["Temperature Capacity Multiplier"] = None
        self._data["Humidity Capacity Multiplier"] = None
        self._data["Carbon Dioxide Capacity Multiplier"] = None
        self._data["Generic Contaminant Capacity Multiplier"] = None

    def read(self, vals):
        """ Read values

        Args:
            vals (list): list of strings representing values
        """
        i = 0
        if len(vals[i]) == 0:
            self.temperature_capacity_multiplier = None
        else:
            self.temperature_capacity_multiplier = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.humidity_capacity_multiplier = None
        else:
            self.humidity_capacity_multiplier = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.carbon_dioxide_capacity_multiplier = None
        else:
            self.carbon_dioxide_capacity_multiplier = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.generic_contaminant_capacity_multiplier = None
        else:
            self.generic_contaminant_capacity_multiplier = vals[i]
        i += 1

    @property
    def temperature_capacity_multiplier(self):
        """Get temperature_capacity_multiplier

        Returns:
            float: the value of `temperature_capacity_multiplier` or None if not set
        """
        return self._data["Temperature Capacity Multiplier"]

    @temperature_capacity_multiplier.setter
    def temperature_capacity_multiplier(self, value=1.0 ):
        """  Corresponds to IDD Field `temperature_capacity_multiplier`
        Used to alter the capacitance of zone air with respect to heat or temperature

        Args:
            value (float): value for IDD Field `temperature_capacity_multiplier`
                Default value: 1.0
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
                                 'for field `temperature_capacity_multiplier`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `temperature_capacity_multiplier`')

        self._data["Temperature Capacity Multiplier"] = value

    @property
    def humidity_capacity_multiplier(self):
        """Get humidity_capacity_multiplier

        Returns:
            float: the value of `humidity_capacity_multiplier` or None if not set
        """
        return self._data["Humidity Capacity Multiplier"]

    @humidity_capacity_multiplier.setter
    def humidity_capacity_multiplier(self, value=1.0 ):
        """  Corresponds to IDD Field `humidity_capacity_multiplier`
        Used to alter the capacitance of zone air with respect to moisture or humidity ratio

        Args:
            value (float): value for IDD Field `humidity_capacity_multiplier`
                Default value: 1.0
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
                                 'for field `humidity_capacity_multiplier`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `humidity_capacity_multiplier`')

        self._data["Humidity Capacity Multiplier"] = value

    @property
    def carbon_dioxide_capacity_multiplier(self):
        """Get carbon_dioxide_capacity_multiplier

        Returns:
            float: the value of `carbon_dioxide_capacity_multiplier` or None if not set
        """
        return self._data["Carbon Dioxide Capacity Multiplier"]

    @carbon_dioxide_capacity_multiplier.setter
    def carbon_dioxide_capacity_multiplier(self, value=1.0 ):
        """  Corresponds to IDD Field `carbon_dioxide_capacity_multiplier`
        Used to alter the capacitance of zone air with respect to zone air carbob dioxide concentration

        Args:
            value (float): value for IDD Field `carbon_dioxide_capacity_multiplier`
                Default value: 1.0
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
                                 'for field `carbon_dioxide_capacity_multiplier`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `carbon_dioxide_capacity_multiplier`')

        self._data["Carbon Dioxide Capacity Multiplier"] = value

    @property
    def generic_contaminant_capacity_multiplier(self):
        """Get generic_contaminant_capacity_multiplier

        Returns:
            float: the value of `generic_contaminant_capacity_multiplier` or None if not set
        """
        return self._data["Generic Contaminant Capacity Multiplier"]

    @generic_contaminant_capacity_multiplier.setter
    def generic_contaminant_capacity_multiplier(self, value=1.0 ):
        """  Corresponds to IDD Field `generic_contaminant_capacity_multiplier`
        Used to alter the capacitance of zone air with respect to zone air generic contaminant concentration

        Args:
            value (float): value for IDD Field `generic_contaminant_capacity_multiplier`
                Default value: 1.0
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
                                 'for field `generic_contaminant_capacity_multiplier`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `generic_contaminant_capacity_multiplier`')

        self._data["Generic Contaminant Capacity Multiplier"] = value

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
        out.append(self._to_str(self.temperature_capacity_multiplier))
        out.append(self._to_str(self.humidity_capacity_multiplier))
        out.append(self._to_str(self.carbon_dioxide_capacity_multiplier))
        out.append(self._to_str(self.generic_contaminant_capacity_multiplier))
        return ",".join(out)