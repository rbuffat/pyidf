from collections import OrderedDict

class Timestep(object):
    """ Corresponds to IDD object `Timestep`
        Specifies the "basic" timestep for the simulation. The
        value entered here is also known as the Zone Timestep.  This is used in
        the Zone Heat Balance Model calculation as the driving timestep for heat
        transfer and load calculations.
    """
    internal_name = "Timestep"
    field_count = 1

    def __init__(self):
        """ Init data dictionary object for EPW IDD  `Timestep`
        """
        self._data = OrderedDict()
        self._data["Number of Timesteps per Hour"] = None

    def read(self, vals):
        """ Read values

        Args:
            vals (list): list of strings representing values
        """
        i = 0
        if len(vals[i]) == 0:
            self.number_of_timesteps_per_hour = None
        else:
            self.number_of_timesteps_per_hour = vals[i]
        i += 1

    @property
    def number_of_timesteps_per_hour(self):
        """Get number_of_timesteps_per_hour

        Returns:
            int: the value of `number_of_timesteps_per_hour` or None if not set
        """
        return self._data["Number of Timesteps per Hour"]

    @number_of_timesteps_per_hour.setter
    def number_of_timesteps_per_hour(self, value=6 ):
        """  Corresponds to IDD Field `number_of_timesteps_per_hour`
        Number in hour: normal validity 4 to 60: 6 suggested
        Must be evenly divisible into 60
        Allowable values include 1, 2, 3, 4, 5, 6, 10, 12, 15, 20, 30, and 60
        Normal 6 is mimimum as lower values may cause inaccuracies
        A minimum value of 20 is suggested for both ConductionFiniteDifference
        and CombinedHeatAndMoistureFiniteElement surface heat balance alogorithms
        A minimum of 12 is suggested for simulations involving a Vegetated Roof (Material:RoofVegetation).

        Args:
            value (int): value for IDD Field `number_of_timesteps_per_hour`
                Default value: 6
                value >= 1
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
                                 'for field `number_of_timesteps_per_hour`'.format(value))
            if value < 1:
                raise ValueError('value need to be greater or equal 1 '
                                 'for field `number_of_timesteps_per_hour`')
            if value > 60:
                raise ValueError('value need to be smaller 60 '
                                 'for field `number_of_timesteps_per_hour`')

        self._data["Number of Timesteps per Hour"] = value

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
        out.append(self._to_str(self.number_of_timesteps_per_hour))
        return ",".join(out)