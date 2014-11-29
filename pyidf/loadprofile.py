from collections import OrderedDict

class LoadProfilePlant(object):
    """ Corresponds to IDD object `LoadProfile:Plant`
        Used to simulate a scheduled plant loop demand profile.  Load and flow rate are
        specified using schedules. Positive values are heating loads, and negative values are
        cooling loads. The actual load met is dependent on the performance of the supply
        loop components.
    """
    internal_name = "LoadProfile:Plant"
    field_count = 6

    def __init__(self):
        """ Init data dictionary object for EPW IDD  `LoadProfile:Plant`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Inlet Node Name"] = None
        self._data["Outlet Node Name"] = None
        self._data["Load Schedule Name"] = None
        self._data["Peak Flow Rate"] = None
        self._data["Flow Rate Fraction Schedule Name"] = None

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
            self.inlet_node_name = None
        else:
            self.inlet_node_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.outlet_node_name = None
        else:
            self.outlet_node_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.load_schedule_name = None
        else:
            self.load_schedule_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.peak_flow_rate = None
        else:
            self.peak_flow_rate = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.flow_rate_fraction_schedule_name = None
        else:
            self.flow_rate_fraction_schedule_name = vals[i]
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
    def inlet_node_name(self):
        """Get inlet_node_name

        Returns:
            str: the value of `inlet_node_name` or None if not set
        """
        return self._data["Inlet Node Name"]

    @inlet_node_name.setter
    def inlet_node_name(self, value=None):
        """  Corresponds to IDD Field `inlet_node_name`

        Args:
            value (str): value for IDD Field `inlet_node_name`
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
                                 'for field `inlet_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `inlet_node_name`')

        self._data["Inlet Node Name"] = value

    @property
    def outlet_node_name(self):
        """Get outlet_node_name

        Returns:
            str: the value of `outlet_node_name` or None if not set
        """
        return self._data["Outlet Node Name"]

    @outlet_node_name.setter
    def outlet_node_name(self, value=None):
        """  Corresponds to IDD Field `outlet_node_name`

        Args:
            value (str): value for IDD Field `outlet_node_name`
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
                                 'for field `outlet_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `outlet_node_name`')

        self._data["Outlet Node Name"] = value

    @property
    def load_schedule_name(self):
        """Get load_schedule_name

        Returns:
            str: the value of `load_schedule_name` or None if not set
        """
        return self._data["Load Schedule Name"]

    @load_schedule_name.setter
    def load_schedule_name(self, value=None):
        """  Corresponds to IDD Field `load_schedule_name`
        Schedule values are load in [W]

        Args:
            value (str): value for IDD Field `load_schedule_name`
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
                                 'for field `load_schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `load_schedule_name`')

        self._data["Load Schedule Name"] = value

    @property
    def peak_flow_rate(self):
        """Get peak_flow_rate

        Returns:
            float: the value of `peak_flow_rate` or None if not set
        """
        return self._data["Peak Flow Rate"]

    @peak_flow_rate.setter
    def peak_flow_rate(self, value=None):
        """  Corresponds to IDD Field `peak_flow_rate`

        Args:
            value (float): value for IDD Field `peak_flow_rate`
                Unit: m3/s
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
                                 'for field `peak_flow_rate`'.format(value))

        self._data["Peak Flow Rate"] = value

    @property
    def flow_rate_fraction_schedule_name(self):
        """Get flow_rate_fraction_schedule_name

        Returns:
            str: the value of `flow_rate_fraction_schedule_name` or None if not set
        """
        return self._data["Flow Rate Fraction Schedule Name"]

    @flow_rate_fraction_schedule_name.setter
    def flow_rate_fraction_schedule_name(self, value=None):
        """  Corresponds to IDD Field `flow_rate_fraction_schedule_name`

        Args:
            value (str): value for IDD Field `flow_rate_fraction_schedule_name`
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
                                 'for field `flow_rate_fraction_schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `flow_rate_fraction_schedule_name`')

        self._data["Flow Rate Fraction Schedule Name"] = value

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
        out.append(self._to_str(self.inlet_node_name))
        out.append(self._to_str(self.outlet_node_name))
        out.append(self._to_str(self.load_schedule_name))
        out.append(self._to_str(self.peak_flow_rate))
        out.append(self._to_str(self.flow_rate_fraction_schedule_name))
        return ",".join(out)