from collections import OrderedDict

class ProgramControl(object):
    """ Corresponds to IDD object `ProgramControl`
        used to support various efforts in time reduction for simulation including threading
    """
    internal_name = "ProgramControl"
    field_count = 1

    def __init__(self):
        """ Init data dictionary object for EPW IDD  `ProgramControl`
        """
        self._data = OrderedDict()
        self._data["Number of Threads Allowed"] = None

    def read(self, vals):
        """ Read values

        Args:
            vals (list): list of strings representing values
        """
        i = 0
        if len(vals[i]) == 0:
            self.number_of_threads_allowed = None
        else:
            self.number_of_threads_allowed = vals[i]
        i += 1

    @property
    def number_of_threads_allowed(self):
        """Get number_of_threads_allowed

        Returns:
            int: the value of `number_of_threads_allowed` or None if not set
        """
        return self._data["Number of Threads Allowed"]

    @number_of_threads_allowed.setter
    def number_of_threads_allowed(self, value=None):
        """  Corresponds to IDD Field `number_of_threads_allowed`
        This is currently used only in the Interior Radiant Exchange module -- view factors on # surfaces
        if value is 0, then maximum number allowed will be used.

        Args:
            value (int): value for IDD Field `number_of_threads_allowed`
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
                                 'for field `number_of_threads_allowed`'.format(value))
            if value < 0:
                raise ValueError('value need to be greater or equal 0 '
                                 'for field `number_of_threads_allowed`')

        self._data["Number of Threads Allowed"] = value

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
        out.append(self._to_str(self.number_of_threads_allowed))
        return ",".join(out)