from collections import OrderedDict

class DemandManagerExteriorLights(object):
    """ Corresponds to IDD object `DemandManager:ExteriorLights`
        used for demand limiting Exterior:Lights objects.
    """
    internal_name = "DemandManager:ExteriorLights"
    field_count = 18

    def __init__(self):
        """ Init data dictionary object for EPW IDD  `DemandManager:ExteriorLights`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Availability Schedule Name"] = None
        self._data["Limit Control"] = None
        self._data["Minimum Limit Duration"] = None
        self._data["Maximum Limit Fraction"] = None
        self._data["Limit Step Change"] = None
        self._data["Selection Control"] = None
        self._data["Rotation Duration"] = None
        self._data["Exterior Lights 1 Name"] = None
        self._data["Exterior Lights 2 Name"] = None
        self._data["Exterior Lights 3 Name"] = None
        self._data["Exterior Lights 4 Name"] = None
        self._data["Exterior Lights 5 Name"] = None
        self._data["Exterior Lights 6 Name"] = None
        self._data["Exterior Lights 7 Name"] = None
        self._data["Exterior Lights 8 Name"] = None
        self._data["Exterior Lights 9 Name"] = None
        self._data["Exterior Lights 10 Name"] = None

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
            self.availability_schedule_name = None
        else:
            self.availability_schedule_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.limit_control = None
        else:
            self.limit_control = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.minimum_limit_duration = None
        else:
            self.minimum_limit_duration = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.maximum_limit_fraction = None
        else:
            self.maximum_limit_fraction = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.limit_step_change = None
        else:
            self.limit_step_change = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.selection_control = None
        else:
            self.selection_control = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.rotation_duration = None
        else:
            self.rotation_duration = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.exterior_lights_1_name = None
        else:
            self.exterior_lights_1_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.exterior_lights_2_name = None
        else:
            self.exterior_lights_2_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.exterior_lights_3_name = None
        else:
            self.exterior_lights_3_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.exterior_lights_4_name = None
        else:
            self.exterior_lights_4_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.exterior_lights_5_name = None
        else:
            self.exterior_lights_5_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.exterior_lights_6_name = None
        else:
            self.exterior_lights_6_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.exterior_lights_7_name = None
        else:
            self.exterior_lights_7_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.exterior_lights_8_name = None
        else:
            self.exterior_lights_8_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.exterior_lights_9_name = None
        else:
            self.exterior_lights_9_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.exterior_lights_10_name = None
        else:
            self.exterior_lights_10_name = vals[i]
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
    def availability_schedule_name(self):
        """Get availability_schedule_name

        Returns:
            str: the value of `availability_schedule_name` or None if not set
        """
        return self._data["Availability Schedule Name"]

    @availability_schedule_name.setter
    def availability_schedule_name(self, value=None):
        """  Corresponds to IDD Field `availability_schedule_name`
        Availability schedule name for this system. Schedule value > 0 means the system is available.
        If this field is blank, the system is always available.

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

    @property
    def limit_control(self):
        """Get limit_control

        Returns:
            str: the value of `limit_control` or None if not set
        """
        return self._data["Limit Control"]

    @limit_control.setter
    def limit_control(self, value=None):
        """  Corresponds to IDD Field `limit_control`

        Args:
            value (str): value for IDD Field `limit_control`
                Accepted values are:
                      - Off
                      - Fixed
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
                                 'for field `limit_control`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `limit_control`')
            vals = set()
            vals.add("Off")
            vals.add("Fixed")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `limit_control`'.format(value))

        self._data["Limit Control"] = value

    @property
    def minimum_limit_duration(self):
        """Get minimum_limit_duration

        Returns:
            int: the value of `minimum_limit_duration` or None if not set
        """
        return self._data["Minimum Limit Duration"]

    @minimum_limit_duration.setter
    def minimum_limit_duration(self, value=None):
        """  Corresponds to IDD Field `minimum_limit_duration`
        If blank, duration defaults to the timestep

        Args:
            value (int): value for IDD Field `minimum_limit_duration`
                Unit: minutes
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
                                 'for field `minimum_limit_duration`'.format(value))
            if value <= 0:
                raise ValueError('value need to be greater 0 '
                                 'for field `minimum_limit_duration`')

        self._data["Minimum Limit Duration"] = value

    @property
    def maximum_limit_fraction(self):
        """Get maximum_limit_fraction

        Returns:
            float: the value of `maximum_limit_fraction` or None if not set
        """
        return self._data["Maximum Limit Fraction"]

    @maximum_limit_fraction.setter
    def maximum_limit_fraction(self, value=None):
        """  Corresponds to IDD Field `maximum_limit_fraction`

        Args:
            value (float): value for IDD Field `maximum_limit_fraction`
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
                                 'for field `maximum_limit_fraction`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `maximum_limit_fraction`')
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `maximum_limit_fraction`')

        self._data["Maximum Limit Fraction"] = value

    @property
    def limit_step_change(self):
        """Get limit_step_change

        Returns:
            float: the value of `limit_step_change` or None if not set
        """
        return self._data["Limit Step Change"]

    @limit_step_change.setter
    def limit_step_change(self, value=None):
        """  Corresponds to IDD Field `limit_step_change`
        Not yet implemented

        Args:
            value (float): value for IDD Field `limit_step_change`
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
                                 'for field `limit_step_change`'.format(value))

        self._data["Limit Step Change"] = value

    @property
    def selection_control(self):
        """Get selection_control

        Returns:
            str: the value of `selection_control` or None if not set
        """
        return self._data["Selection Control"]

    @selection_control.setter
    def selection_control(self, value=None):
        """  Corresponds to IDD Field `selection_control`

        Args:
            value (str): value for IDD Field `selection_control`
                Accepted values are:
                      - All
                      - RotateMany
                      - RotateOne
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
                                 'for field `selection_control`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `selection_control`')
            vals = set()
            vals.add("All")
            vals.add("RotateMany")
            vals.add("RotateOne")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `selection_control`'.format(value))

        self._data["Selection Control"] = value

    @property
    def rotation_duration(self):
        """Get rotation_duration

        Returns:
            int: the value of `rotation_duration` or None if not set
        """
        return self._data["Rotation Duration"]

    @rotation_duration.setter
    def rotation_duration(self, value=None):
        """  Corresponds to IDD Field `rotation_duration`
        If blank, duration defaults to the timestep

        Args:
            value (int): value for IDD Field `rotation_duration`
                Unit: minutes
                value >= 0
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
                                 'for field `rotation_duration`'.format(value))
            if value < 0:
                raise ValueError('value need to be greater or equal 0 '
                                 'for field `rotation_duration`')

        self._data["Rotation Duration"] = value

    @property
    def exterior_lights_1_name(self):
        """Get exterior_lights_1_name

        Returns:
            str: the value of `exterior_lights_1_name` or None if not set
        """
        return self._data["Exterior Lights 1 Name"]

    @exterior_lights_1_name.setter
    def exterior_lights_1_name(self, value=None):
        """  Corresponds to IDD Field `exterior_lights_1_name`
        Enter the name of an Exterior:Lights object.

        Args:
            value (str): value for IDD Field `exterior_lights_1_name`
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
                                 'for field `exterior_lights_1_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `exterior_lights_1_name`')

        self._data["Exterior Lights 1 Name"] = value

    @property
    def exterior_lights_2_name(self):
        """Get exterior_lights_2_name

        Returns:
            str: the value of `exterior_lights_2_name` or None if not set
        """
        return self._data["Exterior Lights 2 Name"]

    @exterior_lights_2_name.setter
    def exterior_lights_2_name(self, value=None):
        """  Corresponds to IDD Field `exterior_lights_2_name`
        Enter the name of an Exterior:Lights object.

        Args:
            value (str): value for IDD Field `exterior_lights_2_name`
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
                                 'for field `exterior_lights_2_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `exterior_lights_2_name`')

        self._data["Exterior Lights 2 Name"] = value

    @property
    def exterior_lights_3_name(self):
        """Get exterior_lights_3_name

        Returns:
            str: the value of `exterior_lights_3_name` or None if not set
        """
        return self._data["Exterior Lights 3 Name"]

    @exterior_lights_3_name.setter
    def exterior_lights_3_name(self, value=None):
        """  Corresponds to IDD Field `exterior_lights_3_name`
        Enter the name of an Exterior:Lights object.

        Args:
            value (str): value for IDD Field `exterior_lights_3_name`
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
                                 'for field `exterior_lights_3_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `exterior_lights_3_name`')

        self._data["Exterior Lights 3 Name"] = value

    @property
    def exterior_lights_4_name(self):
        """Get exterior_lights_4_name

        Returns:
            str: the value of `exterior_lights_4_name` or None if not set
        """
        return self._data["Exterior Lights 4 Name"]

    @exterior_lights_4_name.setter
    def exterior_lights_4_name(self, value=None):
        """  Corresponds to IDD Field `exterior_lights_4_name`
        Enter the name of an Exterior:Lights object.

        Args:
            value (str): value for IDD Field `exterior_lights_4_name`
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
                                 'for field `exterior_lights_4_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `exterior_lights_4_name`')

        self._data["Exterior Lights 4 Name"] = value

    @property
    def exterior_lights_5_name(self):
        """Get exterior_lights_5_name

        Returns:
            str: the value of `exterior_lights_5_name` or None if not set
        """
        return self._data["Exterior Lights 5 Name"]

    @exterior_lights_5_name.setter
    def exterior_lights_5_name(self, value=None):
        """  Corresponds to IDD Field `exterior_lights_5_name`
        Enter the name of an Exterior:Lights object.

        Args:
            value (str): value for IDD Field `exterior_lights_5_name`
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
                                 'for field `exterior_lights_5_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `exterior_lights_5_name`')

        self._data["Exterior Lights 5 Name"] = value

    @property
    def exterior_lights_6_name(self):
        """Get exterior_lights_6_name

        Returns:
            str: the value of `exterior_lights_6_name` or None if not set
        """
        return self._data["Exterior Lights 6 Name"]

    @exterior_lights_6_name.setter
    def exterior_lights_6_name(self, value=None):
        """  Corresponds to IDD Field `exterior_lights_6_name`
        Enter the name of an Exterior:Lights object.

        Args:
            value (str): value for IDD Field `exterior_lights_6_name`
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
                                 'for field `exterior_lights_6_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `exterior_lights_6_name`')

        self._data["Exterior Lights 6 Name"] = value

    @property
    def exterior_lights_7_name(self):
        """Get exterior_lights_7_name

        Returns:
            str: the value of `exterior_lights_7_name` or None if not set
        """
        return self._data["Exterior Lights 7 Name"]

    @exterior_lights_7_name.setter
    def exterior_lights_7_name(self, value=None):
        """  Corresponds to IDD Field `exterior_lights_7_name`
        Enter the name of an Exterior:Lights object.

        Args:
            value (str): value for IDD Field `exterior_lights_7_name`
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
                                 'for field `exterior_lights_7_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `exterior_lights_7_name`')

        self._data["Exterior Lights 7 Name"] = value

    @property
    def exterior_lights_8_name(self):
        """Get exterior_lights_8_name

        Returns:
            str: the value of `exterior_lights_8_name` or None if not set
        """
        return self._data["Exterior Lights 8 Name"]

    @exterior_lights_8_name.setter
    def exterior_lights_8_name(self, value=None):
        """  Corresponds to IDD Field `exterior_lights_8_name`
        Enter the name of an Exterior:Lights object.

        Args:
            value (str): value for IDD Field `exterior_lights_8_name`
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
                                 'for field `exterior_lights_8_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `exterior_lights_8_name`')

        self._data["Exterior Lights 8 Name"] = value

    @property
    def exterior_lights_9_name(self):
        """Get exterior_lights_9_name

        Returns:
            str: the value of `exterior_lights_9_name` or None if not set
        """
        return self._data["Exterior Lights 9 Name"]

    @exterior_lights_9_name.setter
    def exterior_lights_9_name(self, value=None):
        """  Corresponds to IDD Field `exterior_lights_9_name`
        Enter the name of an Exterior:Lights object.

        Args:
            value (str): value for IDD Field `exterior_lights_9_name`
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
                                 'for field `exterior_lights_9_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `exterior_lights_9_name`')

        self._data["Exterior Lights 9 Name"] = value

    @property
    def exterior_lights_10_name(self):
        """Get exterior_lights_10_name

        Returns:
            str: the value of `exterior_lights_10_name` or None if not set
        """
        return self._data["Exterior Lights 10 Name"]

    @exterior_lights_10_name.setter
    def exterior_lights_10_name(self, value=None):
        """  Corresponds to IDD Field `exterior_lights_10_name`
        Enter the name of an Exterior:Lights object.

        Args:
            value (str): value for IDD Field `exterior_lights_10_name`
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
                                 'for field `exterior_lights_10_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `exterior_lights_10_name`')

        self._data["Exterior Lights 10 Name"] = value

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
        out.append(self._to_str(self.availability_schedule_name))
        out.append(self._to_str(self.limit_control))
        out.append(self._to_str(self.minimum_limit_duration))
        out.append(self._to_str(self.maximum_limit_fraction))
        out.append(self._to_str(self.limit_step_change))
        out.append(self._to_str(self.selection_control))
        out.append(self._to_str(self.rotation_duration))
        out.append(self._to_str(self.exterior_lights_1_name))
        out.append(self._to_str(self.exterior_lights_2_name))
        out.append(self._to_str(self.exterior_lights_3_name))
        out.append(self._to_str(self.exterior_lights_4_name))
        out.append(self._to_str(self.exterior_lights_5_name))
        out.append(self._to_str(self.exterior_lights_6_name))
        out.append(self._to_str(self.exterior_lights_7_name))
        out.append(self._to_str(self.exterior_lights_8_name))
        out.append(self._to_str(self.exterior_lights_9_name))
        out.append(self._to_str(self.exterior_lights_10_name))
        return ",".join(out)

