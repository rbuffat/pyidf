from collections import OrderedDict

class SurfaceContaminantSourceAndSinkGenericPressureDriven(object):
    """ Corresponds to IDD object `SurfaceContaminantSourceAndSink:Generic:PressureDriven`
        Simulate generic contaminant source driven by the pressure difference across a surface.
    """
    internal_name = "SurfaceContaminantSourceAndSink:Generic:PressureDriven"
    field_count = 5

    def __init__(self):
        """ Init data dictionary object for EPW IDD  `SurfaceContaminantSourceAndSink:Generic:PressureDriven`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Surface Name"] = None
        self._data["Design Generation Rate Coefficient"] = None
        self._data["Generation Schedule Name"] = None
        self._data["Generation Exponent"] = None

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
            self.surface_name = None
        else:
            self.surface_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.design_generation_rate_coefficient = None
        else:
            self.design_generation_rate_coefficient = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.generation_schedule_name = None
        else:
            self.generation_schedule_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.generation_exponent = None
        else:
            self.generation_exponent = vals[i]
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
    def surface_name(self):
        """Get surface_name

        Returns:
            str: the value of `surface_name` or None if not set
        """
        return self._data["Surface Name"]

    @surface_name.setter
    def surface_name(self, value=None):
        """  Corresponds to IDD Field `surface_name`

        Args:
            value (str): value for IDD Field `surface_name`
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
                                 'for field `surface_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `surface_name`')

        self._data["Surface Name"] = value

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
    def generation_schedule_name(self):
        """Get generation_schedule_name

        Returns:
            str: the value of `generation_schedule_name` or None if not set
        """
        return self._data["Generation Schedule Name"]

    @generation_schedule_name.setter
    def generation_schedule_name(self, value=None):
        """  Corresponds to IDD Field `generation_schedule_name`
        Value in this schedule should be a fraction (generally 0.0 - 1.0) applied to the
        Design Generation Rate Coefficient

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
    def generation_exponent(self):
        """Get generation_exponent

        Returns:
            float: the value of `generation_exponent` or None if not set
        """
        return self._data["Generation Exponent"]

    @generation_exponent.setter
    def generation_exponent(self, value=None):
        """  Corresponds to IDD Field `generation_exponent`

        Args:
            value (float): value for IDD Field `generation_exponent`
                Unit: dimensionless
                value > 0.0
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
                                 'for field `generation_exponent`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `generation_exponent`')
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `generation_exponent`')

        self._data["Generation Exponent"] = value

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
        out.append(self._to_str(self.surface_name))
        out.append(self._to_str(self.design_generation_rate_coefficient))
        out.append(self._to_str(self.generation_schedule_name))
        out.append(self._to_str(self.generation_exponent))
        return ",".join(out)

