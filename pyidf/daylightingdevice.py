from collections import OrderedDict

class DaylightingDeviceTubular(object):
    """ Corresponds to IDD object `DaylightingDevice:Tubular`
        Defines a tubular daylighting device (TDD) consisting of three components:
        a dome, a pipe, and a diffuser. The dome and diffuser are defined separately using the
        FenestrationSurface:Detailed object.
    """
    internal_name = "DaylightingDevice:Tubular"
    field_count = 15

    def __init__(self):
        """ Init data dictionary object for EPW IDD  `DaylightingDevice:Tubular`
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
            self.dome_name = None
        else:
            self.dome_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.diffuser_name = None
        else:
            self.diffuser_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.construction_name = None
        else:
            self.construction_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.diameter = None
        else:
            self.diameter = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.total_length = None
        else:
            self.total_length = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.effective_thermal_resistance = None
        else:
            self.effective_thermal_resistance = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.transition_zone_1_name = None
        else:
            self.transition_zone_1_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.transition_zone_1_length = None
        else:
            self.transition_zone_1_length = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.transition_zone_2_name = None
        else:
            self.transition_zone_2_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.transition_zone_2_length = None
        else:
            self.transition_zone_2_length = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.transition_zone_3_name = None
        else:
            self.transition_zone_3_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.transition_zone_3_length = None
        else:
            self.transition_zone_3_length = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.transition_zone_4_name = None
        else:
            self.transition_zone_4_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.transition_zone_4_length = None
        else:
            self.transition_zone_4_length = vals[i]
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
                Unit: m
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
                Unit: m
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
                Unit: m2-K/W
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
                Unit: m
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
                Unit: m
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
                Unit: m
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
                Unit: m
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
        out.append(self._to_str(self.dome_name))
        out.append(self._to_str(self.diffuser_name))
        out.append(self._to_str(self.construction_name))
        out.append(self._to_str(self.diameter))
        out.append(self._to_str(self.total_length))
        out.append(self._to_str(self.effective_thermal_resistance))
        out.append(self._to_str(self.transition_zone_1_name))
        out.append(self._to_str(self.transition_zone_1_length))
        out.append(self._to_str(self.transition_zone_2_name))
        out.append(self._to_str(self.transition_zone_2_length))
        out.append(self._to_str(self.transition_zone_3_name))
        out.append(self._to_str(self.transition_zone_3_length))
        out.append(self._to_str(self.transition_zone_4_name))
        out.append(self._to_str(self.transition_zone_4_length))
        return ",".join(out)

class DaylightingDeviceShelf(object):
    """ Corresponds to IDD object `DaylightingDevice:Shelf`
        Defines a daylighting which can have an inside shelf, an outside shelf, or both.
        The inside shelf is defined as a building surface and the outside shelf is defined
        as a shading surface.
    """
    internal_name = "DaylightingDevice:Shelf"
    field_count = 6

    def __init__(self):
        """ Init data dictionary object for EPW IDD  `DaylightingDevice:Shelf`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Window Name"] = None
        self._data["Inside Shelf Name"] = None
        self._data["Outside Shelf Name"] = None
        self._data["Outside Shelf Construction Name"] = None
        self._data["View Factor to Outside Shelf"] = None

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
            self.window_name = None
        else:
            self.window_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.inside_shelf_name = None
        else:
            self.inside_shelf_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.outside_shelf_name = None
        else:
            self.outside_shelf_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.outside_shelf_construction_name = None
        else:
            self.outside_shelf_construction_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.view_factor_to_outside_shelf = None
        else:
            self.view_factor_to_outside_shelf = vals[i]
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
        out.append(self._to_str(self.window_name))
        out.append(self._to_str(self.inside_shelf_name))
        out.append(self._to_str(self.outside_shelf_name))
        out.append(self._to_str(self.outside_shelf_construction_name))
        out.append(self._to_str(self.view_factor_to_outside_shelf))
        return ",".join(out)

class DaylightingDeviceLightWell(object):
    """ Corresponds to IDD object `DaylightingDevice:LightWell`
        Applies only to exterior windows in daylighting-controlled zones or
        in zones that share an interior window with a daylighting-controlled  zone.
        Generally used with skylights.
    """
    internal_name = "DaylightingDevice:LightWell"
    field_count = 5

    def __init__(self):
        """ Init data dictionary object for EPW IDD  `DaylightingDevice:LightWell`
        """
        self._data = OrderedDict()
        self._data["Exterior Window Name"] = None
        self._data["Height of Well"] = None
        self._data["Perimeter of Bottom of Well"] = None
        self._data["Area of Bottom of Well"] = None
        self._data["Visible Reflectance of Well Walls"] = None

    def read(self, vals):
        """ Read values

        Args:
            vals (list): list of strings representing values
        """
        i = 0
        if len(vals[i]) == 0:
            self.exterior_window_name = None
        else:
            self.exterior_window_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.height_of_well = None
        else:
            self.height_of_well = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.perimeter_of_bottom_of_well = None
        else:
            self.perimeter_of_bottom_of_well = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.area_of_bottom_of_well = None
        else:
            self.area_of_bottom_of_well = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.visible_reflectance_of_well_walls = None
        else:
            self.visible_reflectance_of_well_walls = vals[i]
        i += 1

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
                Unit: m
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
                Unit: m
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
                Unit: dimensionless
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
        out.append(self._to_str(self.exterior_window_name))
        out.append(self._to_str(self.height_of_well))
        out.append(self._to_str(self.perimeter_of_bottom_of_well))
        out.append(self._to_str(self.area_of_bottom_of_well))
        out.append(self._to_str(self.visible_reflectance_of_well_walls))
        return ",".join(out)