from collections import OrderedDict

class HeatBalanceAlgorithm(object):
    """ Corresponds to IDD object `HeatBalanceAlgorithm`
        Determines which Heat Balance Algorithm will be used ie.
        CTF (Conduction Transfer Functions),
        EMPD (Effective Moisture Penetration Depth with Conduction Transfer Functions).
        Advanced/Research Usage: CondFD (Conduction Finite Difference)
        Advanced/Research Usage: ConductionFiniteDifferenceSimplified
        Advanced/Research Usage: HAMT (Combined Heat And Moisture Finite Element)
    """
    internal_name = "HeatBalanceAlgorithm"
    field_count = 4

    def __init__(self):
        """ Init data dictionary object for EPW IDD  `HeatBalanceAlgorithm`
        """
        self._data = OrderedDict()
        self._data["Algorithm"] = None
        self._data["Surface Temperature Upper Limit"] = None
        self._data["Minimum Surface Convection Heat Transfer Coefficient Value"] = None
        self._data["Maximum Surface Convection Heat Transfer Coefficient Value"] = None

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
        if len(vals[i]) == 0:
            self.surface_temperature_upper_limit = None
        else:
            self.surface_temperature_upper_limit = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.minimum_surface_convection_heat_transfer_coefficient_value = None
        else:
            self.minimum_surface_convection_heat_transfer_coefficient_value = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.maximum_surface_convection_heat_transfer_coefficient_value = None
        else:
            self.maximum_surface_convection_heat_transfer_coefficient_value = vals[i]
        i += 1

    @property
    def algorithm(self):
        """Get algorithm

        Returns:
            str: the value of `algorithm` or None if not set
        """
        return self._data["Algorithm"]

    @algorithm.setter
    def algorithm(self, value="ConductionTransferFunction"):
        """  Corresponds to IDD Field `algorithm`

        Args:
            value (str): value for IDD Field `algorithm`
                Accepted values are:
                      - ConductionTransferFunction
                      - MoisturePenetrationDepthConductionTransferFunction
                      - ConductionFiniteDifference
                      - CombinedHeatAndMoistureFiniteElement
                Default value: ConductionTransferFunction
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
            vals.add("ConductionTransferFunction")
            vals.add("MoisturePenetrationDepthConductionTransferFunction")
            vals.add("ConductionFiniteDifference")
            vals.add("CombinedHeatAndMoistureFiniteElement")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `algorithm`'.format(value))

        self._data["Algorithm"] = value

    @property
    def surface_temperature_upper_limit(self):
        """Get surface_temperature_upper_limit

        Returns:
            float: the value of `surface_temperature_upper_limit` or None if not set
        """
        return self._data["Surface Temperature Upper Limit"]

    @surface_temperature_upper_limit.setter
    def surface_temperature_upper_limit(self, value=200.0 ):
        """  Corresponds to IDD Field `surface_temperature_upper_limit`

        Args:
            value (float): value for IDD Field `surface_temperature_upper_limit`
                Unit: C
                Default value: 200.0
                value >= 200.0
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
                                 'for field `surface_temperature_upper_limit`'.format(value))
            if value < 200.0:
                raise ValueError('value need to be greater or equal 200.0 '
                                 'for field `surface_temperature_upper_limit`')

        self._data["Surface Temperature Upper Limit"] = value

    @property
    def minimum_surface_convection_heat_transfer_coefficient_value(self):
        """Get minimum_surface_convection_heat_transfer_coefficient_value

        Returns:
            float: the value of `minimum_surface_convection_heat_transfer_coefficient_value` or None if not set
        """
        return self._data["Minimum Surface Convection Heat Transfer Coefficient Value"]

    @minimum_surface_convection_heat_transfer_coefficient_value.setter
    def minimum_surface_convection_heat_transfer_coefficient_value(self, value=0.1 ):
        """  Corresponds to IDD Field `minimum_surface_convection_heat_transfer_coefficient_value`

        Args:
            value (float): value for IDD Field `minimum_surface_convection_heat_transfer_coefficient_value`
                Unit: W/m2-K
                Default value: 0.1
                value > 0.0
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
                                 'for field `minimum_surface_convection_heat_transfer_coefficient_value`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `minimum_surface_convection_heat_transfer_coefficient_value`')

        self._data["Minimum Surface Convection Heat Transfer Coefficient Value"] = value

    @property
    def maximum_surface_convection_heat_transfer_coefficient_value(self):
        """Get maximum_surface_convection_heat_transfer_coefficient_value

        Returns:
            float: the value of `maximum_surface_convection_heat_transfer_coefficient_value` or None if not set
        """
        return self._data["Maximum Surface Convection Heat Transfer Coefficient Value"]

    @maximum_surface_convection_heat_transfer_coefficient_value.setter
    def maximum_surface_convection_heat_transfer_coefficient_value(self, value=1000.0 ):
        """  Corresponds to IDD Field `maximum_surface_convection_heat_transfer_coefficient_value`

        Args:
            value (float): value for IDD Field `maximum_surface_convection_heat_transfer_coefficient_value`
                Unit: W/m2-K
                Default value: 1000.0
                value >= 1.0
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
                                 'for field `maximum_surface_convection_heat_transfer_coefficient_value`'.format(value))
            if value < 1.0:
                raise ValueError('value need to be greater or equal 1.0 '
                                 'for field `maximum_surface_convection_heat_transfer_coefficient_value`')

        self._data["Maximum Surface Convection Heat Transfer Coefficient Value"] = value

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
        out.append(self._to_str(self.surface_temperature_upper_limit))
        out.append(self._to_str(self.minimum_surface_convection_heat_transfer_coefficient_value))
        out.append(self._to_str(self.maximum_surface_convection_heat_transfer_coefficient_value))
        return ",".join(out)