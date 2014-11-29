from collections import OrderedDict

class ZoneAirContaminantBalance(object):
    """ Corresponds to IDD object `ZoneAirContaminantBalance`
        Determines which contaminant concentration will be simulates.
    """
    internal_name = "ZoneAirContaminantBalance"
    field_count = 4

    def __init__(self):
        """ Init data dictionary object for EPW IDD  `ZoneAirContaminantBalance`
        """
        self._data = OrderedDict()
        self._data["Carbon Dioxide Concentration"] = None
        self._data["Outdoor Carbon Dioxide Schedule Name"] = None
        self._data["Generic Contaminant Concentration"] = None
        self._data["Outdoor Generic Contaminant Schedule Name"] = None

    def read(self, vals):
        """ Read values

        Args:
            vals (list): list of strings representing values
        """
        i = 0
        if len(vals[i]) == 0:
            self.carbon_dioxide_concentration = None
        else:
            self.carbon_dioxide_concentration = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.outdoor_carbon_dioxide_schedule_name = None
        else:
            self.outdoor_carbon_dioxide_schedule_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.generic_contaminant_concentration = None
        else:
            self.generic_contaminant_concentration = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.outdoor_generic_contaminant_schedule_name = None
        else:
            self.outdoor_generic_contaminant_schedule_name = vals[i]
        i += 1

    @property
    def carbon_dioxide_concentration(self):
        """Get carbon_dioxide_concentration

        Returns:
            str: the value of `carbon_dioxide_concentration` or None if not set
        """
        return self._data["Carbon Dioxide Concentration"]

    @carbon_dioxide_concentration.setter
    def carbon_dioxide_concentration(self, value="No"):
        """  Corresponds to IDD Field `carbon_dioxide_concentration`
        If Yes, CO2 simulation will be performed.

        Args:
            value (str): value for IDD Field `carbon_dioxide_concentration`
                Accepted values are:
                      - Yes
                      - No
                Default value: No
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
                                 'for field `carbon_dioxide_concentration`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `carbon_dioxide_concentration`')
            vals = set()
            vals.add("Yes")
            vals.add("No")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `carbon_dioxide_concentration`'.format(value))

        self._data["Carbon Dioxide Concentration"] = value

    @property
    def outdoor_carbon_dioxide_schedule_name(self):
        """Get outdoor_carbon_dioxide_schedule_name

        Returns:
            str: the value of `outdoor_carbon_dioxide_schedule_name` or None if not set
        """
        return self._data["Outdoor Carbon Dioxide Schedule Name"]

    @outdoor_carbon_dioxide_schedule_name.setter
    def outdoor_carbon_dioxide_schedule_name(self, value=None):
        """  Corresponds to IDD Field `outdoor_carbon_dioxide_schedule_name`
        Schedule values should be in parts per million (ppm)

        Args:
            value (str): value for IDD Field `outdoor_carbon_dioxide_schedule_name`
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
                                 'for field `outdoor_carbon_dioxide_schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `outdoor_carbon_dioxide_schedule_name`')

        self._data["Outdoor Carbon Dioxide Schedule Name"] = value

    @property
    def generic_contaminant_concentration(self):
        """Get generic_contaminant_concentration

        Returns:
            str: the value of `generic_contaminant_concentration` or None if not set
        """
        return self._data["Generic Contaminant Concentration"]

    @generic_contaminant_concentration.setter
    def generic_contaminant_concentration(self, value="No"):
        """  Corresponds to IDD Field `generic_contaminant_concentration`
        If Yes, generic contaminant simulation will be performed.

        Args:
            value (str): value for IDD Field `generic_contaminant_concentration`
                Accepted values are:
                      - Yes
                      - No
                Default value: No
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
                                 'for field `generic_contaminant_concentration`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `generic_contaminant_concentration`')
            vals = set()
            vals.add("Yes")
            vals.add("No")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `generic_contaminant_concentration`'.format(value))

        self._data["Generic Contaminant Concentration"] = value

    @property
    def outdoor_generic_contaminant_schedule_name(self):
        """Get outdoor_generic_contaminant_schedule_name

        Returns:
            str: the value of `outdoor_generic_contaminant_schedule_name` or None if not set
        """
        return self._data["Outdoor Generic Contaminant Schedule Name"]

    @outdoor_generic_contaminant_schedule_name.setter
    def outdoor_generic_contaminant_schedule_name(self, value=None):
        """  Corresponds to IDD Field `outdoor_generic_contaminant_schedule_name`
        Schedule values should be generic contaminant concentration in parts per
        million (ppm)

        Args:
            value (str): value for IDD Field `outdoor_generic_contaminant_schedule_name`
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
                                 'for field `outdoor_generic_contaminant_schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `outdoor_generic_contaminant_schedule_name`')

        self._data["Outdoor Generic Contaminant Schedule Name"] = value

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
        out.append(self._to_str(self.carbon_dioxide_concentration))
        out.append(self._to_str(self.outdoor_carbon_dioxide_schedule_name))
        out.append(self._to_str(self.generic_contaminant_concentration))
        out.append(self._to_str(self.outdoor_generic_contaminant_schedule_name))
        return ",".join(out)