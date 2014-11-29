from collections import OrderedDict

class Version(object):
    """ Corresponds to IDD object `Version`
        Specifies the EnergyPlus version of the IDF file.
    """
    internal_name = "Version"
    field_count = 1

    def __init__(self):
        """ Init data dictionary object for EPW IDD  `Version`
        """
        self._data = OrderedDict()
        self._data["Version Identifier"] = None

    def read(self, vals):
        """ Read values

        Args:
            vals (list): list of strings representing values
        """
        i = 0
        if len(vals[i]) == 0:
            self.version_identifier = None
        else:
            self.version_identifier = vals[i]
        i += 1

    @property
    def version_identifier(self):
        """Get version_identifier

        Returns:
            str: the value of `version_identifier` or None if not set
        """
        return self._data["Version Identifier"]

    @version_identifier.setter
    def version_identifier(self, value="7.0"):
        """  Corresponds to IDD Field `version_identifier`

        Args:
            value (str): value for IDD Field `version_identifier`
                Default value: 7.0
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
                                 'for field `version_identifier`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `version_identifier`')

        self._data["Version Identifier"] = value

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
        out.append(self._to_str(self.version_identifier))
        return ",".join(out)