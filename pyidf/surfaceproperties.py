from collections import OrderedDict

class SurfacePropertiesVaporCoefficients(object):
    """ Corresponds to IDD object `SurfaceProperties:VaporCoefficients`
        The interior and external vapor transfer coefficients.
        Normally these value are calculated using the heat convection coefficient values.
        Use this object to used fixed constant values.
        Units are kg/Pa.s.m2
        This will only work with the CombinedHeatAndMoistureFiniteElement algorithm for surfaces.
        Other algorithms will ignore these coefficients
    """
    internal_name = "SurfaceProperties:VaporCoefficients"
    field_count = 5

    def __init__(self):
        """ Init data dictionary object for EPW IDD  `SurfaceProperties:VaporCoefficients`
        """
        self._data = OrderedDict()
        self._data["Surface Name"] = None
        self._data["Constant External Vapor Transfer Coefficient"] = None
        self._data["External Vapor Coefficient Value"] = None
        self._data["Constant Internal vapor Transfer Coefficient"] = None
        self._data["Internal Vapor Coefficient Value"] = None

    def read(self, vals):
        """ Read values

        Args:
            vals (list): list of strings representing values
        """
        i = 0
        if len(vals[i]) == 0:
            self.surface_name = None
        else:
            self.surface_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.constant_external_vapor_transfer_coefficient = None
        else:
            self.constant_external_vapor_transfer_coefficient = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.external_vapor_coefficient_value = None
        else:
            self.external_vapor_coefficient_value = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.constant_internal_vapor_transfer_coefficient = None
        else:
            self.constant_internal_vapor_transfer_coefficient = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.internal_vapor_coefficient_value = None
        else:
            self.internal_vapor_coefficient_value = vals[i]
        i += 1

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
    def constant_external_vapor_transfer_coefficient(self):
        """Get constant_external_vapor_transfer_coefficient

        Returns:
            str: the value of `constant_external_vapor_transfer_coefficient` or None if not set
        """
        return self._data["Constant External Vapor Transfer Coefficient"]

    @constant_external_vapor_transfer_coefficient.setter
    def constant_external_vapor_transfer_coefficient(self, value="No"):
        """  Corresponds to IDD Field `constant_external_vapor_transfer_coefficient`

        Args:
            value (str): value for IDD Field `constant_external_vapor_transfer_coefficient`
                Accepted values are:
                      - Yes
                      - No
                Default value: No
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
                                 'for field `constant_external_vapor_transfer_coefficient`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `constant_external_vapor_transfer_coefficient`')
            vals = set()
            vals.add("Yes")
            vals.add("No")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `constant_external_vapor_transfer_coefficient`'.format(value))

        self._data["Constant External Vapor Transfer Coefficient"] = value

    @property
    def external_vapor_coefficient_value(self):
        """Get external_vapor_coefficient_value

        Returns:
            float: the value of `external_vapor_coefficient_value` or None if not set
        """
        return self._data["External Vapor Coefficient Value"]

    @external_vapor_coefficient_value.setter
    def external_vapor_coefficient_value(self, value=0.0 ):
        """  Corresponds to IDD Field `external_vapor_coefficient_value`

        Args:
            value (float): value for IDD Field `external_vapor_coefficient_value`
                Unit: kg/Pa-s-m2
                Default value: 0.0
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
                                 'for field `external_vapor_coefficient_value`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `external_vapor_coefficient_value`')

        self._data["External Vapor Coefficient Value"] = value

    @property
    def constant_internal_vapor_transfer_coefficient(self):
        """Get constant_internal_vapor_transfer_coefficient

        Returns:
            str: the value of `constant_internal_vapor_transfer_coefficient` or None if not set
        """
        return self._data["Constant Internal vapor Transfer Coefficient"]

    @constant_internal_vapor_transfer_coefficient.setter
    def constant_internal_vapor_transfer_coefficient(self, value="No"):
        """  Corresponds to IDD Field `constant_internal_vapor_transfer_coefficient`

        Args:
            value (str): value for IDD Field `constant_internal_vapor_transfer_coefficient`
                Accepted values are:
                      - Yes
                      - No
                Default value: No
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
                                 'for field `constant_internal_vapor_transfer_coefficient`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `constant_internal_vapor_transfer_coefficient`')
            vals = set()
            vals.add("Yes")
            vals.add("No")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `constant_internal_vapor_transfer_coefficient`'.format(value))

        self._data["Constant Internal vapor Transfer Coefficient"] = value

    @property
    def internal_vapor_coefficient_value(self):
        """Get internal_vapor_coefficient_value

        Returns:
            float: the value of `internal_vapor_coefficient_value` or None if not set
        """
        return self._data["Internal Vapor Coefficient Value"]

    @internal_vapor_coefficient_value.setter
    def internal_vapor_coefficient_value(self, value=0.0 ):
        """  Corresponds to IDD Field `internal_vapor_coefficient_value`

        Args:
            value (float): value for IDD Field `internal_vapor_coefficient_value`
                Unit: kg/Pa-s-m2
                Default value: 0.0
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
                                 'for field `internal_vapor_coefficient_value`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `internal_vapor_coefficient_value`')

        self._data["Internal Vapor Coefficient Value"] = value

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
        out.append(self._to_str(self.surface_name))
        out.append(self._to_str(self.constant_external_vapor_transfer_coefficient))
        out.append(self._to_str(self.external_vapor_coefficient_value))
        out.append(self._to_str(self.constant_internal_vapor_transfer_coefficient))
        out.append(self._to_str(self.internal_vapor_coefficient_value))
        return ",".join(out)