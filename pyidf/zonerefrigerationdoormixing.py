from collections import OrderedDict

class ZoneRefrigerationDoorMixing(object):
    """ Corresponds to IDD object `ZoneRefrigerationDoorMixing`
        Refrigeration Door Mixing is used for an opening between two zones that are at the
        same elevation but have different air temperatures.  In this case, the mixing air flow
        between the two zones is determined by the density difference between the two zones.
        This would typically be used between two zones in a refrigerated warehouse that are
        controlled at different temperatures.  It could also be used to model a door to a walk-in
        refrigerated space if that space were modeled as a zone instead of using the object Refrigeration:WalkIn.
    """
    internal_name = "ZoneRefrigerationDoorMixing"
    field_count = 7

    def __init__(self):
        """ Init data dictionary object for EPW IDD  `ZoneRefrigerationDoorMixing`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Zone 1 Name"] = None
        self._data["Zone 2 Name"] = None
        self._data["Schedule Name"] = None
        self._data["Door Height"] = None
        self._data["Door Area"] = None
        self._data["Door Protection Type"] = None

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
            self.zone_1_name = None
        else:
            self.zone_1_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.zone_2_name = None
        else:
            self.zone_2_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.schedule_name = None
        else:
            self.schedule_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.door_height = None
        else:
            self.door_height = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.door_area = None
        else:
            self.door_area = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.door_protection_type = None
        else:
            self.door_protection_type = vals[i]
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
    def zone_1_name(self):
        """Get zone_1_name

        Returns:
            str: the value of `zone_1_name` or None if not set
        """
        return self._data["Zone 1 Name"]

    @zone_1_name.setter
    def zone_1_name(self, value=None):
        """  Corresponds to IDD Field `zone_1_name`

        Args:
            value (str): value for IDD Field `zone_1_name`
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
                                 'for field `zone_1_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `zone_1_name`')

        self._data["Zone 1 Name"] = value

    @property
    def zone_2_name(self):
        """Get zone_2_name

        Returns:
            str: the value of `zone_2_name` or None if not set
        """
        return self._data["Zone 2 Name"]

    @zone_2_name.setter
    def zone_2_name(self, value=None):
        """  Corresponds to IDD Field `zone_2_name`

        Args:
            value (str): value for IDD Field `zone_2_name`
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
                                 'for field `zone_2_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `zone_2_name`')

        self._data["Zone 2 Name"] = value

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
        This schedule defines the fraction of the time the refrigeration door is open
        For example, if the warehouse is closed at night and there are no door openings
        between two zones, the value for that time period would be 0.
        If doors were propped open, the value  over that time period would be 1.0
        If the doors were open about 20% of the time, the value over that period would be 0.2
        Schedule values must lie between 0 and 1.0

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
    def door_height(self):
        """Get door_height

        Returns:
            float: the value of `door_height` or None if not set
        """
        return self._data["Door Height"]

    @door_height.setter
    def door_height(self, value=3.0 ):
        """  Corresponds to IDD Field `door_height`

        Args:
            value (float): value for IDD Field `door_height`
                Unit: m
                Default value: 3.0
                value >= 0.0
                value <= 50.0
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
                                 'for field `door_height`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `door_height`')
            if value > 50.0:
                raise ValueError('value need to be smaller 50.0 '
                                 'for field `door_height`')

        self._data["Door Height"] = value

    @property
    def door_area(self):
        """Get door_area

        Returns:
            float: the value of `door_area` or None if not set
        """
        return self._data["Door Area"]

    @door_area.setter
    def door_area(self, value=9.0 ):
        """  Corresponds to IDD Field `door_area`

        Args:
            value (float): value for IDD Field `door_area`
                Unit: m2
                Default value: 9.0
                value >= 0.0
                value <= 400.0
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
                                 'for field `door_area`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `door_area`')
            if value > 400.0:
                raise ValueError('value need to be smaller 400.0 '
                                 'for field `door_area`')

        self._data["Door Area"] = value

    @property
    def door_protection_type(self):
        """Get door_protection_type

        Returns:
            str: the value of `door_protection_type` or None if not set
        """
        return self._data["Door Protection Type"]

    @door_protection_type.setter
    def door_protection_type(self, value="None"):
        """  Corresponds to IDD Field `door_protection_type`
        Door protection can reduce the air flow through a refrigeration door
        The default value is "None"
        Choices: "None", "AirCurtain", and "StripCurtain"
        A strip curtain reduces the air flow more than an air curtain

        Args:
            value (str): value for IDD Field `door_protection_type`
                Accepted values are:
                      - None
                      - AirCurtain
                      - StripCurtain
                Default value: None
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
                                 'for field `door_protection_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `door_protection_type`')
            vals = set()
            vals.add("None")
            vals.add("AirCurtain")
            vals.add("StripCurtain")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `door_protection_type`'.format(value))

        self._data["Door Protection Type"] = value

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
        out.append(self._to_str(self.zone_1_name))
        out.append(self._to_str(self.zone_2_name))
        out.append(self._to_str(self.schedule_name))
        out.append(self._to_str(self.door_height))
        out.append(self._to_str(self.door_area))
        out.append(self._to_str(self.door_protection_type))
        return ",".join(out)