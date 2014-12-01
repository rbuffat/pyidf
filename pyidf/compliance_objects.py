from collections import OrderedDict

class ComplianceBuilding(object):
    """ Corresponds to IDD object `Compliance:Building`
        Building level inputs related to compliance to building standards, building codes, and beyond energy code programs.
    
    """
    internal_name = "Compliance:Building"
    field_count = 1
    required_fields = []

    def __init__(self):
        """ Init data dictionary object for IDD  `Compliance:Building`
        """
        self._data = OrderedDict()
        self._data["Building Rotation for Appendix G"] = None
        self.accept_substring = False

    def read(self, vals, accept_substring=True):
        """ Read values

        Args:
            vals (list): list of strings representing values
        """
        self.accept_substring = accept_substring
        i = 0
        if len(vals[i]) == 0:
            self.building_rotation_for_appendix_g = None
        else:
            self.building_rotation_for_appendix_g = vals[i]
        i += 1
        if i >= len(vals):
            return

    @property
    def building_rotation_for_appendix_g(self):
        """Get building_rotation_for_appendix_g

        Returns:
            float: the value of `building_rotation_for_appendix_g` or None if not set
        """
        return self._data["Building Rotation for Appendix G"]

    @building_rotation_for_appendix_g.setter
    def building_rotation_for_appendix_g(self, value=0.0):
        """  Corresponds to IDD Field `Building Rotation for Appendix G`
        Additional degrees of rotation to be used with the requirement in ASHRAE Standard 90.1 Appendix G
        that states that the baseline building should be rotated in four directions.

        Args:
            value (float): value for IDD Field `Building Rotation for Appendix G`
                Units: deg
                Default value: 0.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `building_rotation_for_appendix_g`'.format(value))
        self._data["Building Rotation for Appendix G"] = value

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

    def export(self):
        """ Export values of data object as list of strings"""
        out = []
        for key, value in self._data.iteritems():
            out.append(self._to_str(value))
        return out

    def __str__(self):
        out = [self.internal_name]
        out += self.export()
        return ",".join(out[:20])