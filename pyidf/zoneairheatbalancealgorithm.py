from collections import OrderedDict

class ZoneAirHeatBalanceAlgorithm(object):
    """ Corresponds to IDD object `ZoneAirHeatBalanceAlgorithm`
        Determines which algorithm will be used to solve the zone air heat balance.
    """
    internal_name = "ZoneAirHeatBalanceAlgorithm"
    field_count = 1

    def __init__(self):
        """ Init data dictionary object for EPW IDD  `ZoneAirHeatBalanceAlgorithm`
        """
        self._data = OrderedDict()
        self._data["Algorithm"] = None

    def read(self, vals):
        """ Read values

        Args:
            vals (list): list of strings representing values
        """
        i = 0
        if len(vals[i]) == 0:
            self.algorithm = None
        else:
            self.algorithm = vals[i]
        i += 1

    @property
    def algorithm(self):
        """Get algorithm

        Returns:
            str: the value of `algorithm` or None if not set
        """
        return self._data["Algorithm"]

    @algorithm.setter
    def algorithm(self, value="ThirdOrderBackwardDifference"):
        """  Corresponds to IDD Field `algorithm`

        Args:
            value (str): value for IDD Field `algorithm`
                Accepted values are:
                      - ThirdOrderBackwardDifference
                      - AnalyticalSolution
                      - EulerMethod
                Default value: ThirdOrderBackwardDifference
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
                                 'for field `algorithm`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `algorithm`')
            vals = set()
            vals.add("ThirdOrderBackwardDifference")
            vals.add("AnalyticalSolution")
            vals.add("EulerMethod")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `algorithm`'.format(value))

        self._data["Algorithm"] = value

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
        out.append(self._to_str(self.algorithm))
        return ",".join(out)