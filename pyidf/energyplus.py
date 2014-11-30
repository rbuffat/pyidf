from collections import OrderedDict

class LeadInput(object):
    """ Corresponds to IDD object `Lead Input`
    
    """
    internal_name = "Lead Input"
    field_count = 0
    required_fields = []

    def __init__(self):
        """ Init data dictionary object for IDD  `Lead Input`
        """
        self._data = OrderedDict()

    def read(self, vals):
        """ Read values

        Args:
            vals (list): list of strings representing values
        """
        i = 0

    def check(self):
        """ Checks if all required fields are not None
        """
        good = True
        for key in self.required_fields:
            if self._data[key] is None:
                good = False
                break
        return good

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
        return ",".join(out)

class SimulationData(object):
    """ Corresponds to IDD object `Simulation Data`
    
    """
    internal_name = "Simulation Data"
    field_count = 0
    required_fields = []

    def __init__(self):
        """ Init data dictionary object for IDD  `Simulation Data`
        """
        self._data = OrderedDict()

    def read(self, vals):
        """ Read values

        Args:
            vals (list): list of strings representing values
        """
        i = 0

    def check(self):
        """ Checks if all required fields are not None
        """
        good = True
        for key in self.required_fields:
            if self._data[key] is None:
                good = False
                break
        return good

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
        return ",".join(out)