class DemandManagerLights(object):
    """ Corresponds to IDD object `DemandManager:Lights`
        used for demand limiting Lights objects.
    """
    internal_name = "DemandManager:Lights"
    field_count = 18

    def __init__(self):
        """ Init data dictionary object for EPW IDD  `DemandManager:Lights`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Availability Schedule Name"] = None
        self._data["Limit Control"] = None
        self._data["Minimum Limit Duration"] = None
        self._data["Maximum Limit Fraction"] = None
        self._data["Limit Step Change"] = None
        self._data["Selection Control"] = None
        self._data["Rotation Duration"] = None
        self._data["Lights 1 Name"] = None
        self._data["Lights 2 Name"] = None
        self._data["Lights 3 Name"] = None
        self._data["Lights 4 Name"] = None
        self._data["Lights 5 Name"] = None
        self._data["Lights 6 Name"] = None
        self._data["Lights 7 Name"] = None
        self._data["Lights 8 Name"] = None
        self._data["Lights 9 Name"] = None
        self._data["Lights 10 Name"] = None

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
            self.availability_schedule_name = None
        else:
            self.availability_schedule_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.limit_control = None
        else:
            self.limit_control = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.minimum_limit_duration = None
        else:
            self.minimum_limit_duration = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.maximum_limit_fraction = None
        else:
            self.maximum_limit_fraction = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.limit_step_change = None
        else:
            self.limit_step_change = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.selection_control = None
        else:
            self.selection_control = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.rotation_duration = None
        else:
            self.rotation_duration = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.lights_1_name = None
        else:
            self.lights_1_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.lights_2_name = None
        else:
            self.lights_2_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.lights_3_name = None
        else:
            self.lights_3_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.lights_4_name = None
        else:
            self.lights_4_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.lights_5_name = None
        else:
            self.lights_5_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.lights_6_name = None
        else:
            self.lights_6_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.lights_7_name = None
        else:
            self.lights_7_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.lights_8_name = None
        else:
            self.lights_8_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.lights_9_name = None
        else:
            self.lights_9_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.lights_10_name = None
        else:
            self.lights_10_name = vals[i]
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
    def availability_schedule_name(self):
        """Get availability_schedule_name

        Returns:
            str: the value of `availability_schedule_name` or None if not set
        """
        return self._data["Availability Schedule Name"]

    @availability_schedule_name.setter
    def availability_schedule_name(self, value=None):
        """  Corresponds to IDD Field `availability_schedule_name`
        Availability schedule name for this system. Schedule value > 0 means the system is available.
        If this field is blank, the system is always available.

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

    @property
    def limit_control(self):
        """Get limit_control

        Returns:
            str: the value of `limit_control` or None if not set
        """
        return self._data["Limit Control"]

    @limit_control.setter
    def limit_control(self, value=None):
        """  Corresponds to IDD Field `limit_control`

        Args:
            value (str): value for IDD Field `limit_control`
                Accepted values are:
                      - Off
                      - Fixed
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
                                 'for field `limit_control`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `limit_control`')
            vals = set()
            vals.add("Off")
            vals.add("Fixed")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `limit_control`'.format(value))

        self._data["Limit Control"] = value

    @property
    def minimum_limit_duration(self):
        """Get minimum_limit_duration

        Returns:
            int: the value of `minimum_limit_duration` or None if not set
        """
        return self._data["Minimum Limit Duration"]

    @minimum_limit_duration.setter
    def minimum_limit_duration(self, value=None):
        """  Corresponds to IDD Field `minimum_limit_duration`
        If blank, duration defaults to the timestep

        Args:
            value (int): value for IDD Field `minimum_limit_duration`
                Unit: minutes
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
                                 'for field `minimum_limit_duration`'.format(value))
            if value <= 0:
                raise ValueError('value need to be greater 0 '
                                 'for field `minimum_limit_duration`')

        self._data["Minimum Limit Duration"] = value

    @property
    def maximum_limit_fraction(self):
        """Get maximum_limit_fraction

        Returns:
            float: the value of `maximum_limit_fraction` or None if not set
        """
        return self._data["Maximum Limit Fraction"]

    @maximum_limit_fraction.setter
    def maximum_limit_fraction(self, value=None):
        """  Corresponds to IDD Field `maximum_limit_fraction`

        Args:
            value (float): value for IDD Field `maximum_limit_fraction`
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
                                 'for field `maximum_limit_fraction`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `maximum_limit_fraction`')
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `maximum_limit_fraction`')

        self._data["Maximum Limit Fraction"] = value

    @property
    def limit_step_change(self):
        """Get limit_step_change

        Returns:
            float: the value of `limit_step_change` or None if not set
        """
        return self._data["Limit Step Change"]

    @limit_step_change.setter
    def limit_step_change(self, value=None):
        """  Corresponds to IDD Field `limit_step_change`
        Not yet implemented

        Args:
            value (float): value for IDD Field `limit_step_change`
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
                                 'for field `limit_step_change`'.format(value))

        self._data["Limit Step Change"] = value

    @property
    def selection_control(self):
        """Get selection_control

        Returns:
            str: the value of `selection_control` or None if not set
        """
        return self._data["Selection Control"]

    @selection_control.setter
    def selection_control(self, value=None):
        """  Corresponds to IDD Field `selection_control`

        Args:
            value (str): value for IDD Field `selection_control`
                Accepted values are:
                      - All
                      - RotateMany
                      - RotateOne
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
                                 'for field `selection_control`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `selection_control`')
            vals = set()
            vals.add("All")
            vals.add("RotateMany")
            vals.add("RotateOne")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `selection_control`'.format(value))

        self._data["Selection Control"] = value

    @property
    def rotation_duration(self):
        """Get rotation_duration

        Returns:
            int: the value of `rotation_duration` or None if not set
        """
        return self._data["Rotation Duration"]

    @rotation_duration.setter
    def rotation_duration(self, value=None):
        """  Corresponds to IDD Field `rotation_duration`
        If blank, duration defaults to the timestep

        Args:
            value (int): value for IDD Field `rotation_duration`
                Unit: minutes
                value >= 0
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
                                 'for field `rotation_duration`'.format(value))
            if value < 0:
                raise ValueError('value need to be greater or equal 0 '
                                 'for field `rotation_duration`')

        self._data["Rotation Duration"] = value

    @property
    def lights_1_name(self):
        """Get lights_1_name

        Returns:
            str: the value of `lights_1_name` or None if not set
        """
        return self._data["Lights 1 Name"]

    @lights_1_name.setter
    def lights_1_name(self, value=None):
        """  Corresponds to IDD Field `lights_1_name`
        Enter the name of an Lights object.
        if ZoneList option is used on the Lights object,
        a single lights object from that assignment
        can be selected by entering <Zone Name><space><Global Lights Object Name>.

        Args:
            value (str): value for IDD Field `lights_1_name`
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
                                 'for field `lights_1_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `lights_1_name`')

        self._data["Lights 1 Name"] = value

    @property
    def lights_2_name(self):
        """Get lights_2_name

        Returns:
            str: the value of `lights_2_name` or None if not set
        """
        return self._data["Lights 2 Name"]

    @lights_2_name.setter
    def lights_2_name(self, value=None):
        """  Corresponds to IDD Field `lights_2_name`
        Enter the name of an Lights object.
        if ZoneList option is used on the Lights object,
        a single lights object from that assignment
        can be selected by entering <Zone Name><space><Global Lights Object Name>.

        Args:
            value (str): value for IDD Field `lights_2_name`
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
                                 'for field `lights_2_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `lights_2_name`')

        self._data["Lights 2 Name"] = value

    @property
    def lights_3_name(self):
        """Get lights_3_name

        Returns:
            str: the value of `lights_3_name` or None if not set
        """
        return self._data["Lights 3 Name"]

    @lights_3_name.setter
    def lights_3_name(self, value=None):
        """  Corresponds to IDD Field `lights_3_name`
        Enter the name of an Lights object.
        if ZoneList option is used on the Lights object,
        a single lights object from that assignment
        can be selected by entering <Zone Name><space><Global Lights Object Name>.

        Args:
            value (str): value for IDD Field `lights_3_name`
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
                                 'for field `lights_3_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `lights_3_name`')

        self._data["Lights 3 Name"] = value

    @property
    def lights_4_name(self):
        """Get lights_4_name

        Returns:
            str: the value of `lights_4_name` or None if not set
        """
        return self._data["Lights 4 Name"]

    @lights_4_name.setter
    def lights_4_name(self, value=None):
        """  Corresponds to IDD Field `lights_4_name`
        Enter the name of an Lights object.
        if ZoneList option is used on the Lights object,
        a single lights object from that assignment
        can be selected by entering <Zone Name><space><Global Lights Object Name>.

        Args:
            value (str): value for IDD Field `lights_4_name`
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
                                 'for field `lights_4_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `lights_4_name`')

        self._data["Lights 4 Name"] = value

    @property
    def lights_5_name(self):
        """Get lights_5_name

        Returns:
            str: the value of `lights_5_name` or None if not set
        """
        return self._data["Lights 5 Name"]

    @lights_5_name.setter
    def lights_5_name(self, value=None):
        """  Corresponds to IDD Field `lights_5_name`
        Enter the name of an Lights object.
        if ZoneList option is used on the Lights object,
        a single lights object from that assignment
        can be selected by entering <Zone Name><space><Global Lights Object Name>.

        Args:
            value (str): value for IDD Field `lights_5_name`
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
                                 'for field `lights_5_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `lights_5_name`')

        self._data["Lights 5 Name"] = value

    @property
    def lights_6_name(self):
        """Get lights_6_name

        Returns:
            str: the value of `lights_6_name` or None if not set
        """
        return self._data["Lights 6 Name"]

    @lights_6_name.setter
    def lights_6_name(self, value=None):
        """  Corresponds to IDD Field `lights_6_name`
        Enter the name of an Lights object.
        if ZoneList option is used on the Lights object,
        a single lights object from that assignment
        can be selected by entering <Zone Name><space><Global Lights Object Name>.

        Args:
            value (str): value for IDD Field `lights_6_name`
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
                                 'for field `lights_6_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `lights_6_name`')

        self._data["Lights 6 Name"] = value

    @property
    def lights_7_name(self):
        """Get lights_7_name

        Returns:
            str: the value of `lights_7_name` or None if not set
        """
        return self._data["Lights 7 Name"]

    @lights_7_name.setter
    def lights_7_name(self, value=None):
        """  Corresponds to IDD Field `lights_7_name`
        Enter the name of an Lights object.
        if ZoneList option is used on the Lights object,
        a single lights object from that assignment
        can be selected by entering <Zone Name><space><Global Lights Object Name>.

        Args:
            value (str): value for IDD Field `lights_7_name`
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
                                 'for field `lights_7_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `lights_7_name`')

        self._data["Lights 7 Name"] = value

    @property
    def lights_8_name(self):
        """Get lights_8_name

        Returns:
            str: the value of `lights_8_name` or None if not set
        """
        return self._data["Lights 8 Name"]

    @lights_8_name.setter
    def lights_8_name(self, value=None):
        """  Corresponds to IDD Field `lights_8_name`
        Enter the name of an Lights object.
        if ZoneList option is used on the Lights object,
        a single lights object from that assignment
        can be selected by entering <Zone Name><space><Global Lights Object Name>.

        Args:
            value (str): value for IDD Field `lights_8_name`
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
                                 'for field `lights_8_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `lights_8_name`')

        self._data["Lights 8 Name"] = value

    @property
    def lights_9_name(self):
        """Get lights_9_name

        Returns:
            str: the value of `lights_9_name` or None if not set
        """
        return self._data["Lights 9 Name"]

    @lights_9_name.setter
    def lights_9_name(self, value=None):
        """  Corresponds to IDD Field `lights_9_name`
        Enter the name of an Lights object.
        if ZoneList option is used on the Lights object,
        a single lights object from that assignment
        can be selected by entering <Zone Name><space><Global Lights Object Name>.

        Args:
            value (str): value for IDD Field `lights_9_name`
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
                                 'for field `lights_9_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `lights_9_name`')

        self._data["Lights 9 Name"] = value

    @property
    def lights_10_name(self):
        """Get lights_10_name

        Returns:
            str: the value of `lights_10_name` or None if not set
        """
        return self._data["Lights 10 Name"]

    @lights_10_name.setter
    def lights_10_name(self, value=None):
        """  Corresponds to IDD Field `lights_10_name`
        Enter the name of an Lights object.
        if ZoneList option is used on the Lights object,
        a single lights object from that assignment
        can be selected by entering <Zone Name><space><Global Lights Object Name>.

        Args:
            value (str): value for IDD Field `lights_10_name`
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
                                 'for field `lights_10_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `lights_10_name`')

        self._data["Lights 10 Name"] = value

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
        out.append(self._to_str(self.availability_schedule_name))
        out.append(self._to_str(self.limit_control))
        out.append(self._to_str(self.minimum_limit_duration))
        out.append(self._to_str(self.maximum_limit_fraction))
        out.append(self._to_str(self.limit_step_change))
        out.append(self._to_str(self.selection_control))
        out.append(self._to_str(self.rotation_duration))
        out.append(self._to_str(self.lights_1_name))
        out.append(self._to_str(self.lights_2_name))
        out.append(self._to_str(self.lights_3_name))
        out.append(self._to_str(self.lights_4_name))
        out.append(self._to_str(self.lights_5_name))
        out.append(self._to_str(self.lights_6_name))
        out.append(self._to_str(self.lights_7_name))
        out.append(self._to_str(self.lights_8_name))
        out.append(self._to_str(self.lights_9_name))
        out.append(self._to_str(self.lights_10_name))
        return ",".join(out)

