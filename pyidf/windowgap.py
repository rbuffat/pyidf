from collections import OrderedDict

class WindowGapSupportPillar(object):
    """ Corresponds to IDD object `WindowGap:SupportPillar`
        used to define pillar geometry for support pillars
    """
    internal_name = "WindowGap:SupportPillar"
    field_count = 3

    def __init__(self):
        """ Init data dictionary object for EPW IDD  `WindowGap:SupportPillar`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Spacing"] = None
        self._data["Radius"] = None

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
            self.spacing = None
        else:
            self.spacing = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.radius = None
        else:
            self.radius = vals[i]
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
    def spacing(self):
        """Get spacing

        Returns:
            float: the value of `spacing` or None if not set
        """
        return self._data["Spacing"]

    @spacing.setter
    def spacing(self, value=0.04 ):
        """  Corresponds to IDD Field `spacing`

        Args:
            value (float): value for IDD Field `spacing`
                Unit: m
                Default value: 0.04
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
                                 'for field `spacing`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `spacing`')

        self._data["Spacing"] = value

    @property
    def radius(self):
        """Get radius

        Returns:
            float: the value of `radius` or None if not set
        """
        return self._data["Radius"]

    @radius.setter
    def radius(self, value=0.0004 ):
        """  Corresponds to IDD Field `radius`

        Args:
            value (float): value for IDD Field `radius`
                Unit: m
                Default value: 0.0004
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
                                 'for field `radius`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `radius`')

        self._data["Radius"] = value

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
        out.append(self._to_str(self.spacing))
        out.append(self._to_str(self.radius))
        return ",".join(out)

class WindowGapDeflectionState(object):
    """ Corresponds to IDD object `WindowGap:DeflectionState`
        Used to enter data describing deflection state of the gap. It is referenced from
        WindowMaterial:Gap object only and it is used only when deflection model is set to
        MeasuredDeflection, otherwise it is ignored.
    """
    internal_name = "WindowGap:DeflectionState"
    field_count = 4

    def __init__(self):
        """ Init data dictionary object for EPW IDD  `WindowGap:DeflectionState`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Deflected Thickness"] = None
        self._data["Initial Temperature"] = None
        self._data["Initial Pressure"] = None

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
            self.deflected_thickness = None
        else:
            self.deflected_thickness = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.initial_temperature = None
        else:
            self.initial_temperature = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.initial_pressure = None
        else:
            self.initial_pressure = vals[i]
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
    def deflected_thickness(self):
        """Get deflected_thickness

        Returns:
            float: the value of `deflected_thickness` or None if not set
        """
        return self._data["Deflected Thickness"]

    @deflected_thickness.setter
    def deflected_thickness(self, value=0.0 ):
        """  Corresponds to IDD Field `deflected_thickness`
        If left blank will be considered that gap has no deflection.

        Args:
            value (float): value for IDD Field `deflected_thickness`
                Unit: m
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
                                 'for field `deflected_thickness`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `deflected_thickness`')

        self._data["Deflected Thickness"] = value

    @property
    def initial_temperature(self):
        """Get initial_temperature

        Returns:
            float: the value of `initial_temperature` or None if not set
        """
        return self._data["Initial Temperature"]

    @initial_temperature.setter
    def initial_temperature(self, value=25.0 ):
        """  Corresponds to IDD Field `initial_temperature`

        Args:
            value (float): value for IDD Field `initial_temperature`
                Unit: C
                Default value: 25.0
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
                                 'for field `initial_temperature`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `initial_temperature`')

        self._data["Initial Temperature"] = value

    @property
    def initial_pressure(self):
        """Get initial_pressure

        Returns:
            float: the value of `initial_pressure` or None if not set
        """
        return self._data["Initial Pressure"]

    @initial_pressure.setter
    def initial_pressure(self, value=101325.0 ):
        """  Corresponds to IDD Field `initial_pressure`

        Args:
            value (float): value for IDD Field `initial_pressure`
                Unit: Pa
                Default value: 101325.0
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
                                 'for field `initial_pressure`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `initial_pressure`')

        self._data["Initial Pressure"] = value

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
        out.append(self._to_str(self.deflected_thickness))
        out.append(self._to_str(self.initial_temperature))
        out.append(self._to_str(self.initial_pressure))
        return ",".join(out)