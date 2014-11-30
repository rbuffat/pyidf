from collections import OrderedDict

class ComplianceBuilding(object):
    """ Corresponds to IDD object `Compliance:Building`
        Building level inputs related to compliance to building standards, building codes, and beyond energy code programs.
    """
    internal_name = "Compliance:Building"
    field_count = 1

    def __init__(self):
        """ Init data dictionary object for IDD  `Compliance:Building`
        """
        self._data = OrderedDict()
        self._data["Building Rotation for Appendix G"] = None

    def read(self, vals):
        """ Read values

        Args:
            vals (list): list of strings representing values
        """
        i = 0
        if len(vals[i]) == 0:
            self.building_rotation_for_appendix_g = None
        else:
            self.building_rotation_for_appendix_g = vals[i]
        i += 1

    @property
    def building_rotation_for_appendix_g(self):
        """Get building_rotation_for_appendix_g

        Returns:
            float: the value of `building_rotation_for_appendix_g` or None if not set
        """
        return self._data["Building Rotation for Appendix G"]

    @building_rotation_for_appendix_g.setter
    def building_rotation_for_appendix_g(self, value=0.0 ):
        """  Corresponds to IDD Field `building_rotation_for_appendix_g`
        Additional degrees of rotation to be used with the requirement in ASHRAE Standard 90.1 Appendix G
        that states that the baseline building should be rotated in four directions.

        Args:
            value (float): value for IDD Field `building_rotation_for_appendix_g`
                Unit: deg
                Default value: 0.0
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
                                 'for field `building_rotation_for_appendix_g`'.format(value))

        self._data["Building Rotation for Appendix G"] = value

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
        out.append(self._to_str(self.building_rotation_for_appendix_g))
        return ",".join(out)