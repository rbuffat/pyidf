from collections import OrderedDict

class TemperingValve(object):
    """ Corresponds to IDD object `TemperingValve`
        Temperature-controlled diversion valve used to divert flow around one or more plant
        components such as a hot water heater. It can only be used on one of two branches
        between a Splitter and a Mixer.
    """
    internal_name = "TemperingValve"
    field_count = 6

    def __init__(self):
        """ Init data dictionary object for EPW IDD  `TemperingValve`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Inlet Node Name"] = None
        self._data["Outlet Node Name"] = None
        self._data["Stream 2 Source Node Name"] = None
        self._data["Temperature Setpoint Node Name"] = None
        self._data["Pump Outlet Node Name"] = None

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
            self.stream_2_source_node_name = None
        else:
            self.stream_2_source_node_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.temperature_setpoint_node_name = None
        else:
            self.temperature_setpoint_node_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.pump_outlet_node_name = None
        else:
            self.pump_outlet_node_name = vals[i]
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
        Name of a Node

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
        Name of a Node

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
    def stream_2_source_node_name(self):
        """Get stream_2_source_node_name

        Returns:
            str: the value of `stream_2_source_node_name` or None if not set
        """
        return self._data["Stream 2 Source Node Name"]

    @stream_2_source_node_name.setter
    def stream_2_source_node_name(self, value=None):
        """  Corresponds to IDD Field `stream_2_source_node_name`
        Name of a Node

        Args:
            value (str): value for IDD Field `stream_2_source_node_name`
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
                                 'for field `stream_2_source_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `stream_2_source_node_name`')

        self._data["Stream 2 Source Node Name"] = value

    @property
    def temperature_setpoint_node_name(self):
        """Get temperature_setpoint_node_name

        Returns:
            str: the value of `temperature_setpoint_node_name` or None if not set
        """
        return self._data["Temperature Setpoint Node Name"]

    @temperature_setpoint_node_name.setter
    def temperature_setpoint_node_name(self, value=None):
        """  Corresponds to IDD Field `temperature_setpoint_node_name`
        Name of a Node

        Args:
            value (str): value for IDD Field `temperature_setpoint_node_name`
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
                                 'for field `temperature_setpoint_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `temperature_setpoint_node_name`')

        self._data["Temperature Setpoint Node Name"] = value

    @property
    def pump_outlet_node_name(self):
        """Get pump_outlet_node_name

        Returns:
            str: the value of `pump_outlet_node_name` or None if not set
        """
        return self._data["Pump Outlet Node Name"]

    @pump_outlet_node_name.setter
    def pump_outlet_node_name(self, value=None):
        """  Corresponds to IDD Field `pump_outlet_node_name`

        Args:
            value (str): value for IDD Field `pump_outlet_node_name`
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
                                 'for field `pump_outlet_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `pump_outlet_node_name`')

        self._data["Pump Outlet Node Name"] = value

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
        out.append(self._to_str(self.stream_2_source_node_name))
        out.append(self._to_str(self.temperature_setpoint_node_name))
        out.append(self._to_str(self.pump_outlet_node_name))
        return ",".join(out)