class DemandManagerElectricEquipment(object):
    """ Corresponds to IDD object `DemandManager:ElectricEquipment`
        used for demand limiting ElectricEquipment objects.
    """
    internal_name = "DemandManager:ElectricEquipment"
    field_count = 18

    def __init__(self):
        """ Init data dictionary object for EPW IDD  `DemandManager:ElectricEquipment`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Availability Schedule Name"] = None
        self._data["Limit Control"] = None
        self._data["Minimum Limit Duration"] = None
        self._data["Maximum Limit Fraction"] = None
        self._data["Limit Step Change"] = None
        self._data["Selection Control"] = None
        self._data["Rotation Duration"] = None
        self._data["Electric Equipment 1 Name"] = None
        self._data["Electric Equipment 2 Name"] = None
        self._data["Electric Equipment 3 Name"] = None
        self._data["Electric Equipment 4 Name"] = None
        self._data["Electric Equipment 5 Name"] = None
        self._data["Electric Equipment 6 Name"] = None
        self._data["Electric Equipment 7 Name"] = None
        self._data["Electric Equipment 8 Name"] = None
        self._data["Electric Equipment 9 Name"] = None
        self._data["Electric Equipment 10 Name"] = None

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
            self.availability_schedule_name = None
        else:
            self.availability_schedule_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.limit_control = None
        else:
            self.limit_control = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.minimum_limit_duration = None
        else:
            self.minimum_limit_duration = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.maximum_limit_fraction = None
        else:
            self.maximum_limit_fraction = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.limit_step_change = None
        else:
            self.limit_step_change = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.selection_control = None
        else:
            self.selection_control = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.rotation_duration = None
        else:
            self.rotation_duration = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.electric_equipment_1_name = None
        else:
            self.electric_equipment_1_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.electric_equipment_2_name = None
        else:
            self.electric_equipment_2_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.electric_equipment_3_name = None
        else:
            self.electric_equipment_3_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.electric_equipment_4_name = None
        else:
            self.electric_equipment_4_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.electric_equipment_5_name = None
        else:
            self.electric_equipment_5_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.electric_equipment_6_name = None
        else:
            self.electric_equipment_6_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.electric_equipment_7_name = None
        else:
            self.electric_equipment_7_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.electric_equipment_8_name = None
        else:
            self.electric_equipment_8_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.electric_equipment_9_name = None
        else:
            self.electric_equipment_9_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.electric_equipment_10_name = None
        else:
            self.electric_equipment_10_name = vals[i]
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
    def availability_schedule_name(self):
        """Get availability_schedule_name

        Returns:
            str: the value of `availability_schedule_name` or None if not set
        """
        return self._data["Availability Schedule Name"]

    @availability_schedule_name.setter
    def availability_schedule_name(self, value=None):
        """  Corresponds to IDD Field `availability_schedule_name`
        Availability schedule name for this system. Schedule value > 0 means the system is available.
        If this field is blank, the system is always available.

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

    @property
    def limit_control(self):
        """Get limit_control

        Returns:
            str: the value of `limit_control` or None if not set
        """
        return self._data["Limit Control"]

    @limit_control.setter
    def limit_control(self, value=None):
        """  Corresponds to IDD Field `limit_control`

        Args:
            value (str): value for IDD Field `limit_control`
                Accepted values are:
                      - Off
                      - Fixed
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
                                 'for field `limit_control`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `limit_control`')
            vals = set()
            vals.add("Off")
            vals.add("Fixed")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `limit_control`'.format(value))

        self._data["Limit Control"] = value

    @property
    def minimum_limit_duration(self):
        """Get minimum_limit_duration

        Returns:
            int: the value of `minimum_limit_duration` or None if not set
        """
        return self._data["Minimum Limit Duration"]

    @minimum_limit_duration.setter
    def minimum_limit_duration(self, value=None):
        """  Corresponds to IDD Field `minimum_limit_duration`
        If blank, duration defaults to the timestep

        Args:
            value (int): value for IDD Field `minimum_limit_duration`
                Unit: minutes
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
                                 'for field `minimum_limit_duration`'.format(value))
            if value <= 0:
                raise ValueError('value need to be greater 0 '
                                 'for field `minimum_limit_duration`')

        self._data["Minimum Limit Duration"] = value

    @property
    def maximum_limit_fraction(self):
        """Get maximum_limit_fraction

        Returns:
            float: the value of `maximum_limit_fraction` or None if not set
        """
        return self._data["Maximum Limit Fraction"]

    @maximum_limit_fraction.setter
    def maximum_limit_fraction(self, value=None):
        """  Corresponds to IDD Field `maximum_limit_fraction`

        Args:
            value (float): value for IDD Field `maximum_limit_fraction`
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
                                 'for field `maximum_limit_fraction`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `maximum_limit_fraction`')
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `maximum_limit_fraction`')

        self._data["Maximum Limit Fraction"] = value

    @property
    def limit_step_change(self):
        """Get limit_step_change

        Returns:
            float: the value of `limit_step_change` or None if not set
        """
        return self._data["Limit Step Change"]

    @limit_step_change.setter
    def limit_step_change(self, value=None):
        """  Corresponds to IDD Field `limit_step_change`
        Not yet implemented

        Args:
            value (float): value for IDD Field `limit_step_change`
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
                                 'for field `limit_step_change`'.format(value))

        self._data["Limit Step Change"] = value

    @property
    def selection_control(self):
        """Get selection_control

        Returns:
            str: the value of `selection_control` or None if not set
        """
        return self._data["Selection Control"]

    @selection_control.setter
    def selection_control(self, value=None):
        """  Corresponds to IDD Field `selection_control`

        Args:
            value (str): value for IDD Field `selection_control`
                Accepted values are:
                      - All
                      - RotateMany
                      - RotateOne
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
                                 'for field `selection_control`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `selection_control`')
            vals = set()
            vals.add("All")
            vals.add("RotateMany")
            vals.add("RotateOne")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `selection_control`'.format(value))

        self._data["Selection Control"] = value

    @property
    def rotation_duration(self):
        """Get rotation_duration

        Returns:
            int: the value of `rotation_duration` or None if not set
        """
        return self._data["Rotation Duration"]

    @rotation_duration.setter
    def rotation_duration(self, value=None):
        """  Corresponds to IDD Field `rotation_duration`
        If blank, duration defaults to the timestep

        Args:
            value (int): value for IDD Field `rotation_duration`
                Unit: minutes
                value >= 0
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
                                 'for field `rotation_duration`'.format(value))
            if value < 0:
                raise ValueError('value need to be greater or equal 0 '
                                 'for field `rotation_duration`')

        self._data["Rotation Duration"] = value

    @property
    def electric_equipment_1_name(self):
        """Get electric_equipment_1_name

        Returns:
            str: the value of `electric_equipment_1_name` or None if not set
        """
        return self._data["Electric Equipment 1 Name"]

    @electric_equipment_1_name.setter
    def electric_equipment_1_name(self, value=None):
        """  Corresponds to IDD Field `electric_equipment_1_name`
        Enter the name of an ElectricEquipment object.
        if ZoneList option is used on the ElectricEquipment object,
        a single equipment object from that assignment
        can be selected by entering <Zone Name><space><Global ElectricEquipment Object Name>.

        Args:
            value (str): value for IDD Field `electric_equipment_1_name`
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
                                 'for field `electric_equipment_1_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `electric_equipment_1_name`')

        self._data["Electric Equipment 1 Name"] = value

    @property
    def electric_equipment_2_name(self):
        """Get electric_equipment_2_name

        Returns:
            str: the value of `electric_equipment_2_name` or None if not set
        """
        return self._data["Electric Equipment 2 Name"]

    @electric_equipment_2_name.setter
    def electric_equipment_2_name(self, value=None):
        """  Corresponds to IDD Field `electric_equipment_2_name`
        Enter the name of an ElectricEquipment object.
        if ZoneList option is used on the ElectricEquipment object,
        a single equipment object from that assignment
        can be selected by entering <Zone Name><space><Global ElectricEquipment Object Name>.

        Args:
            value (str): value for IDD Field `electric_equipment_2_name`
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
                                 'for field `electric_equipment_2_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `electric_equipment_2_name`')

        self._data["Electric Equipment 2 Name"] = value

    @property
    def electric_equipment_3_name(self):
        """Get electric_equipment_3_name

        Returns:
            str: the value of `electric_equipment_3_name` or None if not set
        """
        return self._data["Electric Equipment 3 Name"]

    @electric_equipment_3_name.setter
    def electric_equipment_3_name(self, value=None):
        """  Corresponds to IDD Field `electric_equipment_3_name`
        Enter the name of an ElectricEquipment object.
        if ZoneList option is used on the ElectricEquipment object,
        a single equipment object from that assignment
        can be selected by entering <Zone Name><space><Global ElectricEquipment Object Name>.

        Args:
            value (str): value for IDD Field `electric_equipment_3_name`
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
                                 'for field `electric_equipment_3_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `electric_equipment_3_name`')

        self._data["Electric Equipment 3 Name"] = value

    @property
    def electric_equipment_4_name(self):
        """Get electric_equipment_4_name

        Returns:
            str: the value of `electric_equipment_4_name` or None if not set
        """
        return self._data["Electric Equipment 4 Name"]

    @electric_equipment_4_name.setter
    def electric_equipment_4_name(self, value=None):
        """  Corresponds to IDD Field `electric_equipment_4_name`
        Enter the name of an ElectricEquipment object.
        if ZoneList option is used on the ElectricEquipment object,
        a single equipment object from that assignment
        can be selected by entering <Zone Name><space><Global ElectricEquipment Object Name>.

        Args:
            value (str): value for IDD Field `electric_equipment_4_name`
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
                                 'for field `electric_equipment_4_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `electric_equipment_4_name`')

        self._data["Electric Equipment 4 Name"] = value

    @property
    def electric_equipment_5_name(self):
        """Get electric_equipment_5_name

        Returns:
            str: the value of `electric_equipment_5_name` or None if not set
        """
        return self._data["Electric Equipment 5 Name"]

    @electric_equipment_5_name.setter
    def electric_equipment_5_name(self, value=None):
        """  Corresponds to IDD Field `electric_equipment_5_name`
        Enter the name of an ElectricEquipment object.
        if ZoneList option is used on the ElectricEquipment object,
        a single equipment object from that assignment
        can be selected by entering <Zone Name><space><Global ElectricEquipment Object Name>.

        Args:
            value (str): value for IDD Field `electric_equipment_5_name`
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
                                 'for field `electric_equipment_5_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `electric_equipment_5_name`')

        self._data["Electric Equipment 5 Name"] = value

    @property
    def electric_equipment_6_name(self):
        """Get electric_equipment_6_name

        Returns:
            str: the value of `electric_equipment_6_name` or None if not set
        """
        return self._data["Electric Equipment 6 Name"]

    @electric_equipment_6_name.setter
    def electric_equipment_6_name(self, value=None):
        """  Corresponds to IDD Field `electric_equipment_6_name`
        Enter the name of an ElectricEquipment object.
        if ZoneList option is used on the ElectricEquipment object,
        a single equipment object from that assignment
        can be selected by entering <Zone Name><space><Global ElectricEquipment Object Name>.

        Args:
            value (str): value for IDD Field `electric_equipment_6_name`
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
                                 'for field `electric_equipment_6_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `electric_equipment_6_name`')

        self._data["Electric Equipment 6 Name"] = value

    @property
    def electric_equipment_7_name(self):
        """Get electric_equipment_7_name

        Returns:
            str: the value of `electric_equipment_7_name` or None if not set
        """
        return self._data["Electric Equipment 7 Name"]

    @electric_equipment_7_name.setter
    def electric_equipment_7_name(self, value=None):
        """  Corresponds to IDD Field `electric_equipment_7_name`
        Enter the name of an ElectricEquipment object.
        if ZoneList option is used on the ElectricEquipment object,
        a single equipment object from that assignment
        can be selected by entering <Zone Name><space><Global ElectricEquipment Object Name>.

        Args:
            value (str): value for IDD Field `electric_equipment_7_name`
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
                                 'for field `electric_equipment_7_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `electric_equipment_7_name`')

        self._data["Electric Equipment 7 Name"] = value

    @property
    def electric_equipment_8_name(self):
        """Get electric_equipment_8_name

        Returns:
            str: the value of `electric_equipment_8_name` or None if not set
        """
        return self._data["Electric Equipment 8 Name"]

    @electric_equipment_8_name.setter
    def electric_equipment_8_name(self, value=None):
        """  Corresponds to IDD Field `electric_equipment_8_name`
        Enter the name of an ElectricEquipment object.
        if ZoneList option is used on the ElectricEquipment object,
        a single equipment object from that assignment
        can be selected by entering <Zone Name><space><Global ElectricEquipment Object Name>.

        Args:
            value (str): value for IDD Field `electric_equipment_8_name`
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
                                 'for field `electric_equipment_8_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `electric_equipment_8_name`')

        self._data["Electric Equipment 8 Name"] = value

    @property
    def electric_equipment_9_name(self):
        """Get electric_equipment_9_name

        Returns:
            str: the value of `electric_equipment_9_name` or None if not set
        """
        return self._data["Electric Equipment 9 Name"]

    @electric_equipment_9_name.setter
    def electric_equipment_9_name(self, value=None):
        """  Corresponds to IDD Field `electric_equipment_9_name`
        Enter the name of an ElectricEquipment object.
        if ZoneList option is used on the ElectricEquipment object,
        a single equipment object from that assignment
        can be selected by entering <Zone Name><space><Global ElectricEquipment Object Name>.

        Args:
            value (str): value for IDD Field `electric_equipment_9_name`
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
                                 'for field `electric_equipment_9_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `electric_equipment_9_name`')

        self._data["Electric Equipment 9 Name"] = value

    @property
    def electric_equipment_10_name(self):
        """Get electric_equipment_10_name

        Returns:
            str: the value of `electric_equipment_10_name` or None if not set
        """
        return self._data["Electric Equipment 10 Name"]

    @electric_equipment_10_name.setter
    def electric_equipment_10_name(self, value=None):
        """  Corresponds to IDD Field `electric_equipment_10_name`
        Enter the name of an ElectricEquipment object.
        if ZoneList option is used on the ElectricEquipment object,
        a single equipment object from that assignment
        can be selected by entering <Zone Name><space><Global ElectricEquipment Object Name>.

        Args:
            value (str): value for IDD Field `electric_equipment_10_name`
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
                                 'for field `electric_equipment_10_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `electric_equipment_10_name`')

        self._data["Electric Equipment 10 Name"] = value

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
        out.append(self._to_str(self.availability_schedule_name))
        out.append(self._to_str(self.limit_control))
        out.append(self._to_str(self.minimum_limit_duration))
        out.append(self._to_str(self.maximum_limit_fraction))
        out.append(self._to_str(self.limit_step_change))
        out.append(self._to_str(self.selection_control))
        out.append(self._to_str(self.rotation_duration))
        out.append(self._to_str(self.electric_equipment_1_name))
        out.append(self._to_str(self.electric_equipment_2_name))
        out.append(self._to_str(self.electric_equipment_3_name))
        out.append(self._to_str(self.electric_equipment_4_name))
        out.append(self._to_str(self.electric_equipment_5_name))
        out.append(self._to_str(self.electric_equipment_6_name))
        out.append(self._to_str(self.electric_equipment_7_name))
        out.append(self._to_str(self.electric_equipment_8_name))
        out.append(self._to_str(self.electric_equipment_9_name))
        out.append(self._to_str(self.electric_equipment_10_name))
        return ",".join(out)

