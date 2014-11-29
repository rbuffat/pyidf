from collections import OrderedDict

class ZoneAirBalanceOutdoorAir(object):
    """ Corresponds to IDD object `ZoneAirBalance:OutdoorAir`
        Provide a combined zone outdoor air flow by including interactions between
        mechanical ventilation, infiltration and duct leakage.
        This object will combine outdoor flows from all ZoneInfiltration and
        ZoneVentilation objects in the same zone. Balanced flows will be summed, while
        unbalanced flows will be added in quadrature.
    """
    internal_name = "ZoneAirBalance:OutdoorAir"
    field_count = 5

    def __init__(self):
        """ Init data dictionary object for EPW IDD  `ZoneAirBalance:OutdoorAir`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Zone Name"] = None
        self._data["Air Balance Method"] = None
        self._data["Induced Outdoor Air Due to Unbalanced Duct Leakage"] = None
        self._data["Induced Outdoor Air Schedule Name"] = None

    def read(self, vals):
        """ Read values

        Args:
            vals (list): list of strings representing values
        """
        i = 0
        if len(vals[i]) == 0:
            self.name = None
        else:
            self.name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.zone_name = None
        else:
            self.zone_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.air_balance_method = None
        else:
            self.air_balance_method = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.induced_outdoor_air_due_to_unbalanced_duct_leakage = None
        else:
            self.induced_outdoor_air_due_to_unbalanced_duct_leakage = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.induced_outdoor_air_schedule_name = None
        else:
            self.induced_outdoor_air_schedule_name = vals[i]
        i += 1

    @property
    def name(self):
        """Get name

        Returns:
            str: the value of `name` or None if not set
        """
        return self._data["Name"]

    @name.setter
    def name(self, value=None):
        """  Corresponds to IDD Field `name`

        Args:
            value (str): value for IDD Field `name`
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
                                 'for field `name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `name`')

        self._data["Name"] = value

    @property
    def zone_name(self):
        """Get zone_name

        Returns:
            str: the value of `zone_name` or None if not set
        """
        return self._data["Zone Name"]

    @zone_name.setter
    def zone_name(self, value=None):
        """  Corresponds to IDD Field `zone_name`

        Args:
            value (str): value for IDD Field `zone_name`
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
                                 'for field `zone_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `zone_name`')

        self._data["Zone Name"] = value

    @property
    def air_balance_method(self):
        """Get air_balance_method

        Returns:
            str: the value of `air_balance_method` or None if not set
        """
        return self._data["Air Balance Method"]

    @air_balance_method.setter
    def air_balance_method(self, value="Quadrature"):
        """  Corresponds to IDD Field `air_balance_method`
        None: Only perform simple calculations without using a combined zone outdoor air.
        Quadrature: A combined outdoor air is used in the quadrature sum.

        Args:
            value (str): value for IDD Field `air_balance_method`
                Accepted values are:
                      - Quadrature
                      - None
                Default value: Quadrature
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
                                 'for field `air_balance_method`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `air_balance_method`')
            vals = set()
            vals.add("Quadrature")
            vals.add("None")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `air_balance_method`'.format(value))

        self._data["Air Balance Method"] = value

    @property
    def induced_outdoor_air_due_to_unbalanced_duct_leakage(self):
        """Get induced_outdoor_air_due_to_unbalanced_duct_leakage

        Returns:
            float: the value of `induced_outdoor_air_due_to_unbalanced_duct_leakage` or None if not set
        """
        return self._data["Induced Outdoor Air Due to Unbalanced Duct Leakage"]

    @induced_outdoor_air_due_to_unbalanced_duct_leakage.setter
    def induced_outdoor_air_due_to_unbalanced_duct_leakage(self, value=0.0 ):
        """  Corresponds to IDD Field `induced_outdoor_air_due_to_unbalanced_duct_leakage`

        Args:
            value (float): value for IDD Field `induced_outdoor_air_due_to_unbalanced_duct_leakage`
                Unit: m3/s
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
                                 'for field `induced_outdoor_air_due_to_unbalanced_duct_leakage`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `induced_outdoor_air_due_to_unbalanced_duct_leakage`')

        self._data["Induced Outdoor Air Due to Unbalanced Duct Leakage"] = value

    @property
    def induced_outdoor_air_schedule_name(self):
        """Get induced_outdoor_air_schedule_name

        Returns:
            str: the value of `induced_outdoor_air_schedule_name` or None if not set
        """
        return self._data["Induced Outdoor Air Schedule Name"]

    @induced_outdoor_air_schedule_name.setter
    def induced_outdoor_air_schedule_name(self, value=None):
        """  Corresponds to IDD Field `induced_outdoor_air_schedule_name`
        This schedule contains the fraction values applied to the Induced Outdoor Air given in the
        previous input field (0.0 - 1.0).

        Args:
            value (str): value for IDD Field `induced_outdoor_air_schedule_name`
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
                                 'for field `induced_outdoor_air_schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `induced_outdoor_air_schedule_name`')

        self._data["Induced Outdoor Air Schedule Name"] = value

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
        out.append(self._to_str(self.name))
        out.append(self._to_str(self.zone_name))
        out.append(self._to_str(self.air_balance_method))
        out.append(self._to_str(self.induced_outdoor_air_due_to_unbalanced_duct_leakage))
        out.append(self._to_str(self.induced_outdoor_air_schedule_name))
        return ",".join(out)