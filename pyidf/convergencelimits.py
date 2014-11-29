from collections import OrderedDict

class ConvergenceLimits(object):
    """ Corresponds to IDD object `ConvergenceLimits`
        Specifies limits on HVAC system simulation timesteps and iterations.
        This item is an advanced feature that should be used only with caution.
    """
    internal_name = "ConvergenceLimits"
    field_count = 4

    def __init__(self):
        """ Init data dictionary object for EPW IDD  `ConvergenceLimits`
        """
        self._data = OrderedDict()
        self._data["Minimum System Timestep"] = None
        self._data["Maximum HVAC Iterations"] = None
        self._data["Minimum Plant Iterations"] = None
        self._data["Maximum Plant Iterations"] = None

    def read(self, vals):
        """ Read values

        Args:
            vals (list): list of strings representing values
        """
        i = 0
        if len(vals[i]) == 0:
            self.minimum_system_timestep = None
        else:
            self.minimum_system_timestep = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.maximum_hvac_iterations = None
        else:
            self.maximum_hvac_iterations = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.minimum_plant_iterations = None
        else:
            self.minimum_plant_iterations = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.maximum_plant_iterations = None
        else:
            self.maximum_plant_iterations = vals[i]
        i += 1

    @property
    def minimum_system_timestep(self):
        """Get minimum_system_timestep

        Returns:
            int: the value of `minimum_system_timestep` or None if not set
        """
        return self._data["Minimum System Timestep"]

    @minimum_system_timestep.setter
    def minimum_system_timestep(self, value=None):
        """  Corresponds to IDD Field `minimum_system_timestep`
        0 sets the minimum to the zone timestep (ref: Timestep)
        1 is normal (ratchet down to 1 minute)
        setting greater than zone timestep (in minutes) will effectively set to zone timestep

        Args:
            value (int): value for IDD Field `minimum_system_timestep`
                Unit: minutes
                value >= 0
                value <= 60
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
                                 'for field `minimum_system_timestep`'.format(value))
            if value < 0:
                raise ValueError('value need to be greater or equal 0 '
                                 'for field `minimum_system_timestep`')
            if value > 60:
                raise ValueError('value need to be smaller 60 '
                                 'for field `minimum_system_timestep`')

        self._data["Minimum System Timestep"] = value

    @property
    def maximum_hvac_iterations(self):
        """Get maximum_hvac_iterations

        Returns:
            int: the value of `maximum_hvac_iterations` or None if not set
        """
        return self._data["Maximum HVAC Iterations"]

    @maximum_hvac_iterations.setter
    def maximum_hvac_iterations(self, value=20 ):
        """  Corresponds to IDD Field `maximum_hvac_iterations`

        Args:
            value (int): value for IDD Field `maximum_hvac_iterations`
                Default value: 20
                value >= 1
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
                                 'for field `maximum_hvac_iterations`'.format(value))
            if value < 1:
                raise ValueError('value need to be greater or equal 1 '
                                 'for field `maximum_hvac_iterations`')

        self._data["Maximum HVAC Iterations"] = value

    @property
    def minimum_plant_iterations(self):
        """Get minimum_plant_iterations

        Returns:
            int: the value of `minimum_plant_iterations` or None if not set
        """
        return self._data["Minimum Plant Iterations"]

    @minimum_plant_iterations.setter
    def minimum_plant_iterations(self, value=2 ):
        """  Corresponds to IDD Field `minimum_plant_iterations`
        Controls the minimum number of plant system solver iterations within a single HVAC iteration
        Larger values will increase runtime but might improve solution accuracy for complicated plant systems
        Complex plants include: several interconnected loops, heat recovery, thermal load following generators, etc.

        Args:
            value (int): value for IDD Field `minimum_plant_iterations`
                Default value: 2
                value >= 1
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
                                 'for field `minimum_plant_iterations`'.format(value))
            if value < 1:
                raise ValueError('value need to be greater or equal 1 '
                                 'for field `minimum_plant_iterations`')

        self._data["Minimum Plant Iterations"] = value

    @property
    def maximum_plant_iterations(self):
        """Get maximum_plant_iterations

        Returns:
            int: the value of `maximum_plant_iterations` or None if not set
        """
        return self._data["Maximum Plant Iterations"]

    @maximum_plant_iterations.setter
    def maximum_plant_iterations(self, value=8 ):
        """  Corresponds to IDD Field `maximum_plant_iterations`
        Controls the maximum number of plant system solver iterations within a single HVAC iteration
        Smaller values might decrease runtime but could decrease solution accuracy for complicated plant systems

        Args:
            value (int): value for IDD Field `maximum_plant_iterations`
                Default value: 8
                value >= 2
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
                                 'for field `maximum_plant_iterations`'.format(value))
            if value < 2:
                raise ValueError('value need to be greater or equal 2 '
                                 'for field `maximum_plant_iterations`')

        self._data["Maximum Plant Iterations"] = value

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
        out.append(self._to_str(self.minimum_system_timestep))
        out.append(self._to_str(self.maximum_hvac_iterations))
        out.append(self._to_str(self.minimum_plant_iterations))
        out.append(self._to_str(self.maximum_plant_iterations))
        return ",".join(out)