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
    required_fields = ["Name", "Inlet Node Name", "Outlet Node Name", "Load Schedule Name", "Peak Flow Rate", "Flow Rate Fraction Schedule Name"]

    def __init__(self):
        """ Init data dictionary object for IDD  `LoadProfile:Plant`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Inlet Node Name"] = None
        self._data["Outlet Node Name"] = None
        self._data["Load Schedule Name"] = None
        self._data["Peak Flow Rate"] = None
        self._data["Flow Rate Fraction Schedule Name"] = None
        self.accept_substring = False

    def read(self, vals, accept_substring=True):
        """ Read values

        Args:
            vals (list): list of strings representing values
        """
        self.accept_substring = accept_substring
        i = 0
        if len(vals[i]) == 0:
            self.name = None
        else:
            self.name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.inlet_node_name = None
        else:
            self.inlet_node_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.outlet_node_name = None
        else:
            self.outlet_node_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.load_schedule_name = None
        else:
            self.load_schedule_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.peak_flow_rate = None
        else:
            self.peak_flow_rate = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.flow_rate_fraction_schedule_name = None
        else:
            self.flow_rate_fraction_schedule_name = vals[i]
        i += 1
        if i >= len(vals):
            return

    @property
    def name(self):
        """Get name

        Returns:
            str: the value of `name` or None if not set
        """
        return self._data["Name"]

    @name.setter
    def name(self, value=None):
        """  Corresponds to IDD Field `Name`

        Args:
            value (str): value for IDD Field `Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
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
        """  Corresponds to IDD Field `Inlet Node Name`

        Args:
            value (str): value for IDD Field `Inlet Node Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `inlet_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `inlet_node_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
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
        """  Corresponds to IDD Field `Outlet Node Name`

        Args:
            value (str): value for IDD Field `Outlet Node Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `outlet_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `outlet_node_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
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
        """  Corresponds to IDD Field `Load Schedule Name`
        Schedule values are load in [W]

        Args:
            value (str): value for IDD Field `Load Schedule Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `load_schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `load_schedule_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
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
        """  Corresponds to IDD Field `Peak Flow Rate`

        Args:
            value (float): value for IDD Field `Peak Flow Rate`
                Units: m3/s
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
        """  Corresponds to IDD Field `Flow Rate Fraction Schedule Name`

        Args:
            value (str): value for IDD Field `Flow Rate Fraction Schedule Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `flow_rate_fraction_schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `flow_rate_fraction_schedule_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `flow_rate_fraction_schedule_name`')
        self._data["Flow Rate Fraction Schedule Name"] = value

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