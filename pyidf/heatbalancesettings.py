from collections import OrderedDict

class HeatBalanceSettingsConductionFiniteDifference(object):
    """ Corresponds to IDD object `HeatBalanceSettings:ConductionFiniteDifference`
        Determines settings for the Conduction Finite Difference
        algorithm for surface heat transfer modeling.
    """
    internal_name = "HeatBalanceSettings:ConductionFiniteDifference"
    field_count = 4

    def __init__(self):
        """ Init data dictionary object for EPW IDD  `HeatBalanceSettings:ConductionFiniteDifference`
        """
        self._data = OrderedDict()
        self._data["Difference Scheme"] = None
        self._data["Space Discretization Constant"] = None
        self._data["Relaxation Factor"] = None
        self._data["Inside Face Surface Temperature Convergence Criteria"] = None

    def read(self, vals):
        """ Read values

        Args:
            vals (list): list of strings representing values
        """
        i = 0
        if len(vals[i]) == 0:
            self.difference_scheme = None
        else:
            self.difference_scheme = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.space_discretization_constant = None
        else:
            self.space_discretization_constant = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.relaxation_factor = None
        else:
            self.relaxation_factor = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.inside_face_surface_temperature_convergence_criteria = None
        else:
            self.inside_face_surface_temperature_convergence_criteria = vals[i]
        i += 1

    @property
    def difference_scheme(self):
        """Get difference_scheme

        Returns:
            str: the value of `difference_scheme` or None if not set
        """
        return self._data["Difference Scheme"]

    @difference_scheme.setter
    def difference_scheme(self, value="FullyImplicitFirstOrder"):
        """  Corresponds to IDD Field `difference_scheme`

        Args:
            value (str): value for IDD Field `difference_scheme`
                Accepted values are:
                      - CrankNicholsonSecondOrder
                      - FullyImplicitFirstOrder
                Default value: FullyImplicitFirstOrder
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
                                 'for field `difference_scheme`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `difference_scheme`')
            vals = set()
            vals.add("CrankNicholsonSecondOrder")
            vals.add("FullyImplicitFirstOrder")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `difference_scheme`'.format(value))

        self._data["Difference Scheme"] = value

    @property
    def space_discretization_constant(self):
        """Get space_discretization_constant

        Returns:
            float: the value of `space_discretization_constant` or None if not set
        """
        return self._data["Space Discretization Constant"]

    @space_discretization_constant.setter
    def space_discretization_constant(self, value=3.0 ):
        """  Corresponds to IDD Field `space_discretization_constant`
        increase or decrease number of nodes

        Args:
            value (float): value for IDD Field `space_discretization_constant`
                Default value: 3.0
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
                                 'for field `space_discretization_constant`'.format(value))

        self._data["Space Discretization Constant"] = value

    @property
    def relaxation_factor(self):
        """Get relaxation_factor

        Returns:
            float: the value of `relaxation_factor` or None if not set
        """
        return self._data["Relaxation Factor"]

    @relaxation_factor.setter
    def relaxation_factor(self, value=1.0 ):
        """  Corresponds to IDD Field `relaxation_factor`

        Args:
            value (float): value for IDD Field `relaxation_factor`
                Default value: 1.0
                value >= 0.01
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
                                 'for field `relaxation_factor`'.format(value))
            if value < 0.01:
                raise ValueError('value need to be greater or equal 0.01 '
                                 'for field `relaxation_factor`')
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `relaxation_factor`')

        self._data["Relaxation Factor"] = value

    @property
    def inside_face_surface_temperature_convergence_criteria(self):
        """Get inside_face_surface_temperature_convergence_criteria

        Returns:
            float: the value of `inside_face_surface_temperature_convergence_criteria` or None if not set
        """
        return self._data["Inside Face Surface Temperature Convergence Criteria"]

    @inside_face_surface_temperature_convergence_criteria.setter
    def inside_face_surface_temperature_convergence_criteria(self, value=0.002 ):
        """  Corresponds to IDD Field `inside_face_surface_temperature_convergence_criteria`

        Args:
            value (float): value for IDD Field `inside_face_surface_temperature_convergence_criteria`
                Default value: 0.002
                value >= 1e-07
                value <= 0.01
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
                                 'for field `inside_face_surface_temperature_convergence_criteria`'.format(value))
            if value < 1e-07:
                raise ValueError('value need to be greater or equal 1e-07 '
                                 'for field `inside_face_surface_temperature_convergence_criteria`')
            if value > 0.01:
                raise ValueError('value need to be smaller 0.01 '
                                 'for field `inside_face_surface_temperature_convergence_criteria`')

        self._data["Inside Face Surface Temperature Convergence Criteria"] = value

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
        out.append(self._to_str(self.difference_scheme))
        out.append(self._to_str(self.space_discretization_constant))
        out.append(self._to_str(self.relaxation_factor))
        out.append(self._to_str(self.inside_face_surface_temperature_convergence_criteria))
        return ",".join(out)