class DemandManagerThermostats(object):
    """ Corresponds to IDD object `DemandManager:Thermostats`
        used for demand limiting ZoneControl:Thermostat objects.
    """
    internal_name = "DemandManager:Thermostats"
    field_count = 19

    def __init__(self):
        """ Init data dictionary object for EPW IDD  `DemandManager:Thermostats`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Availability Schedule Name"] = None
        self._data["Reset Control"] = None
        self._data["Minimum Reset Duration"] = None
        self._data["Maximum Heating Setpoint Reset"] = None
        self._data["Maximum Cooling Setpoint Reset"] = None
        self._data["Reset Step Change"] = None
        self._data["Selection Control"] = None
        self._data["Rotation Duration"] = None
        self._data["Thermostat 1 Name"] = None
        self._data["Thermostat 2 Name"] = None
        self._data["Thermostat 3 Name"] = None
        self._data["Thermostat 4 Name"] = None
        self._data["Thermostat 5 Name"] = None
        self._data["Thermostat 6 Name"] = None
        self._data["Thermostat 7 Name"] = None
        self._data["Thermostat 8 Name"] = None
        self._data["Thermostat 9 Name"] = None
        self._data["Thermostat 10 Name"] = None

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
            self.availability_schedule_name = None
        else:
            self.availability_schedule_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.reset_control = None
        else:
            self.reset_control = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.minimum_reset_duration = None
        else:
            self.minimum_reset_duration = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.maximum_heating_setpoint_reset = None
        else:
            self.maximum_heating_setpoint_reset = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.maximum_cooling_setpoint_reset = None
        else:
            self.maximum_cooling_setpoint_reset = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.reset_step_change = None
        else:
            self.reset_step_change = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.selection_control = None
        else:
            self.selection_control = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.rotation_duration = None
        else:
            self.rotation_duration = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.thermostat_1_name = None
        else:
            self.thermostat_1_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.thermostat_2_name = None
        else:
            self.thermostat_2_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.thermostat_3_name = None
        else:
            self.thermostat_3_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.thermostat_4_name = None
        else:
            self.thermostat_4_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.thermostat_5_name = None
        else:
            self.thermostat_5_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.thermostat_6_name = None
        else:
            self.thermostat_6_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.thermostat_7_name = None
        else:
            self.thermostat_7_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.thermostat_8_name = None
        else:
            self.thermostat_8_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.thermostat_9_name = None
        else:
            self.thermostat_9_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.thermostat_10_name = None
        else:
            self.thermostat_10_name = vals[i]
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
    def availability_schedule_name(self):
        """Get availability_schedule_name

        Returns:
            str: the value of `availability_schedule_name` or None if not set
        """
        return self._data["Availability Schedule Name"]

    @availability_schedule_name.setter
    def availability_schedule_name(self, value=None):
        """  Corresponds to IDD Field `availability_schedule_name`
        Availability schedule name for this system. Schedule value > 0 means the system is available.
        If this field is blank, the system is always available.

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

    @property
    def reset_control(self):
        """Get reset_control

        Returns:
            str: the value of `reset_control` or None if not set
        """
        return self._data["Reset Control"]

    @reset_control.setter
    def reset_control(self, value=None):
        """  Corresponds to IDD Field `reset_control`

        Args:
            value (str): value for IDD Field `reset_control`
                Accepted values are:
                      - Off
                      - Fixed
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
                                 'for field `reset_control`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `reset_control`')
            vals = set()
            vals.add("Off")
            vals.add("Fixed")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `reset_control`'.format(value))

        self._data["Reset Control"] = value

    @property
    def minimum_reset_duration(self):
        """Get minimum_reset_duration

        Returns:
            int: the value of `minimum_reset_duration` or None if not set
        """
        return self._data["Minimum Reset Duration"]

    @minimum_reset_duration.setter
    def minimum_reset_duration(self, value=None):
        """  Corresponds to IDD Field `minimum_reset_duration`
        If blank, duration defaults to the timestep

        Args:
            value (int): value for IDD Field `minimum_reset_duration`
                Unit: minutes
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
                                 'for field `minimum_reset_duration`'.format(value))
            if value <= 0:
                raise ValueError('value need to be greater 0 '
                                 'for field `minimum_reset_duration`')

        self._data["Minimum Reset Duration"] = value

    @property
    def maximum_heating_setpoint_reset(self):
        """Get maximum_heating_setpoint_reset

        Returns:
            float: the value of `maximum_heating_setpoint_reset` or None if not set
        """
        return self._data["Maximum Heating Setpoint Reset"]

    @maximum_heating_setpoint_reset.setter
    def maximum_heating_setpoint_reset(self, value=None):
        """  Corresponds to IDD Field `maximum_heating_setpoint_reset`

        Args:
            value (float): value for IDD Field `maximum_heating_setpoint_reset`
                Unit: C
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
                                 'for field `maximum_heating_setpoint_reset`'.format(value))

        self._data["Maximum Heating Setpoint Reset"] = value

    @property
    def maximum_cooling_setpoint_reset(self):
        """Get maximum_cooling_setpoint_reset

        Returns:
            float: the value of `maximum_cooling_setpoint_reset` or None if not set
        """
        return self._data["Maximum Cooling Setpoint Reset"]

    @maximum_cooling_setpoint_reset.setter
    def maximum_cooling_setpoint_reset(self, value=None):
        """  Corresponds to IDD Field `maximum_cooling_setpoint_reset`

        Args:
            value (float): value for IDD Field `maximum_cooling_setpoint_reset`
                Unit: C
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
                                 'for field `maximum_cooling_setpoint_reset`'.format(value))

        self._data["Maximum Cooling Setpoint Reset"] = value

    @property
    def reset_step_change(self):
        """Get reset_step_change

        Returns:
            float: the value of `reset_step_change` or None if not set
        """
        return self._data["Reset Step Change"]

    @reset_step_change.setter
    def reset_step_change(self, value=None):
        """  Corresponds to IDD Field `reset_step_change`
        Not yet implemented

        Args:
            value (float): value for IDD Field `reset_step_change`
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
                                 'for field `reset_step_change`'.format(value))

        self._data["Reset Step Change"] = value

    @property
    def selection_control(self):
        """Get selection_control

        Returns:
            str: the value of `selection_control` or None if not set
        """
        return self._data["Selection Control"]

    @selection_control.setter
    def selection_control(self, value=None):
        """  Corresponds to IDD Field `selection_control`

        Args:
            value (str): value for IDD Field `selection_control`
                Accepted values are:
                      - All
                      - RotateMany
                      - RotateOne
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
                                 'for field `selection_control`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `selection_control`')
            vals = set()
            vals.add("All")
            vals.add("RotateMany")
            vals.add("RotateOne")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `selection_control`'.format(value))

        self._data["Selection Control"] = value

    @property
    def rotation_duration(self):
        """Get rotation_duration

        Returns:
            int: the value of `rotation_duration` or None if not set
        """
        return self._data["Rotation Duration"]

    @rotation_duration.setter
    def rotation_duration(self, value=None):
        """  Corresponds to IDD Field `rotation_duration`
        If blank, duration defaults to the timestep

        Args:
            value (int): value for IDD Field `rotation_duration`
                Unit: minutes
                value >= 0
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
                                 'for field `rotation_duration`'.format(value))
            if value < 0:
                raise ValueError('value need to be greater or equal 0 '
                                 'for field `rotation_duration`')

        self._data["Rotation Duration"] = value

    @property
    def thermostat_1_name(self):
        """Get thermostat_1_name

        Returns:
            str: the value of `thermostat_1_name` or None if not set
        """
        return self._data["Thermostat 1 Name"]

    @thermostat_1_name.setter
    def thermostat_1_name(self, value=None):
        """  Corresponds to IDD Field `thermostat_1_name`
        Enter the name of a ZoneControl:Thermostat object.
        if ZoneList option is used on the ZoneControl:Thermostat object,
        a single thermostat object from that assignment
        can be selected by entering <Zone Name><space><Global Thermostat Object Name>.

        Args:
            value (str): value for IDD Field `thermostat_1_name`
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
                                 'for field `thermostat_1_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `thermostat_1_name`')

        self._data["Thermostat 1 Name"] = value

    @property
    def thermostat_2_name(self):
        """Get thermostat_2_name

        Returns:
            str: the value of `thermostat_2_name` or None if not set
        """
        return self._data["Thermostat 2 Name"]

    @thermostat_2_name.setter
    def thermostat_2_name(self, value=None):
        """  Corresponds to IDD Field `thermostat_2_name`
        Enter the name of a ZoneControl:Thermostat object.
        if ZoneList option is used on the ZoneControl:Thermostat object,
        a single thermostat object from that assignment
        can be selected by entering <Zone Name><space><Global Thermostat Object Name>.

        Args:
            value (str): value for IDD Field `thermostat_2_name`
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
                                 'for field `thermostat_2_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `thermostat_2_name`')

        self._data["Thermostat 2 Name"] = value

    @property
    def thermostat_3_name(self):
        """Get thermostat_3_name

        Returns:
            str: the value of `thermostat_3_name` or None if not set
        """
        return self._data["Thermostat 3 Name"]

    @thermostat_3_name.setter
    def thermostat_3_name(self, value=None):
        """  Corresponds to IDD Field `thermostat_3_name`
        Enter the name of a ZoneControl:Thermostat object.
        if ZoneList option is used on the ZoneControl:Thermostat object,
        a single thermostat object from that assignment
        can be selected by entering <Zone Name><space><Global Thermostat Object Name>.

        Args:
            value (str): value for IDD Field `thermostat_3_name`
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
                                 'for field `thermostat_3_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `thermostat_3_name`')

        self._data["Thermostat 3 Name"] = value

    @property
    def thermostat_4_name(self):
        """Get thermostat_4_name

        Returns:
            str: the value of `thermostat_4_name` or None if not set
        """
        return self._data["Thermostat 4 Name"]

    @thermostat_4_name.setter
    def thermostat_4_name(self, value=None):
        """  Corresponds to IDD Field `thermostat_4_name`
        Enter the name of a ZoneControl:Thermostat object.
        if ZoneList option is used on the ZoneControl:Thermostat object,
        a single thermostat object from that assignment
        can be selected by entering <Zone Name><space><Global Thermostat Object Name>.

        Args:
            value (str): value for IDD Field `thermostat_4_name`
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
                                 'for field `thermostat_4_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `thermostat_4_name`')

        self._data["Thermostat 4 Name"] = value

    @property
    def thermostat_5_name(self):
        """Get thermostat_5_name

        Returns:
            str: the value of `thermostat_5_name` or None if not set
        """
        return self._data["Thermostat 5 Name"]

    @thermostat_5_name.setter
    def thermostat_5_name(self, value=None):
        """  Corresponds to IDD Field `thermostat_5_name`
        Enter the name of a ZoneControl:Thermostat object.
        if ZoneList option is used on the ZoneControl:Thermostat object,
        a single thermostat object from that assignment
        can be selected by entering <Zone Name><space><Global Thermostat Object Name>.

        Args:
            value (str): value for IDD Field `thermostat_5_name`
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
                                 'for field `thermostat_5_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `thermostat_5_name`')

        self._data["Thermostat 5 Name"] = value

    @property
    def thermostat_6_name(self):
        """Get thermostat_6_name

        Returns:
            str: the value of `thermostat_6_name` or None if not set
        """
        return self._data["Thermostat 6 Name"]

    @thermostat_6_name.setter
    def thermostat_6_name(self, value=None):
        """  Corresponds to IDD Field `thermostat_6_name`
        Enter the name of a ZoneControl:Thermostat object.
        if ZoneList option is used on the ZoneControl:Thermostat object,
        a single thermostat object from that assignment
        can be selected by entering <Zone Name><space><Global Thermostat Object Name>.

        Args:
            value (str): value for IDD Field `thermostat_6_name`
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
                                 'for field `thermostat_6_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `thermostat_6_name`')

        self._data["Thermostat 6 Name"] = value

    @property
    def thermostat_7_name(self):
        """Get thermostat_7_name

        Returns:
            str: the value of `thermostat_7_name` or None if not set
        """
        return self._data["Thermostat 7 Name"]

    @thermostat_7_name.setter
    def thermostat_7_name(self, value=None):
        """  Corresponds to IDD Field `thermostat_7_name`
        Enter the name of a ZoneControl:Thermostat object.
        if ZoneList option is used on the ZoneControl:Thermostat object,
        a single thermostat object from that assignment
        can be selected by entering <Zone Name><space><Global Thermostat Object Name>.

        Args:
            value (str): value for IDD Field `thermostat_7_name`
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
                                 'for field `thermostat_7_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `thermostat_7_name`')

        self._data["Thermostat 7 Name"] = value

    @property
    def thermostat_8_name(self):
        """Get thermostat_8_name

        Returns:
            str: the value of `thermostat_8_name` or None if not set
        """
        return self._data["Thermostat 8 Name"]

    @thermostat_8_name.setter
    def thermostat_8_name(self, value=None):
        """  Corresponds to IDD Field `thermostat_8_name`
        Enter the name of a ZoneControl:Thermostat object.
        if ZoneList option is used on the ZoneControl:Thermostat object,
        a single thermostat object from that assignment
        can be selected by entering <Zone Name><space><Global Thermostat Object Name>.

        Args:
            value (str): value for IDD Field `thermostat_8_name`
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
                                 'for field `thermostat_8_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `thermostat_8_name`')

        self._data["Thermostat 8 Name"] = value

    @property
    def thermostat_9_name(self):
        """Get thermostat_9_name

        Returns:
            str: the value of `thermostat_9_name` or None if not set
        """
        return self._data["Thermostat 9 Name"]

    @thermostat_9_name.setter
    def thermostat_9_name(self, value=None):
        """  Corresponds to IDD Field `thermostat_9_name`
        Enter the name of a ZoneControl:Thermostat object.
        if ZoneList option is used on the ZoneControl:Thermostat object,
        a single thermostat object from that assignment
        can be selected by entering <Zone Name><space><Global Thermostat Object Name>.

        Args:
            value (str): value for IDD Field `thermostat_9_name`
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
                                 'for field `thermostat_9_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `thermostat_9_name`')

        self._data["Thermostat 9 Name"] = value

    @property
    def thermostat_10_name(self):
        """Get thermostat_10_name

        Returns:
            str: the value of `thermostat_10_name` or None if not set
        """
        return self._data["Thermostat 10 Name"]

    @thermostat_10_name.setter
    def thermostat_10_name(self, value=None):
        """  Corresponds to IDD Field `thermostat_10_name`
        Enter the name of a ZoneControl:Thermostat object.
        if ZoneList option is used on the ZoneControl:Thermostat object,
        a single thermostat object from that assignment
        can be selected by entering <Zone Name><space><Global Thermostat Object Name>.

        Args:
            value (str): value for IDD Field `thermostat_10_name`
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
                                 'for field `thermostat_10_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `thermostat_10_name`')

        self._data["Thermostat 10 Name"] = value

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
        out.append(self._to_str(self.availability_schedule_name))
        out.append(self._to_str(self.reset_control))
        out.append(self._to_str(self.minimum_reset_duration))
        out.append(self._to_str(self.maximum_heating_setpoint_reset))
        out.append(self._to_str(self.maximum_cooling_setpoint_reset))
        out.append(self._to_str(self.reset_step_change))
        out.append(self._to_str(self.selection_control))
        out.append(self._to_str(self.rotation_duration))
        out.append(self._to_str(self.thermostat_1_name))
        out.append(self._to_str(self.thermostat_2_name))
        out.append(self._to_str(self.thermostat_3_name))
        out.append(self._to_str(self.thermostat_4_name))
        out.append(self._to_str(self.thermostat_5_name))
        out.append(self._to_str(self.thermostat_6_name))
        out.append(self._to_str(self.thermostat_7_name))
        out.append(self._to_str(self.thermostat_8_name))
        out.append(self._to_str(self.thermostat_9_name))
        out.append(self._to_str(self.thermostat_10_name))
        return ",".join(out)