class SurfaceContaminantSourceAndSinkGenericBoundaryLayerDiffusion(object):
    """ Corresponds to IDD object `SurfaceContaminantSourceAndSink:Generic:BoundaryLayerDiffusion`
        Simulate generic contaminant source driven by the boundary layer diffusion controlled model.
    """
    internal_name = "SurfaceContaminantSourceAndSink:Generic:BoundaryLayerDiffusion"
    field_count = 5

    def __init__(self):
        """ Init data dictionary object for EPW IDD  `SurfaceContaminantSourceAndSink:Generic:BoundaryLayerDiffusion`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Surface Name"] = None
        self._data["Mass Transfer Coefficient"] = None
        self._data["Schedule Name"] = None
        self._data["Henry adsorption constant or partition coefficient"] = None

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
            self.surface_name = None
        else:
            self.surface_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.mass_transfer_coefficient = None
        else:
            self.mass_transfer_coefficient = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.schedule_name = None
        else:
            self.schedule_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.henry_adsorption_constant_or_partition_coefficient = None
        else:
            self.henry_adsorption_constant_or_partition_coefficient = vals[i]
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
    def surface_name(self):
        """Get surface_name

        Returns:
            str: the value of `surface_name` or None if not set
        """
        return self._data["Surface Name"]

    @surface_name.setter
    def surface_name(self, value=None):
        """  Corresponds to IDD Field `surface_name`

        Args:
            value (str): value for IDD Field `surface_name`
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
                                 'for field `surface_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `surface_name`')

        self._data["Surface Name"] = value

    @property
    def mass_transfer_coefficient(self):
        """Get mass_transfer_coefficient

        Returns:
            float: the value of `mass_transfer_coefficient` or None if not set
        """
        return self._data["Mass Transfer Coefficient"]

    @mass_transfer_coefficient.setter
    def mass_transfer_coefficient(self, value=None):
        """  Corresponds to IDD Field `mass_transfer_coefficient`

        Args:
            value (float): value for IDD Field `mass_transfer_coefficient`
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
                                 'for field `mass_transfer_coefficient`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `mass_transfer_coefficient`')

        self._data["Mass Transfer Coefficient"] = value

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
    def henry_adsorption_constant_or_partition_coefficient(self):
        """Get henry_adsorption_constant_or_partition_coefficient

        Returns:
            float: the value of `henry_adsorption_constant_or_partition_coefficient` or None if not set
        """
        return self._data["Henry adsorption constant or partition coefficient"]

    @henry_adsorption_constant_or_partition_coefficient.setter
    def henry_adsorption_constant_or_partition_coefficient(self, value=None):
        """  Corresponds to IDD Field `henry_adsorption_constant_or_partition_coefficient`

        Args:
            value (float): value for IDD Field `henry_adsorption_constant_or_partition_coefficient`
                Unit: dimensionless
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
                                 'for field `henry_adsorption_constant_or_partition_coefficient`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `henry_adsorption_constant_or_partition_coefficient`')

        self._data["Henry adsorption constant or partition coefficient"] = value

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
        out.append(self._to_str(self.surface_name))
        out.append(self._to_str(self.mass_transfer_coefficient))
        out.append(self._to_str(self.schedule_name))
        out.append(self._to_str(self.henry_adsorption_constant_or_partition_coefficient))
        return ",".join(out)

class SurfaceContaminantSourceAndSinkGenericDepositionVelocitySink(object):
    """ Corresponds to IDD object `SurfaceContaminantSourceAndSink:Generic:DepositionVelocitySink`
        Simulate generic contaminant source driven by the boundary layer diffusion controlled model.
    """
    internal_name = "SurfaceContaminantSourceAndSink:Generic:DepositionVelocitySink"
    field_count = 4

    def __init__(self):
        """ Init data dictionary object for EPW IDD  `SurfaceContaminantSourceAndSink:Generic:DepositionVelocitySink`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Surface Name"] = None
        self._data["Deposition Velocity"] = None
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
            self.surface_name = None
        else:
            self.surface_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.deposition_velocity = None
        else:
            self.deposition_velocity = vals[i]
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
    def surface_name(self):
        """Get surface_name

        Returns:
            str: the value of `surface_name` or None if not set
        """
        return self._data["Surface Name"]

    @surface_name.setter
    def surface_name(self, value=None):
        """  Corresponds to IDD Field `surface_name`

        Args:
            value (str): value for IDD Field `surface_name`
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
                                 'for field `surface_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `surface_name`')

        self._data["Surface Name"] = value

    @property
    def deposition_velocity(self):
        """Get deposition_velocity

        Returns:
            float: the value of `deposition_velocity` or None if not set
        """
        return self._data["Deposition Velocity"]

    @deposition_velocity.setter
    def deposition_velocity(self, value=None):
        """  Corresponds to IDD Field `deposition_velocity`

        Args:
            value (float): value for IDD Field `deposition_velocity`
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
                                 'for field `deposition_velocity`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `deposition_velocity`')

        self._data["Deposition Velocity"] = value

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
        out.append(self._to_str(self.surface_name))
        out.append(self._to_str(self.deposition_velocity))
        out.append(self._to_str(self.schedule_name))
        return ",".join(out)